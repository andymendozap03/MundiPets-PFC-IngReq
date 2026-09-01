# Análisis de revistas objetivo — MundiPets

**Proyecto:** MundiPets — Detección automática de ambigüedad en requisitos
**Asignatura:** Ingeniería de Requerimientos [20303] · UTEQ · PPA 2026–2027
**Documento:** requisito de la Sección 6.4 de la guía de la Entrega 3 (2A), criterio C10
**Última actualización:** 1 de septiembre de 2026 (Entrega 4 / 2B — corpus final N=61)
**Responsable:** Fuertes Arraes, Edson Daniel (analista líder)

---

## 0. Corrección respecto de la versión anterior (2 de agosto de 2026)

Esta versión corrige un error de alcance de la versión 1.0: el documento evaluaba
seis revistas (*Scientific Reports*, *Heliyon*, *IEEE Access*, *IEEE Transactions on
Software Engineering*, además de *Requirements Engineering* e *Information and
Software Technology*), de las cuales **cuatro no forman parte de la lista cerrada**
que exige la Sección 2 de la Guía y Rúbrica de la Entrega 4 (2B). Esa sección
autoriza únicamente:

| Revista | Editorial | Dato oficial verificado al 02/07/2026 |
|---|---|---|
| *Requirements Engineering* | Springer (Springer London) | ISSN 0947-3602, 1432-010X; JIF 2024 = 3,3; Q2 en *Computer Science, Software Engineering*, posición 64/131; mediana de 5 días a primera decisión editorial |
| *Information and Software Technology* | Elsevier | ISSN 0950-5849; JIF 2024 = 4,3; Q1 |
| *Empirical Software Engineering* | Springer | ISSN 1382-3256; Q1 |
| *Journal of Systems and Software* | Elsevier | ISSN 0164-1212; Q1 |

Como conferencias *ranking A/A\** del área CORE: **REFSQ 2027** (Basel, Suiza,
12–15 de abril de 2027) e **IEEE International Requirements Engineering Conference
2027 (RE 2027)**.

Toda la Sección 3 de este documento se reescribe sobre esta lista cerrada. Las
tablas de la versión anterior sobre *Scientific Reports*, *Heliyon*, *IEEE Access*
e *IEEE Transactions on Software Engineering* se retiran: no son opciones válidas
para esta entrega, independientemente de su ajuste temático o su factor de
impacto.

---

## 1. Insumos para la búsqueda

Título y resumen finales del manuscrito, ya cerrado con las secciones de Resultados
y Conclusiones (Entrega 4).

**Título**

> Accuracy of a requirements ambiguity detector: case of a pet social network

**Resumen** (versión final, manuscrito 2.0)

