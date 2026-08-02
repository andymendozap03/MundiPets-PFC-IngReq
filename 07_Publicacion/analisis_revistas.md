# Análisis de revistas objetivo — MundiPets

**Proyecto:** MundiPets — Detección automática de ambigüedad en requisitos
**Asignatura:** Ingeniería de Requerimientos [20303] · UTEQ · PPA 2026–2027
**Documento:** requisito de la Sección 6.4 de la guía de la Entrega 3 (2A), criterio C10
**Última actualización:** 2 de agosto de 2026
**Responsable:** Fuertes Arraes, Edson Daniel (analista líder)

---

## 1. Insumos para la búsqueda

Estos son el título y el resumen que deben pegarse en las tres herramientas oficiales
de la Sección 6.3. No modificar aquí sin actualizar también el manuscrito.

**Título**

> Accuracy of a requirements ambiguity detector: case of a pet social network

**Resumen** (versión 1.0; las secciones de Resultados y Conclusiones se cierran
en la Entrega 4 y deben incorporarse aquí antes de la decisión de la semana 16)

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
> **Methods.** We conducted a paired quasi-experiment over 50 requirements (25
> functional, 16 non-functional and 9 design constraints) specified according to an
> eight-attribute template. A purpose-built rule-based detector, implemented in
> Python and frozen before data collection, classified each requirement as ambiguous
> or non-ambiguous using four lexical and syntactic rules. In parallel, three
> independent software engineers, blind to the detector output and to one another,
> classified the same requirements in randomised order using a shared rubric. The
> protocol was preregistered on the Open Science Framework before any data were
> collected. Agreement was quantified with precision, recall, F1, Cohen's kappa and
> Fleiss' kappa.

> Para pegar en las herramientas oficiales basta con el bloque de Context, Objective
> y Methods; los buscadores de las editoriales truncan a unas 250 palabras.

**Palabras clave**

> Requirements Engineering · Empirical Software Engineering · Natural Language
> Processing · Interrater Agreement · Requirements Quality

---

## 2. Ejecución de las herramientas oficiales

Las tres herramientas exigen pegar el título y el resumen en un formulario y devuelven
una puntuación de ajuste. **Esta ejecución debe hacerla el equipo**: la puntuación es
evidencia del proceso y sin la captura no es verificable.

| Editorial | Herramienta | Fecha de ejecución | Resultado principal (revista + puntuación de ajuste) |
|---|---|---|---|
| Springer Nature | journalsuggester.springer.com | Pendiente | Pendiente |
| Elsevier | journalfinder.elsevier.com | Pendiente | Pendiente |
| IEEE | publication-recommender.ieee.org | Pendiente | Pendiente |

> Adjuntar captura de pantalla de cada ejecución en esta misma carpeta con el nombre
> `captura_<editorial>_<YYYY-MM-DD>.png`.

## 3. Candidatas por editorial

Dos candidatas por editorial, como exige la guía: una en acceso abierto con APC y otra
por suscripción o híbrida sin cargo obligatorio.

**Sobre el origen de las cifras.** Las marcadas como *(oficial)* provienen de la página
de la propia revista o de la lista de títulos de la editorial, consultadas el
**2 de agosto de 2026**. Las marcadas como *(secundaria)* provienen de fuentes de
terceros y **deben confirmarse antes del envío**. El cuartil JCR vigente debe
verificarse en Journal Citation Reports de Clarivate mediante el acceso institucional
de la UTEQ; donde no se pudo, se indica el cuartil de SCImago, que no es equivalente.

### 3.1 Springer Nature

| Campo | Candidata A: Scientific Reports | Candidata B: Requirements Engineering |
|---|---|---|
| Editorial | Springer Nature (Nature Portfolio) | Springer Nature (Springer London) |
| Indexación | SCIE, Scopus, PubMed Central *(oficial)* | SCIE, Scopus, EI Compendex, DBLP, ACM DL *(oficial)* |
| Cuartil | Q1 en Multidisciplinary Sciences *(secundaria)* | Q2 en Information Systems y en Software, según SCImago *(secundaria)* |
| Factor de impacto | 4,9 (JCR 2025) *(oficial, nature.com/srep)* | 3,3 (2025); a 5 años 3,0 *(oficial, link.springer.com/journal/766)* |
| Modelo de acceso | Acceso abierto completo (gold), CC BY | Híbrida — publicar por suscripción **no tiene cargo** |
| Tarifa APC (USD) | ≈2.500–2.900 según región y moneda; las fuentes consultadas difieren *(secundaria — confirmar en la página de tarifas)* | Sin cargo en modalidad suscripción. Open Choice opcional *(confirmar tarifa en Fees and funding)* |
| Tiempo a primera decisión | Mediana 20 días *(oficial)* | Mediana 5 días *(oficial)* |
| Tasa de aceptación | No divulgada por la editorial | No publicada |
| Ajuste temático | Alcance amplio, lo que reduce el riesgo de rechazo de escritorio por tema. Abdeahad et al. (2026), citado en el manuscrito, se publicó aquí. | Revista central del área y el mejor ajuste temático posible. También la más exigente en alcance empírico. |

