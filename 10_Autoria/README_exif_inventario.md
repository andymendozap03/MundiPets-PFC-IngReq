# Nota sobre `exif_inventario.csv`

Este inventario cubre las 9 fotografías reales del proyecto: las 3 fotos del
equipo (`10_Autoria/fotos_equipo/`) y las 6 fotos de aplicación del
cuestionario (`02_Evidencias/Cuestionario/Fotos_Aplicacion/`).

## Por qué 6 de las 9 fotografías no tienen fecha ni dispositivo EXIF

Las fotos `EvidenciaEncuestado_01` a `06` fueron recibidas por el equipo a
través de WhatsApp, enviadas directamente por las personas encuestadas como
evidencia de haber respondido el cuestionario. WhatsApp recomprime
automáticamente toda imagen enviada por chat y, como parte de ese proceso,
elimina los metadatos EXIF originales (fecha de captura, modelo de
dispositivo, GPS), dejando únicamente el perfil de color del dispositivo de
origen — lo cual sí se verificó y quedó reflejado en el inventario (perfiles
de Apple y de Google detectables en cada archivo).

Esta es una limitación técnica de la vía de recepción del archivo, no una
omisión del equipo: las 3 fotos del equipo se tomaron directamente con el
celular usado para depositarlas en el repositorio (sin pasar por WhatsApp),
por lo que sí conservan el EXIF completo.

## Qué sí se verificó para las 6 fotos sin EXIF

- Hash SHA-256 real de cada archivo, calculado directamente sobre el
  contenido del que se dispone.
- Perfil de color embebido (ICC), que confirma que provienen de un
  dispositivo real (Apple o Google) y no fueron generadas o alteradas
  artificialmente.

Ninguna fecha ni dispositivo fue inventado para completar el inventario: donde
el metadato no existe, el CSV lo declara explícitamente como `SIN EXIF`.
