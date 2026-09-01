# ANONYMIZATION.md — Procedimiento de anonimización y seudonimización

**Proyecto:** MundiPets — Proyecto Fin de Curso, Ingeniería de Requerimientos [20303], UTEQ, 2026–2027 PPA
**Alcance de este documento:** describe cómo se anonimizó o seudonimizó cada tipo de evidencia antes de su inclusión en este paquete de replicación depositado en Zenodo, en cumplimiento de la Sección 3 de la Guía y Rúbrica de la Entrega 4 (2B) y de la Ley Orgánica de Protección de Datos Personales del Ecuador (LOPDP, Registro Oficial Suplemento 459, 26 de mayo de 2021).

## 1. Principio general

Todo el material publicado en este depósito corresponde a la **zona pública
[P]** definida en la Sección 3 de la guía del curso. El material identificable
(zona restringida [R]) nunca sale del repositorio de GitHub del equipo, donde
permanece dentro de un contenedor cifrado con AES-256, con la contraseña
entregada únicamente al docente responsable por el Sistema de Gestión
Académica (SGA). Ningún archivo de este depósito de Zenodo proviene de la
zona restringida sin pasar antes por el procedimiento descrito abajo.

## 2. Esquema de seudonimización

Cada persona participante recibe un código de participante que sustituye su
nombre en todo el material público, siguiendo el patrón `TIPO-NN`:

| Prefijo | Rol |
|---|---|
| `PROP-NN` | Propietario o propietaria de mascota |
| `VET-NN` | Médico o médica veterinaria |
| `EXP-NN` | Experto o experta evaluadora (panel del componente empírico) |
| `OBS-NN` | Sesión de observación directa |

Este código es el único identificador de persona que aparece en nombres de
archivo, transcripciones, actas y fichas técnicas de la zona pública. La
correspondencia entre el código y la identidad real solo existe en los
consentimientos informados originales, guardados en la zona restringida
cifrada; no se distribuye ninguna tabla de correspondencia código↔nombre
fuera de ese contenedor.

**Nota de verificación abierta:** al auditar el repositorio se detectaron tres
archivos de consentimiento del panel de expertos
(`06_Experimento/instrumentos/`) nombrados con el nombre y apellido real de
la persona en lugar de su código `EXP-NN`. Antes de subir el paquete final a
Zenodo, el equipo debe confirmar que estos tres archivos fueron renombrados
al esquema `EXP-01`/`EXP-02`/`EXP-03`, que la cédula y la firma quedaron
enmascaradas en la copia pública, y que el archivo original íntegro se movió
al contenedor cifrado. Ningún archivo con nombre propio de una persona debe
llegar a Zenodo.

## 3. Tratamiento por tipo de evidencia

### 3.1 Transcripciones de entrevistas

- El nombre propio de la persona entrevistada nunca aparece en el cuerpo del
  texto; los turnos de habla se etiquetan genéricamente como
  **Entrevistador** / **Entrevistado**.
- El nombre del archivo lleva fecha, tipo de participante y código de
  participante (ejemplo: `2026-05-17_PropietarioMascota_PROP-01_TranscripcionEntrevista.md`),
  nunca el nombre propio.
- Se revisó cada transcripción para eliminar menciones incidentales de
  nombres propios de terceros (por ejemplo, el nombre de una mascota o de un
  familiar) que pudieran aparecer espontáneamente durante la entrevista.
- Los audios y videos originales de estas entrevistas permanecen únicamente
  en la zona restringida cifrada; no se publica ningún archivo de audio o
  video en este depósito.

### 3.2 Consentimientos informados

- La copia pública (`02_Evidencias/Consentimientos/` en el repositorio de
  GitHub) muestra el documento con la **cédula y la firma cubiertas** y el
  código de participante visible.
- El documento original íntegro, con firma y cédula legibles, se conserva
  exclusivamente en la zona restringida cifrada.
- Ningún consentimiento, ni en su versión pública ni en su versión completa,
  forma parte de este depósito de Zenodo: los consentimientos son evidencia
  del repositorio de GitHub, no del paquete de datos de investigación.

### 3.3 Fotografías y material del entorno

- Toda fotografía publicada (`02_Evidencias/Fotos_Entorno/`,
  `Cuestionario/Fotos_Aplicacion/`) fue revisada para excluir rostros
  reconocibles de personas y metadatos de coordenadas GPS (EXIF).
- Las fotografías del entorno veterinario documentan procedimientos,
  instalaciones o el uso de la aplicación, no a las personas que los
  realizan.

### 3.4 Respuestas del cuestionario

- El archivo `respuestas_cuestionario.csv` de este paquete se generó a partir
  del cuestionario original **eliminando** cualquier columna de nombre,
  correo electrónico, número de teléfono o dirección IP.
- La única columna temporal es la marca de fecha y hora de la respuesta, que
  no es un dato identificable por sí sola.
- Las respuestas de texto libre fueron revisadas para verificar que ninguna
  persona escribió, sin que se le pidiera, su nombre completo u otro dato de
  contacto dentro de una respuesta abierta.

### 3.5 Actas de validación (*walkthrough* y *member checking*)

- Las actas públicas muestran el código de participante, no el nombre propio,
  y no incluyen imagen de firma.
- La grabación de cada sesión permanece únicamente en la zona restringida
  cifrada.

### 3.6 Corpus de requisitos y clasificaciones del experimento

- El corpus de 61 requisitos (Sección 2.3 de `README_dataset.md`) no contiene
  datos personales: son especificaciones funcionales, no funcionales y
  restricciones de diseño del sistema, redactadas por el equipo.
- El identificador anónimo `REQ-01`…`REQ-61` asignado a cada requisito
  (Sección 3.4 del manuscrito) no identifica a ninguna persona; identifica un
  ítem de la especificación. Su propósito es cegar a los evaluadores respecto
  del tipo de requisito (RF/RNF/RD), no proteger datos personales.
- Las clasificaciones y justificaciones de los tres expertos evaluadores se
  publican asociadas a su rol (`Experto 1`, `Experto 2`, `Experto 3`) y no a
  su nombre. La correspondencia entre `Experto N` y la identidad real de la
  persona solo existe en el consentimiento de rol firmado por cada experto,
  conservado en la zona restringida (ver nota de verificación de la
  Sección 2).

## 4. Verificación técnica

El hash SHA-256 de cada archivo multimedia se calcula **antes** de cifrarlo y
se registra en `fichas_tecnicas.csv` (zona restringida del repositorio de
GitHub). Este mecanismo permite al docente responsable verificar, mediante
`sha256sum -c`, que el contenido del contenedor cifrado corresponde
exactamente a lo declarado, sin necesidad de descifrarlo fuera del entorno de
evaluación. Ningún archivo de este depósito de Zenodo requiere dicha
verificación porque ninguno proviene de la zona restringida.

## 5. Base legal

El procedimiento de minimización y seudonimización descrito en este documento
sigue los principios de la LOPDP del Ecuador (Art. 25, minimización de datos;
Art. 39, protección de datos desde el diseño y por defecto) y los principios
FAIR de gestión de datos científicos (Wilkinson et al., 2016). El alcance del
consentimiento firmado por cada persona participante se documenta en
`ETHICS.md`.
