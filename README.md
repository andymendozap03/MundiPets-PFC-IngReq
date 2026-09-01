# MundiPets — Plataforma para el Cruce y la Adopción Responsable de Mascotas

## Descripción

**MundiPets** es una aplicación web orientada a facilitar la adopción responsable, la evaluación de compatibilidad para cruzas y la gestión del historial médico de mascotas, conectando a propietarios, médicos veterinarios y criadores bajo criterios de bienestar animal y tenencia responsable.

Este repositorio contiene toda la documentación desarrollada durante el Proyecto Fin de Curso (PFC) de la asignatura **Ingeniería de Requerimientos [20303]**, cuarto nivel, paralelo B, de la Universidad Técnica Estatal de Quevedo (UTEQ), periodo académico **2026–2027 PPA**, siguiendo el estándar **ISO/IEC/IEEE 29148:2018** y el modelo de calidad **ISO/IEC 25010:2023**.

---

## Objetivos

- Elicitar requisitos mediante evidencia real de campo (entrevistas, encuestas, observación, Design Thinking y walkthrough).
- Elaborar una Especificación de Requisitos de Software (ERS/SRS) completa y trazable, conforme a IEEE/ISO/IEC 29148:2018.
- Modelar el sistema mediante UML completo y modelado organizacional i* (SD/SR).
- Mantener la trazabilidad extendida entre evidencias, requisitos, casos de uso, historias de usuario y mockups.
- Diseñar y desplegar un Producto Mínimo Viable (MVP) basado en los requisitos priorizados (MoSCoW, Kano, WSJF).
- Ejecutar un componente empírico (detección automática de ambigüedad en requisitos) con registro previo en el Open Science Framework (OSF).
- Preparar el proyecto para una publicación científica en una revista indexada en el Journal Citation Reports (JCR).

---

## Tecnologías y herramientas

- LaTeX (IEEEtran, biblatex/biber)
- Git y GitHub
- Visual Paradigm
- Draw.io
- Markdown
- Visual Studio Code
- Python (scripts de análisis estadístico del componente empírico)
- Open Science Framework (OSF) y Zenodo

---

## Integrantes y roles

| Integrante | Cédula | Correo institucional | Rol |
|---|---|---|---|
| Fuertes Arraes Edson Daniel | 0929115087 | efuertesa2@uteq.edu.ec | Analista líder |
| Gutiérrez Ortega Génesis Adriana | 1250274477 | ggutierrezo@uteq.edu.ec | Verificadora |
| Mendoza Párraga Andy Johel | 1251401590 | amedozap9@uteq.edu.ec | Modelador |
| Morales Sánchez Gary Alejandro | 1251154173 | gmoraless2@uteq.edu.ec | Documentador |
| Nieves Sánchez Jimmy Samuel | 1250907878 | jnievess@uteq.edu.ec | Verificador |

**Docente responsable:** Ing. Gleiston Guerrero Ulloa, PhD — gguerrero@uteq.edu.ec

---

## Responsabilidades

### Fuertes Arraes Edson Daniel — Analista líder
- Coordinación general del equipo y del cronograma.
- Validación de requisitos con stakeholders.
- Redacción de requisitos funcionales e historias de usuario.
- Gestión del repositorio Git y firma electrónica del documento ERS/SRS.

### Gutiérrez Ortega Génesis Adriana — Verificadora
- Control de calidad de los requisitos no funcionales.
- Verificación de los requisitos de explicabilidad (RNF de componentes IA/ML).
- Verificación del marco legal (trazabilidad LOPDP → RF/RNF).
- Revisión de evidencias de campo.

### Mendoza Párraga Andy Johel — Modelador
- Elaboración de los diagramas UML exigidos (casos de uso, clases, secuencia, actividades, estados, componentes, despliegue).
- Elaboración de los mockups de alta fidelidad (MU-01 a MU-08).

