"""
06_calcular_power_cuestionario.py

Calculo de potencia estadistica (power calculation) para el cuestionario
v2.0 de MundiPets, perfil dominante "Propietario de mascota".

Contexto
--------
El perfil dominante del cuestionario reunio n = 47 respuestas validas,
por debajo del minimo de n >= 60 por perfil establecido en la guia de la
Entrega 4 (2B), Seccion 5 (Tabla de evidencia minima terminal) y en el
gatekeeper G5. La propia guia admite como alternativa un calculo de
potencia estadistica explicito, fijando:

    alpha       = 0.05
    1 - beta    = 0.80  (potencia minima exigida)
    d de Cohen  = 0.5   (tamano de efecto mediano)

Este script calcula, de forma reproducible:
    1. El tamano de muestra minimo requerido para alcanzar una potencia
       de 0.80 con d = 0.5 y alpha = 0.05 (prueba t de una muestra).
    2. La potencia estadistica REAL alcanzada con el n disponible (47).
    3. Una conclusion explicita sobre si el n disponible es suficiente.

El resultado se escribe en:
    tabla_power_cuestionario.csv (misma carpeta)

Requiere: statsmodels (pip install statsmodels)

Ejecucion:
    python 06_calcular_power_cuestionario.py
"""

import csv
from pathlib import Path

from statsmodels.stats.power import TTestPower

# ---------------------------------------------------------------------
# Parametros fijados por la guia de la asignatura (Seccion 5 / G5)
# ---------------------------------------------------------------------
ALPHA = 0.05
POTENCIA_MINIMA = 0.80
COHEN_D = 0.5

# Datos reales del cuestionario v2.0 (Apendice B.4 del ERS/SRS)
N_TOTAL_RESPUESTAS = 61
N_PERFIL_DOMINANTE = 47  # Propietarios de mascota
PERFIL_DOMINANTE = "Propietario de mascota"

OUTPUT_CSV = Path(__file__).parent / "tabla_power_cuestionario.csv"


def calcular_n_minimo_requerido(d: float, alpha: float, power: float) -> float:
    """N minimo (prueba t de una muestra) para alcanzar 'power' dado d y alpha."""
    analysis = TTestPower()
    return analysis.solve_power(
        effect_size=d, alpha=alpha, power=power, alternative="two-sided"
    )


def calcular_potencia_alcanzada(n: int, d: float, alpha: float) -> float:
    """Potencia estadistica real alcanzada con un n fijo (prueba t de una muestra)."""
    analysis = TTestPower()
    return analysis.solve_power(
        effect_size=d, nobs=n, alpha=alpha, alternative="two-sided"
    )


def main() -> None:
    n_minimo = calcular_n_minimo_requerido(COHEN_D, ALPHA, POTENCIA_MINIMA)
    potencia_real = calcular_potencia_alcanzada(N_PERFIL_DOMINANTE, COHEN_D, ALPHA)
    suficiente = potencia_real >= POTENCIA_MINIMA

    print("=" * 70)
    print("Calculo de potencia estadistica - Cuestionario MundiPets v2.0")
    print("=" * 70)
    print(f"Perfil evaluado:                 {PERFIL_DOMINANTE}")
    print(f"n disponible (perfil dominante):  {N_PERFIL_DOMINANTE}")
    print(f"n total de respuestas validas:    {N_TOTAL_RESPUESTAS}")
    print(f"Tamano de efecto (d de Cohen):     {COHEN_D}")
    print(f"Nivel de significancia (alpha):    {ALPHA}")
    print(f"Potencia minima exigida (1-beta):  {POTENCIA_MINIMA}")
    print("-" * 70)
    print(f"n minimo requerido para 1-beta=0.80: {n_minimo:.2f} "
          f"(redondeado hacia arriba: {int(n_minimo) + 1})")
    print(f"Potencia REAL alcanzada con n={N_PERFIL_DOMINANTE}: "
          f"{potencia_real:.4f} ({potencia_real * 100:.2f} %)")
    print("-" * 70)
    if suficiente:
        print("CONCLUSION: el n disponible SUPERA el minimo requerido para "
              "alcanzar una potencia estadistica de al menos 80 %.")
    else:
        print("CONCLUSION: el n disponible NO alcanza la potencia minima "
              "exigida de 80 %.")
    print("=" * 70)

    # Escribir tabla de resultados (reproducible, sin edicion manual)
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["metrica", "valor"])
        writer.writerow(["perfil_evaluado", PERFIL_DOMINANTE])
        writer.writerow(["n_perfil_dominante", N_PERFIL_DOMINANTE])
        writer.writerow(["n_total_respuestas", N_TOTAL_RESPUESTAS])
        writer.writerow(["cohen_d", COHEN_D])
        writer.writerow(["alpha", ALPHA])
        writer.writerow(["potencia_minima_exigida", POTENCIA_MINIMA])
        writer.writerow(["n_minimo_requerido", round(n_minimo, 4)])
        writer.writerow(["n_minimo_requerido_redondeado", int(n_minimo) + 1])
        writer.writerow(["potencia_alcanzada", round(potencia_real, 4)])
        writer.writerow(["potencia_alcanzada_pct", round(potencia_real * 100, 2)])
        writer.writerow(["cumple_potencia_minima", "SI" if suficiente else "NO"])
        writer.writerow(["prueba_utilizada", "t de una muestra (one-sample t-test)"])
        writer.writerow(["paquete", "statsmodels.stats.power.TTestPower"])

    print(f"\nTabla de resultados escrita en: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
