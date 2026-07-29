#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_generar_tablas_figuras.py
============================

Genera las tablas y figuras del análisis empírico de MundiPets a partir de:

1. salida_detector.csv
   Columnas mínimas:
   ID_Anonimo, Clasificacion_Detector, Reglas_Activadas, Texto_Requisito

2. evaluacion_expertos.csv
   Columnas mínimas:
   ID_Anonimo, Clasificacion_Experto, Evaluador

La clase positiva es "Ambiguo".

Salidas:
- Siete tablas CSV.
- Cuatro figuras PNG a 300 dpi.
- Un resumen narrativo TXT.

El script no inventa datos. Se detiene si faltan archivos, columnas,
clasificaciones, evaluadores o identificadores comunes.
"""

import argparse
import csv
import os
import sys
from collections import Counter, defaultdict
from itertools import combinations

import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    cohen_kappa_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


VALID_LABELS = {"Ambiguo", "No ambiguo"}
POSITIVE_LABEL = "Ambiguo"
NEGATIVE_LABEL = "No ambiguo"


def read_csv(path):
    if not os.path.exists(path):
        sys.exit(f"ERROR: no se encontró el archivo: {path}")
    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def require_columns(rows, required, path):
    if not rows:
        sys.exit(f"ERROR: el archivo está vacío: {path}")
    available = set(rows[0].keys())
    missing = required - available
    if missing:
        sys.exit(
            f"ERROR: {path} no contiene las columnas requeridas: "
            f"{sorted(missing)}"
        )


def write_csv(path, headers, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(headers)
        writer.writerows(rows)


def percentage(value, total):
    return 100.0 * value / total if total else 0.0


def interpret_kappa(kappa):
    if kappa < 0:
        return "Sin acuerdo (peor que el azar)"
    if kappa <= 0.20:
        return "Leve"
    if kappa <= 0.40:
        return "Aceptable"
    if kappa <= 0.60:
        return "Moderado"
    if kappa <= 0.80:
        return "Sustancial"
    return "Casi perfecto"


def fleiss_kappa(evaluations_by_item, categories):
    """
    Kappa de Fleiss para un número constante de evaluadores por ítem.
    evaluations_by_item = {id: {evaluador: clasificación}}
    """
    item_ids = sorted(evaluations_by_item)
    if len(item_ids) < 2:
        raise ValueError("Se requieren al menos dos ítems para kappa de Fleiss.")

    number_of_raters = len(evaluations_by_item[item_ids[0]])
    if number_of_raters < 2:
        raise ValueError("Se requieren al menos dos evaluadores.")

    for item_id in item_ids:
        if len(evaluations_by_item[item_id]) != number_of_raters:
            raise ValueError(
                "Todos los ítems deben tener el mismo número de evaluadores "
                "para calcular kappa de Fleiss."
            )

    count_matrix = []
    for item_id in item_ids:
        counts = Counter(evaluations_by_item[item_id].values())
        count_matrix.append([counts.get(category, 0) for category in categories])

    item_agreements = []
    for row in count_matrix:
        squared_sum = sum(count * count for count in row)
        agreement = (
            squared_sum - number_of_raters
        ) / (number_of_raters * (number_of_raters - 1))
        item_agreements.append(agreement)

    observed_agreement = sum(item_agreements) / len(item_agreements)

    category_totals = [
        sum(row[column_index] for row in count_matrix)
        for column_index in range(len(categories))
    ]
    total_ratings = len(item_ids) * number_of_raters
    category_proportions = [
        total / total_ratings for total in category_totals
    ]
    expected_agreement = sum(value * value for value in category_proportions)

    if expected_agreement == 1:
        return 1.0, observed_agreement, expected_agreement

    kappa = (
        observed_agreement - expected_agreement
    ) / (1 - expected_agreement)
    return kappa, observed_agreement, expected_agreement


def majority_consensus(classifications):
    counts = Counter(classifications)
    most_common = counts.most_common()
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        raise ValueError(
            "Se produjo un empate. El consenso mayoritario requiere un "
            "número impar de evaluadores o una regla de desempate."
        )
    return most_common[0][0], most_common[0][1]


def main():
    parser = argparse.ArgumentParser(
        description="Genera tablas y figuras del análisis de ambigüedad."
    )
    parser.add_argument("--detector", required=True)
    parser.add_argument("--expertos", required=True)
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()

    detector_rows = read_csv(arguments.detector)
    expert_rows = read_csv(arguments.expertos)

    require_columns(
        detector_rows,
        {"ID_Anonimo", "Clasificacion_Detector"},
        arguments.detector,
    )
    require_columns(
        expert_rows,
        {"ID_Anonimo", "Clasificacion_Experto", "Evaluador"},
        arguments.expertos,
    )

    detector = {}
    detector_rules = {}
    detector_text = {}
    for row in detector_rows:
        item_id = row["ID_Anonimo"].strip()
        label = row["Clasificacion_Detector"].strip()
        if not item_id:
            continue
        if label not in VALID_LABELS:
            sys.exit(
                f"ERROR: clasificación inválida del detector para {item_id}: "
                f"{label!r}"
            )
        detector[item_id] = label
        detector_rules[item_id] = row.get("Reglas_Activadas", "").strip()
        detector_text[item_id] = row.get("Texto_Requisito", "").strip()

    experts_by_item = defaultdict(dict)
    metadata_by_item = {}
    confidence_by_evaluator = defaultdict(list)
    smell_counts = Counter()

    for row in expert_rows:
        item_id = row["ID_Anonimo"].strip()
        evaluator = row["Evaluador"].strip()
        label = row["Clasificacion_Experto"].strip()
        if not item_id or not evaluator:
            continue
        if label not in VALID_LABELS:
            sys.exit(
                f"ERROR: clasificación experta inválida para {item_id}: "
                f"{label!r}"
            )
        if evaluator in experts_by_item[item_id]:
            sys.exit(
                f"ERROR: clasificación duplicada de {evaluator} para {item_id}."
            )

        experts_by_item[item_id][evaluator] = label
        metadata_by_item[item_id] = {
            "ID_Real": row.get("ID_Real", "").strip(),
            "Tipo": row.get("Tipo", "").strip(),
            "Texto_Requisito": row.get("Texto_Requisito", "").strip(),
        }

        confidence_value = row.get("Confianza", "").strip()
        if confidence_value:
            try:
                confidence_by_evaluator[evaluator].append(
                    float(confidence_value)
                )
            except ValueError:
                sys.exit(
                    f"ERROR: confianza no numérica para {item_id}: "
                    f"{confidence_value!r}"
                )

        smell_type = row.get("Tipo_Mal_Olor", "").strip()
        if label == POSITIVE_LABEL and smell_type and smell_type != "Ninguno":
            smell_counts[smell_type] += 1

    common_ids = sorted(
        set(detector) & set(experts_by_item),
        key=lambda value: int(value.split("-")[-1]),
    )

    if not common_ids:
        sys.exit(
            "ERROR: no existen identificadores comunes entre detector y expertos."
        )

    missing_detector = sorted(set(experts_by_item) - set(detector))
    missing_experts = sorted(set(detector) - set(experts_by_item))
    if missing_detector or missing_experts:
        sys.exit(
            "ERROR: los corpus no coinciden exactamente.\n"
            f"Sin detector: {missing_detector}\n"
            f"Sin expertos: {missing_experts}"
        )

    rater_counts = {len(experts_by_item[item_id]) for item_id in common_ids}
    if len(rater_counts) != 1:
        sys.exit(
            "ERROR: no todos los requisitos tienen el mismo número de expertos."
        )
    number_of_raters = next(iter(rater_counts))
    if number_of_raters != 3:
        sys.exit(
            f"ERROR: se esperaban 3 expertos por requisito y se encontraron "
            f"{number_of_raters}."
        )

    evaluators = sorted(
        {evaluator for item in experts_by_item.values() for evaluator in item}
    )

    consensus = {}
    agreement_level = {}
    for item_id in common_ids:
        consensus[item_id], agreement_level[item_id] = majority_consensus(
            experts_by_item[item_id].values()
        )

    actual = [consensus[item_id] for item_id in common_ids]
    predicted = [detector[item_id] for item_id in common_ids]

    accuracy = accuracy_score(actual, predicted)
    precision = precision_score(
        actual,
        predicted,
        pos_label=POSITIVE_LABEL,
        average="binary",
        zero_division=0,
    )
    sensitivity = recall_score(
        actual,
        predicted,
        pos_label=POSITIVE_LABEL,
        average="binary",
        zero_division=0,
    )
    f1 = f1_score(
        actual,
        predicted,
        pos_label=POSITIVE_LABEL,
        average="binary",
        zero_division=0,
    )
    detector_kappa = cohen_kappa_score(actual, predicted)

    matrix = confusion_matrix(
        actual,
        predicted,
        labels=[NEGATIVE_LABEL, POSITIVE_LABEL],
    )
    true_negative, false_positive = matrix[0]
    false_negative, true_positive = matrix[1]

    specificity = (
        true_negative / (true_negative + false_positive)
        if (true_negative + false_positive)
        else 0.0
    )
    negative_predictive_value = (
        true_negative / (true_negative + false_negative)
        if (true_negative + false_negative)
        else 0.0
    )
    balanced_accuracy = (sensitivity + specificity) / 2

    pairwise_kappas = []
    for evaluator_1, evaluator_2 in combinations(evaluators, 2):
        labels_1 = [
            experts_by_item[item_id][evaluator_1] for item_id in common_ids
        ]
        labels_2 = [
            experts_by_item[item_id][evaluator_2] for item_id in common_ids
        ]
        observed_agreement = sum(
            value_1 == value_2
            for value_1, value_2 in zip(labels_1, labels_2)
        ) / len(common_ids)
        kappa = cohen_kappa_score(labels_1, labels_2)
        pairwise_kappas.append(
            (
                f"{evaluator_1} vs {evaluator_2}",
                kappa,
                observed_agreement,
                interpret_kappa(kappa),
            )
        )

    fleiss_value, fleiss_observed, fleiss_expected = fleiss_kappa(
        {item_id: experts_by_item[item_id] for item_id in common_ids},
        [NEGATIVE_LABEL, POSITIVE_LABEL],
    )

    tables_directory = os.path.join(arguments.output, "tablas")
    figures_directory = os.path.join(arguments.output, "figuras")
    os.makedirs(tables_directory, exist_ok=True)
    os.makedirs(figures_directory, exist_ok=True)

    # Tabla 1: distribución de clasificaciones.
    classification_summary = []
    sources = evaluators + ["Consenso experto", "Detector automático"]
    for source in sources:
        if source in evaluators:
            labels = [
                experts_by_item[item_id][source] for item_id in common_ids
            ]
        elif source == "Consenso experto":
            labels = [consensus[item_id] for item_id in common_ids]
        else:
            labels = [detector[item_id] for item_id in common_ids]

        counts = Counter(labels)
        ambiguous = counts.get(POSITIVE_LABEL, 0)
        non_ambiguous = counts.get(NEGATIVE_LABEL, 0)
        classification_summary.append(
            [
                source,
                len(labels),
                ambiguous,
                f"{percentage(ambiguous, len(labels)):.2f}",
                non_ambiguous,
                f"{percentage(non_ambiguous, len(labels)):.2f}",
            ]
        )

    write_csv(
        os.path.join(tables_directory, "tabla_1_resumen_clasificaciones.csv"),
        [
            "Fuente",
            "N",
            "Ambiguos_n",
            "Ambiguos_porcentaje",
            "No_ambiguos_n",
            "No_ambiguos_porcentaje",
        ],
        classification_summary,
    )

    # Tabla 2: desempeño del detector.
    metric_rows = [
        ["Exactitud", f"{accuracy:.4f}", "Proporción total de aciertos"],
        ["Precisión", f"{precision:.4f}", "Clase positiva: Ambiguo"],
        ["Exhaustividad / Sensibilidad", f"{sensitivity:.4f}", "Clase positiva: Ambiguo"],
        ["Especificidad", f"{specificity:.4f}", "Clase negativa: No ambiguo"],
        ["Valor predictivo negativo", f"{negative_predictive_value:.4f}", ""],
        ["Exactitud balanceada", f"{balanced_accuracy:.4f}", ""],
        ["F1", f"{f1:.4f}", "Clase positiva: Ambiguo"],
        [
            "Kappa de Cohen: detector vs consenso",
            f"{detector_kappa:.4f}",
            interpret_kappa(detector_kappa),
        ],
    ]
    write_csv(
        os.path.join(tables_directory, "tabla_2_metricas_detector.csv"),
        ["Metrica", "Valor", "Interpretacion_o_nota"],
        metric_rows,
    )

    # Tabla 3: matriz de confusión.
    write_csv(
        os.path.join(tables_directory, "tabla_3_matriz_confusion.csv"),
        [
            "Clasificacion_real",
            "Detector_No_ambiguo",
            "Detector_Ambiguo",
        ],
        [
            [NEGATIVE_LABEL, int(true_negative), int(false_positive)],
            [POSITIVE_LABEL, int(false_negative), int(true_positive)],
        ],
    )

    # Tabla 4: acuerdo entre evaluadores.
    agreement_rows = [
        [
            comparison,
            f"{kappa:.4f}",
            f"{observed:.4f}",
            interpretation,
        ]
        for comparison, kappa, observed, interpretation in pairwise_kappas
    ]
    agreement_rows.append(
        [
            "Panel completo: kappa de Fleiss",
            f"{fleiss_value:.4f}",
            f"{fleiss_observed:.4f}",
            interpret_kappa(fleiss_value),
        ]
    )
    write_csv(
        os.path.join(tables_directory, "tabla_4_acuerdo_interevaluador.csv"),
        ["Comparacion", "Kappa", "Acuerdo_observado", "Interpretacion"],
        agreement_rows,
    )

    # Tabla 5: detalle y consenso por requisito.
    item_rows = []
    for item_id in common_ids:
        item_metadata = metadata_by_item.get(item_id, {})
        expert_labels = [
            experts_by_item[item_id][evaluator] for evaluator in evaluators
        ]
        item_rows.append(
            [
                item_id,
                item_metadata.get("ID_Real", ""),
                item_metadata.get("Tipo", ""),
                item_metadata.get("Texto_Requisito", detector_text.get(item_id, "")),
                *expert_labels,
                consensus[item_id],
                f"{agreement_level[item_id]}/{number_of_raters}",
                detector[item_id],
                detector_rules.get(item_id, ""),
                "Sí" if detector[item_id] == consensus[item_id] else "No",
            ]
        )

    write_csv(
        os.path.join(tables_directory, "tabla_5_consenso_por_requisito.csv"),
        [
            "ID_Anonimo",
            "ID_Real",
            "Tipo",
            "Texto_Requisito",
            *evaluators,
            "Consenso_experto",
            "Nivel_acuerdo",
            "Clasificacion_detector",
            "Reglas_detector",
            "Coincide",
        ],
        item_rows,
    )

    # Tabla 6: tipos de ambigüedad señalados por los expertos.
    smell_rows = [
        [smell_type, count, f"{percentage(count, sum(smell_counts.values())):.2f}"]
        for smell_type, count in smell_counts.most_common()
    ]
    write_csv(
        os.path.join(tables_directory, "tabla_6_tipos_ambiguedad.csv"),
        ["Tipo_de_ambiguedad", "Frecuencia", "Porcentaje_sobre_marcaciones_ambiguas"],
        smell_rows,
    )

    # Tabla 7: confianza.
    confidence_rows = []
    for evaluator in evaluators:
        values = confidence_by_evaluator.get(evaluator, [])
        confidence_rows.append(
            [
                evaluator,
                len(values),
                f"{sum(values) / len(values):.2f}" if values else "",
                f"{min(values):.0f}" if values else "",
                f"{max(values):.0f}" if values else "",
            ]
        )
    write_csv(
        os.path.join(tables_directory, "tabla_7_confianza_evaluadores.csv"),
        ["Evaluador", "N", "Confianza_media", "Minimo", "Maximo"],
        confidence_rows,
    )

    # Figura 1: clasificación por fuente.
    figure_labels = sources
    ambiguous_values = [
        int(row[2]) for row in classification_summary
    ]
    non_ambiguous_values = [
        int(row[4]) for row in classification_summary
    ]
    x_positions = list(range(len(figure_labels)))
    width = 0.36

    fig, axis = plt.subplots(figsize=(10, 6))
    axis.bar(
        [position - width / 2 for position in x_positions],
        ambiguous_values,
        width,
        label=POSITIVE_LABEL,
    )
    axis.bar(
        [position + width / 2 for position in x_positions],
        non_ambiguous_values,
        width,
        label=NEGATIVE_LABEL,
    )
    axis.set_title("Clasificación de requisitos por evaluador, consenso y detector")
    axis.set_xlabel("Fuente de clasificación")
    axis.set_ylabel("Número de requisitos")
    axis.set_xticks(x_positions)
    axis.set_xticklabels(figure_labels, rotation=20, ha="right")
    axis.legend()
    axis.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(
        os.path.join(figures_directory, "figura_1_clasificaciones_por_fuente.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(fig)

    # Figura 2: matriz de confusión.
    fig, axis = plt.subplots(figsize=(7, 6))
    image = axis.imshow(matrix)
    axis.set_title("Matriz de confusión: detector frente al consenso experto")
    axis.set_xlabel("Clasificación del detector")
    axis.set_ylabel("Consenso experto")
    axis.set_xticks([0, 1])
    axis.set_xticklabels([NEGATIVE_LABEL, POSITIVE_LABEL])
    axis.set_yticks([0, 1])
    axis.set_yticklabels([NEGATIVE_LABEL, POSITIVE_LABEL])

    for row_index in range(matrix.shape[0]):
        for column_index in range(matrix.shape[1]):
            axis.text(
                column_index,
                row_index,
                str(matrix[row_index, column_index]),
                ha="center",
                va="center",
            )
    fig.colorbar(image, ax=axis)
    fig.tight_layout()
    fig.savefig(
        os.path.join(figures_directory, "figura_2_matriz_confusion.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(fig)

    # Figura 3: kappas.
    kappa_labels = [
        comparison.replace("Experto ", "E")
        for comparison, _, _, _ in pairwise_kappas
    ] + ["Panel (Fleiss)", "Detector vs consenso"]
    kappa_values = [
        kappa for _, kappa, _, _ in pairwise_kappas
    ] + [fleiss_value, detector_kappa]

    fig, axis = plt.subplots(figsize=(10, 6))
    axis.bar(kappa_labels, kappa_values)
    axis.set_title("Coeficientes de acuerdo")
    axis.set_xlabel("Comparación")
    axis.set_ylabel("Valor de kappa")
    axis.set_ylim(min(-0.1, min(kappa_values) - 0.1), 1.0)
    axis.tick_params(axis="x", rotation=20)
    axis.grid(axis="y", alpha=0.25)
    for index, value in enumerate(kappa_values):
        axis.text(index, value, f"{value:.3f}", ha="center", va="bottom")
    fig.tight_layout()
    fig.savefig(
        os.path.join(figures_directory, "figura_3_coeficientes_kappa.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(fig)

    # Figura 4: tipos de ambigüedad.
    smell_labels = [row[0] for row in smell_rows]
    smell_values = [int(row[1]) for row in smell_rows]

    fig, axis = plt.subplots(figsize=(10, 6))
    axis.barh(smell_labels, smell_values)
    axis.set_title("Tipos de ambigüedad identificados por los expertos")
    axis.set_xlabel("Número de marcaciones")
    axis.set_ylabel("Tipo de ambigüedad")
    axis.grid(axis="x", alpha=0.25)
    for index, value in enumerate(smell_values):
        axis.text(value, index, f" {value}", va="center")
    fig.tight_layout()
    fig.savefig(
        os.path.join(figures_directory, "figura_4_tipos_ambiguedad.png"),
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(fig)

    exact_agreement = sum(
        agreement_level[item_id] == number_of_raters for item_id in common_ids
    )
    majority_agreement = len(common_ids) - exact_agreement

    summary_path = os.path.join(arguments.output, "resumen_resultados.txt")
    with open(summary_path, "w", encoding="utf-8") as file:
        file.write("RESULTADOS DEL COMPONENTE EMPÍRICO MUNDIPETS\n")
        file.write("=" * 49 + "\n\n")
        file.write(f"Requisitos analizados: {len(common_ids)}\n")
        file.write(f"Evaluadores por requisito: {number_of_raters}\n")
        file.write(
            f"Consenso experto: {actual.count(POSITIVE_LABEL)} ambiguos y "
            f"{actual.count(NEGATIVE_LABEL)} no ambiguos.\n"
        )
        file.write(
            f"Detector automático: {predicted.count(POSITIVE_LABEL)} ambiguos y "
            f"{predicted.count(NEGATIVE_LABEL)} no ambiguos.\n"
        )
        file.write(
            f"Acuerdo unánime entre expertos: {exact_agreement}/{len(common_ids)} "
            f"({percentage(exact_agreement, len(common_ids)):.2f} %).\n"
        )
        file.write(
            f"Acuerdo por mayoría 2/3: {majority_agreement}/{len(common_ids)} "
            f"({percentage(majority_agreement, len(common_ids)):.2f} %).\n\n"
        )
        file.write("DESEMPEÑO DEL DETECTOR\n")
        file.write(f"Exactitud: {accuracy:.4f}\n")
        file.write(f"Precisión: {precision:.4f}\n")
        file.write(f"Sensibilidad: {sensitivity:.4f}\n")
        file.write(f"Especificidad: {specificity:.4f}\n")
        file.write(f"F1: {f1:.4f}\n")
        file.write(
            f"Kappa detector-consenso: {detector_kappa:.4f} "
            f"({interpret_kappa(detector_kappa)}).\n\n"
        )
        file.write("ACUERDO ENTRE EXPERTOS\n")
        for comparison, kappa, observed, interpretation in pairwise_kappas:
            file.write(
                f"{comparison}: kappa={kappa:.4f}, "
                f"acuerdo observado={observed:.4f}, {interpretation}.\n"
            )
        file.write(
            f"Panel completo: kappa de Fleiss={fleiss_value:.4f} "
            f"({interpret_kappa(fleiss_value)}).\n\n"
        )
        file.write("NOTA METODOLÓGICA\n")
        file.write(
            "El análisis se efectuó sobre los 50 requisitos presentes tanto en "
            "la salida del detector como en las evaluaciones: 25 RF, 16 RNF y "
            "9 RD. Las cinco obligaciones legales RL-01 a RL-05 del Excel no "
            "se compararon porque no forman parte del archivo original "
            "salida_detector.csv. No se imputaron ni inventaron resultados.\n"
        )

    print(f"Análisis completado sobre {len(common_ids)} requisitos.")
    print(
        f"Exactitud={accuracy:.4f}; Precisión={precision:.4f}; "
        f"Sensibilidad={sensitivity:.4f}; F1={f1:.4f}"
    )
    print(
        f"Kappa detector-consenso={detector_kappa:.4f}; "
        f"Kappa de Fleiss={fleiss_value:.4f}"
    )
    print(f"Resultados guardados en: {arguments.output}")


if __name__ == "__main__":
    main()
