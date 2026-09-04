# Declaración de uso de IA — MundiPets PFC

Este documento declara, sección por sección, si se utilizó alguna
herramienta de inteligencia artificial (Claude, ChatGPT, Copilot u otra),
para qué se usó, quién verificó el resultado y con qué método.

El elemento A9 de la guía exige la declaración **por sección del
documento** — es decir, del documento principal del proyecto
(`01_ERS/ERS_SRS_2B_v2.0.tex`). La **Parte 1** de este archivo cubre
exactamente eso, sección por sección del ERS, incluidas las secciones en
las que no se usó ninguna herramienta.

La **Parte 2** extiende la misma declaración, con el mismo nivel de
detalle, al resto de artefactos del repositorio (evidencias, modelado,
manuscrito, ética, defensa) donde también se usó IA como apoyo.

**Alcance general del uso de IA en este proyecto:** el equipo declara que
usó **Claude (Anthropic)** de forma transversal como **apoyo de redacción,
revisión de estilo/forma de escritura y validación de coherencia** (por
ejemplo, revisar que los modelos y diagramas fueran consistentes entre sí y
con el texto que los describe), no para generar contenido sustantivo,
hallazgos, datos o decisiones técnicas — esos siguen siendo trabajo y
juicio propio del equipo. Cada integrante verificó el resultado de su
propia sección antes de integrarla al repositorio.

---

# Parte 1 — Documento ERS (`01_ERS/ERS_SRS_2B_v2.0.tex`)

Esta es la declaración exigida explícitamente por el elemento A9: cubre,
sección por sección, el documento principal del proyecto.

| Sección | Herramienta usada | Para qué | Quién verificó | Cómo verificó |
|---|---|---|---|---|
| Propósito, alcance y visión general | Claude | Apoyo de redacción y revisión de forma de escritura | Andy Mendoza | Leyó el texto final y confirmó que reflejara lo que el equipo había definido |
| Entorno operativo | Claude | Apoyo de redacción y revisión de forma de escritura | Gary Morales | Revisó que la descripción del entorno coincidiera con lo levantado durante el trabajo de campo |
| Interfaces externas (mockups) | Claude | Apoyo de redacción y revisión de forma de escritura | Genesis Gutierrez | Contrastó el texto con las imágenes de los mockups antes de subirlo |
| Glosario de términos y referencias | Claude | Apoyo de redacción y revisión de forma de escritura | Jimmy Nieves | Verificó que cada término definido correspondiera a su uso real en el resto del documento |
| Interfaz de software y hardware | Claude | Apoyo de redacción y revisión de forma de escritura | Genesis Gutierrez | Revisó que las especificaciones descritas fueran consistentes con las herramientas realmente usadas |
| Planificación del proyecto | Claude | Apoyo de redacción y revisión de forma de escritura | Edson Daniel Fuertes Arraes | Cotejó el cronograma descrito contra los avances reales registrados en el repositorio |
| Clases y características de usuarios (stakeholders) | Claude | Apoyo de redacción y revisión de forma de escritura | Jimmy Nieves | Confirmó que el mapa de stakeholders reflejara a las personas entrevistadas realmente |
| Requisitos funcionales | Claude | Apoyo de redacción y revisión de forma de escritura | Gary Morales y Genesis Gutierrez | Cada uno releyó los requisitos que redactó antes del commit |
| Requisitos no funcionales | Claude | Apoyo de redacción y revisión de forma de escritura | Gary Morales | Revisó que cada requisito fuera medible y correspondiera a lo acordado por el equipo |
| Restricciones y requisitos legales | Claude | Apoyo de redacción y revisión de forma de escritura | Gary Morales | Contrastó el texto contra la normativa ecuatoriana aplicable citada |
| Clasificación, priorización y trazabilidad (MoSCoW, matriz) | Claude | Apoyo de redacción y revisión de forma de escritura | Genesis Gutierrez y Jimmy Nieves | Cada uno releyó su parte antes del commit |
| Trabajo de campo y catálogo de evidencias | Claude | Apoyo de redacción y revisión de forma de escritura | Andy Mendoza y Gary Morales | Cada uno releyó su parte antes del commit |
| Modelado UML (diagramas de clases, casos de uso, secuencia, actividades, estados, componentes, despliegue) | Claude | Apoyo para validar la coherencia de los modelos entre sí y con el texto que los describe, y revisión de forma de escritura | Andy Mendoza y Gary Morales | Compararon cada diagrama contra los requisitos correspondientes del ERS antes del commit |
| Producto mínimo viable (MVP) | Claude | Apoyo de redacción y revisión de forma de escritura | Andy Mendoza y Jimmy Nieves | Releyeron la sección comparándola con el código real del MVP |
| Componente empírico del proyecto | Claude | Apoyo de redacción y revisión de forma de escritura | Jimmy Nieves | Comparó la sección contra los resultados reales generados por los scripts |
| Apéndices A–I | Claude | Apoyo de redacción y revisión de forma de escritura | Edson Daniel Fuertes Arraes y Genesis Gutierrez | Cada uno releyó los apéndices que redactó antes del commit |

