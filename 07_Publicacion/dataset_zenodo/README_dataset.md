# README_dataset.md — Paquete de replicación MundiPets (Enfoque 2: detección automática de ambigüedad)

**Proyecto:** MundiPets — Adopción y cruza responsable de mascotas
**Asignatura:** Ingeniería de Requerimientos [20303] · UTEQ · Período 2026–2027 PPA
**Componente empírico:** Enfoque 2 — Detección automática de ambigüedad y malos olores en requisitos
**Licencia de los datos y la documentación:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Licencia del código (scripts y detector):** MIT
**Registro previo del protocolo (OSF):** https://osf.io/khyf2/overview
**DOI de este depósito:** https://doi.org/10.5281/zenodo.22218780
**Repositorio de desarrollo (GitHub):** https://github.com/andymendozap03/MundiPets-PFC-IngReq

## Abstract (English)

This is the replication package for an empirical comparison between a rule-based ambiguity detector and the blind consensus of three independent software-engineering experts, over the complete requirements corpus (N = 61: 27 functional requirements, 16 non-functional requirements, 9 design constraints and 9 legal requirements) of MundiPets, a real social network for responsible pet adoption
and breeding in Ecuador. It contains the anonymised requirements corpus, the
detector's rule-based output, the individual and consensus expert
classifications, the traceability matrix, and the versioned Python scripts
that regenerate every table and figure of the associated manuscript from the
raw data. No personally identifiable information is included in this package;
see `ANONYMIZATION.md` and `ETHICS.md` for details.

## 1. Cómo citar este depósito

Citar usando los metadatos de `CITATION.cff` en la raíz del repositorio de
GitHub, o directamente el registro de Zenodo:

> Fuertes Arraes, E. D., Gutiérrez Ortega, G. A., Mendoza Párraga, A. J.,
> Morales Sánchez, G. A., Nieves Sánchez, J. S., & Guerrero Ulloa, G. C.
> (2026). *Replication package for "Accuracy of a requirements ambiguity
> detector: case of a pet social network"* [Data set]. Zenodo.
> `https://doi.org/10.5281/zenodo.22218780`

Al citar el software (scripts de análisis, detector) por separado del
conjunto de datos, seguir los principios de citación de software de
Smith et al. (2016), *Software citation principles*, PeerJ Computer Science.

## 2. Contenido del paquete y diccionario de datos

### 2.1 Corpus de requisitos

| Archivo | Formato | Descripción |
|---|---|---|
| `corpus_RF_MundiPets_2B.json` | JSON | Corpus etiquetado de los 27 Requisitos Funcionales del sistema, con esquema de 11 atributos (`id`, `nombre`, `descripcion`, `actor`, `origen_evidencia`, `entradas`, `salidas`, `precondiciones`, `postcondiciones`, `prioridad_moscow`, `criterio_verificacion`). Fuente: Sección 3.2 del ERS/SRS, Entrega 4 (2B). No incluye RNF ni RD; para el corpus completo de 50 ítems usado en el experimento (RF+RNF+RD) ver `tabla_5_consenso_por_requisito.csv` en la sección 2.3. |

**Nota sobre alcance:** este JSON documenta únicamente los 25 Requisitos
Funcionales tal como quedaron en el ERS/SRS. El corpus experimental completo
(N = 50: 25 RF + 16 RNF + 9 RD) que se comparó entre el detector y el panel de
expertos vive en las tablas de la subsección 2.3, identificado con el
esquema de identificadores anónimos REQ-01 a REQ-61 descrito ahí.

### 2.2 Evidencia de campo anonimizada

| Archivo / carpeta | Formato | Descripción |
|---|---|---|
| `transcripciones/*.md` | Markdown | 18 transcripciones de entrevistas (propietarios de mascotas y veterinarios), en formato diálogo Entrevistador/Entrevistado. El nombre del archivo lleva fecha, tipo de participante y código de participante (p. ej. `PROP-01`, `VET-03`); ningún nombre propio aparece en el contenido. |
| `respuestas_cuestionario.csv` | CSV, UTF-8 | 61 respuestas del cuestionario digital: 47 de propietarios de mascotas, 7 de interesados en adopción y 7 de interesados en cruza. Incluye marca temporal y 17 preguntas de opción/escala/texto libre. No contiene columnas de nombre, correo, teléfono ni IP. |
| `codificacion_tematica.csv` | CSV | Codificación temática abierta (fragmento, código, categoría, requisito derivado, ID de evidencia, analista) sobre las 24 evidencias de campo (EV-01 a EV-24). |
| `curva_saturacion.png` | PNG | Curva de saturación de códigos temáticos, generada por script desde `codificacion_tematica.csv`. |

### 2.3 Corpus, clasificaciones y resultados del experimento (Enfoque 2)

| Archivo | Formato | Descripción |
|---|---|---|
| `salida_detector.csv` | CSV | Salida cruda del detector basado en reglas sobre los 61 requisitos (identificador anónimo REQ-01…REQ-61, clasificación Ambiguo/No ambiguo, regla(s) disparada(s)). |
| `evaluacion_expertos.csv` | CSV | 183 filas (61 requisitos × 3 expertos): clasificación individual, tipo de mal olor percibido, justificación, confianza autorreportada (escala 1–5) y fecha. |
| `consenso_experto_vs_detector.csv` | CSV | Tabla procesada: consenso experto (voto mayoritario) por requisito, contrastado con la clasificación del detector. Generada por `02_generar_datos_procesados.py`. |
| `tabla_1_resumen_clasificaciones.csv` … `tabla_11_coincidencia_por_tipo.csv` | CSV | Las once tablas de resultados citadas en el manuscrito (Sección 5), generadas íntegramente por los scripts de `scripts_analisis/` — ver diccionario detallado en `scripts_analisis/README_ejecucion_scripts_analisis.md`. |
| `figuras/*.png` | PNG | Las cuatro figuras del manuscrito (clasificaciones por fuente, matriz de confusión, coeficientes kappa, tipos de ambigüedad), generadas por script, no editadas manualmente. |

