# Ejecución del análisis de MundiPets

Este documento explica cómo organizar los archivos y ejecutar el script que genera las tablas y figuras del componente empírico del proyecto MundiPets.

## 1. Crear la carpeta principal

Cree una carpeta llamada:

```text
scripts_analisis
```

Dentro de esa carpeta deben colocarse:

```text
scripts_analisis/
├── 03_generar_tablas_figuras_excel_corregido.py
└── datos_entrada/
```

## 2. Crear la carpeta de datos de entrada

Dentro de `scripts_analisis`, cree una subcarpeta llamada:

```text
datos_entrada
```

En esta carpeta coloque los siguientes archivos:

```text
datos_entrada/
├── salida_detector.csv
└── evaluacion_expertos.csv
```

La estructura completa debe quedar así:

```text
scripts_analisis/
├── 03_generar_tablas_figuras_excel_corregido.py
└── datos_entrada/
    ├── salida_detector.csv
    └── evaluacion_expertos.csv
```

## 3. Abrir la terminal dentro de la carpeta

Abra la carpeta `scripts_analisis` en el Explorador de archivos de Windows.

Después:

1. Haga clic en la barra de dirección de la carpeta.
2. Escriba:

```text
cmd
```

3. Presione `Enter`.

Se abrirá la terminal directamente en la carpeta `scripts_analisis`.

La ruta debe verse de forma similar a:

```text
C:\Users\NombreUsuario\Desktop\scripts_analisis>
```

## 4. Instalar las librerías necesarias

Este paso se realiza solamente la primera vez.

En la terminal, copie y ejecute:

```cmd
py -m pip install matplotlib scikit-learn numpy
```

Espere hasta que la instalación termine correctamente.

## 5. Ejecutar el programa

En la misma terminal, copie y ejecute:

```cmd
py 03_generar_tablas_figuras_excel_corregido.py --detector datos_entrada\salida_detector.csv --expertos datos_entrada\evaluacion_expertos.csv --output resultados
```

El script procesará los datos del detector automático y las evaluaciones expertas.

## 6. Revisar los archivos generados

Después de ejecutar el programa, se creará automáticamente una carpeta llamada:

```text
resultados
```

La estructura final será:

```text
scripts_analisis/
├── 03_generar_tablas_figuras_excel_corregido.py
├── datos_entrada/
│   ├── salida_detector.csv
│   └── evaluacion_expertos.csv
└── resultados/
    ├── tablas/
    └── figuras/
```

Las tablas se encontrarán en:

```text
resultados\tablas
```

Las imágenes se encontrarán en:

```text
resultados\figuras
```

## 7. Archivos esperados

Dentro de `resultados\figuras` se generarán archivos como:

```text
figura_1_clasificaciones_por_fuente.png
figura_2_matriz_confusion.png
figura_3_coeficientes_kappa.png
figura_4_tipos_ambiguedad.png
```

Dentro de `resultados\tablas` se generarán archivos CSV con los resultados del análisis.

## 8. Problemas frecuentes

### El comando `py` no funciona

Pruebe con:

```cmd
python 03_generar_tablas_figuras_excel_corregido.py --detector datos_entrada\salida_detector.csv --expertos datos_entrada\evaluacion_expertos.csv --output resultados
```

### Falta una librería

Ejecute nuevamente:

```cmd
py -m pip install matplotlib scikit-learn numpy
```

### No se encuentran los archivos CSV

Verifique que los archivos tengan exactamente estos nombres:

```text
salida_detector.csv
evaluacion_expertos.csv
```

También confirme que estén dentro de la carpeta:

```text
datos_entrada
```

### Las tablas aparecen en una sola columna en Excel

Utilice el script:

```text
03_generar_tablas_figuras_excel_corregido.py
```

Este archivo genera tablas compatibles con la configuración regional de Excel en español.

## 9. Reproducibilidad

El procedimiento debe ejecutarse siempre con los mismos archivos de entrada y sin modificar manualmente los resultados. De esta forma, las tablas y figuras pueden reproducirse directamente desde los datos originales.
