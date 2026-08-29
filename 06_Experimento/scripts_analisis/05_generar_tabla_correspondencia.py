#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
05_generar_tabla_correspondencia.py
=====================================

Genera la tabla de correspondencia entre afirmación y resultado que exige
la Sección 5.8 de la Guía-Rúbrica (Entrega Final / 2B): una fila por
afirmación de la sección "Discusión" del reporte, donde cada afirmación
remite al resultado o a la referencia que la sostiene.

No inventa datos ni redacta afirmaciones con números fijos en el código:
lee los valores reales desde las tablas ya generadas por
03_generar_tablas_figuras_excel_corregido.py y
04_calcular_significancia_estadistica.py, y arma cada afirmación
sustituyendo esos valores. Si el experimento se vuelve a ejecutar con
datos distintos, esta tabla se recalcula con los nuevos números.

Debe ejecutarse DESPUÉS de 03 y 04 (run_all.py ya respeta ese orden).

Uso:
    python 05_generar_tabla_correspondencia.py

Salida:
    06_Experimento/resultados/tablas/tabla_9_correspondencia_afirmacion_resultado.csv
"""

import csv
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
EXPERIMENTO_DIR = BASE_DIR.parent
TABLAS_DIR = EXPERIMENTO_DIR / "resultados" / "tablas"

TABLA_1 = TABLAS_DIR / "tabla_1_resumen_clasificaciones.csv"
TABLA_2 = TABLAS_DIR / "tabla_2_metricas_detector.csv"
TABLA_3 = TABLAS_DIR / "tabla_3_matriz_confusion.csv"
TABLA_4 = TABLAS_DIR / "tabla_4_acuerdo_interevaluador.csv"
TABLA_6 = TABLAS_DIR / "tabla_6_tipos_ambiguedad.csv"
TABLA_8 = TABLAS_DIR / "tabla_8_significancia_estadistica.csv"
OUTPUT_CSV = TABLAS_DIR / "tabla_9_correspondencia_afirmacion_resultado.csv"


def leer_filas(path):
    if not path.exists():
        sys.exit(f"ERROR: no se encontró {path}. Ejecuta primero 03 y 04 (o run_all.py).")
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def fnum(valor):
    """Convierte '0.5200' -> 0.5200 (float), tolerando coma o punto decimal."""
    return float(str(valor).replace(",", "."))


def como_coma(valor, decimales=4):
    return f"{valor:.{decimales}f}".replace(".", ",")


def main():
    filas1 = leer_filas(TABLA_1)
    filas2 = leer_filas(TABLA_2)
    filas3 = leer_filas(TABLA_3)
    filas4 = leer_filas(TABLA_4)
    filas6 = leer_filas(TABLA_6)
    filas8 = leer_filas(TABLA_8)

    # ---- AFI-01: clasificación por fuente (tabla 1) ----
    fila_detector = next(f for f in filas1 if f["Fuente"] == "Detector automático")
    fila_consenso = next(f for f in filas1 if f["Fuente"] == "Consenso experto")
    n_total = fila_detector["N"]
    pct_detector = fnum(fila_detector["Ambiguos_porcentaje"])
    pct_consenso = fnum(fila_consenso["Ambiguos_porcentaje"])
    n_detector = fila_detector["Ambiguos_n"]
    n_consenso = fila_consenso["Ambiguos_n"]

    afi_01 = (
        f"El detector automático sobre-marca ambigüedad respecto al consenso experto: "
        f"{pct_detector:.2f}".replace(".", ",") + f"% ({n_detector}/{n_total}) frente a "
        f"{pct_consenso:.2f}".replace(".", ",") + f"% ({n_consenso}/{n_total})."
    )

    # ---- AFI-02: métricas del detector (tabla 2) ----
    metricas2 = {f["Metrica"]: fnum(f["Valor"]) for f in filas2}
    afi_02 = (
        f"El detector alcanza una exactitud de {como_coma(metricas2['Exactitud'])}, "
        f"con precisión de {como_coma(metricas2['Precisión'])} y sensibilidad de "
        f"{como_coma(metricas2['Exhaustividad / Sensibilidad'])} respecto al consenso experto."
    )

    # ---- AFI-03: matriz de confusión (tabla 3) ----
    fila_no_amb = next(f for f in filas3 if f["Clasificacion_real"] == "No ambiguo")
    fila_amb = next(f for f in filas3 if f["Clasificacion_real"] == "Ambiguo")
    tn = int(fila_no_amb["Detector_No_ambiguo"])
    fp = int(fila_no_amb["Detector_Ambiguo"])
    fn = int(fila_amb["Detector_No_ambiguo"])
    tp = int(fila_amb["Detector_Ambiguo"])
    aciertos = tn + tp
    n_matriz = tn + fp + fn + tp
    afi_03 = (
        f"De los {n_matriz} requisitos evaluados, el detector clasificó correctamente "
        f"{aciertos} ({tn} no ambiguos + {tp} ambiguos), equivalente a la exactitud reportada."
    )

    # ---- AFI-04: acuerdo interevaluador (tabla 4) ----
    fila_fleiss = next(f for f in filas4 if f["Comparacion"].startswith("Panel completo"))
    kappa_fleiss = fnum(fila_fleiss["Kappa"])
    acuerdo_obs = fnum(fila_fleiss["Acuerdo_observado"]) * 100
    afi_04 = (
        f"Los expertos humanos muestran un acuerdo casi perfecto entre sí, con Kappa de Fleiss = "
        f"{como_coma(kappa_fleiss)} ({acuerdo_obs:.2f}".replace(".", ",") +
        "% de acuerdo observado) para el panel completo."
    )

    # ---- AFI-05: significancia estadística (tabla 8) ----
    valores8 = {f["Métrica"]: f["Valor / Estadístico"] for f in filas8}
    interpretacion = valores8.get("Interpretación", "").strip()
    chi2 = valores8.get("Estadístico (chi2)", "").strip()
    p_valor = valores8.get("Valor p", "").strip()
    afi_05 = (
        f"Prueba de hipótesis (chi-cuadrado={chi2}, p={p_valor}): {interpretacion}"
    )

    # ---- AFI-06: tipos de ambigüedad (tabla 6) ----
    filas6_ordenadas = sorted(filas6, key=lambda f: fnum(f["Porcentaje_sobre_marcaciones_ambiguas"]), reverse=True)
    top3 = filas6_ordenadas[:3]
    partes = []
    for i, f in enumerate(top3):
        pct = fnum(f["Porcentaje_sobre_marcaciones_ambiguas"])
        if i == 0:
            partes.append(
                f"El tipo de ambigüedad predominante es {f['Tipo_de_ambiguedad'].lower()}, presente en el "
                f"{pct:.2f}".replace(".", ",") + f"% de las marcaciones ambiguas ({f['Frecuencia']} casos)"
            )
        else:
            partes.append(
                f"{f['Tipo_de_ambiguedad'].lower()} ({pct:.2f}".replace(".", ",") + "%)"
            )
    afi_06 = partes[0] + ", seguido de " + " y ".join(partes[1:]) + "."

    filas_salida = [
        ["AFI-01", afi_01, "Tabla de resumen de clasificaciones por fuente", TABLA_1.name],
        ["AFI-02", afi_02, "Tabla de métricas del detector", TABLA_2.name],
        ["AFI-03", afi_03, "Matriz de confusión detector vs. consenso experto", TABLA_3.name],
        ["AFI-04", afi_04, "Tabla de acuerdo interevaluador", TABLA_4.name],
        ["AFI-05", afi_05, "Tabla de significancia estadística", TABLA_8.name],
        ["AFI-06", afi_06, "Tabla de tipos de ambigüedad", TABLA_6.name],
    ]

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["ID_Afirmacion", "Afirmacion", "Resultado_o_Referencia", "Archivo_Fuente"])
        writer.writerows(filas_salida)

    print(f"{len(filas_salida)} afirmaciones generadas a partir de las tablas 1, 2, 3, 4, 6 y 8.")
    print(f"Tabla guardada en: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
