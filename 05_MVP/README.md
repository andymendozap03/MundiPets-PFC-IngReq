# 05_MVP — Producto Mínimo Viable de MundiPets

El código fuente del Producto Mínimo Viable (MVP) de MundiPets **no reside en este
repositorio**. Debido a su volumen, se aloja en un repositorio Git independiente,
siguiendo lo permitido en la Sección 7.6 de la rúbrica de la Entrega 4 (2B).

## Repositorio del MVP

**Enlace:** https://github.com/jnievess-lang/MVP_MundiPets.git

## Contenido del repositorio del MVP

El repositorio `MVP_MundiPets` contiene:

- Código fuente organizado por módulos (páginas HTML, hoja de estilos única y
  módulos de JavaScript para sesión, datos y utilidades).
- Instrucciones de despliegue local sin dependencias externas ni contenedores.
- Cobertura de los requisitos funcionales de prioridad *Debe tener* (Must),
  marcada explícitamente en el `README.md` de dicho repositorio.
- Video de demostración funcional (duración ≤ 3 minutos) en
  `video_demo.mp4`.

## Resumen de la solución implementada

MundiPets MVP es una aplicación web ejecutable construida con HTML5, CSS3 y
JavaScript, sin frameworks ni proceso de compilación, que persiste su
información en el almacenamiento local del navegador (`localStorage`) en
lugar de un servidor de base de datos, en coherencia con el alcance de un
prototipo de demostración académica. El MVP cubre **27 de 27 requisitos
funcionales *Must* definidos en el ERS/SRS (100 %)**, y un total de **26 de 27
requisitos funcionales del proyecto (96,3 %)**, superando ampliamente el
mínimo del 80 % (criterio C3) exigido por la rúbrica.

El repositorio del MVP documenta de forma honesta las limitaciones de esta
iteración: el RF-06 (evaluación de compatibilidad para cruza) se implementa
mediante una heurística de reglas explícitas y explicables —no mediante un
modelo de aprendizaje automático entrenado—, y el RF-20 (coordinar encuentros
de socialización supervisados, prioridad *Could*) no fue implementado en este
alcance.

## Trazabilidad del commit evaluado

Para asegurar que el commit evaluado en esta entrega quede fijado y no se
vea afectado por cambios posteriores en el repositorio del MVP, este se
referencia como **submódulo Git** dentro de la carpeta `05_MVP/mvp/`.

Para clonar este repositorio junto con el submódulo del MVP:

```bash
git clone --recurse-submodules <URL-de-este-repositorio>
```

Si el repositorio ya fue clonado sin el submódulo:

```bash
git submodule update --init --recursive
```

Para consultar el commit exacto del MVP fijado en esta entrega:

```bash
git submodule status
```

## Advertencia sobre los datos de demostración

Todos los usuarios, mascotas, historiales médicos, solicitudes y mensajes
contenidos en el MVP son ficticios y se generaron exclusivamente con fines
de demostración académica. No representan personas, animales ni información
sanitaria reales.