### Morales Sánchez Gary Alejandro — Documentador
- Estructuración del ERS/SRS conforme a ISO/IEC/IEEE 29148:2018.
- Descripción general, contexto del sistema y modelado organizacional i* (SD/SR).
- Consolidación de la matriz de trazabilidad extendida.

### Nieves Sánchez Jimmy Samuel — Verificador
- Responsable del componente empírico (detección automática de ambigüedad, Enfoque 2).
- Responsable del Producto Mínimo Viable (MVP).
- Responsable del paquete de publicación y del conjunto de datos depositado en Zenodo/OSF.

---

## Estado del proyecto

| Entrega | Hito oficial | Estado |
|---|---|---|
| Entrega 1 (1A) | Semana 4 — Planificación y elicitación inicial | Completada |
| Entrega 2 (1B) | Semana 10 — ERS/SRS parcial | Completada |
| Entrega 3 (2A) | Semana 13 — ERS/SRS completa, validación, trazabilidad, MVP y componente empírico | Completada |
| Entrega 4 (2B) / Defensa | Semana 17 — Manuscrito final y defensa | Completada |

---

## Estructura del repositorio

```text
MundiPets-PFC-IngReq/
├── .gitattributes
├── .gitignore
├── .gitmodules
├── CHANGELOG.md
├── checksums.sha256
├── CITATION.cff
├── fair_assessment.pdf              # Autoevaluación FAIR (F-UJI, 92 %)
├── LICENSE
├── README.md
│
├── 01_ERS/
│   ├── ERS_SRS_2B_v2.0.pdf
│   ├── ERS_SRS_2B_v2.0.tex
│   ├── referencias.bib
│   └── figuras/
│
├── 02_Evidencias/
│   ├── 00_Restringido/              # [R] zona restringida, cifrada AES-256
│   │   ├── fichas_tecnicas.csv
│   │   ├── README_evidencias_restringidas.md
│   │   └── evidencias_restringidas/ # volumen 7z fragmentado (audio/video originales)
│   ├── Codificacion_Tematica/
│   ├── Consentimientos/             # [P] copias enmascaradas
│   ├── Cuestionario/
│   │   ├── Fotos_Aplicacion/
│   │   ├── Respuestas/
│   │   └── power_calculation/       # Cálculo de potencia estadística (perfil dominante)
│   ├── Documentos_Organizacion/
│   ├── Fotos_Entorno/
│   ├── Member_Checking/
│   ├── Transcripciones/
│   └── Validacion_Walkthrough/
│
├── 03_Modelado/
│   ├── Diagramas_UML/
│   │   ├── Casos de Uso/
│   │   ├── Diagrama de Componentes/
│   │   ├── Diagrama de Contexto/
│   │   ├── Diagrama de Dependencia Estrategica/
│   │   ├── Diagrama de Despliegue/
│   │   ├── Diagrama de Razon Estrategica/
│   │   ├── Diagramas de Actividades/
│   │   ├── Diagramas de Clases/
│   │   ├── Diagramas de Maquinas de Estado/
│   │   └── Diagramas de Secuencia/
│   └── Mockups/
│
├── 04_Trazabilidad/
│   ├── matriz_trazabilidad.csv      # 61 filas
│   ├── priorizacion_moscow_kano.csv
│   └── sincronizacion_tablero.csv
│
├── 05_MVP/
│   ├── README.md
│   ├── codigo/                      # Submódulo Git → jnievess-lang/MVP_MundiPets.git
│   └── video_demo.mp4               # Git LFS
│
├── 06_Experimento/
│   ├── osf_registration.pdf
│   ├── osf_deviations.pdf
│   ├── protocolo.pdf
│   ├── README_osf_registration.md
│   ├── instrumentos/
│   ├── prompts_llm/
│   ├── datos_crudos/
│   ├── datos_procesados/
│   ├── resultados/
│   │   ├── figuras/
│   │   └── tablas/
│   └── scripts_analisis/
│       ├── run_all.py
│       └── datos_entrada/
│
├── 07_Publicacion/
│   ├── analisis_revistas.md
│   ├── manuscrito_final.pdf
│   ├── manuscrito_final.tex
│   ├── referencias.bib
│   ├── sn-jnl.cls
│   ├── sn-mathphys-num.bst
│   ├── bst/
│   ├── figuras/
│   ├── tablas/
│   └── dataset_zenodo/              # Paquete de replicación depositado en Zenodo
│       ├── README_dataset.md
│       ├── ANONYMIZATION.md
│       ├── ETHICS.md
│       ├── corpus/
│       ├── transcripciones/
│       ├── respuestas_cuestionarios/
│       ├── trazabilidad/
│       ├── prompts_llm/
│       └── scripts_analisis/
│
├── 08_Etica/
│   ├── A01_Protocolo_Investigacion.pdf
│   ├── A02_Instrumentos_Recoleccion.pdf
│   ├── A02.1_Guia_entrevista_semi-estructurada.pdf
│   ├── A02.2_Cuestionario_Encuesta.pdf
│   ├── A02.3_Protocolo_Observacion.pdf
│   ├── A02.4_Guion_Sesion_Design_Thinking.pdf
│   ├── A03_Consentimiento_Informado.pdf
│   ├── A04_Plan_Gestion_Datos.pdf
│   ├── A05_Aval_Institucional.pdf
│   ├── A06_Declaracion_Conflicto_Intereses.pdf
│   ├── A07_Compromiso_Confidencialidad.pdf
│   ├── A08_CV_Docente.pdf
│   ├── A09_Nomina_Equipo.pdf
│   ├── A10_Cronograma_Gantt.pdf
│   ├── A11_Analisis_Riesgos.pdf
│   ├── A13_Participantes_Externos.pdf
│   ├── Adenda_Segunda_Ronda.pdf
│   ├── README_Etica.md
│   └── Categoria_B/
│       ├── CB01_Aval_Organizacion.pdf
│       ├── CB02_Protocolo_Proteccion_Datos_Personales.pdf
│       ├── CB03_Compromiso_De_No_Uso_De_Datos_Reales.pdf
│       ├── CB05_Politica_Manejo_Datos_Menores_De_Edad.pdf
│       └── CheckList_Categoria_B_MundiPets.pdf
│
└── 09_Defensa/
    ├── Presentacion.pdf
    ├── Presentacion.pptx
    ├── guion.pdf
    └── folleto_una_hoja.pdf
```