> **Context.** Ambiguity is one of the most persistent defects in natural-language
> requirements specifications, and rule-based detectors are frequently proposed as
> a low-cost mechanism to flag it before requirements reach design. Evidence on how
> closely such detectors reproduce human expert judgement remains scarce for
> Spanish-language specifications produced in Latin American settings.
>
> **Objective.** This study measures the extent to which a rule-based ambiguity
> detector replicates the consensus judgement of independent human experts over the
> complete requirements corpus of MundiPets, a real social network for responsible
> pet adoption and breeding, and characterises the patterns of disagreement between
> the two.
>
> **Methods.** We conducted a paired quasi-experiment over 61 requirements (27
> functional, 16 non-functional, 9 design constraints and 9 legal requirements)
> specified according to an eight-attribute template. A purpose-built rule-based
> detector, implemented in Python and frozen before data collection, classified
> each requirement as ambiguous or non-ambiguous using four lexical and syntactic
> rules. In parallel, three independent software engineers, blind to the detector
> output and to one another, classified the same requirements in randomised order
> using a shared rubric. The protocol was preregistered on the Open Science
> Framework before any data were collected. Agreement was quantified with
> precision, recall, F1, Cohen's kappa and Fleiss' kappa.
>
> **Results.** The detector flagged 32.79% of requirements as ambiguous (20/61)
> against 26.23% (16/61) for the expert consensus, yielding accuracy = 0.8033,
> precision = 0.600, recall = 0.750 and F1 = 0.667 for the ambiguous class.
> Agreement between detector and consensus was moderate (Cohen's kappa = 0.530,
> 95% CI [0.280, 0.737]) and a chi-squared test of independence found the detector
> significantly associated with expert consensus beyond chance (chi-squared =
> 15.037, d.f. = 1, p = 0.0001). The expert panel itself agreed almost perfectly
> (Fleiss' kappa = 0.857). Coincidence with expert consensus was strongest for
> legal requirements (9/9, 100%) and non-functional requirements (14/16, 87.5%),
> and weakest for design constraints (5/9, 55.6%).
>
> **Conclusion.** A four-rule lexical-syntactic detector achieves moderate,
> statistically significant agreement with an almost-perfectly agreeing expert
> panel on a real, Spanish-language requirements corpus, performing best on
> non-functional and legal requirements and worst on design constraints. The
> result supports using such a detector as a first-pass triage tool in a review
> workflow, while showing that design constraints in particular still require
> human judgement.

**Palabras clave**

> Requirements Engineering · Empirical Software Engineering · Natural Language
> Processing · Interrater Agreement · Requirements Quality

---

## 2. Ejecución de las herramientas oficiales

**Este paso sigue sin ejecutarse.** Las tres herramientas de sugerencia editorial
(Springer Journal Suggester para las dos candidatas Springer, y el equivalente de
Elsevier para las dos candidatas Elsevier) deben correrse con el resumen final de
la Sección 1 antes del envío real. No se completa esta tabla con valores
estimados: hacerlo sería fabricación académica y dispara el gatekeeper G4.

| Editorial | Herramienta | Fecha de ejecución | Resultado principal |
|---|---|---|---|
| Springer Nature | journalsuggester.springer.com | Pendiente | Pendiente |
| Elsevier | journalfinder.elsevier.com | Pendiente | Pendiente |

> Adjuntar captura de pantalla de cada ejecución en esta misma carpeta con el
> nombre `captura_<editorial>_<YYYY-MM-DD>.png`.

---

## 3. Candidatas — lista cerrada de la guía (Sección 2)

### 3.1 Requirements Engineering (Springer)

| Campo | Dato |
|---|---|
| Editorial | Springer (Springer London) |
| ISSN | 0947-3602 (impreso), 1432-010X (electrónico) |
| Indexación | SCIE, Scopus |
| Cuartil JCR 2024 | Q2 en *Computer Science, Software Engineering*, posición 64 de 131 *(oficial, dato de la guía del curso, verificado 02/07/2026)* |
| Factor de impacto JCR 2024 | 3,3 *(oficial)* |
| Tiempo a primera decisión | Mediana de 5 días *(oficial, datos de junio de 2026)* |
| Plantilla | `sn-jnl.cls` (Springer Nature LaTeX template), estilo `sn-mathphys-num` |
| Ajuste temático | Revista central del área; es la que estudia específicamente ingeniería de requisitos, no un venue generalista con una sección de software. |

### 3.2 Information and Software Technology (Elsevier)

| Campo | Dato |
|---|---|
| Editorial | Elsevier |
| ISSN | 0950-5849 |
| Indexación | SCIE, Scopus |
| Cuartil JCR 2024 | Q1 *(oficial, dato de la guía del curso)* |
| Factor de impacto JCR 2024 | 4,3 *(oficial)* |
| Plantilla | `elsarticle.cls` |
| Ajuste temático | Publica estudios empíricos de ingeniería de requisitos con frecuencia; buen historial de trabajos citados en la sección de trabajo relacionado del manuscrito. |

### 3.3 Empirical Software Engineering (Springer)

| Campo | Dato |
|---|---|
| Editorial | Springer |
| ISSN | 1382-3256 |
| Indexación | SCIE, Scopus |
| Cuartil JCR 2024 | Q1 *(oficial, dato de la guía del curso)* |
| Factor de impacto JCR 2024 | Pendiente de verificar en JCR (la guía del curso no reporta el valor numérico exacto, solo el cuartil) |
| Plantilla | `sn-jnl.cls` |
| Ajuste temático | Revista natural para un estudio cuasi-experimental con métricas de acuerdo inter-evaluador; exige rigor metodológico alto. |

### 3.4 Journal of Systems and Software (Elsevier)

| Campo | Dato |
|---|---|
| Editorial | Elsevier |
| ISSN | 0164-1212 |
| Indexación | SCIE, Scopus |
| Cuartil JCR 2024 | Q1 *(oficial, dato de la guía del curso)* |
| Factor de impacto JCR 2024 | Pendiente de verificar en JCR |
| Plantilla | `elsarticle.cls` |
| Ajuste temático | Alcance amplio en ingeniería de software; acepta estudios de calidad de requisitos, aunque no es tan específica del área como *Requirements Engineering*. |

### 3.5 Conferencias — alternativa de menor riesgo

| Campo | REFSQ 2027 | IEEE RE 2027 |
|---|---|---|
| Lugar y fecha | Basel, Suiza, 12–15 de abril de 2027 | Por confirmar |
| Track recomendado | *Posters & Tools* — 8 páginas, plantilla `llncs.cls` | — |
| Plazos (track *Posters & Tools*) | Envío 4 de febrero de 2027; notificación 25 de febrero de 2027 | — |
| Nivel de exigencia | La guía del curso lo señala explícitamente como la **opción más accesible** para equipos de pregrado | Exigencia comparable a un journal de prestigio |

---

## 4. Viabilidad económica

Ninguna de las cuatro revistas de la lista cerrada exige pago obligatorio en
modalidad de publicación por suscripción (la vía por defecto, sin *open access*
dorado). Esto simplifica la pregunta que se hacía la versión anterior de este
documento sobre financiamiento de APC: **no es necesario resolverla**, porque
ninguna candidata de la lista cerrada lo exige para publicar.

| Pregunta | Respuesta |
|---|---|
| ¿Alguna candidata exige pago obligatorio en modalidad suscripción? | No. Las cuatro revistas de la Sección 3 aceptan publicación por suscripción sin cargo al equipo. |
| ¿Aplica entonces la pregunta de financiamiento de APC? | No, salvo que el equipo decida voluntariamente pagar por acceso abierto dorado, lo cual no es necesario para cumplir la guía. |

---

## 5. Verificación pendiente antes del envío

1. **Ejecutar las herramientas oficiales de sugerencia editorial** (Sección 2) con
   el resumen final y adjuntar las capturas.
2. **Confirmar en JCR (Clarivate), con acceso institucional de la UTEQ**, el factor
   de impacto exacto de *Empirical Software Engineering* y de *Journal of Systems
   and Software* — la guía del curso solo reporta el cuartil de ambas, no el valor
   numérico.
3. **Verificar la plantilla exacta exigida por la revista finalmente elegida** antes
   de enviar: el manuscrito ya está compilado en `sn-jnl.cls`, que corresponde a
   *Requirements Engineering* y a *Empirical Software Engineering*; si el equipo
   decide enviar a una de las dos revistas de Elsevier, hay que migrar a
   `elsarticle.cls`.

> **No inventar ninguna cifra.** Una tabla con valores no verificables es
> fabricación académica y dispara el gatekeeper G4.

---

## 6. Decisión y justificación

**Decisión:** *Requirements Engineering* (Springer), modalidad por suscripción.

Esta decisión ya está **ejecutada**, no solo recomendada: el manuscrito
(`07_Publicacion/manuscrito_final.tex`) compila desde su primera línea en
`sn-jnl.cls` con la nota explícita *"TEMPLATE: confirmed by the team as sn-jnl.cls
(Springer Nature), Requirements Engineering journal"*. Este documento se actualiza
para reflejar esa decisión en vez de mantenerla como "pendiente", que era la
inconsistencia de la versión anterior.

**Justificación.** Tres razones, en orden de peso:

1. **Ajuste temático directo.** De las cuatro revistas de la lista cerrada, es la
   única especializada exclusivamente en ingeniería de requisitos; las otras tres
   son revistas generalistas de ingeniería de software con una sección relevante.
2. **El riesgo de rechazo de escritorio por alcance empírico limitado, que motivó
   la recomendación provisional anterior hacia *Information and Software
   Technology*, ya no aplica con la misma fuerza.** La versión de agosto de este
   documento razonaba sobre un corpus de N=50 con resultados de acuerdo leve y no
   significativo. El corpus final tiene N=61, con acuerdo moderado
   estadísticamente significativo (κ=0,530, p=0,0001) y un panel de expertos con
   acuerdo casi perfecto (κ=0,857) — un resultado defendible en una revista
   específica del área, no solo en una generalista más permisiva.
3. **Tiempo a primera decisión más rápido** (mediana de 5 días) que le da margen
   al equipo para una eventual segunda ronda si hay retroalimentación editorial
   antes del cierre del semestre.

**Alternativa de menor riesgo si el tribunal o el equipo prefieren no arriesgar un
rechazo en una revista específica:** REFSQ 2027, track *Posters & Tools* — es la
opción que la propia guía del curso señala como la más accesible para un equipo de
pregrado, con plazo de envío (4 de febrero de 2027) fuera del cierre del semestre,
lo que da tiempo de preparación adicional.

**Categoría de envío.** Con el corpus ampliado a 61 requisitos y las cuatro
secciones de resultados, discusión, amenazas a la validez y conclusiones cerradas,
el manuscrito corresponde a un **artículo completo** (no a un *tool paper* corto),
consistente con haber alcanzado el objetivo empírico de la Entrega 2B. La
estimación de la versión anterior (artículo corto, por el corpus de 50 requisitos
sin cerrar) queda superada.

---

## 7. Registro de cambios

| Fecha | Cambio | Responsable |
|---|---|---|
| 2026-08-02 | Creación del documento. Título, resumen (versión 1.0) y palabras clave. Seis candidatas evaluadas, cuatro de ellas fuera de la lista cerrada de la guía. Decisión marcada como pendiente. | Fuertes Arraes, Edson Daniel |
| 2026-09-01 | Corrección de alcance: se retiran las cuatro candidatas no autorizadas (*Scientific Reports*, *Heliyon*, *IEEE Access*, *IEEE Transactions on Software Engineering*) y se reescribe la Sección 3 sobre la lista cerrada de la guía (4 revistas + 2 conferencias). Se actualiza el resumen con las secciones de Resultados y Conclusiones ya cerradas (N=61). Se fija la decisión en *Requirements Engineering* (Springer), consistente con la plantilla ya en uso en el manuscrito. Se elimina la sección de viabilidad de APC por no aplicar a ninguna candidata de la lista cerrada. | Equipo completo |
| Pendiente | Ejecución de las herramientas oficiales de sugerencia editorial y registro de capturas | Fuertes Arraes, Edson Daniel |
| Pendiente | Confirmación en JCR del factor de impacto exacto de *Empirical Software Engineering* y *Journal of Systems and Software* | Pendiente de asignar |
