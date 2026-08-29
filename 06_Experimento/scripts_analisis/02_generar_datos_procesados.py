#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_generar_datos_procesados.py
================================

Genera `datos_procesados/consenso_experto_vs_detector.csv` exclusivamente
a partir de `datos_crudos/evaluacion_expertos.csv` y
`datos_crudos/salida_detector.csv`.

Por qué existe este script: hasta ahora, `consenso_experto_vs_detector.csv`
era un archivo estático sin script que lo regenerara desde los datos
crudos. Eso rompía la promesa de reproducibilidad de
`README_ejecucion_scripts_analisis.md` ("cualquier persona puede
reproducir exactamente las mismas tablas y figuras ejecutando un único
comando"): en un clon limpio sin ese archivo, 04_calcular_significancia
_estadistica.py fallaba. Este script cierra ese hueco.

Transformación que aplica:
    1. Convierte evaluacion_expertos.csv (formato largo: 1 fila por
       requisito x evaluador) a formato ancho (1 fila por requisito,
       con una columna por evaluador).
    2. Calcula el consenso experto por voto mayoritario entre los 3
       evaluadores (con 3 evaluadores nunca hay empate).
    3. Cruza con salida_detector.csv por ID_Anonimo para incorporar la
       clasificación del detector y las reglas que activó.
    4. Calcula si el detector coincide o no con el consenso experto.

No inventa datos: cada valor de salida proviene directamente de una fila
de datos_crudos/, sin generar, imputar ni redondear nada que no esté ahí.

Debe ejecutarse ANTES de 04_calcular_significancia_estadistica.py
(run_all.py ya respeta ese orden).

Uso:
    python 02_generar_datos_procesados.py

Salida:
    06_Experimento/datos_procesados/consenso_experto_vs_detector.csv
"""

import csv
import sys
from collections import OrderedDict, Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
EXPERIMENTO_DIR = BASE_DIR.parent

EVALUACION_CSV = EXPERIMENTO_DIR / "datos_crudos" / "evaluacion_expertos.csv"
DETECTOR_CSV = EXPERIMENTO_DIR / "datos_crudos" / "salida_detector.csv"
OUTPUT_CSV = EXPERIMENTO_DIR / "datos_procesados" / "consenso_experto_vs_detector.csv"

EVALUADORES_ESPERADOS = ["Experto 1", "Experto 2", "Experto 3"]


def leer_csv_coma(path):
    if not path.exists():
        sys.exit(f"ERROR: no se encontró {path}")
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=","))


def construir_tabla_ancha(filas_evaluacion):
    """Convierte el formato largo (1 fila por requisito x evaluador) a
    ancho (1 fila por requisito), calculando consenso y nivel de acuerdo."""
    por_requisito = OrderedDict()

    for fila in filas_evaluacion:
        id_anon = fila["ID_Anonimo"]
        evaluador = fila["Evaluador"]
        clasificacion = fila["Clasificacion_Experto"].strip()

        if id_anon not in por_requisito:
            por_requisito[id_anon] = {
                "ID_Real": fila["ID_Real"],
                "Tipo": fila["Tipo"],
                "Texto_Requisito": fila["Texto_Requisito"],
                "votos": {},
            }
        por_requisito[id_anon]["votos"][evaluador] = clasificacion

    filas_anchas = []
    for id_anon, datos in por_requisito.items():
        votos = datos["votos"]
        faltantes = [e for e in EVALUADORES_ESPERADOS if e not in votos]
        if faltantes:
            sys.exit(f"ERROR: {id_anon} no tiene evaluación de: {', '.join(faltantes)}")

        conteo = Counter(votos[e] for e in EVALUADORES_ESPERADOS)
        consenso, n_mayoria = conteo.most_common(1)[0]
        nivel_acuerdo = f"{n_mayoria}/{len(EVALUADORES_ESPERADOS)}"

        filas_anchas.append({
            "ID_Anonimo": id_anon,
            "ID_Real": datos["ID_Real"],
            "Tipo": datos["Tipo"],
            "Texto_Requisito": datos["Texto_Requisito"],
            "Experto 1": votos["Experto 1"],
            "Experto 2": votos["Experto 2"],
            "Experto 3": votos["Experto 3"],
            "Consenso_experto": consenso,
            "Nivel_acuerdo": nivel_acuerdo,
        })

    return filas_anchas


def cruzar_con_detector(filas_anchas, filas_detector):
    detector_por_id = {f["ID_Anonimo"]: f for f in filas_detector}

    filas_finales = []
    for fila in filas_anchas:
        id_anon = fila["ID_Anonimo"]
        if id_anon not in detector_por_id:
            sys.exit(f"ERROR: {id_anon} no está en salida_detector.csv")
        det = detector_por_id[id_anon]

        clasificacion_detector = det["Clasificacion_Detector"].strip()
        coincide = "Sí" if clasificacion_detector == fila["Consenso_experto"] else "No"

        filas_finales.append([
            fila["ID_Anonimo"],
            fila["ID_Real"],
            fila["Tipo"],
            fila["Texto_Requisito"],
            fila["Experto 1"],
            fila["Experto 2"],
            fila["Experto 3"],
            fila["Consenso_experto"],
            fila["Nivel_acuerdo"],
            clasificacion_detector,
            det["Reglas_Activadas"].strip(),
            coincide,
        ])

    return filas_finales


def main():
    filas_evaluacion = leer_csv_coma(EVALUACION_CSV)
    filas_detector = leer_csv_coma(DETECTOR_CSV)

    filas_anchas = construir_tabla_ancha(filas_evaluacion)
    filas_finales = cruzar_con_detector(filas_anchas, filas_detector)

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([
            "ID_Anonimo", "ID_Real", "Tipo", "Texto_Requisito",
            "Experto 1", "Experto 2", "Experto 3",
            "Consenso_experto", "Nivel_acuerdo",
            "Clasificacion_detector", "Reglas_detector", "Coincide",
        ])
        writer.writerows(filas_finales)

    n_coincide = sum(1 for f in filas_finales if f[-1] == "Sí")
    print(f"{len(filas_finales)} requisitos procesados. Coincidencias detector-consenso: {n_coincide}/{len(filas_finales)}")
    print(f"Tabla guardada en: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
