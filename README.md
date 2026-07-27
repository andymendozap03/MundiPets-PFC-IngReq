# MundiPets – Plataforma para la Gestión Responsable de Mascotas


## Descripción

**MundiPets** es una plataforma orientada a facilitar la adopción responsable, la cruza responsable y la gestión de información veterinaria de mascotas. El proyecto busca centralizar la información clínica, antecedentes médicos, publicaciones de adopción y procesos de interacción entre propietarios y profesionales veterinarios.

Este repositorio contiene toda la documentación desarrollada durante el Proyecto Fin de Curso (PFC) de la asignatura **Ingeniería de Requerimientos** de la Universidad Técnica Estatal de Quevedo (UTEQ), siguiendo las recomendaciones de la norma **ISO/IEC/IEEE 29148:2018** y el modelo de calidad **ISO/IEC 25010**.

---

# Objetivos

- Elicitar requisitos mediante evidencia obtenida de usuarios reales.
- Elaborar una Especificación de Requisitos de Software (ERS/SRS).
- Modelar el sistema utilizando UML e i*.
- Mantener la trazabilidad entre evidencias, requisitos y casos de uso.
- Diseñar un MVP basado en los requisitos priorizados.
- Preparar el proyecto para futuras publicaciones científicas.

---

# Tecnologías y herramientas

- LaTeX
- Git
- GitHub
- Visual Paradigm
- Draw.io
- Markdown
- Visual Studio Code

---

# Integrantes

| Integrante | Rol |
|------------|-----|
| Andy Johel Mendoza Párraga | Analista líder |
| Gary Alejandro Morales Sánchez | Analista de requisitos |
| Jimmy Samuel Nieves Sánchez | Modelador UML |
| Edson Daniel Fuertes Arraes | Documentador |
| Génesis Adriana Gutiérrez Ortega | Verificadora de calidad |

---

# Responsabilidades

## Andy Johel Mendoza Párraga

- Coordinación general del proyecto.
- Gestión del repositorio Git.
- Refinamiento de requisitos.
- Integración del documento ERS.
- Validación con stakeholders.

## Gary Alejandro Morales Sánchez

- Requisitos funcionales.
- Historias de usuario.
- Trazabilidad.
- Priorización.

## Jimmy Samuel Nieves Sánchez

- Diagramas UML.
- Casos de uso.
- Diagramas de clases.
- Diagramas de secuencia.
- Diagramas de actividades.
- Diagramas de estados.

## Edson Daniel Fuertes Arraes

- Documentación técnica.
- Organización del ERS.
- Gestión bibliográfica.
- Revisión documental.

## Génesis Adriana Gutiérrez Ortega

- Control de calidad.
- Validación documental.
- Evidencias.
- Revisión de cumplimiento de la rúbrica.

---

# Estado del proyecto

| Entrega | Estado |
|---------|--------|
| Entrega 1A | Completada |
| Entrega 1B | Completada |
| Entrega 2A | En desarrollo |

---

# Estructura del repositorio

```text
MundiPets-PFC-IngReq
│
├── .gitattributes
├── .gitignore
├── CHANGELOG.md
├── checksums.sha256
├── CITATION.cff
├── LICENSE
├── README.md
│
├── 01_ERS
│   └── figuras
│
├── 02_Evidencias
│   ├── Audio
│   ├── Codificacion_Tematica
│   ├── Consentimientos
│   ├── Cuestionario
│   │   ├── Fotos_Aplicacion
│   │   └── Respuestas
│   ├── Documentos_Organizacion
│   ├── Fotos_Entorno
│   ├── Validacion_Walkthrough
│   └── Video
│
├── 03_Modelado
│   ├── Casos de Uso
│   ├── Diagrama de Contexto
│   ├── Diagramas de Actividades
│   ├── Diagramas de Clases
│   ├── Diagramas de Maquinas de Estado
│   ├── Diagramas de Secuencia
│   ├── Diagramas_UML
│   │   ├── Diagrama de Dependencia Estrategica
│   │   └── Diagrama de Razon Estrategica
│   └── Mockups
│
├── 04_Trazabilidad
│
├── 05_MVP
│
├── 06_Experimento
│   ├── instrumentos
│   ├── prompts_llm
│   ├── resultados
│   └── scripts_analisis
│
├── 07_Publicacion
│   └── dataset_zenodo
│
└── 08_Etica
    └── Categoria_B
```

---

# Compilación del documento ERS

## Requisitos

- TeX Live 2024 o superior
- MiKTeX
- Latexmk (opcional)

## Compilar mediante consola

```bash
pdflatex ERS_SRS_2A_v1.0.tex
bibtex ERS_SRS_2A_v1.0
pdflatex ERS_SRS_2A_v1.0.tex
pdflatex ERS_SRS_2A_v1.0.tex
```

También puede compilarse directamente utilizando **Overleaf o TeXstudio**.

---

# Organización del repositorio

## 01_ERS

Contiene la Especificación de Requisitos de Software (ERS/SRS), las referencias bibliográficas y las figuras utilizadas en el documento.

## 02_Evidencias

Almacena toda la evidencia obtenida durante el proceso de ingeniería de requerimientos:

- Entrevistas en audio.
- Entrevistas en video.
- Consentimientos informados.
- Cuestionarios.
- Fotografías del entorno.
- Documentación proporcionada por los stakeholders.
- Evidencias del walkthrough.
- Codificación temática.

## 03_Modelado

Contiene todos los modelos desarrollados durante la especificación del sistema:

- Diagrama de contexto.
- Casos de uso.
- Diagramas UML.
- Diagramas i*.
- Mockups.

## 04_Trazabilidad

Repositorio destinado a la matriz de trazabilidad y priorización de requisitos.

## 05_MVP

Contendrá el Producto Mínimo Viable del sistema.

## 06_Experimento

Incluye el protocolo experimental, instrumentos, prompts utilizados con LLM, resultados y scripts de análisis.

## 07_Publicacion

Contendrá los artefactos necesarios para la publicación científica y el conjunto de datos destinado a Zenodo.

## 08_Etica

Almacena la documentación ética relacionada con el proyecto.

---

# Evidencias

Las evidencias se obtuvieron mediante:

- Entrevistas semiestructuradas.
- Observación directa.
- Cuestionarios.
- Validación mediante walkthrough.
- Consentimientos informados.

Todas las evidencias mantienen su correspondiente trazabilidad dentro del documento ERS.

---

# Modelado

El proyecto incorpora:

- Diagramas de contexto.
- Diagramas de casos de uso.
- Diagramas de actividades.
- Diagramas de clases.
- Diagramas de secuencia.
- Diagramas de estados.
- Modelado organizacional i*.
- Mockups de alta fidelidad.

---

# Trazabilidad

El proyecto mantiene la siguiente cadena de trazabilidad:

```
Stakeholders
        ↓
 Evidencias
        ↓
 Objetivos
        ↓
 Requisitos
        ↓
 Casos de Uso
        ↓
 Historias de Usuario
        ↓
 Mockups
        ↓
 MVP
```

---

# Control de versiones

El historial de cambios del proyecto se encuentra documentado en:

```
CHANGELOG.md
```

---

# Citación

Si utiliza este repositorio con fines académicos, cite el proyecto utilizando el archivo:

```
CITATION.cff
```

---

# Licencia

Este proyecto se desarrolla exclusivamente con fines académicos dentro de la asignatura **Ingeniería de Requerimientos** de la Universidad Técnica Estatal de Quevedo.

Consulte el archivo **LICENSE** para más información.

---

