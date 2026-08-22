# Ejecución del análisis de MundiPets

Este documento explica cómo ejecutar el análisis completo del componente empírico del proyecto MundiPets: generación de tablas, figuras y significancia estadística.

## 1. Estructura esperada

Los datos de entrada viven en `06_Experimento/datos_crudos/`, no dentro de `scripts_analisis/`. La estructura real y completa de `06_Experimento/` es:

```text
06_Experimento/
├── README_osf_registration.md
├── protocolo.pdf
├── osf_registration.pdf
├── osf_deviations.pdf
├── datos_crudos/
│   ├── evaluacion_expertos.csv
│   ├── salida_detector.csv
│   └── MundiPets_Datos_Crudos_06_Experimento.xlsx
├── datos_procesados/
│   ├── consenso_experto_vs_detector.csv
│   ├── README_procesamiento.md
│   └── MundiPets_Datos_Procesados_06_Experimento.xlsx
├── instrumentos/
│   ├── rubrica_clasificacion_experta.xlsx
│   └── (consentimientos de los 3 expertos del panel)
├── prompts_llm/
│   └── README_prompts_llm.md
├── resultados/
│   ├── tablas/
│   └── figuras/
└── scripts_analisis/
    ├── 03_generar_tablas_figuras_excel_corregido.py
    ├── 04_calcular_significancia_estadistica.py
    ├── run_all.py
    ├── requirements.txt
    ├── README_ejecucion_scripts_analisis.md   (este documento)
    └── datos_entrada/   (copia de respaldo, ya no es la fuente que usa el script)
```

Este documento se enfoca únicamente en `scripts_analisis/` — para el resto de `06_Experimento/` no hace falta hacer nada al ejecutar el análisis.

## 2. Abrir la terminal dentro de `scripts_analisis`

1. Abra la carpeta `06_Experimento/scripts_analisis` en el Explorador de archivos de Windows.
2. Haga clic en la barra de dirección de la carpeta.
3. Escriba `cmd` y presione `Enter`.

La ruta debe verse similar a:

```text
C:\Users\NombreUsuario\Desktop\...\06_Experimento\scripts_analisis>
```

## 3. Instalar las librerías necesarias

Este paso se realiza solamente la primera vez (o si aparece un error de "librería no encontrada").

```cmd
pip install -r requirements.txt
```

Si ese comando da error de "no se encuentra el archivo", instale directamente:

```cmd
pip install matplotlib scikit-learn numpy scipy
```

## 4. Ejecutar TODO el análisis con un solo comando

```cmd
python run_all.py
```

Este comando ejecuta, en orden, los dos scripts de análisis:

1. **`03_generar_tablas_figuras_excel_corregido.py`** — genera las tablas 1 a 7 y las 4 figuras (exactitud, precisión, sensibilidad, especificidad, F1, kappa de Cohen/Fleiss, matriz de confusión).
2. **`04_calcular_significancia_estadistica.py`** — genera la tabla 8, con el intervalo de confianza al 95% (bootstrap, 10 000 réplicas) de cada métrica y la prueba de hipótesis (chi-cuadrado de independencia, con estadístico, grados de libertad, valor p y tamaño del efecto).

No es necesario escribir rutas ni argumentos manualmente — `run_all.py` ya sabe dónde están los datos y dónde guardar los resultados.

## 5. Archivos generados

Al terminar, en `06_Experimento/resultados/tablas/` deben aparecer:

```text
tabla_1_resumen_clasificaciones.csv
tabla_2_metricas_detector.csv
tabla_3_matriz_confusion.csv
tabla_4_acuerdo_interevaluador.csv
tabla_5_consenso_por_requisito.csv
tabla_6_tipos_ambiguedad.csv
tabla_7_confianza_evaluadores.csv
tabla_8_significancia_estadistica.csv   <- nueva (IC 95% + valor p)
```

Y en `06_Experimento/resultados/figuras/`:

```text
figura_1_clasificaciones_por_fuente.png
figura_2_matriz_confusion.png
figura_3_coeficientes_kappa.png
figura_4_tipos_ambiguedad.png
```

Todas las tablas se generan con codificación UTF-8 con BOM y separador `;` (punto y coma), compatibles con la configuración regional de Excel en español — se abren correctamente con doble clic, sin caracteres corruptos ni columnas mal separadas.

## 6. Ejecución manual (alternativa, no recomendada)

Si por algún motivo no se puede usar `run_all.py`, cada script puede ejecutarse por separado:

```cmd
python 03_generar_tablas_figuras_excel_corregido.py --detector ..\datos_crudos\salida_detector.csv --expertos ..\datos_crudos\evaluacion_expertos.csv --output ..\resultados

python 04_calcular_significancia_estadistica.py
```

## 7. Problemas frecuentes

### El comando `python` no funciona

Pruebe con `py` en lugar de `python`:

```cmd
py run_all.py
```

### Falta una librería

```cmd
pip install -r requirements.txt
```

### No se encuentran los archivos CSV / "no se encontró el archivo esperado"

Confirme que existe la carpeta `06_Experimento/datos_crudos/` (como hermana de `scripts_analisis/`, no dentro de ella) y que contiene exactamente:

```text
evaluacion_expertos.csv
salida_detector.csv
```

### Las tablas aparecen en una sola columna, o con acentos corruptos, al abrirlas en Excel

Esto ya está resuelto en la versión actual de ambos scripts (codificación UTF-8 con BOM + separador `;`). Si aún así ocurre, verifique que está usando la versión más reciente de `03_generar_tablas_figuras_excel_corregido.py` y `04_calcular_significancia_estadistica.py`, no una copia anterior.

## 8. Reproducibilidad

El procedimiento debe ejecutarse siempre con los mismos archivos de entrada (`datos_crudos/`) y sin modificar manualmente los resultados. `run_all.py` garantiza que cualquier persona (incluido el docente evaluador) pueda reproducir exactamente las mismas tablas y figuras del manuscrito ejecutando un único comando.