**Esquema de identificadores anónimos.** Cada requisito recibió un
identificador REQ-01 a REQ-61, despojado de su tipo (RF/RNF/RD) y presentado a
los evaluadores en orden aleatorizado independiente por evaluador. La clave
que vincula el identificador anónimo con el identificador real del ERS
(`RF-XX`/`RNF-XX`/`RD-XX`) se conserva en la columna `ID_Real` de
`tabla_5_consenso_por_requisito.csv`.

### 2.4 Trazabilidad

| Archivo | Formato | Descripción |
|---|---|---|
| `matriz_trazabilidad.csv` | CSV | Cadena Ley → Objetivo → Interesado → Evidencia → Requisito (RF/RNF/RD) → Caso de Uso → Historia de Usuario → Criterio de Aceptación → Componente → Mockup. |

### 2.5 Scripts de análisis (reproducibilidad)

| Archivo | Descripción |
|---|---|
| `scripts_analisis/run_all.py` | Punto de entrada único. Ejecuta, en orden, todos los scripts siguientes y regenera cada tabla y figura desde los datos crudos. |
| `scripts_analisis/02_generar_datos_procesados.py` | Cruza `salida_detector.csv` con `evaluacion_expertos.csv` y calcula el consenso experto. |
| `scripts_analisis/03_generar_tablas_figuras_excel_corregido.py` | Genera las tablas 1–7 y las cuatro figuras (exactitud, precisión, sensibilidad, F1, kappa, matriz de confusión, tipos de ambigüedad). |
| `scripts_analisis/04_calcular_significancia_estadistica.py` | Intervalos de confianza al 95 % por bootstrap (10 000 réplicas, semilla 42) y prueba de chi-cuadrado de independencia (tabla 8). |
| `scripts_analisis/05_generar_tabla_correspondencia.py` | Tabla 9: mapea cada afirmación numérica del manuscrito a su tabla fuente. |
| `scripts_analisis/06_analisis_secundario_confianza.py` | Tabla 10: prueba de Shapiro-Wilk y U de Mann-Whitney comparando la confianza autorreportada entre requisitos donde el detector coincide o discrepa del consenso. |
| `scripts_analisis/07_desglose_por_tipo_requisito.py` | Tabla 11: coincidencia detector-consenso desagregada por tipo de requisito (RF/RNF/RD/RL). |
| `scripts_analisis/requirements.txt` | Dependencias de Python: `matplotlib`, `scikit-learn`, `numpy`, `scipy`. |

**Para reproducir todo el análisis desde cero:**

```bash
pip install -r scripts_analisis/requirements.txt
python scripts_analisis/run_all.py
```

Esto regenera, a partir únicamente de `salida_detector.csv` y
`evaluacion_expertos.csv`, las once tablas y las cuatro figuras, sin
intervención manual. Se verificó que la salida es determinista (semilla fija
en el bootstrap) y que coincide exactamente con los valores publicados en el
manuscrito.

### 2.6 Documentos de contexto (no forman parte del análisis)

| Archivo | Descripción |
|---|---|
| `ANONYMIZATION.md` | Procedimiento de anonimización y seudonimización aplicado a este paquete. |
| `ETHICS.md` | Resumen del proceso de consentimiento informado y cumplimiento de la Ley Orgánica de Protección de Datos Personales del Ecuador. |
| `prompts_llm/README_prompts_llm.md` | Declaración de que el Enfoque 2 no utilizó ningún LLM en la ejecución del experimento (el detector es un programa basado en reglas). |

## 3. Lo que este paquete NO contiene

Conforme a la Sección 3 de la Guía y Rúbrica de la Entrega 4 (2B) y a
`ANONYMIZATION.md`/`ETHICS.md`, este paquete **no incluye**: consentimientos
originales con firma o cédula visibles, videos o audios de entrevistas sin
anonimizar, fotografías con rostros o coordenadas GPS, ni ninguna columna con
nombre, correo, teléfono o identificador directo de una persona participante.
Ese material permanece exclusivamente en la zona restringida cifrada
(`02_Evidencias/00_Restringido/` del repositorio de GitHub), con acceso
limitado al docente responsable por el Sistema de Gestión Académica (SGA).

## 4. Estándares y principios seguidos

- **FAIR** (Findable, Accessible, Interoperable, Reusable) — Wilkinson et al.
  (2016), *The FAIR guiding principles for scientific data management and
  stewardship*, Scientific Data.
- **Principios de citación de software** — Smith, Katz & Niemeyer (2016),
  *Software citation principles*, PeerJ Computer Science.
- Formato de fecha: ISO 8601 (`AAAA-MM-DD`) en todos los archivos.
- Codificación de texto: UTF-8 en todos los archivos CSV y Markdown.

## 5. Contacto

Para preguntas sobre este conjunto de datos: equipo MundiPets, Facultad de
Ciencias de la Computación, Universidad Técnica Estatal de Quevedo. Docente
supervisor: Ing. Gleiston Guerrero Ulloa, PhD — gguerrero@uteq.edu.ec.
