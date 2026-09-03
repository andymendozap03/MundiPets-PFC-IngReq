# 05_MVP — Producto Mínimo Viable de MundiPets

El código fuente del Producto Mínimo Viable (MVP) de MundiPets **forma
parte de este repositorio**, en la carpeta `05_MVP/codigo/`. Se incorporó
junto con su historial de commits original (desarrollado inicialmente en
un repositorio independiente y fusionado aquí mediante `git subtree`), de
modo que la autoría y la fecha real de cada cambio quedan preservadas.

## Contenido de `05_MVP/codigo/`

- Frontend en HTML5, CSS3 y JavaScript (sin frameworks ni proceso de
  compilación).
- Backend en [Express](https://expressjs.com/) sobre Node.js (`server.js`),
  que sirve el frontend estático y expone una API REST (`/api/...`).
- Persistencia en una base de datos **en memoria** dentro del proceso Node
  (sin motor de base de datos externo, sin contenedores), inicializada con
  un dataset ficticio en cada arranque del servidor. Las contraseñas se
  almacenan con hash bcrypt.
- Instrucciones de despliegue local documentadas en el `README.md` de esa
  carpeta.
- Cobertura de los requisitos funcionales de prioridad *Debe tener* (Must),
  marcada explícitamente en el `README.md` de esa carpeta.
- Video de demostración funcional (`video_demo.mp4`).

## Resumen de la solución implementada

MundiPets MVP es una aplicación web ejecutable construida con HTML5, CSS3 y
JavaScript en el frontend, y un servidor Express/Node.js en el backend que
expone una API REST y persiste los datos en memoria durante la ejecución
del proceso — en coherencia con el alcance de un prototipo de demostración
académica y no de un sistema en producción.

El MVP cubre **27 de 27 requisitos funcionales del proyecto (100 %)**,
incluidos los 15 requisitos de prioridad *Must*, superando ampliamente el
mínimo del 80 % de cobertura de RF *Must* exigido por el criterio C3 de la
rúbrica.

El repositorio documenta de forma honesta las simulaciones presentes en
esta iteración: el RF-06 (evaluación de compatibilidad para cruza) se
implementa mediante una heurística de reglas explícitas y explicables —no
mediante un modelo de aprendizaje automático entrenado—; el RF-17
(validación de imágenes) y el RF-10 (notificaciones por WhatsApp) se
simulan mediante analizadores y disparadores interactivos en lugar de
invocar servicios externos reales. El detalle completo de cada simulación
y su justificación consta en el `README.md` de `05_MVP/codigo/`.

## Despliegue local

Requiere [Node.js](https://nodejs.org/) (v18 o superior recomendado) y se
levanta con un solo comando, sin necesidad de Docker ni de configurar una
base de datos externa:

```bash
cd 05_MVP/codigo
npm install
npm start
```

Luego abrir `http://localhost:3000` en el navegador. El servidor Express
sirve tanto el frontend como la API, por lo que no hace falta levantar
ningún servicio adicional por separado.

## Cuentas de prueba

Al primer arranque, el servidor inicializa automáticamente cuatro cuentas
de demostración, una por cada rol del sistema:

| Rol | Email | Contraseña |
|---|---|---|
| Adoptante (Ana) | `ana.adoptante@ejemplo.com` | `Ana#2026` |
| Propietario (Carlos) | `carlos.zambrano@ejemplo.com` | `Carlos#2026` |
| Veterinaria (Dra. Melissa) | `melissa.vera@ejemplo.com` | `Melissa#2026` |
| Interesado en Cruza (Jorge) | `jorge.intriago@ejemplo.com` | `Jorge#2026` |

Todas las cuentas anteriores son ficticias y se generaron exclusivamente con
fines de demostración académica; no corresponden a personas reales ni deben
usarse como referencia de una política de contraseñas de producción.

## Advertencia sobre los datos de demostración

Todos los usuarios, mascotas, historiales médicos, solicitudes y mensajes
contenidos en el MVP son ficticios y se generaron exclusivamente con fines
de demostración académica. No representan personas, animales ni información
sanitaria reales.
