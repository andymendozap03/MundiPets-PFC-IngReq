# Evidencias restringidas — 02_Evidencias/00_Restringido/

## Por qué el contenedor está dividido en varias partes

El material de la zona restringida (videos y audios originales de entrevistas,
consentimientos con firma y cédula visibles, actas de walkthrough firmadas y
documentos originales de la organización cliente) pesa en conjunto
aproximadamente **5.19 GB** antes de dividir.

GitHub, incluso usando Git LFS, tiene un límite de **2 GB por archivo
individual** en el plan gratuito (y de 100 MB sin LFS). Para poder mantener
toda la evidencia **dentro del repositorio**, tal como exige la guía de la
Entrega 3 (2A) — Sección 4.1, "Toda la evidencia reside *dentro* del
repositorio" — el contenedor cifrado se dividió en volúmenes de 1000 MB
(1 GB) cada uno usando la función nativa de 7-Zip ("Dividir en volúmenes"),
en lugar de subir el material a un servicio externo (lo cual la guía
penaliza explícitamente en la Sección 2.1).

## Archivos que componen el contenedor

```
evidencias_restringidas.7z.001
evidencias_restringidas.7z.002
evidencias_restringidas.7z.003
evidencias_restringidas.7z.004
evidencias_restringidas.7z.005
evidencias_restringidas.7z.006
...                              (el numero exacto de partes depende
                                   del tamano final del contenido,
                                   aprox. 6 partes de 1000 MB cada una)
```

Estos archivos **no se pueden abrir por separado**. Son fragmentos de un
único archivo `.7z` cifrado con AES-256 y con nombres de archivo también
cifrados.

## Cómo reconstruir y abrir el contenedor

1. Descarga o clona el repositorio completo, asegurándote de que **todas**
   las partes `.7z.001`, `.7z.002`, etc. estén en la misma carpeta
   `02_Evidencias/00_Restringido/`.
2. Con 7-Zip instalado, haz doble clic en el archivo `.7z.001` (el primero
   de la secuencia). 7-Zip reconoce automáticamente los volúmenes
   siguientes y reconstruye el contenido original.
3. Se solicitará la contraseña, entregada únicamente al docente por el
   espacio de la actividad en el Sistema de Gestión Académica (SGA), tal
   como establece la Sección 4.1 de la guía. La contraseña **no** se
   encuentra en este repositorio ni en ningún archivo de texto adjunto.
4. Una vez descifrado, el contenido se puede verificar contra
   `fichas_tecnicas.csv` (en esta misma carpeta) usando `sha256sum -c`
   sobre el hash de cada archivo, calculado **antes** de cifrar.