> **Nota:** el documento `A12_Certificado_Etica.pdf` no está disponible en `08_Etica/`. El equipo lo solicitó formalmente al docente responsable, Ing. Gleiston Guerrero Ulloa, PhD, y **hasta el día de hoy no fue entregado**. Adicionalmente, las opciones externas de certificación (CITI Program, GCP-ICH, CEDIA) requerían pago, inaccesible con recursos propios del equipo. Detalle completo en `08_Etica/README_Etica.md`.

---

## Zonas de evidencia

Toda la evidencia de campo se organiza en dos zonas, conforme a la Sección 4.1 de la Guía y Rúbrica de la Entrega 3 (2A):

- **Zona pública [P]:** transcripciones anonimizadas, copias enmascaradas de consentimientos (cédula y firma cubiertas), fotografías sin rostros ni coordenadas GPS, respuestas de cuestionario sin columnas identificativas, actas de walkthrough enmascaradas.
- **Zona restringida [R]:** consentimientos originales, videos y audios sin anonimizar, documentos originales de la organización — todo dentro de `02_Evidencias/00_Restringido/`, en un volumen fragmentado cifrado con AES-256 (7-Zip). La contraseña se entrega únicamente al docente responsable por el Sistema de Gestión Académica (SGA).

Ningún archivo de la zona restringida se duplica sin cifrar en la zona pública.

---

## Compilación del documento ERS/SRS

### Requisitos

- TeX Live 2024 o superior (o MiKTeX)
- Motor `pdflatex` + `biber` (bibliografía en estilo IEEE vía `biblatex`)
- Latexmk (opcional)

### Compilar mediante consola