### 3.2 Elsevier

| Campo | Candidata A: Heliyon | Candidata B: Information and Software Technology |
|---|---|---|
| Editorial | Elsevier (Cell Press) | Elsevier |
| Indexación | Scopus, Web of Science (ESCI), PubMed, DOAJ *(secundaria)* | Scopus, SCIE, ABDC *(oficial, ScienceDirect)* |
| Cuartil | Q1 en Multidisciplinary Sciences *(secundaria)* | Q1 en Computer Science Applications, Information Systems y Software, según SCImago *(secundaria)* |
| Factor de impacto | 3,6 (JCR 2025); a 5 años 3,9 *(secundaria)* | CiteScore 4,3 *(oficial)*; factor de impacto a verificar en JCR |
| Modelo de acceso | Acceso abierto completo (gold), CC BY | Híbrida — publicar por suscripción **no tiene cargo** |
| Tarifa APC (USD) | 2.270 más impuestos *(oficial, cell.com/heliyon/open-access)* | 3.890 más impuestos si se elige acceso abierto; **0 en modalidad suscripción** *(oficial)* |
| Tiempo a primera decisión | ≈90 días *(secundaria)* | 7 días a primera decisión; 94 días a decisión tras revisión; 217 días a aceptación *(oficial)* |
| Tasa de aceptación | No publicada | No publicada |
| Ajuste temático | Multidisciplinar; acepta por solidez metodológica más que por novedad, lo que favorece a un estudio de réplica como este. | Publicó a Molléri et al. (2020) y a Fischbach et al. (2023), ambos citados en el manuscrito. Tradición fuerte en estudios empíricos de requisitos. |
| Riesgo a considerar | Su cobertura en Web of Science es ESCI, no SCIE. La guía exige indexación en JCR: **confirmar en Clarivate que tiene JIF vigente** antes de elegirla. | Ninguno identificado. |

### 3.3 IEEE

| Campo | Candidata A: IEEE Access | Candidata B: IEEE Transactions on Software Engineering |
|---|---|---|
| Editorial | IEEE | IEEE Computer Society |
| Indexación | SCIE *(oficial, IEEE Title List enero 2026)* | SCIE, Current Contents *(secundaria)* |
| Cuartil | Q2 *(oficial, IEEE Title List)* | Q1 en Software *(secundaria)* |
| Factor de impacto | 3,6; a 5 años 3,9; CiteScore 9,0 *(oficial)* | Entre 5,6 y 6,5 según el año de JCR consultado *(secundaria — verificar el vigente)* |
| Modelo de acceso | Acceso abierto completo (gold) | Híbrida — publicar por suscripción **no tiene cargo** |
| Tarifa APC (USD) | Las fuentes consultadas dan 1.995 y 2.160 *(secundaria — confirmar en open.ieee.org)* | Sin cargo en modalidad suscripción |
| Tiempo a primera decisión | 4 a 6 semanas de envío a publicación *(oficial)* | No publicada |
| Tasa de aceptación | No publicada oficialmente | No publicada |
| Ajuste temático | Publicó a Atoum et al. (2021) y a Said et al. (2026), citados en el manuscrito. Revisión binaria y rápida. | Revista de máximo prestigio del área. Exige contribución empírica de gran alcance; con N = 50 el riesgo de rechazo de escritorio es alto. |

## 4. Viabilidad económica

La guía advierte que el APC en editoriales de alto impacto ronda los 1.500–3.500
USD y que los equipos de pregrado pueden no disponer de ese financiamiento.

| Pregunta | Respuesta |
|---|---|
| ¿El equipo dispone de fondos para APC? | _(completar — decisión del equipo)_ |
| ¿La UTEQ tiene convenio transformativo con alguna de las tres editoriales? | _(consultar en la biblioteca institucional; es la vía que más puede abaratar el envío)_ |
| ¿Existe exención o descuento por país (waiver) aplicable a Ecuador? | Poco probable. Los programas de exención total de las grandes editoriales suelen restringirse a países clasificados por el Banco Mundial como de ingreso bajo o mediano-bajo, y Ecuador figura como de ingreso mediano-alto. **Verificar caso por caso** en la política de cada editorial antes de descartarlo. |

> Si la respuesta a las tres es negativa, la ruta viable es la candidata B de cada
> editorial: híbrida sin cargo obligatorio, publicando en modalidad por suscripción.

---

## 5. Verificación pendiente antes del envío

Tres cifras quedaron sin confirmar en fuente oficial y deben cerrarse antes de la
decisión de la semana 16:

