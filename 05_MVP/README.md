# 05_MVP — Producto Mínimo Viable de MundiPets

El código fuente del Producto Mínimo Viable (MVP) de MundiPets **no reside en este
repositorio**. Debido a su volumen, se aloja en un repositorio Git independiente,
siguiendo lo permitido en la Sección 7.6 de la rúbrica de la Entrega 3 (2A).

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
prototipo de demostración académica. El MVP cubre 14 de los 15 requisitos
funcionales *Must* definidos en el ERS/SRS (93,3 %), superando el mínimo
del 60 % exigido por la rúbrica, e incorpora además dos requisitos
*Should*/*Could* (búsqueda y filtrado, y mensajería entre usuarios) ya
delineados en los mockups de referencia.

El repositorio del MVP documenta de forma honesta las limitaciones de esta
iteración: el RF-06 (evaluación de compatibilidad para cruza) se implementa
mediante una heurística de reglas explícitas y explicables —no mediante un
modelo de aprendizaje automático entrenado—, y el RF-17 (validación de
imágenes contra las políticas de contenido de la plataforma) no fue
implementado en este alcance; el registro de mascotas utiliza en su lugar
la selección directa de un ícono representativo.

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