```bash
pdflatex ERS_SRS_2B_v2.0.tex
biber ERS_SRS_2B_v2.0
pdflatex ERS_SRS_2B_v2.0.tex
pdflatex ERS_SRS_2B_v2.0.tex
```

También puede compilarse directamente en **Overleaf** o **TeXstudio**. El documento usa `biblatex` con backend `biber` (no `bibtex`) y estilo `ieee`.

---

## Organización del repositorio

### 01_ERS
Especificación de Requisitos de Software (ERS/SRS) completa, referencias bibliográficas (mínimo 25 fuentes primarias) y figuras (diagramas i*, UML y mockups).

### 02_Evidencias
Evidencia de campo de la primera y segunda ronda de elicitación: entrevistas (transcripciones en zona pública, audio/video original cifrado en zona restringida), consentimientos informados, cuestionarios, observación, documentos de la organización, validación walkthrough y codificación temática.

### 03_Modelado
Diagrama de contexto, casos de uso, modelado i* (SD/SR), diagramas UML completos (clases, secuencia, actividades, estados, componentes, despliegue) y mockups de alta fidelidad.

### 04_Trazabilidad
Matriz de trazabilidad extendida de 61 filas (Ley → Objetivo → Interesado → Evidencia → Requisito [RF/RNF/RD/RL] → Clase → Caso de Uso → Historia de Usuario → Criterio de Aceptación → Caso de Prueba → Componente → Mockup) y priorización MoSCoW + Kano + WSJF.

### 05_MVP
Producto Mínimo Viable, con cobertura del 100 % de los requisitos funcionales del proyecto (27/27), código fuente como submódulo Git (`05_MVP/codigo`), instrucciones de despliegue local y video de demostración.

### 06_Experimento
Protocolo experimental del componente empírico (Enfoque 2 — detección automática de ambigüedad y malos olores en requisitos), registro previo aceptado en el OSF, instrumentos, resultados y scripts de análisis estadístico.

### 07_Publicacion
Manuscrito final para revista JCR (*Requirements Engineering*, Springer), análisis de las cuatro revistas objetivo permitidas por la guía, y paquete de replicación depositado en Zenodo con licencia CC BY 4.0 y DOI persistente.

### 08_Etica
Documentación ética completa del proyecto (Categoría B — Datos personales), conforme al Paquete Integral de Anexos y Guías de Elaboración de la asignatura.

---

## Evidencias

Las evidencias se obtuvieron mediante:

- Entrevistas semi-estructuradas (18 entrevistas grabadas, con transcripción y ficha técnica).
- Observación directa en un establecimiento veterinario (EV-08).
- Cuestionario digital (61 respuestas, superando el mínimo n ≥ 30; 47 del perfil dominante "Propietario de mascota").
- Validación mediante walkthrough (6 sesiones ejecutadas: 3 con usuarios técnicos, 3 con usuarios no técnicos).
- 18 consentimientos informados firmados.
- Sesión final de miembro-verificación (*member checking*) con 3 participantes previos del estudio.

Todas las evidencias mantienen su trazabilidad dentro del documento ERS/SRS mediante identificadores EV-01 a EV-24.

El corpus final de requisitos consta de **61 requisitos** (27 funcionales, 16 no funcionales, 9 restricciones de diseño y 9 requisitos legales), tras la revisión y corrección de numeración del ERS/SRS v2.0.

---

## Modelado

El proyecto incorpora:

- Diagrama de contexto.
- Modelado organizacional i* (Diagrama de Dependencia Estratégica y Diagrama de Razón Estratégica).
- Diagrama general de casos de uso y especificación textual de los casos de uso *Debe tener*.
- Diagrama de clases refinado.
- Diagramas de secuencia, actividades, estados, componentes y despliegue.
- Mockups de alta fidelidad (MU-01 a MU-08).

---

## Trazabilidad

El proyecto mantiene la siguiente cadena de trazabilidad extendida, en el
orden real de columnas de `04_Trazabilidad/matriz_trazabilidad.csv`:

```
Requisito (RF / RNF / RD / RL)
      ↓
 Caso de Uso (CU-XX)
      ↓
 Clase (modelo de dominio)
      ↓
 Criterio de Aceptación (CA-XX)
      ↓
 Caso de Prueba (CP-XX)
      ↓
 Historia de Usuario (HU-XX)
      ↓
 Estado de la traza
      ↓
 Ley / Normativa (cuando aplica — requisitos legales RL)
      ↓
 Evidencia (ID-EV)
      ↓
 Objetivo
      ↓
 Interesado (Stakeholder)
      ↓
 Mockup (MU-XX)
      ↓
 Componente
```

---

## Componente empírico

El equipo seleccionó el **Enfoque 2 — Detección automática de ambigüedad y malos olores en los requisitos**. El protocolo fue registrado de forma previa y aceptado en el Open Science Framework antes de ejecutar el detector automático sobre el corpus de requisitos:

**Registro OSF:** https://osf.io/khyf2/overview

---

## Control de versiones

El historial de cambios del proyecto se encuentra documentado en `CHANGELOG.md`.

---

## Citación

Si utiliza este repositorio con fines académicos, cite el proyecto utilizando el archivo `CITATION.cff`.

El paquete de replicación completo (datos, corpus y scripts del componente empírico) está depositado en Zenodo con DOI persistente: [10.5281/zenodo.22218780](https://doi.org/10.5281/zenodo.22218780).

### Nota sobre el archivado en Software Heritage

Este repositorio **no cuenta con identificador SWHID de Software Heritage**. Se intentó el archivado mediante la función *Save code now* (archive.softwareheritage.org), pero el proceso fue rechazado por el *loader* de la plataforma con el siguiente error:

```json
{
  "error": "Pack file too big for repository https://github.com/andymendozap03/MundiPets-PFC-IngReq, limit is 4294967296 bytes, current size is 4294967295, would write 16384",
  "worker": "loader@loader-save-code-now-545954c9c4-28thj"
}
```

El *pack file* que Software Heritage debe generar para clonar y preservar el repositorio ya está, en la práctica, en el límite exacto que su *loader* permite (4 294 967 296 bytes = 4 GiB); el siguiente objeto que necesitaría escribir (16 384 bytes) ya no cabe. Esto se debe al peso de la evidencia multimedia cifrada en `02_Evidencias/00_Restringido/`. No es un límite de GitHub ni del equipo, sino una restricción propia del servicio de archivado de Software Heritage para repositorios de este tamaño, y no se resolvió por no comprometer la integridad del historial de commits del repositorio a días de la entrega. El código, los datos anonimizados y los scripts de análisis permanecen accesibles y verificables a través de GitHub y del depósito de Zenodo indicado arriba, que sí cuenta con DOI persistente y cumple, por sí solo, el requisito de depósito FAIR con identificador persistente.

---

## Licencia

El código del MVP se publica bajo licencia MIT o Apache-2.0. El documento ERS/SRS y el conjunto de datos anonimizado depositado en Zenodo se publican bajo licencia **Creative Commons Atribución 4.0 Internacional (CC BY 4.0)**. El material de la zona restringida (`02_Evidencias/00_Restringido/`) no se licencia ni se redistribuye. Consulte el archivo `LICENSE` para más información.

Este proyecto se desarrolla exclusivamente con fines académicos dentro de la asignatura **Ingeniería de Requerimientos [20303]** de la Universidad Técnica Estatal de Quevedo (UTEQ), periodo 2026–2027 PPA.

---

## Nota sobre verificación de referencias bibliográficas

Todas las referencias bibliográficas citadas en el manuscrito final
(`07_Publicacion/manuscrito_final.tex` / `.pdf`, `referencias.bib`) y en el
documento ERS/SRS (`01_ERS/ERS_SRS_2B_v2.0.tex`) se verificaron manualmente
contra la fuente original citada, para confirmar su existencia real y la
correspondencia entre lo afirmado en el texto y el contenido efectivo de
cada trabajo referenciado.
