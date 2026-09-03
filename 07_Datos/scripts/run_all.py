#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_all.py
==========

Punto de entrada único para reproducir todo el análisis empírico de
MundiPets (Enfoque 2 — detección automática de ambigüedad), desde los
datos crudos hasta la tabla de correspondencia afirmación-resultado.

Ejecuta, en orden, los cuatro scripts de análisis con las rutas
correctas, sin que la persona que ejecuta tenga que recordar argumentos.

Uso:
    python run_all.py

Requisitos (instalar una sola vez):
    pip install -r requirements.txt
"""

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
EXPERIMENTO_DIR = BASE_DIR.parent  # 06_Experimento/

SCRIPT_DATOS_PROCESADOS = BASE_DIR / "02_generar_datos_procesados.py"
SCRIPT_TABLAS = BASE_DIR / "03_generar_tablas_figuras_excel_corregido.py"
SCRIPT_SIGNIFICANCIA = BASE_DIR / "04_calcular_significancia_estadistica.py"
SCRIPT_CORRESPONDENCIA = BASE_DIR / "05_generar_tabla_correspondencia.py"

DETECTOR_CSV = EXPERIMENTO_DIR / "datos_crudos" / "salida_detector.csv"
EXPERTOS_CSV = EXPERIMENTO_DIR / "datos_crudos" / "evaluacion_expertos.csv"
OUTPUT_DIR = EXPERIMENTO_DIR / "resultados"


def main():
    for path in (SCRIPT_DATOS_PROCESADOS, SCRIPT_TABLAS, SCRIPT_SIGNIFICANCIA,
                 SCRIPT_CORRESPONDENCIA, DETECTOR_CSV, EXPERTOS_CSV):
        if not path.exists():
            sys.exit(f"ERROR: no se encontró el archivo esperado: {path}")

    print("[1/4] Generando datos_procesados/consenso_experto_vs_detector.csv...")
    resultado0 = subprocess.run([sys.executable, str(SCRIPT_DATOS_PROCESADOS)])
    if resultado0.returncode != 0:
        sys.exit("ERROR: 02_generar_datos_procesados.py terminó con errores.")

    comando_tablas = [
        sys.executable,
        str(SCRIPT_TABLAS),
        "--detector", str(DETECTOR_CSV),
        "--expertos", str(EXPERTOS_CSV),
        "--output", str(OUTPUT_DIR),
    ]

    print("\n[2/4] Generando tablas y figuras principales...")
    print(" ".join(comando_tablas))
    resultado = subprocess.run(comando_tablas)
    if resultado.returncode != 0:
        sys.exit("ERROR: 03_generar_tablas_figuras_excel_corregido.py terminó con errores.")

    print("\n[3/4] Calculando IC 95% (bootstrap) y prueba de hipótesis (chi-cuadrado)...")
    resultado2 = subprocess.run([sys.executable, str(SCRIPT_SIGNIFICANCIA)])
    if resultado2.returncode != 0:
        sys.exit("ERROR: 04_calcular_significancia_estadistica.py terminó con errores.")

    print("\n[4/4] Generando tabla de correspondencia afirmación-resultado...")
    resultado3 = subprocess.run([sys.executable, str(SCRIPT_CORRESPONDENCIA)])
    if resultado3.returncode != 0:
        sys.exit("ERROR: 05_generar_tabla_correspondencia.py terminó con errores.")

    print(f"\nListo. Datos procesados, tablas y figuras generados en: {EXPERIMENTO_DIR}")


if __name__ == "__main__":
    main()