---

# Parte 2 — Resto del repositorio (cobertura adicional, no exigida por A9)

Las siguientes secciones no forman parte del documento ERS, pero se
declaran igualmente por transparencia, ya que también se usó Claude como
apoyo en su redacción.

## 02_Evidencias

| Sección | Herramienta usada | Para qué | Quién verificó | Cómo verificó |
|---|---|---|---|---|
| Transcripción de entrevistas | Claude | Apoyo de redacción y revisión de forma de escritura | Genesis Gutierrez | Comparó la transcripción contra el audio original |
| Síntesis / anonimización de entrevistas | Claude | Apoyo de redacción y revisión de forma de escritura | Genesis Gutierrez | Confirmó que no quedaran datos identificables al comparar con la versión original |
| Consentimientos informados | Claude | Apoyo de redacción y revisión de forma de escritura | Andy Mendoza | Confirmó que el texto legal correspondiera al modelo aprobado |
| Fichas técnicas | Claude | Apoyo de redacción y revisión de forma de escritura | Andy Mendoza | Comparó los datos de la ficha contra la fuente original |

## 03_Modelado

| Sección | Herramienta usada | Para qué | Quién verificó | Cómo verificó |
|---|---|---|---|---|
| Diagramas UML (fuente y exportación) | Claude | Apoyo para validar los modelos: revisar coherencia entre diagramas (clases, casos de uso, secuencia, actividades, estados, componentes, despliegue) y consistencia con los requisitos del ERS | Andy Mendoza y Gary Morales | Compararon cada diagrama exportado contra su archivo fuente y contra los requisitos que representa |

## 04_Trazabilidad

| Sección | Herramienta usada | Para qué | Quién verificó | Cómo verificó |
|---|---|---|---|---|
| Matriz de trazabilidad | Claude | Apoyo de redacción y revisión de forma de escritura | Andy Mendoza y Edson Daniel Fuertes Arraes | Verificaron que cada requisito estuviera enlazado a su elemento de diseño y caso de prueba correspondiente |

## 05_MVP

| Sección | Herramienta usada | Para qué | Quién verificó | Cómo verificó |
|---|---|---|---|---|
| Código del MVP | Claude | Apoyo de redacción y revisión de forma de escritura | Andy Mendoza | Ejecutó el MVP localmente y comparó su comportamiento contra los requisitos funcionales |

## 06_Experimento / 07_Datos

| Sección | Herramienta usada | Para qué | Quién verificó | Cómo verificó |
|---|---|---|---|---|
| Scripts de análisis (generación de datos procesados, significancia estadística, tabla de correspondencia) | Claude | Apoyo de redacción y revisión de forma de escritura | Jimmy Nieves | Ejecutó cada script y comparó la salida contra los datos crudos originales |
| Codificación temática y curva de saturación | Claude | Apoyo de redacción y revisión de forma de escritura | Gary Morales | Comparó la codificación generada contra las transcripciones originales |
| Rúbrica de clasificación experta | Claude | Apoyo de redacción y revisión de forma de escritura | Jimmy Nieves | Comparó la rúbrica contra las respuestas reales del panel de expertos |

