# Datos procesados — 06_Experimento

Esta carpeta contiene los datos **derivados** del análisis empírico terminal, obtenidos a
partir de los datos crudos declarados en `06_Experimento/datos_crudos/`. A diferencia de
los datos crudos, aquí la información ya fue limpiada, cruzada o agregada mediante un
procedimiento documentado y reproducible.

## Archivo: `consenso_experto_vs_detector.csv`

**Origen:** `06_Experimento/datos_crudos/evaluacion_expertos.csv` (183 filas: 61 requisitos
× 3 evaluadores) y `06_Experimento/datos_crudos/salida_detector.csv` (61 filas: una
clasificación directa del detector automático por requisito).

**Transformación aplicada:**
1. Para cada uno de los 61 requisitos (`ID_Anonimo`), se calculó el **consenso experto**
   por mayoría simple entre las clasificaciones individuales de los tres evaluadores
   (`Ambiguo` / `No ambiguo`).
2. Se registró el **nivel de acuerdo** obtenido en cada requisito (`3/3` = unanimidad,
   `2/3` = mayoría simple).
3. Se cruzó el consenso experto contra la clasificación producida por el detector
   automático (`salida_detector.csv`) para el mismo requisito.
4. Se agregó la columna `Coincide` (`Sí` / `No`) indicando si el detector coincidió con
   el consenso experto.

**No se alteró, corrigió ni completó ningún valor individual** de los datos crudos
originales — la única operación aplicada es la agregación por mayoría y el cruce
descrito arriba. Este archivo se genera exclusivamente por script
(`06_Experimento/scripts_analisis/02_generar_datos_procesados.py`), no se edita a mano.

## Relación con `06_Experimento/resultados/`

Este archivo es idéntico a `06_Experimento/resultados/tablas/tabla_5_consenso_por_requisito.csv`.
Se mantiene una copia en ambas carpetas porque cumple dos roles distintos:

- En `datos_procesados/`: es el **insumo intermedio** que alimenta el cálculo de las
  métricas finales (κ de Cohen, κ de Fleiss, matriz de confusión, precisión,
  exhaustividad, F1) reportadas en `tabla_1` a `tabla_4`, `tabla_6` y `tabla_7`.
- En `resultados/tablas/`: es en sí misma una **tabla de resultados** citable en el
  manuscrito (consenso y coincidencia por requisito, requisito por requisito).

## Trazabilidad de la cadena de análisis

```
datos_crudos/evaluacion_expertos.csv   ┐
datos_crudos/salida_detector.csv       ┴─→  datos_procesados/consenso_experto_vs_detector.csv  ─→  resultados/tablas/tabla_1..4, 6, 7 + resultados/figuras/figura_1..4
```

Todo el proceso es reproducible ejecutando `06_Experimento/scripts_analisis/run_all.py`
sobre los archivos de `datos_crudos/` (corpus vigente: 61 requisitos).
