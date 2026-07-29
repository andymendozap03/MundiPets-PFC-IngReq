# MundiPets — MVP funcional (05_MVP)

Producto Mínimo Viable (MVP) del sistema **MundiPets**, una red social orientada a
facilitar procesos de adopción y cruza responsable de mascotas en la provincia de
Los Ríos, Ecuador. Este entregable corresponde a la Sección 6 del documento
ERS/SRS completo (`01_ERS/ERS_SRS_2A_v1.0.pdf`) y al insumo `05_MVP/` exigido por
la rúbrica de la Entrega 3 (2A) de la asignatura Ingeniería de Requerimientos.

## Integrantes del equipo (roles según portada del ERS)

| Integrante | Rol |
|---|---|
| Fuertes Arraes Edson Daniel | Analista líder |
| Gutiérrez Ortega Génesis Adriana | Verificador |
| Mendoza Párraga Andy Johel | Modelador |
| Morales Sánchez Gary Alejandro | Documentador |
| Nieves Sánchez Jimmy Samuel | Verificador |

## Alcance y límites de este entregable

Este repositorio contiene **únicamente la aplicación MVP funcional y su
documentación de despliegue**. No incluye evidencias de campo (entrevistas,
consentimientos, cuestionarios), el protocolo experimental registrado en OSF, ni
el dataset de Zenodo — esos insumos exigen datos primarios reales recolectados
por el equipo y **no pueden generarse artificialmente** (regla operativa de la
rúbrica: "nada declarado puede quedar solo declarado"). Esos artefactos deben
producirse por separado con trabajo de campo real y ubicarse en `02_Evidencias/`,
`06_Experimento/` y `07_Publicacion/` según el árbol de carpetas de la rúbrica.

## Cobertura de Requisitos Funcionales (RF)

Mínimo exigido por la rúbrica (criterio C8): MVP con cobertura **≥ 60 %** de los
RF de prioridad *Debe tener* (Must). El ERS define 15 RF Must; este MVP cubre
**14 de 15 (93 %)**, muy por encima del mínimo.

| RF | Nombre | Prioridad | Cubierto | Pantalla(s) |
|---|---|---|---|---|
| RF-01 | Registrar mascota | Must | ✅ Sí | `pet-add.html` |
| RF-02 | Gestionar historial médico de la mascota | Must | ✅ Sí | `pet-add.html`, `pet-profile.html` |
| RF-03 | Consultar perfil completo de una mascota | Must | ✅ Sí | `pet-detail.html`, `pet-profile.html` |
| RF-04 | Buscar y filtrar mascotas | Should | ✅ Sí (extra) | `explore.html` |
| RF-05 | Gestionar solicitudes de adopción | Must | ✅ Sí | `request.html` |
| RF-06 | Evaluar compatibilidad entre mascotas para cruza | Must | ✅ Sí (heurística explicable, no ML) | `compatibility.html` |
| RF-07 | Sistema de mensajería entre usuarios | Could | ✅ Sí (extra) | `request.html` (panel de chat) |
| RF-08 | Gestionar solicitudes de cruza | Must | ✅ Sí | `request.html` (tipo "Cruza responsable") |
| RF-09 | Validar la información médica de una mascota | Must | ✅ Sí | `vet-panel.html` |
| RF-10 | Gestionar recordatorios de controles preventivos | Should | ❌ No implementado | — |
| RF-11 | Administrar la privacidad de la información | Must | ✅ Sí | `pet-profile.html` |
| RF-12 | Verificar la identidad de los usuarios | Must | ✅ Sí (simulado) | `register.html` |
| RF-13 | Registrar publicaciones de mascotas | Must | ✅ Sí | `pet-profile.html`, `explore.html` |
| RF-14 | Gestionar carnet de vacunación | Must | ✅ Sí | `pet-add.html`, `pet-profile.html` |
| RF-15 | Consultar el historial de procesos de adopción y cruza | Could | ❌ No implementado | — |
| RF-16 | Gestionar antecedentes genéticos y parentesco de la mascota | Must | ✅ Sí | `pet-add.html`, `pet-profile.html` |
| RF-17 | Validar imágenes | Should | ❌ No implementado (selección directa de ícono) | — |
| RF-18 | Gestionar el flujo de solicitud de adopción por etapas | Must | ✅ Sí | `request.html` |
| RF-19 | Validar certificados veterinarios antes de habilitar la cruza | Should | ❌ No implementado | — |
| RF-20 | Coordinar encuentros de socialización supervisados | Could | ❌ No implementado | — |
| RF-21 | Registrar el identificador de microchip de la mascota | Should | ❌ No implementado | — |
| RF-22 | Dar seguimiento post-adopción | Must | ✅ Sí | `post-adoption.html` |
| RF-23 | Emitir alertas de riesgo sanitario o físico en interacciones y cruces | Must | ✅ Sí | `compatibility.html` |
| RF-24 | Registrar trazabilidad de cepa, lote y aplicador de cada vacuna | Should | ❌ No implementado | — |
| RF-25 | Publicar aviso de mascota extraviada | Could | ❌ No implementado | — |

