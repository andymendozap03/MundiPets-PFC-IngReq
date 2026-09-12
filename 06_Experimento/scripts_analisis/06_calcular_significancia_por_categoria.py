#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
06_calcular_significancia_por_categoria.py
============================================

Complementa 04_calcular_significancia_estadistica.py (que reporta las
métricas de forma agregada sobre los 61 requisitos) desglosando el mismo
cálculo de intervalo de confianza al 95 % (bootstrap, 10 000 réplicas)
por tipo de requisito (RF, RNF, RD, RL), tal como exige el ítem B4 de la
Rúbrica de cierre: "Intervalos de confianza para precisión, exhaustividad
y medida F del detector, por categoría."

Advertencia metodológica explícita: al desglosar por categoría, el
tamaño de muestra por grupo es pequeño (RD=9, RL=9, RNF=16, RF=27). Los
intervalos de confianza resultantes son, por diseño, más anchos que el
intervalo agregado sobre N=61, y así se reportan sin suavizarlos ni
ocultarlo. No se calcula una prueba de hipótesis (chi-cuadrado) por
categoría porque el tamaño esperado de celda mínimo para esa prueba
(convencionalmente ≥5) no se cumple en RD ni en RL.

No inventa datos: todo se calcula por remuestreo (bootstrap) sobre las
filas reales de datos_procesados/consenso_experto_vs_detector.csv,
agrupadas por la columna Tipo ya presente en esa tabla.

Uso:
    python 06_calcular_significancia_por_categoria.py

Salida:
    06_Experimento/resultados/tablas/tabla_10_significancia_por_categoria.csv
"""

import csv
import sys
from pathlib import Path
from collections import defaultdict

import numpy as np

BASE_DIR = Path(__file__).resolve().parent
EXPERIMENTO_DIR = BASE_DIR.parent
INPUT_CSV = EXPERIMENTO_DIR / "datos_procesados" / "consenso_experto_vs_detector.csv"
OUTPUT_CSV = EXPERIMENTO_DIR / "resultados" / "tablas" / "tabla_10_significancia_por_categoria.csv"

N_BOOTSTRAP = 10000
SEED = 42


def cargar_datos_por_tipo():
    if not INPUT_CSV.exists():
        sys.exit(f"ERROR: no se encontró {INPUT_CSV}")

    datos = defaultdict(lambda: {"consenso": [], "detector": []})
    with open(INPUT_CSV, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            tipo = row["Tipo"].strip()
            c = row["Consenso_experto"].strip()
            d = row["Clasificacion_detector"].strip()
            if c not in ("Ambiguo", "No ambiguo") or d not in ("Ambiguo", "No ambiguo"):
                sys.exit(f"ERROR: valor inesperado en fila {row}")
            datos[tipo]["consenso"].append(c)
            datos[tipo]["detector"].append(d)

    if not datos:
        sys.exit("ERROR: no hay filas para analizar.")

    return {t: (np.array(v["consenso"]), np.array(v["detector"])) for t, v in datos.items()}


def metricas(consenso, detector):
    """Idéntico al cálculo de 04_calcular_significancia_estadistica.py,
    para que ambos scripts sean consistentes entre sí."""
    tp = np.sum((detector == "Ambiguo") & (consenso == "Ambiguo"))
    tn = np.sum((detector == "No ambiguo") & (consenso == "No ambiguo"))
    fp = np.sum((detector == "Ambiguo") & (consenso == "No ambiguo"))
    fn = np.sum((detector == "No ambiguo") & (consenso == "Ambiguo"))
    n = tp + tn + fp + fn

    exactitud = (tp + tn) / n if n else float("nan")
    precision = tp / (tp + fp) if (tp + fp) else float("nan")
    sensibilidad = tp / (tp + fn) if (tp + fn) else float("nan")
    especificidad = tn / (tn + fp) if (tn + fp) else float("nan")
    f1 = (2 * precision * sensibilidad / (precision + sensibilidad)
          if (precision + sensibilidad) and not np.isnan(precision) and not np.isnan(sensibilidad)
          else float("nan"))

    return {
        "Exactitud": exactitud,
        "Precision": precision,
        "Sensibilidad": sensibilidad,
        "Especificidad": especificidad,
        "F1": f1,
    }, (tp, tn, fp, fn)


def bootstrap_ic95(consenso, detector, n_bootstrap=N_BOOTSTRAP, seed=SEED):
    rng = np.random.default_rng(seed)
    n = len(consenso)
    claves = ["Exactitud", "Precision", "Sensibilidad", "Especificidad", "F1"]
    muestras = {k: [] for k in claves}

    for _ in range(n_bootstrap):
        idx = rng.integers(0, n, n)
        m, _ = metricas(consenso[idx], detector[idx])
        for k in claves:
            v = m[k]
            if not np.isnan(v):
                muestras[k].append(v)

    ic = {}
    n_validas = {}
    for k in claves:
        arr = np.array(muestras[k])
        n_validas[k] = len(arr)
        if len(arr) == 0:
            ic[k] = (float("nan"), float("nan"))
        else:
            ic[k] = (np.percentile(arr, 2.5), np.percentile(arr, 97.5))
    return ic, n_validas


def main():
    datos_por_tipo = cargar_datos_por_tipo()
    orden_tipos = ["RF", "RNF", "RD", "RL"]
    tipos_presentes = [t for t in orden_tipos if t in datos_por_tipo]

    filas = []
    for tipo in tipos_presentes:
        consenso, detector = datos_por_tipo[tipo]
        n = len(consenso)
        m, (tp, tn, fp, fn) = metricas(consenso, detector)
        ic, n_validas = bootstrap_ic95(consenso, detector)

        filas.append([f"--- {tipo} (N={n}; TP={tp}, TN={tn}, FP={fp}, FN={fn}) ---", "", ""])
        for k, v in m.items():
            if np.isnan(v):
                filas.append([f"{tipo} | {k}", "No definida (denominador=0)", ""])
                continue
            lo, hi = ic[k]
            nota = "" if n_validas[k] == N_BOOTSTRAP else f"calculado sobre {n_validas[k]}/{N_BOOTSTRAP} réplicas válidas"
            filas.append([f"{tipo} | {k}", f"{v:.4f}", f"[{lo:.4f}, {hi:.4f}] {nota}".strip()])

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Categoría | Métrica", "Valor", "IC 95% (bootstrap, 10 000 réplicas)"])
        writer.writerows(filas)
        writer.writerow(["", "", ""])
        writer.writerow(["Nota metodológica",
                          "Los IC por categoría son mas anchos que el IC agregado (N=61) por el "
                          "menor tamaño de muestra en cada grupo (RD=9, RL=9, RNF=16, RF=27). No "
                          "se reporta chi-cuadrado por categoria porque el tamaño esperado minimo "
                          "de celda (>=5) no se cumple en RD ni en RL.", ""])

    print(f"Desglose por categoría calculado sobre {sum(len(v[0]) for v in datos_por_tipo.values())} requisitos totales.")
    for tipo in tipos_presentes:
        consenso, detector = datos_por_tipo[tipo]
        m, (tp, tn, fp, fn) = metricas(consenso, detector)
        print(f"\n{tipo} (N={len(consenso)}, TP={tp} TN={tn} FP={fp} FN={fn}):")
        for k, v in m.items():
            print(f"  {k}: {v:.4f}" if not np.isnan(v) else f"  {k}: no definida")
    print(f"\nTabla guardada en: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
