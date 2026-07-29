# Justificación de la carpeta `prompts_llm/`

## Estado

**No aplica para la ejecución del componente empírico seleccionado.**

## Justificación

El proyecto MundiPets adoptó el **Enfoque 2: detección automática de ambigüedad y malos olores en requisitos**. En este enfoque no se utilizó un Modelo Grande de Lenguaje (LLM) para generar, clasificar, modificar ni interpretar los requisitos del corpus experimental.

La clasificación automática fue realizada mediante un **detector propio implementado en Python**, basado en reglas y expresiones regulares previamente definidas. Las reglas analizan patrones textuales como cuantificadores vagos, conjunciones múltiples, voz pasiva o sujeto ausente y ausencia de criterios de verificación.

Por tanto, durante la ejecución del experimento no existieron prompts, parámetros de temperatura, `top-p`, `top-k`, semilla ni respuestas producidas por un LLM que deban registrarse en esta carpeta.

La carpeta `prompts_llm/` se conserva únicamente para mantener la estructura obligatoria del repositorio y dejar constancia explícita de que este insumo no corresponde al diseño experimental ejecutado.

## Material de replicación correspondiente

Los artefactos reproducibles del experimento se encuentran en:

- `../scripts_analisis/`: scripts en Python que ejecutan el detector y reproducen las tablas y figuras.
- `../resultados/`: datos procesados, tablas y figuras obtenidas.
- `../instrumentos/`: rúbrica de clasificación experta y documentos asociados.
- `../protocolo.pdf`: diseño experimental, preguntas de investigación, variables y plan de análisis.

## Declaración de integridad

No se han omitido prompts utilizados durante el experimento. La ausencia de archivos de prompts responde a que el procedimiento automático se ejecutó mediante reglas programadas y no mediante consultas a un LLM.