1. **Cuartil JCR vigente de las seis revistas.** Journal Citation Reports de Clarivate,
   con el acceso institucional de la UTEQ. Los cuartiles anotados arriba como
   *(secundaria)* provienen de SCImago, que usa SJR y **no es equivalente al JCR**.
2. **Tarifa APC exacta de Scientific Reports y de IEEE Access.** Las fuentes consultadas
   difieren entre sí. Confirmar en la página de tarifas de cada revista.
3. **Estado de indexación de Heliyon en Web of Science.** Si su cobertura es ESCI y no
   SCIE, hay que confirmar que igualmente tiene JIF vigente en JCR; de lo contrario no
   cumple el requisito de la guía y debe sustituirse por otra candidata de Elsevier.

> **No inventar ninguna cifra.** Una tabla con valores no verificables es fabricación
> académica y dispara el gatekeeper G4.

## 6. Decisión y justificación

La política del PFC es que el envío final se decida en la **semana 16**, comparando
las candidatas de las tres editoriales. La justificación no puede basarse solo en
familiaridad o en presencia previa en la editorial: debe sustentarse en la
puntuación de ajuste de la herramienta oficial, en la coherencia entre el resumen
del manuscrito y el alcance publicado de la revista, y en la viabilidad económica y
temporal del envío.

**Recomendación provisional (2 de agosto de 2026):** *Information and Software
Technology* (Elsevier), en modalidad por suscripción.

**Justificación de la recomendación provisional.** Es la única candidata que combina
las tres condiciones que importan aquí. Primero, ajuste temático demostrado: publicó a
Molléri et al. (2020) y a Fischbach et al. (2023), ambos citados en el trabajo
relacionado del manuscrito, y tiene tradición en estudios empíricos de requisitos.
Segundo, costo cero: en modalidad suscripción no cobra APC, lo que elimina la
dependencia de un financiamiento que el equipo probablemente no tiene. Tercero,
indexación SCIE confirmada en fuente oficial, que es lo que exige la guía.

Frente a las alternativas: *Requirements Engineering* tiene mejor ajuste temático aún,
pero es la más exigente en alcance empírico y con N = 50 el riesgo de rechazo de
escritorio es alto; *IEEE Transactions on Software Engineering* tiene el mismo problema
agravado. *IEEE Access* y *Heliyon* son las salidas rápidas si se consigue APC, pero
cuestan entre 2.000 y 2.300 dólares y Heliyon además tiene el problema de indexación
señalado en la Sección 5.

**Decisión final (semana 16):** Pendiente. La política del PFC exige decidir comparando
las candidatas de las tres editoriales con las puntuaciones de ajuste de la Sección 2,
que todavía no se han ejecutado. Esta recomendación es provisional y puede cambiar con
esos resultados.

**Categoría de envío prevista.** Según la Sección 7.11 de la guía, depende del
volumen de evidencia alcanzado:

- Objetivo 2B alcanzado → artículo completo (15–20 páginas) en revista JCR.
- Entre el mínimo 2A y el objetivo 2B → artículo corto o *tool paper* (6–8 páginas).
- Por debajo del mínimo 2A → póster o demostración.

**Categoría estimada al cierre de la Entrega 3 (2A):** artículo corto o *tool paper*
(6–8 páginas), a confirmar contrastando las evidencias del repositorio contra la tabla
de la Sección 4.2 de la guía.

> Consideración de alcance empírico, a tener en cuenta al elegir. El estudio se
> apoya en un corpus de 50 requisitos de un solo sistema, evaluado por un panel de
> tres personas. *IEEE Transactions on Software Engineering* y *Requirements
> Engineering* son las de mejor ajuste temático, pero también las que exigen mayor
> alcance empírico; con este N el riesgo de rechazo de escritorio es alto. Las
> candidatas realistas para un artículo corto o *tool paper* son *IEEE Access* y
> *Heliyon*, y entre ellas la decisión depende de si se consigue financiamiento
> para el APC.

---

## 7. Registro de cambios

| Fecha | Cambio | Responsable |
|---|---|---|
| 2026-08-02 | Creación del documento. Se definen título, resumen y palabras clave definitivos de la versión 1.0 del manuscrito. Se proponen dos candidatas por editorial (una OA con APC y una híbrida sin cargo obligatorio) con justificación de ajuste temático basada en las revistas donde aparecen los trabajos citados en la sección de trabajo relacionado. Quedan pendientes las métricas bibliométricas y la ejecución de las tres herramientas oficiales. | Fuertes Arraes, Edson Daniel |
| Pendiente | Ejecución de las tres herramientas oficiales y registro de capturas | Fuertes Arraes, Edson Daniel |
| Pendiente | Confirmación en Clarivate de los tres puntos de la Sección 5 | Pendiente de asignar |
| Pendiente (semana 16) | Decisión final de revista | Equipo completo |
