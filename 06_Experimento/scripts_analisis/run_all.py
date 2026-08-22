#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_all.py
==========

Punto de entrada único para reproducir todo el análisis empírico de
MundiPets (Enfoque 2 — detección automática de ambigüedad).

Ejecuta 03_generar_tablas_figuras_excel_corregido.py con las rutas
correctas hacia los datos crudos y hacia la carpeta de resultados,
sin que la persona que ejecuta tenga que recordar argumentos.

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

SCRIPT_TABLAS = BASE_DIR / "03_generar_tablas_figuras_excel_corregido.py"
SCRIPT_SIGNIFICANCIA = BASE_DIR / "04_calcular_significancia_estadistica.py"
DETECTOR_CSV = EXPERIMENTO_DIR / "datos_crudos" / "salida_detector.csv"
EXPERTOS_CSV = EXPERIMENTO_DIR / "datos_crudos" / "evaluacion_expertos.csv"
OUTPUT_DIR = EXPERIMENTO_DIR / "resultados"


def main():
    for path in (SCRIPT_TABLAS, SCRIPT_SIGNIFICANCIA, DETECTOR_CSV, EXPERTOS_CSV):
        if not path.exists():
            sys.exit(f"ERROR: no se encontró el archivo esperado: {path}")

    comando_tablas = [
        sys.executable,
        str(SCRIPT_TABLAS),
        "--detector", str(DETECTOR_CSV),
        "--expertos", str(EXPERTOS_CSV),
        "--output", str(OUTPUT_DIR),
    ]

    print("[1/2] Generando tablas y figuras principales...")
    print(" ".join(comando_tablas))
    resultado = subprocess.run(comando_tablas)
    if resultado.returncode != 0:
        sys.exit("ERROR: 03_generar_tablas_figuras_excel_corregido.py terminó con errores.")

    print("\n[2/2] Calculando IC 95% (bootstrap) y prueba de hipótesis (chi-cuadrado)...")
    comando_significancia = [sys.executable, str(SCRIPT_SIGNIFICANCIA)]
    resultado2 = subprocess.run(comando_significancia)
    if resultado2.returncode != 0:
        sys.exit("ERROR: 04_calcular_significancia_estadistica.py terminó con errores.")

    print(f"\nListo. Tablas y figuras generadas en: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
