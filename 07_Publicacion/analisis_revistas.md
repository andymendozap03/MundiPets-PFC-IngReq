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

| Editorial | Herramienta | Fecha de ejecución | Resultado principal (revista + puntuación de ajuste) |
|---|---|---|---|
| Springer Nature | journalsuggester.springer.com | _(completar)_ | _(completar)_ |
| Elsevier | journalfinder.elsevier.com | _(completar)_ | _(completar)_ |
| IEEE | publication-recommender.ieee.org | _(completar)_ | _(completar)_ |

> Adjuntar captura de pantalla de cada ejecución en esta misma carpeta con el
> nombre `captura_<editorial>_<YYYY-MM-DD>.png`. Sin la captura, la ejecución no
> es verificable.

---

## 3. Candidatas por editorial

La guía exige **al menos dos candidatas por editorial**: una en acceso abierto con
APC y otra por suscripción o híbrida sin cargo obligatorio para las personas
autoras. Las revistas listadas abajo son propuestas iniciales por ajuste temático;
**todas las cifras deben verificarse** en la fuente indicada en la Sección 5 antes
de considerarse válidas.

### 3.1 Springer Nature

| Campo | Candidata A (OA con APC) | Candidata B (suscripción/híbrida) |
|---|---|---|
| Nombre completo | Scientific Reports | Requirements Engineering |
| Editorial | Springer Nature | Springer Nature |
| Indexación JCR | _(verificar)_ | _(verificar)_ |
| Cuartil vigente | _(verificar)_ | _(verificar)_ |
| Factor de impacto | _(verificar)_ | _(verificar)_ |
| Modelo de acceso | Acceso abierto (gold) | Híbrida |
| Tarifa APC (USD) | _(verificar)_ | _(verificar; sin cargo si no se elige OA)_ |
| Tiempo medio a primera decisión | _(verificar)_ | _(verificar)_ |
| Tasa de aceptación | _(verificar)_ | _(verificar)_ |
| Ajuste temático | Publica trabajo de ingeniería de requisitos; Abdeahad et al. (2026), citado en el manuscrito, apareció aquí. Alcance amplio, lo que reduce el riesgo de rechazo de escritorio por tema. | Revista central del área. Máximo ajuste temático con el estudio; también la más exigente en tamaño de muestra y madurez del diseño. |

### 3.2 Elsevier

| Campo | Candidata A (OA con APC) | Candidata B (suscripción/híbrida) |
|---|---|---|
| Nombre completo | Heliyon | Information and Software Technology |
| Editorial | Elsevier | Elsevier |
| Indexación JCR | _(verificar)_ | _(verificar)_ |
| Cuartil vigente | _(verificar)_ | _(verificar)_ |
| Factor de impacto | _(verificar)_ | _(verificar)_ |
| Modelo de acceso | Acceso abierto (gold) | Híbrida |
| Tarifa APC (USD) | _(verificar)_ | _(verificar)_ |
| Tiempo medio a primera decisión | _(verificar)_ | _(verificar)_ |
| Tasa de aceptación | _(verificar)_ | _(verificar)_ |
| Ajuste temático | Sección de ciencias de la computación con alcance amplio. | Publicó Molléri et al. (2020) y Fischbach et al. (2023), ambos citados en el manuscrito. Fuerte tradición en estudios empíricos de requisitos. |

### 3.3 IEEE

| Campo | Candidata A (OA con APC) | Candidata B (suscripción/híbrida) |
|---|---|---|
| Nombre completo | IEEE Access | IEEE Transactions on Software Engineering |
| Editorial | IEEE | IEEE |
| Indexación JCR | _(verificar)_ | _(verificar)_ |
| Cuartil vigente | _(verificar)_ | _(verificar)_ |
| Factor de impacto | _(verificar)_ | _(verificar)_ |
| Modelo de acceso | Acceso abierto (gold) | Híbrida |
| Tarifa APC (USD) | _(verificar)_ | _(verificar)_ |
| Tiempo medio a primera decisión | _(verificar)_ | _(verificar)_ |
| Tasa de aceptación | _(verificar)_ | _(verificar)_ |
| Ajuste temático | Publicó Atoum et al. (2021) y Said et al. (2026), citados en el manuscrito. Revisión rápida y alcance amplio. | Revista de máximo prestigio del área. Exige contribución empírica de gran alcance; el N = 50 de este estudio probablemente queda por debajo de su umbral. |

---

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

## 5. Dónde verificar cada cifra

- **Indexación JCR, cuartil y factor de impacto:** Journal Citation Reports de
  Clarivate, vía el acceso institucional de la UTEQ. No usar cifras de sitios
  agregadores no oficiales.
- **Tarifa APC:** página de la revista en el sitio de la editorial, sección
  *Open access* o *Article processing charges*.
- **Tiempo medio a primera decisión y tasa de aceptación:** normalmente en la
  página *Journal metrics* o *About* de cada revista. Si no está publicada, anotar
  "no publicada" en lugar de estimarla.
- **Puntuación de ajuste temático:** la que devuelve la herramienta oficial de la
  Sección 6.3.

> **No inventar ninguna cifra.** Una tabla con valores no verificables es
> fabricación académica y dispara el gatekeeper G4.

---

## 6. Decisión y justificación

La política del PFC es que el envío final se decida en la **semana 16**, comparando
las candidatas de las tres editoriales. La justificación no puede basarse solo en
familiaridad o en presencia previa en la editorial: debe sustentarse en la
puntuación de ajuste de la herramienta oficial, en la coherencia entre el resumen
del manuscrito y el alcance publicado de la revista, y en la viabilidad económica y
temporal del envío.

**Revista seleccionada:** _(completar en la semana 16)_

**Justificación:** _(completar)_

**Categoría de envío prevista.** Según la Sección 7.11 de la guía, depende del
volumen de evidencia alcanzado:

- Objetivo 2B alcanzado → artículo completo (15–20 páginas) en revista JCR.
- Entre el mínimo 2A y el objetivo 2B → artículo corto o *tool paper* (6–8 páginas).
- Por debajo del mínimo 2A → póster o demostración.

**Categoría estimada al cierre de la Entrega 3 (2A):** _(completar tras contrastar
las evidencias del repositorio contra la tabla de la Sección 4.2 de la guía)_

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
| _(completar)_ | Ejecución de las tres herramientas oficiales y registro de capturas | _(completar)_ |
| _(completar)_ | Incorporación de métricas verificadas en JCR | _(completar)_ |
| _(completar)_ | Decisión final de revista (semana 16) | _(completar)_ |
