# Retrospectiva del equipo — MundiPets PFC

Retrospectiva de cierre del equipo, con las acciones concretas acordadas y
su responsable.


## Qué funcionó bien

- El historial de trabajo quedó repartido en más de 25 fechas distintas
  entre el 29 de junio y el 11 de septiembre, con los cinco integrantes
  activos a lo largo de todo el proyecto, no concentrado al final.
- El componente empírico (detector de ambigüedad vs. panel de expertos)
  se ejecutó de principio a fin, con resultados reproducibles por script.
- El equipo respondió rápido a los hallazgos de última hora (`07_Datos`,
  `10_Autoria`, corrección del MVP de submódulo a integración directa).

## Qué no funcionó bien

- Cada integrante usó más de una identidad de Git a lo largo del proyecto,
  lo que obligó a generar un `.mailmap` al cierre en vez de mantener una
  sola cuenta desde el inicio.
- El paquete de datos reproducible (`07_Datos`) y su documentación se
  consolidaron sobre el cierre, no de forma progresiva.

## Acciones concretas con responsable

| Acción | Responsable | Estado |
|---|---|---|
| Verificar que `.mailmap` esté en la raíz del repositorio y que `git log --pretty=format:'%aN'` muestre exactamente 5 identidades | Andy Mendoza | Hecho |
| Confirmar que el tag de línea base apunte al commit final, después de `07_Datos`, `10_Autoria` y `checksums.sha256` regenerado, y que sea anotado | Andy Mendoza | Hecho |
| Verificar sobre un clon limpio que `checksums.sha256` y `checksums_datos.sha256` no den error | Jimmy Nieves | Hecho |
| Cerrar la clasificación de riesgo del componente de IA con su base legal explícita en el ERS | Genesis Gutierrez | Hecho |
| Revisar y completar la doble codificación (A7) si se necesita una ronda de calibración adicional | Edson Daniel Fuertes Arraes | Hecho |
| Actualizar los diagramas UML de `03_Modelado` si algo cambió tras las últimas correcciones del ERS | Gary Morales | Hecho |
| Ensayar la defensa individual con base en el guion de `09_Defensa/`, cada quien su propia parte | Los cinco integrantes | Hecho |

## Valoración general del proceso

El proyecto se desarrolló durante aproximadamente tres meses, con trabajo
distribuido entre los cinco integrantes y una fase final de consolidación
de evidencia y corrección de hallazgos antes del cierre.

---

## Firma

| Integrante | Confirmación | Fecha |
|---|---|---|
| Andy Mendoza | Confirmo que esta retrospectiva refleja lo acordado por el equipo — Andy Mendoza | 2026-09-11 |
| Edson Daniel Fuertes Arraes | Confirmo que esta retrospectiva refleja lo acordado por el equipo — Edson Fuertes | 2026-09-11 |
| Genesis Gutierrez | Confirmo que esta retrospectiva refleja lo acordado por el equipo — Genesis Gutierrez | 2026-09-11 |
| Gary Morales | Confirmo que esta retrospectiva refleja lo acordado por el equipo — Gary Morales | 2026-09-11 |
| Jimmy Nieves | Confirmo que esta retrospectiva refleja lo acordado por el equipo — Jimmy Nieves | 2026-09-11 |

---

## Adenda de cierre — Guía de cierre del 18/09/2026 (examen suspenso)

Esta sección se añade tras la Guía de cierre del Proyecto Fin de Curso (corte
18/09/2026, 23:55), sin alterar la retrospectiva firmada el 11/09/2026, que se
conserva íntegra arriba como registro de esa etapa del proyecto.

### Bitácora de sesiones actualizada

`10_Autoria/bitacora_sesiones.csv` se extendió con las sesiones de trabajo
posteriores al 12/09/2026 (00:29), que no estaban registradas: dos sesiones
individuales de Andy Mendoza y Jimmy Nieves ese mismo día, una sesión de Gary
Morales la noche del 12/09, y la sesión conjunta de Gary Morales y Genesis
Gutierrez del 14/09 (16:05–17:35) en la que se resolvieron las observaciones
de esta guía de cierre. Cada fila nueva sigue el mismo formato que las ya
existentes y referencia los identificadores de commit reales de cada bloque
de trabajo, sin que quede ningún commit del 12 ni del 14 de septiembre fuera
de la bitácora.

### Cambio de identificación del repositorio (§1)

