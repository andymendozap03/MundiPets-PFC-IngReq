# 07_Datos — Paquete de datos del componente empírico (Enfoque 2)

## Qué contiene

| Carpeta | Contenido |
|---|---|
| `datos_crudos/` | Salida original del detector automático y de la evaluación de los tres expertos, sin ninguna edición manual. |
| `datos_procesados/` | Consenso experto y contraste detector-consenso, generados exclusivamente por script a partir de `datos_crudos/`. |
| `scripts/` | Los cinco scripts de análisis y el orquestador único `run_all.py`. |
| `resultados/` | Las cuatro figuras y las nueve tablas citadas en el manuscrito, generadas por los scripts. |

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

---
Generado: 2026-09-03
