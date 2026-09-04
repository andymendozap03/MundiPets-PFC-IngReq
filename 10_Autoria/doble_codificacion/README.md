# Doble codificación (elemento A7 — evidencia de autoría)

Esta carpeta corresponde al elemento **A7** de la guía de desarrollo: evidencia
de que dos integrantes del equipo codificaron, de forma **independiente**, el
mismo subconjunto del corpus de requisitos, más el cálculo del coeficiente de
acuerdo entre ambos.

Esto es distinto del panel de expertos (EXP-01/02/03) usado en el componente
empírico del estudio (`06_Experimento` / `07_Datos`): aquella es evidencia
científica del detector; esta carpeta es evidencia de **trabajo propio del
equipo**.

## Contenido

| Archivo | Qué es |
|---|---|
| `muestra_seleccionada.csv` | Los 18 requisitos (≈30% del corpus de 61) elegidos aleatoriamente con semilla fija (42) para la doble codificación. Referencia, no se edita. |
| `hoja_codificacion_AndyMendoza.csv` | Hoja a completar por Andy Mendoza. |
| `hoja_codificacion_EdsonFuertes.csv` | Hoja a completar por Edson Fuertes. |
| `calcular_acuerdo.py` | Script que calcula el Kappa de Cohen, el acuerdo observado y su intervalo de confianza al 95% (bootstrap), a partir de las dos hojas ya completadas. |
| `requirements.txt` | Librerías necesarias para ejecutar el script. |

## Procedimiento

1. **Andy y Edson codifican por separado, sin verse ni discutir entre sí**,
   cada uno su propia copia de la hoja (`Clasificacion`: Ambiguo / No ambiguo;
   `Tipo_Mal_Olor`: Ninguno / Cuantificador vago / Terminología imprecisa /
   Conjunción múltiple / Requisito no verificable; `Justificacion`: texto
   libre; `Confianza`: escala 1 a 5). Usen el mismo criterio que se documentó
   en la rúbrica de clasificación experta del panel, para que el ejercicio
   sea comparable.
2. Cuando **ambas hojas estén completas**, instalen las dependencias y
   ejecuten el script:

   ```bash
   pip install -r requirements.txt
   python calcular_acuerdo.py
   ```

3. Esto genera `resultado_acuerdo_doble_codificacion.csv` con el Kappa, el
   acuerdo observado, el intervalo de confianza y el detalle de cualquier
   discrepancia entre ambos evaluadores.
4. No editen a mano el resultado — si algo no cuadra, corrijan la hoja de
   codificación y vuelvan a correr el script.

## Nota

Si alguna clasificación cambia después de una discusión posterior entre
ambos (algo normal y esperable), documenten esa decisión en
`10_Autoria/bitacora_sesiones.csv`, pero conserven también la codificación
**original** de cada uno tal como la hicieron por separado — es esa
independencia inicial la que da valor a la evidencia.
