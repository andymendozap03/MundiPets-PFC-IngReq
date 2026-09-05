# Changelog

Todos los cambios relevantes de este proyecto se documentan en este archivo.

El formato sigue las convenciones de [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/), adaptado a las entregas oficiales del Proyecto Fin de Curso (PFC) de la asignatura Ingeniería de Requerimientos [20303], UTEQ, periodo 2026–2027 PPA: Entrega 1 (1A, semana 4) · Entrega 2 (1B, semana 10) · Entrega 3 (2A, semana 13) · Entrega 4 (2B/Defensa, semana 17).

---

## [4.0] — Entrega 4 (2B / Defensa) — 2026-09-04

Cierre del ciclo del PFC: ejecución completa del componente empírico, manuscrito final para revista JCR, depósito FAIR en Zenodo, y preparación de la defensa oral.

### Added
- Corpus de requisitos corregido y ampliado a 61 ítems (27 RF + 16 RNF + 9 RD + 9 RL), tras la revisión de numeración del ERS/SRS v2.0.
- Ejecución completa del experimento (Enfoque 2): detector automático de ambigüedad frente al consenso de un panel de tres expertos, sobre los 61 requisitos.
- Resultados finales: exactitud = 0,8033; precisión = 0,600; sensibilidad = 0,750; F1 = 0,667; κ de Cohen (detector-consenso) = 0,530 (moderado, IC 95% [0,280, 0,737]); χ²(1) = 15,037, p = 0,0001 (significativo); κ de Fleiss (panel experto) = 0,857 (casi perfecto).
- Manuscrito final completo (`07_Publicacion/manuscrito_final.tex` / `.pdf`): Introduction, Related work, Methodology, Results, Discussion, Threats to validity y Conclusions cerrados, con las cuatro tablas y figuras adicionales generadas por script.
- Scripts de análisis ampliados: desglose de coincidencia por tipo de requisito y análisis secundario de confianza autorreportada (Mann-Whitney, δ de Cliff).
- Matriz de trazabilidad ampliada a 61 filas, superando el mínimo de 60 exigido.
- Depósito FAIR publicado en Zenodo con DOI persistente: [10.5281/zenodo.22218780](https://doi.org/10.5281/zenodo.22218780), con el paquete de replicación completo (corpus, transcripciones, respuestas de cuestionario, scripts de análisis, `README_dataset.md`, `ANONYMIZATION.md`, `ETHICS.md`).
- Autoevaluación FAIR con F-UJI: 92 % de los indicadores, `fair_assessment.pdf` en la raíz del repositorio.
- Código fuente completo del MVP incorporado directamente al repositorio principal (`05_MVP/codigo/`) mediante `git subtree`, conservando el historial real de commits del desarrollo del MVP (autores y fechas originales preservados, visible con `git log -- 05_MVP/codigo`). No se usa submódulo Git.
- Cuentas de prueba documentadas en `05_MVP/README.md`, una por cada rol del sistema (Adoptante, Propietario, Veterinaria, Interesado en Cruza).
- Power calculation del cuestionario, perfil dominante ("Propietario de mascota", n=47): potencia estadística de 91,86 % (Cohen d=0,5, α=0,05, 1−β=0,80), calculada con `statsmodels` y versionada en `02_Evidencias/Cuestionario/power_calculation/`.
- Fichas técnicas de evidencia actualizadas al corpus terminal: 20 participantes, 18 entrevistas (audio + video), 18 consentimientos, 6 sesiones de *walkthrough* (3 técnicas + 3 no técnicas), 1 sesión de *member checking*, 61 respuestas de cuestionario.
- `checksums.sha256` regenerado sobre un clon limpio, cubriendo la totalidad del repositorio, incluidas las carpetas `07_Datos/` y `10_Autoria/` agregadas en esta misma versión.
- Carpeta `09_Defensa/` con presentación (PDF y PPTX), guion de la defensa, video de la defensa y folleto de una hoja para el tribunal.
- Análisis de revistas objetivo (`07_Publicacion/analisis_revistas.md`) reescrito sobre la lista cerrada de la guía: *Requirements Engineering*, *Information and Software Technology*, *Empirical Software Engineering*, *Journal of Systems and Software*, REFSQ 2027 y RE 2027. Decisión final: *Requirements Engineering* (Springer), consistente con la plantilla `sn-jnl.cls` ya en uso en el manuscrito.
- Paquete de datos independiente y autocontenido en `07_Datos/`, reproducible de punta a punta desde un clon limpio con `python run_all.py`: datos crudos, datos procesados, scripts de análisis, resultados (figuras y tablas), diccionario de datos, licencia propia (`LICENSE-DATA.txt`), registro de depósito y manifiesto de sumas (`checksums_datos.sha256`).
- Carpeta `10_Autoria/` con la evidencia de autoría y trabajo propio del equipo exigida por la Guía de Desarrollo del PFC (elementos A1 a A12): bitácora de sesiones derivada del historial real de `git log`, capturas de pantalla y grabaciones de sesiones de trabajo, notas de campo escaneadas, fotografías del equipo con metadatos EXIF verificados, fuentes editables de todos los diagramas, doble codificación independiente del corpus de requisitos entre dos integrantes (κ de Cohen = 0,550, moderado), correspondencia con la organización, declaración de uso de IA por sección del ERS, y aporte individual de cada integrante con sus commits acreditativos.
- Archivo `.mailmap` en la raíz del repositorio, unificando las diez identidades de Git detectadas en las cinco personas reales del equipo.
- Espejo del repositorio `MundiPets-PFC-IngReq-espejo-SWH`, generado con `git filter-repo` para excluir `02_Evidencias/00_Restringido/` y los archivos `.mp4`/`.mp3` de todo el historial, y archivado correctamente en Software Heritage con SWHID persistente (ver Apéndice E del ERS/SRS y README.md raíz).

### Changed
- Nombres de archivo del ERS corregidos a la notación exigida por la rúbrica (`ERS_SRS_2B_v2.0.pdf` / `.tex`).
- `CITATION.cff` actualizado a versión 2.0, con el DOI de Zenodo y fecha de publicación real.
- Datos de evaluadores expertos anonimizados en todo el pipeline (columna `Evaluador` → `Experto 1/2/3`) en datos crudos, procesados, tablas y figuras.
- Consentimientos del panel de expertos renombrados a código de participante (`EXP-01`/`EXP-02`/`EXP-03`) con cédula y firma enmascaradas en la copia pública.
- `LICENSE` corregido: se excluye expresamente `02_Evidencias/00_Restringido/` de la licencia CC BY 4.0 de documentación y datos.
- README.md raíz actualizado con las cifras reales de evidencia (18 entrevistas, 61 respuestas, 6 *walkthroughs*, 18 consentimientos, corpus de 61 requisitos) y con enlaces al manuscrito final, al DOI de Zenodo y al registro OSF.
- Estructura de `07_Publicacion/` reorganizada: `manuscrito_final.tex`, `.pdf`, `referencias.bib`, `figuras/` y `tablas/` ahora en la raíz de la carpeta, conforme al árbol obligatorio de la Sección 9.1 de la guía.

### Fixed
- Corregido el desfase entre la evidencia declarada y la evidencia real del repositorio en `fichas_tecnicas.csv` (faltaban VET-07, PROP-12 y dos sesiones de *walkthrough*).
- Cuestionario digital por debajo del mínimo n≥60 en el perfil dominante ("Propietario de mascota": 47 de 61 respuestas): subsanado mediante cálculo de potencia estadística (Cohen d=0,5, α=0,05, 1−β=0,80), que arroja una potencia real de 91,86 % con n=47, muy por encima del mínimo del 80 % exigido. Script y resultado en `02_Evidencias/Cuestionario/power_calculation/`.
- Archivado en Software Heritage: el intento inicial con "Save code now" sobre el repositorio principal falló por exceder el límite de 4 GiB del *loader* de la plataforma, debido al peso de la evidencia multimedia cifrada y los archivos gestionados por Git LFS. Se resolvió generando el espejo `MundiPets-PFC-IngReq-espejo-SWH` (historial completo de commits preservado, excluyendo `02_Evidencias/00_Restringido/` y los archivos `.mp4`/`.mp3` mediante `git filter-repo` sobre la historia completa), que sí se archivó correctamente y cuenta con SWHID persistente, referenciado en `README.md` y `CITATION.cff`.

### Known issues
- Documento `A12_Certificado_Etica.pdf` no disponible en `08_Etica/`: el equipo lo solicitó formalmente al docente responsable, Ing. Gleiston Guerrero Ulloa, PhD, y no fue proporcionado. Las opciones externas de certificación (CITI Program, GCP-ICH, CEDIA) requerían pago, inaccesible con recursos propios del equipo. Detalle en `08_Etica/README_Etica.md`.

---

## [3.0] — Entrega 3 (2A) — 2026-07-29

Documento ERS/SRS completo, validado con evidencia real de campo y con trazabilidad total evidencia–requisito–caso de uso.

### Added
- 25 requisitos funcionales (RF) con los ocho atributos exigidos, incluida la referencia explícita al identificador de evidencia (EV-XX).
- 16 requisitos no funcionales (RNF) cuantificados según las nueve características de calidad de ISO/IEC 25010:2023, incluido el requisito de explicabilidad para el componente de IA/ML del sistema.
- 9 restricciones de diseño (RD) y requisitos legales mapeados a la Ley Orgánica de Protección de Datos Personales del Ecuador (LOPDP), con trazabilidad Ley → Artículo → RF/RNF.
- Historias de usuario en formato Connextra para los RF de prioridad *Debe tener*, con criterios de aceptación redactados en Gherkin.
- Modelado UML completo: diagrama general de casos de uso, 13 casos de uso detallados, diagrama de clases refinado, diagramas de secuencia, actividades, estados, componentes y despliegue.
- Modelado organizacional i* (Diagrama de Dependencia Estratégica y Diagrama de Razón Estratégica).
- Mockups de alta fidelidad (MU-01 a MU-08), trazados a los RF que soportan.
- Priorización combinada MoSCoW + Kano (aproximación por importancia declarada) + WSJF.
- Matriz de trazabilidad extendida (Ley → Objetivo → Interesado → Evidencia → RF/RNF/RD → CU → HU → CA → Componente → Mockup).
- Producto Mínimo Viable (MVP) con video de demostración, en `05_MVP/`.
- Componente empírico: Enfoque 2 — detección automática de ambigüedad y malos olores en los requisitos, con protocolo experimental, registro previo aceptado en el Open Science Framework (OSF, https://osf.io/khyf2/overview) y panel de tres personas evaluadoras expertas.
- Segunda ronda de campo: 10 nuevas entrevistas (EV-09 a EV-18), 1 sesión de observación (EV-08), 4 sesiones de validación *walkthrough* (EV-19 a EV-22), cuestionario ampliado v2.0 (38 respuestas) y 16 consentimientos informados firmados en total.
- Codificación temática y curva de saturación del corpus de evidencias (EV-01 a EV-22).
- Corpus de requisitos etiquetado (`corpus_RF_MundiPets_2A.json`), preparado para depósito en Zenodo con licencia CC BY 4.0.
- Análisis comparativo de revistas objetivo (Springer Nature, Elsevier, IEEE) y borrador inicial del manuscrito paralelo.
- Documentación ética completa en `08_Etica/`: Anexos A.1 a A.11, A.13 (participantes externos y adenda de segunda ronda) y checklist de Categoría B (CB-1, CB-2, CB-3, CB-5).
- Apéndice B.9 — Índice de multimedia, con el listado completo de evidencias EV-01 a EV-22 y su ubicación en zona pública [P] / zona restringida [R].
- Apéndice E — Repositorio GitHub, actualizado con el árbol de carpetas real del repositorio, incluida la carpeta `08_Etica/`.

### Changed
- Instrumentos de recolección actualizados a versión 2.0 (guía de entrevista, cuestionario, protocolo de observación, guía de Design Thinking, guion de walkthrough).
- Estructura del repositorio reorganizada conforme a la Sección 8.1 de la Guía y Rúbrica de la Entrega 3 (2A): separación de evidencias en zona pública [P] y zona restringida [R] cifrada (`02_Evidencias/00_Restringido/`).

### Known issues
- Sesiones de *walkthrough*: se ejecutaron 4 de las 6 recomendadas para el objetivo 2B (faltan 1 sesión con usuario técnico y 1 con usuario no técnico).
- Documento `A12_Certificado_Etica.pdf` no disponible en `08_Etica/`: los cursos de certificación ética consultados (CITI Program, GCP-ICH, CEDIA) requerían pago, situación comunicada al docente responsable sin recibir alternativa gratuita. Detalle en `08_Etica/README_Etica.md`.
- Estructura de carpetas, `checksums.sha256` y artefactos de `04_Trazabilidad/` en proceso de consolidación final antes del corte, conforme al checklist de aceptación (Apéndice H del ERS/SRS).

---

## [2.0] — Entrega 2 (1B) — 2026-07-05

ERS/SRS parcial. Incorpora las correcciones señaladas en la Entrega 1 (1A) y agrega requisitos, modelado UML inicial, priorización y trazabilidad.

### Added
- Primera versión de los requisitos funcionales y no funcionales.
- Primeros diagramas UML (casos de uso, clases conceptuales).
- Primera ronda de elicitación: entrevistas iniciales (EV-01 a EV-06), consentimientos informados firmados.
- Matriz de trazabilidad inicial.

### Changed
- Incorporación de observaciones docentes de la Entrega 1 (1A).

---

## [1.0] — Entrega 1 (1A) — 2026-05-30

Planificación y elicitación inicial del proyecto.

### Added
- Diagnóstico y definición de objetivos del proyecto.
- Identificación de stakeholders (propietarios de mascotas, médicos veterinarios).
- Diseño de los instrumentos de recolección de datos versión 1.0.
- Estructura inicial del repositorio.

---

## Convenciones de este archivo

- **Added** — funcionalidades, artefactos o documentos nuevos.
- **Changed** — cambios en artefactos o documentos ya existentes.
- **Fixed** — correcciones de errores o inconsistencias detectadas.
- **Known issues** — pendientes declarados de forma expresa por el equipo, sin autocertificar como completos, conforme al principio de la Sección 8.10 de la Guía y Rúbrica de la Entrega 3 (2A): "nada declarado en el ERS puede quedar solo declarado".

Cada versión del `CHANGELOG.md` corresponde a la versión declarada en el historial de versiones de `01_ERS/ERS_SRS_2A_v1.0.pdf` (portada e historial de versiones del documento).