## 07_Publicacion (manuscrito final)

| Sección | Herramienta usada | Para qué | Quién verificó | Cómo verificó |
|---|---|---|---|---|
| Resumen e introducción | Claude | Apoyo de redacción y revisión de forma de escritura | Edson Daniel Fuertes Arraes | Leyó el resumen y confirmó que representara fielmente el contenido completo del manuscrito |
| Trabajos relacionados | Claude | Apoyo de redacción y revisión de forma de escritura | Andy Mendoza | Verificó que las referencias citadas correspondieran a fuentes reales de referencias.bib |
| Metodología | Claude | Apoyo de redacción y revisión de forma de escritura | Genesis Gutierrez | Comparó la metodología descrita contra el procedimiento real seguido |
| Resultados | Claude | Apoyo de redacción y revisión de forma de escritura | Gary Morales | Comparó cada cifra citada contra las tablas generadas por los scripts |
| Discusión | Claude | Apoyo de redacción y revisión de forma de escritura | Gary Morales | Confirmó que las interpretaciones planteadas se sostuvieran en los resultados obtenidos |
| Amenazas a la validez | Claude | Apoyo de redacción y revisión de forma de escritura | Genesis Gutierrez | Revisó que cada amenaza descrita correspondiera a una limitación real del estudio |
| Conclusiones | Claude | Apoyo de redacción y revisión de forma de escritura | Jimmy Nieves | Confirmó que las conclusiones se derivaran directamente de los resultados presentados |

## 08_Etica

| Sección | Herramienta usada | Para qué | Quién verificó | Cómo verificó |
|---|---|---|---|---|
| Documentos de ética y protección de datos | Claude | Apoyo de redacción y revisión de forma de escritura | Edson Daniel Fuertes Arraes y Gary Morales | Cada uno releyó su parte comparándola con la Ley Orgánica de Protección de Datos Personales del Ecuador |
| Registro y desviaciones del protocolo (OSF) | Claude | Apoyo de redacción y revisión de forma de escritura | Jimmy Nieves | Comparó el registro contra la plataforma OSF real |

## 09_Defensa

| Sección | Herramienta usada | Para qué | Quién verificó | Cómo verificó |
|---|---|---|---|---|
| Diapositivas de la defensa | Claude | Apoyo de redacción y revisión de forma de escritura | Genesis Gutierrez | Confirmó que cada diapositiva reflejara con precisión el contenido final del ERS y del manuscrito |
| Guion de la defensa | Claude | Apoyo de redacción y revisión de forma de escritura | Gary Morales | Ensayó el guion y verificó que cubriera los puntos clave del proyecto |
| Folleto de una hoja para el tribunal | Claude | Apoyo de redacción y revisión de forma de escritura | Andy Mendoza | Revisó que el folleto resumiera correctamente los puntos centrales sin omitir información relevante |

---

## Declaración final

Los cinco integrantes confirmamos que ninguna herramienta de IA generó
contenido sustantivo (hallazgos, datos, decisiones de diseño, resultados
del componente empírico) sin verificación humana posterior, y que todo
resultado numérico presentado en los documentos del proyecto procede de la
ejecución de scripts sobre datos reales, no de una herramienta de IA.

| Integrante | Confirmación | Fecha |
|---|---|---|
| Andy Mendoza | Confirmo que esta declaración es exacta — Andy Mendoza | 2026-09-04 |
| Edson Daniel Fuertes Arraes | Confirmo que la descripción de mi aporte es exacta — Edson Fuertes | 2026-09-04 |
| Genesis Gutierrez | Confirmo que esta declaración es exacta - Genesis Gutierrez | 2026-09-04 | 
| Gary Morales | Confirmo que esta declaración es exacta — Gary Morales | 2026-09-04 |
| Jimmy Nieves |  | 2026-09-04 |