**Resumen:** 14/15 RF Must cubiertos (93 %) + 2 RF Should/Could adicionales
(RF-04, RF-07) por estar delineados en los mockups de referencia.

> Nota sobre "IA": el ERS pide componentes de inteligencia artificial (RF-06,
> RF-17, moderación de mensajes). En este MVP, RF-06 se implementa como una
> **heurística de reglas explícitas y explicables** (parentesco, estado
> sanitario, edad reproductiva, disparidad de tamaño), no como un modelo de
> aprendizaje automático real — se declara así honestamente porque entrenar o
> integrar un modelo de ML está fuera del alcance de un MVP de datos ficticios.
> RF-17 (validación de imágenes) no se implementó; en su lugar el registro de
> mascotas usa selección directa de un ícono representativo.

## Stack técnico

- HTML5 + CSS3 + JavaScript (vanilla, sin frameworks ni build step).
- Persistencia 100 % en el navegador con `localStorage` (sin backend, sin
  PostgreSQL, sin Docker), a través de la capa `js/db.js`.
- Datos ficticios (seed) precargados: 4 usuarios de demostración (Propietario,
  Adoptante, Interesado en cruza, Veterinaria) y 4 mascotas (Firulais, Michi,
  Toby, Luna), inspirados en los mockups de referencia del proyecto.
- Diseño responsivo (mobile / tablet / desktop) mediante CSS Grid/Flexbox y
  media queries en `css/styles.css`.

## Estructura del repositorio

```
MVP_MundiPets/
├── index.html            Login / selección de cuenta de demostración
├── register.html         Crear cuenta (RF-12)
├── dashboard.html         Panel según rol (Propietario / Adoptante / Veterinaria)
├── pet-add.html            Wizard de registro de mascota (RF-01, RF-02, RF-14, RF-16)
├── pet-profile.html        Perfil propio, historial médico y privacidad (RF-03, RF-11, RF-13)
├── explore.html             Búsqueda y filtros (RF-04)
├── pet-detail.html          Perfil público de una mascota (RF-03)
├── request.html               Solicitud de adopción/cruza por etapas + chat (RF-05, RF-08, RF-18, RF-07)
├── compatibility.html         Evaluación de compatibilidad de cruza (RF-06, RF-23)
├── vet-panel.html              Panel de validación veterinaria (RF-09)
├── post-adoption.html          Seguimiento post-adopción (RF-22)
├── css/styles.css               Estilos y diseño responsivo
├── js/db.js                     Capa de datos sobre localStorage + seed ficticio
├── js/auth.js                   Sesión de rol simulada
└── js/utils.js                  Helpers compartidos (badges, toasts, topbar)
```

## Instrucciones de despliegue local (sin Docker)

No se requiere instalación de dependencias ni servidor de aplicaciones. Basta un
servidor estático (o incluso abrir el archivo directamente):

**Opción 1 — Python (viene preinstalado en la mayoría de sistemas):**
```bash
cd MVP_MundiPets
python -m http.server 8000
```
Luego abrir `http://localhost:8000` en el navegador.

**Opción 2 — Node.js:**
```bash
cd MVP_MundiPets
npx serve .
```

**Opción 3 — directo:**
Abrir `index.html` con doble clic en el navegador (Chrome, Firefox o Edge
actualizados). Algunas funciones de `localStorage` funcionan igual en modo
`file://`, pero se recomienda la Opción 1 o 2 para una experiencia idéntica en
todos los navegadores.

Al primer arranque, la aplicación crea automáticamente los datos de ejemplo en
`localStorage`. Para restablecerlos en cualquier momento, usar el enlace
**"Restablecer datos de ejemplo"** en la pantalla de inicio de sesión.

## Recorrido funcional sugerido para la demo

1. Ingresar como **Carlos Zambrano** (Propietario) → registrar una mascota nueva
   con el wizard de 4 pasos → publicarla para adopción.
2. Cerrar sesión e ingresar como **Ana Adoptante** → explorar mascotas con
   filtros → ver el perfil de Firulais → enviar una solicitud de adopción →
   conversar por el chat simulado.
3. Volver a ingresar como Carlos → avanzar la solicitud por las 5 etapas hasta
   completarla → revisar el seguimiento post-adopción generado automáticamente.
4. Ingresar como **Dra. Melissa Vera** (Veterinaria) → abrir el panel de
   validaciones → validar o rechazar un documento médico pendiente.
5. Ingresar como **Jorge Intriago** (Interesado en cruza) → ver a Toby (cruza
   responsable) → evaluar compatibilidad con otra mascota → observar el
   resultado explicado y las alertas de riesgo.

## Video de demostración

La rúbrica exige un video corto (≤ 3 min) en `05_MVP/video_demo.mp4` mostrando
este recorrido. Grabarlo no es una acción que un asistente de código pueda
realizar; el equipo debe grabarlo siguiendo el recorrido descrito arriba y
depositarlo en esa ruta antes del corte.

## Advertencia sobre los datos

Todos los usuarios, mascotas, historiales médicos, solicitudes y mensajes de
este MVP son **ficticios**, generados únicamente para fines de demostración
académica. No representan personas, animales ni información sanitaria reales.