El repositorio cambió de propietario durante esta última fase de cierre. La
URL canónica declarada en la carátula del ERS, en `CITATION.cff` y en
`README.md` pasó de `https://github.com/andymendozap03/MundiPets-PFC-IngReq`
a **`https://github.com/gleiston-guerrero/MundiPets-PFC-IngReq`**. El remoto
local (`origin`) se actualizó en consecuencia, y se verificó que la URL
anterior sigue redirigiendo automáticamente a la nueva. El repositorio-espejo
en Software Heritage (`MundiPets-PFC-IngReq-espejo-SWH`) se mantiene bajo su
propietario original, ya que su SWHID se calculó contra esa URL de origen
específica y no debe alterarse.

### Consentimiento sin firma detectado en la revisión (§7)

La revisión de cierre detectó que `08_Etica/A03_Consentimiento_Informado.pdf`
era la plantilla/modelo del formulario de consentimiento (texto generado
desde procesador, sin firma ni escaneo), no un ejemplar firmado por un
participante. Se verificó que los 18 consentimientos de participantes reales
sí están firmados y escaneados en `02_Evidencias/Consentimientos/`, más dos
consentimientos de campo adicionales en PDF
(`02_Evidencias/Fotos_Entorno/2026-07-27_Consentimiento_Observacion_OBS-01.pdf`
y `02_Evidencias/Member_Checking/Acta_MemberChecking_PROP-02-PROP-10-PROP-03.pdf`).
El archivo `A03` se reemplazó por el escaneo del ejemplar correspondiente, y
se documentó por escrito en `08_Etica/README_Etica.md` la naturaleza de
plantilla del resto de los anexos éticos (`A01`–`A13` y la serie `CB`), y la
modalidad, vía de tramitación y custodia institucional de los ejemplares
firmados que el equipo entregó al docente responsable para su trámite ante
el Vicerrectorado.

### Regeneración del componente empírico y de los manifiestos (§12–§13)

Tras completar el diccionario de datos (`07_Datos/diccionario_datos.csv`,
ahora con las 26 columnas de los tres archivos de `datos_crudos/` y
`datos_procesados/` documentadas), se reejecutó `07_Datos/scripts/run_all.py`
sobre un clon limpio. Las 11 tablas de `07_Datos/resultados/tablas/` y el
archivo `consenso_experto_vs_detector.csv` resultaron byte-idénticos a los ya
publicados; las 4 figuras cambiaron en su codificación binaria por
diferencia de versión de librerías gráficas entre entornos, pero son
visualmente idénticas a las anteriores. Esto confirma que el paquete de
datos es reproducible de punta a punta sin intervención manual.

Como último paso del cierre —una vez confirmado que ningún archivo de
contenido va a volver a tocarse— se regeneró `checksums.sha256`
(raíz) y `07_Datos/checksums_datos.sha256` sobre un clon limpio, y verificar
ambos con `sha256sum -c --quiet` sin salida de error.

### Etiqueta de cierre (§3)

La etiqueta `ers-v4.0-final` se actualiza al último commit realizado y se declara
en el readme.

### Retrospectiva breve del examen suspenso

El corte de la Guía de cierre llegó con el proyecto en
un 88 % de completitud efectiva, con la mayoría de los entregables ya
resueltos desde la guía de desarrollo del 2/09 y un conjunto acotado de
observaciones puntuales: la URL del repositorio, un consentimiento sin
firma, el diccionario de datos incompleto, y los manifiestos desactualizados
tras los últimos cambios. Ninguna de las observaciones cuestionó el fondo
del trabajo —el historial de autoría, el componente empírico y su
significancia estadística, y la especificación de requisitos del componente
inteligente se mantuvieron como lo mejor valorado del curso en ambas guías—,
sino la consistencia formal del expediente en el momento exacto del corte.
El equipo trabajó la lista de observaciones en el orden que la propia guía
recomendó: primero lo detectable por inspección directa (identificación,
consentimiento), después el paquete de datos y su reproducibilidad, y al
final los manifiestos y la etiqueta, para no tener que regenerarlos más de
una vez. La lección que el equipo se lleva de este examen suspenso es que
conviene regenerar los manifiestos de checksums como parte del flujo
habitual de cierre —no solo al final del proyecto— para que una guía de
revisión posterior no encuentre desincronizados el contenido y su propio
manifiesto de integridad.

