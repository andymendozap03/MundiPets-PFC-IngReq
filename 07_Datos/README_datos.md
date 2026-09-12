# 07_Datos — Paquete de datos del componente empírico (Enfoque 2)

## Qué contiene

| Carpeta | Contenido |
|---|---|
| `datos_crudos/` | Salida original del detector automático y de la evaluación de los tres expertos, sin ninguna edición manual. |
| `datos_procesados/` | Consenso experto y contraste detector-consenso, generados exclusivamente por script a partir de `datos_crudos/`. |
| `scripts/` | Los siete scripts de análisis y el orquestador único `run_all.py`. |
| `resultados/` | Las cuatro figuras y las once tablas citadas en el manuscrito, generadas por los scripts. |

## Cómo se generó

`datos_crudos/` es la exportación directa de la rúbrica de clasificación
experta (Sección 7.6 del ERS/SRS) y de la salida del detector basado en
reglas. Ningún valor de esta carpeta fue calculado, redondeado o corregido
a mano.

## Cómo se reproduce

```bash
cd 07_Datos/scripts
pip install -r requirements.txt
python run_all.py
```

Esto regenera, a partir únicamente de `datos_crudos/`, el contenido completo
de `datos_procesados/` y `resultados/`, sin intervención manual. Ver el
detalle de cada script en `scripts/README_ejecucion_scripts_analisis.md`.

## Tablas generadas

| Tabla | Contenido |
|---|---|
| `tabla_1_resumen_clasificaciones.csv` | Resumen de clasificaciones por fuente (detector vs. expertos). |
| `tabla_2_metricas_detector.csv` | Exactitud, precisión, sensibilidad, especificidad, F1 y kappa del detector frente al consenso experto. |
| `tabla_3_matriz_confusion.csv` | Matriz de confusión detector vs. consenso. |
| `tabla_4_acuerdo_interevaluador.csv` | Kappa de Cohen por pares y Kappa de Fleiss del panel de expertos. |
| `tabla_5_consenso_por_requisito.csv` | Consenso experto para cada uno de los 61 requisitos. |
| `tabla_6_tipos_ambiguedad.csv` | Frecuencia de cada tipo de mal olor entre las marcaciones de ambigüedad. |
| `tabla_7_confianza_evaluadores.csv` | Confianza autorreportada por evaluador. |
| `tabla_8_significancia_estadistica.csv` | IC 95 % (bootstrap) de las métricas globales y prueba de chi-cuadrado detector-consenso. |
| `tabla_9_correspondencia_afirmacion_resultado.csv` | Correspondencia entre cada afirmación del manuscrito y la tabla/figura que la sustenta. |
| `tabla_10_significancia_por_categoria.csv` | Exactitud, precisión, sensibilidad, especificidad y F1 con IC 95 % (bootstrap), desglosados por tipo de requisito (RF, RNF, RD, RL). |
| `tabla_11_justificacion_muestra_detector.csv` | Justificación del tamaño de muestra del detector (N=61): potencia alcanzada para el efecto observado, efecto mínimo detectable con ese N, y comparación con el N que habría hecho falta para efectos menores. |

## Diccionario de datos

Ver `diccionario_datos.csv`: describe, columna por columna, nombre, tipo,
unidad, rango admisible, codificación de valores perdidos y procedencia de
cada archivo de `datos_crudos/` y `datos_procesados/`.

## Desviaciones respecto del protocolo

Ver `desviaciones.md`.

## Identificador persistente del depósito

Ver `registro_deposito.md`.

## Licencia

Los datos de esta carpeta se distribuyen bajo la licencia indicada en
`LICENSE-DATA.txt`, distinta de la licencia del código del proyecto.


