#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_calcular_significancia_estadistica.py
==========================================

Complementa el análisis de 03_generar_tablas_figuras_excel_corregido.py
agregando lo que exige la Sección 4.4 de la Guía-Rúbrica (Entrega 4 / 2B),
"elementos comunes obligatorios a los tres enfoques":

    - Intervalo de confianza al 95% (bootstrap, 10 000 réplicas) para
      exactitud, precisión, sensibilidad, especificidad, F1 y kappa
      detector-consenso.
    - Prueba de hipótesis con nombre exacto, estadístico y valor p con
      3+ decimales: chi-cuadrado de independencia sobre la matriz de
      confusión (¿la clasificación del detector está asociada con el
      consenso experto, o es indistinguible del azar?).

No inventa datos: todo se calcula por remuestreo (bootstrap) sobre las
50 filas reales de datos_procesados/consenso_experto_vs_detector.csv.

Uso:
    python 04_calcular_significancia_estadistica.py

Salida:
    06_Experimento/resultados/tablas/tabla_8_significancia_estadistica.csv
"""

import csv
import sys
from pathlib import Path

import numpy as np
from scipy import stats

BASE_DIR = Path(__file__).resolve().parent
EXPERIMENTO_DIR = BASE_DIR.parent
INPUT_CSV = EXPERIMENTO_DIR / "datos_procesados" / "consenso_experto_vs_detector.csv"
OUTPUT_CSV = EXPERIMENTO_DIR / "resultados" / "tablas" / "tabla_8_significancia_estadistica.csv"

N_BOOTSTRAP = 10000
SEED = 42


def cargar_datos():
    if not INPUT_CSV.exists():
        sys.exit(f"ERROR: no se encontró {INPUT_CSV}")

    consenso = []
    detector = []
    with open(INPUT_CSV, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            c = row["Consenso_experto"].strip()
            d = row["Clasificacion_detector"].strip()
            if c not in ("Ambiguo", "No ambiguo") or d not in ("Ambiguo", "No ambiguo"):
                sys.exit(f"ERROR: valor inesperado en fila {row}")
            consenso.append(c)
            detector.append(d)

    if len(consenso) == 0:
        sys.exit("ERROR: no hay filas para analizar.")

    return np.array(consenso), np.array(detector)


def metricas(consenso, detector):
    """Calcula exactitud, precisión, sensibilidad, especificidad, F1 y kappa
    tratando 'Ambiguo' como clase positiva."""
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
          if (precision + sensibilidad) else float("nan"))

    # Kappa de Cohen entre detector y consenso
    po = exactitud
    p_det_amb = (tp + fp) / n
    p_con_amb = (tp + fn) / n
    pe = p_det_amb * p_con_amb + (1 - p_det_amb) * (1 - p_con_amb)
    kappa = (po - pe) / (1 - pe) if (1 - pe) != 0 else float("nan")

    return {
        "Exactitud": exactitud,
        "Precision": precision,
        "Sensibilidad": sensibilidad,
        "Especificidad": especificidad,
        "F1": f1,
        "Kappa_detector_consenso": kappa,
    }, (tp, tn, fp, fn)


def bootstrap_ic95(consenso, detector, n_bootstrap=N_BOOTSTRAP, seed=SEED):
    rng = np.random.default_rng(seed)
    n = len(consenso)
    claves = ["Exactitud", "Precision", "Sensibilidad", "Especificidad", "F1", "Kappa_detector_consenso"]
    muestras = {k: [] for k in claves}

    for _ in range(n_bootstrap):
        idx = rng.integers(0, n, n)
        m, _ = metricas(consenso[idx], detector[idx])
        for k in claves:
            v = m[k]
            if not np.isnan(v):
                muestras[k].append(v)

    ic = {}
    for k in claves:
        arr = np.array(muestras[k])
        if len(arr) == 0:
            ic[k] = (float("nan"), float("nan"))
        else:
            ic[k] = (np.percentile(arr, 2.5), np.percentile(arr, 97.5))
    return ic


def prueba_chi_cuadrado(tp, tn, fp, fn):
    """Chi-cuadrado de independencia: ¿la clasificación del detector está
    asociada con el consenso experto, o son independientes (= azar)?"""
    tabla = np.array([[tp, fn], [fp, tn]])
    chi2, p, dof, esperado = stats.chi2_contingency(tabla, correction=True)
    return chi2, p, dof, esperado


def main():
    consenso, detector = cargar_datos()
    n = len(consenso)

    m, (tp, tn, fp, fn) = metricas(consenso, detector)
    ic = bootstrap_ic95(consenso, detector)
    chi2, p_valor, dof, esperado = prueba_chi_cuadrado(tp, tn, fp, fn)

    # Tamaño del efecto para la prueba chi-cuadrado 2x2: phi
    n_total = tp + tn + fp + fn
    phi = np.sqrt(chi2 / n_total) if n_total else float("nan")

    filas = []
    for k, v in m.items():
        lo, hi = ic[k]
        filas.append([k, f"{v:.4f}", f"[{lo:.4f}, {hi:.4f}]"])

    filas.append(["", "", ""])
    filas.append(["Prueba de hipótesis", "Chi-cuadrado de independencia (Pearson, corrección de continuidad)", ""])
    filas.append(["Estadístico (chi2)", f"{chi2:.4f}", f"gl={dof}"])
    filas.append(["Valor p", f"{p_valor:.4f}", "N=" + str(n)])
    filas.append(["Tamaño del efecto (phi)", f"{phi:.4f}", ""])
    filas.append(["Interpretación",
                  (f"El detector está asociado con el consenso experto más allá del azar (p={p_valor:.4f}<0.05)."
                   if p_valor < 0.05 else
                   f"Con N={n} requisitos, el estudio no alcanza significancia estadística "
                   f"(p={p_valor:.4f}) para afirmar asociación entre el detector y el consenso "
                   f"experto. Esto es coherente con el tamaño de muestra reducido y debe "
                   f"reportarse como limitación de potencia estadística, no como evidencia de "
                   f"que el detector no funciona."),
                  ""])

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Métrica", "Valor / Estadístico", "IC 95% / Detalle"])
        writer.writerows(filas)

    print(f"N = {n} requisitos analizados (bootstrap: {N_BOOTSTRAP} réplicas, semilla={SEED})")
    for k, v in m.items():
        lo, hi = ic[k]
        print(f"  {k}: {v:.4f}  IC95%=[{lo:.4f}, {hi:.4f}]")
    print(f"  Chi-cuadrado={chi2:.4f}, gl={dof}, p={p_valor:.4f}, phi={phi:.4f}")
    print(f"\nTabla guardada en: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
