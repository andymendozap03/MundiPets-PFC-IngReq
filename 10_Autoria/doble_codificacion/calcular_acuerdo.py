"""
Calcula el coeficiente de acuerdo (Kappa de Cohen) entre las dos hojas de
codificacion producidas de forma independiente por dos integrantes del
equipo, sobre el mismo subconjunto de 18 requisitos del corpus MundiPets.

Uso:
    pip install scikit-learn numpy scipy
    python calcular_acuerdo.py

Entrada esperada (en la misma carpeta):
    hoja_codificacion_AndyMendoza.csv
    hoja_codificacion_EdsonFuertes.csv

Cada hoja debe tener, ya completada, la columna 'Clasificacion' con los
valores 'Ambiguo' o 'No ambiguo' para cada uno de los 18 requisitos,
en el mismo orden de ID_Anonimo.

Salida:
    resultado_acuerdo_doble_codificacion.csv
    (con el kappa, el acuerdo observado, el intervalo de confianza al 95%
    y el numero de requisitos comparados)
"""

import csv
import numpy as np
from sklearn.metrics import cohen_kappa_score

ARCHIVO_A = "hoja_codificacion_AndyMendoza.csv"
ARCHIVO_B = "hoja_codificacion_EdsonFuertes.csv"
NOMBRE_A = "Andy Mendoza"
NOMBRE_B = "Edson Fuertes"
SALIDA = "resultado_acuerdo_doble_codificacion.csv"
N_BOOTSTRAP = 10000
SEMILLA = 42


def leer_hoja(ruta):
    with open(ruta, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        filas = list(reader)
    faltantes = [r["ID_Anonimo"] for r in filas if not r["Clasificacion"].strip()]
    if faltantes:
        raise ValueError(
            f"La hoja '{ruta}' tiene {len(faltantes)} requisito(s) sin "
            f"clasificar todavia: {', '.join(faltantes)}. "
            "Completa la columna 'Clasificacion' (Ambiguo / No ambiguo) "
            "para todos los requisitos antes de ejecutar este script."
        )
    return {r["ID_Anonimo"]: r["Clasificacion"].strip() for r in filas}


def bootstrap_ic_kappa(y1, y2, n_boot=N_BOOTSTRAP, seed=SEMILLA):
    """Intervalo de confianza al 95% del kappa via bootstrap por pares."""
    rng = np.random.default_rng(seed)
    n = len(y1)
    y1 = np.array(y1)
    y2 = np.array(y2)
    kappas = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        try:
            k = cohen_kappa_score(y1[idx], y2[idx])
        except Exception:
            continue
        if not np.isnan(k):
            kappas.append(k)
    kappas = np.array(kappas)
    ic_inf = np.percentile(kappas, 2.5)
    ic_sup = np.percentile(kappas, 97.5)
    return ic_inf, ic_sup


def interpretar_kappa(k):
    if k < 0:
        return "Sin acuerdo"
    elif k <= 0.20:
        return "Insignificante"
    elif k <= 0.40:
        return "Discreto"
    elif k <= 0.60:
        return "Moderado"
    elif k <= 0.80:
        return "Sustancial"
    else:
        return "Casi perfecto"


def main():
    hoja_a = leer_hoja(ARCHIVO_A)
    hoja_b = leer_hoja(ARCHIVO_B)

    ids_a = set(hoja_a.keys())
    ids_b = set(hoja_b.keys())
    if ids_a != ids_b:
        raise ValueError(
            "Las dos hojas no tienen exactamente los mismos requisitos. "
            f"Solo en {NOMBRE_A}: {ids_a - ids_b or 'ninguno'}. "
            f"Solo en {NOMBRE_B}: {ids_b - ids_a or 'ninguno'}."
        )

    ids_ordenados = sorted(ids_a)
    y1 = [hoja_a[i] for i in ids_ordenados]
    y2 = [hoja_b[i] for i in ids_ordenados]

    n = len(ids_ordenados)
    acuerdo_observado = sum(1 for a, b in zip(y1, y2) if a == b) / n
    kappa = cohen_kappa_score(y1, y2)
    ic_inf, ic_sup = bootstrap_ic_kappa(y1, y2)
    interpretacion = interpretar_kappa(kappa)

    print(f"Requisitos comparados: {n}")
    print(f"Acuerdo observado: {acuerdo_observado:.4f}")
    print(f"Kappa de Cohen: {kappa:.4f}")
    print(f"IC 95% (bootstrap, {N_BOOTSTRAP} replicas): [{ic_inf:.4f}, {ic_sup:.4f}]")
    print(f"Interpretacion: {interpretacion}")

    # Detalle de discrepancias, para que el equipo las revise si quiere
    discrepancias = [
        (i, hoja_a[i], hoja_b[i]) for i in ids_ordenados if hoja_a[i] != hoja_b[i]
    ]

    with open(SALIDA, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Metrica", "Valor"])
        writer.writerow(["N_requisitos_comparados", n])
        writer.writerow(["Evaluador_A", NOMBRE_A])
        writer.writerow(["Evaluador_B", NOMBRE_B])
        writer.writerow(["Acuerdo_observado", f"{acuerdo_observado:.4f}"])
        writer.writerow(["Kappa_Cohen", f"{kappa:.4f}"])
        writer.writerow(["IC_95_inferior", f"{ic_inf:.4f}"])
        writer.writerow(["IC_95_superior", f"{ic_sup:.4f}"])
        writer.writerow(["Interpretacion", interpretacion])
        writer.writerow(["N_discrepancias", len(discrepancias)])
        writer.writerow([])
        writer.writerow(["ID_Anonimo", f"Clasificacion_{NOMBRE_A}", f"Clasificacion_{NOMBRE_B}"])
        for i, a, b in discrepancias:
            writer.writerow([i, a, b])

    print(f"\nResultado guardado en: {SALIDA}")
    if discrepancias:
        print(f"Hubo {len(discrepancias)} discrepancia(s) — revisenlas en el CSV de salida.")


if __name__ == "__main__":
    main()
