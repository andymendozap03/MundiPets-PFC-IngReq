# Nota sobre `exif_inventario.csv`

Este inventario cubre las **29 fotografías reales** del proyecto: las 3 fotos
del equipo (`10_Autoria/fotos_equipo/`), las 6 fotos de aplicación del
cuestionario (`02_Evidencias/Cuestionario/Fotos_Aplicacion/`) y las 20 fotos
de entorno de la observación OBS-01 (`02_Evidencias/Fotos_Entorno/`).

## Por qué 6 de las 29 fotografías no tienen fecha ni dispositivo EXIF (fotos de aplicación del cuestionario)

Las fotos `EvidenciaEncuestado_01` a `06` fueron recibidas por el equipo a
través de WhatsApp, enviadas directamente por las personas encuestadas como
evidencia de haber respondido el cuestionario. WhatsApp recomprime
automáticamente toda imagen enviada por chat y, como parte de ese proceso,
elimina los metadatos EXIF originales (fecha de captura, modelo de
dispositivo, GPS). En 5 de las 6 fotos (`_02` a `_06`) sobrevive el perfil de
color del dispositivo de origen, verificado con `exiftool`: `_02` y `_03`
llevan `Profile Copyright: Google Inc. 2016`, y `_04`, `_05` y `_06` llevan
`Profile Copyright: Copyright Apple Inc., 2022`. La foto `_01` no conserva
ningún perfil de color embebido — no hay ningún dato, ni EXIF ni de perfil,
que permita inferir el dispositivo de origen; el CSV la marca como
`SIN EXIF` igual que las demás, sin atribuir ningún fabricante.

## Por qué las 20 fotos de entorno (OBS-01) no tienen fecha ni dispositivo EXIF

Las fotos `*_FotosEntorno.png` están en formato **PNG**. A diferencia del
JPEG, el formato PNG no define campos de metadatos de captura tipo EXIF
(`DateTimeOriginal`, `Model`, GPS, etc.). Se verificó con `exiftool` que
ninguno de los 20 archivos contiene esos campos: no hay fecha de captura ni
modelo de dispositivo en ninguno.

Aclaración importante para no confundir esto con una omisión: 4 de los 20
archivos (`CorteDePeloPerro`, `EcografiaGato`, `InyeccionPerro` y
`RegistroInformacionPerro`) sí traen un chunk estándar de PNG (`tIME`) con
una fecha — por ejemplo `2026:07:29 01:45:32` — dos días posterior a la
fecha que llevan en el nombre de archivo (27 de julio). Ese chunk **no es
EXIF y no es fecha de captura**: es la marca de última modificación del
propio archivo PNG, típicamente escrita por la herramienta que lo exportó o
editó por última vez, y por eso no coincide con la fecha real de la sesión
de observación. No se usó ese dato para rellenar la columna
`fecha_captura_exif` del inventario, precisamente porque no es una fecha de
captura fiable ni verificable contra el momento real en que se tomó la foto;
las 20 filas se mantienen como `SIN EXIF` por igual. Las 16 fotos restantes
no traen ningún chunk de fecha.

Esta ausencia de EXIF de captura es una limitación del formato de archivo
(PNG), no una omisión del equipo ni un caso equivalente al de WhatsApp: las
imágenes no perdieron metadatos por recompresión de una app de mensajería,
sino que se generaron o exportaron directamente en un formato que no
transporta ese tipo de dato.

Además, las 20 fotografías de entorno pasaron por un proceso de edición
posterior a la captura: se censuraron los rostros de las personas que
aparecen en ellas (pacientes, personal del centro veterinario y
transeúntes), para proteger su identidad conforme al tratamiento de datos
personales declarado en `08_Etica/`. La edición se realizó con una
herramienta en línea (basada en navegador/web), lo cual es coherente con la
ausencia de un campo `Software` o `CreatorTool` en los metadatos: a
diferencia de una aplicación de escritorio instalada localmente, muchas
herramientas de edición en línea no escriben ese dato al exportar la imagen
resultante, por lo que no hay forma de identificar la herramienta específica
a partir del archivo. Ese reprocesamiento —editar en línea y exportar la
imagen ya censurada como PNG— es coherente con, y explica en parte, la fecha
de modificación (`tIME`) posterior a la de captura que se observa en 4 de
los 20 archivos (ver más abajo): el archivo que hoy está en el repositorio
no es el original de cámara, sino el resultado de esa edición en línea, por
lo que es normal que su metadato de "última modificación" no coincida con
el momento en que se tomó la foto. La ausencia de EXIF de captura, entonces,
responde tanto a la naturaleza del formato PNG como al propio paso de
edición por el que se generó el archivo final.

## Qué sí se verificó para las 26 fotos sin EXIF

- Hash SHA-256 real de cada archivo, calculado directamente sobre el
  contenido del que se dispone.
- Para 5 de las 6 fotos de WhatsApp (`_02` a `_06`): perfil de color
  embebido (ICC), que confirma que provienen de un dispositivo real (Apple
  o Google) y no fueron generadas o alteradas artificialmente. La foto
  `_01` no tiene perfil de color ni ningún otro dato de origen.
- Para las 20 fotos de entorno: inspección completa de metadatos con
  `exiftool` (formato, dimensiones, perfil de render, y chunks auxiliares
  `tIME`/`tEXt` donde existen), confirmando ausencia total de campos EXIF
  de captura (`DateTimeOriginal`, `Model`, GPS) en las 20, y presencia de
  una fecha de modificación de archivo (no de captura) en 4 de ellas. La
  censura de rostros con una herramienta en línea es información del
  proceso de trabajo del equipo, no algo detectable con certeza desde los
  metadatos: ninguna de las 20 declara un campo `Software` o
  `CreatorTool` (comportamiento típico de las herramientas de edición web,
  a diferencia de las de escritorio), así que ni la censura ni la
  herramienta usada quedan acreditadas por el propio archivo, solo por el
  conocimiento directo del equipo sobre cómo se generaron estas imágenes.

Ninguna fecha ni dispositivo fue inventado para completar el inventario:
donde el metadato no existe, el CSV lo declara explícitamente como
`SIN EXIF`, junto con la razón técnica específica de cada caso.
