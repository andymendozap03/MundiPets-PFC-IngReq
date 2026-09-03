# MundiPets — MVP funcional (05_MVP)

Producto Mínimo Viable (MVP) del sistema **MundiPets**, una red social orientada a
facilitar procesos de adopción y cruza responsable de mascotas en la provincia de
Los Ríos, Ecuador. Este entregable corresponde a la Sección 6 del documento
ERS/SRS completo (`01_ERS/ERS_SRS_2B_v2.0.pdf`) y al insumo `05_MVP/` exigido por
la rúbrica de la Entrega 4 (2B) de la asignatura Ingeniería de Requerimientos.

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
por el equipo y **no pueden generarse artificialmente**. Esos artefactos deben
producirse por separado con trabajo de campo real y ubicarse en `02_Evidencias/`,
`06_Experimento/` y `07_Publicacion/`.
## Cobertura de Requisitos Funcionales (RF)

Mínimo exigido por la rúbrica (criterio C8): MVP con cobertura **≥ 80 %** de los RF de prioridad *Debe tener* (Must). En esta versión actualizada, el MVP cubre **15 de 15 (100%)** de los requisitos *Must*, y la **totalidad: 27 de 27 (100%)** de los requisitos funcionales del proyecto.

| RF | Nombre | Prioridad | Cubierto | Pantalla(s) / Flujo |
|---|---|---|---|---|
| RF-01 | Registrar mascota | Must | ✅ Sí | `pet-add.html` |
| RF-02 | Gestionar historial médico de la mascota | Must | ✅ Sí | `pet-add.html`, `pet-profile.html` |
| RF-03 | Consultar perfil completo de una mascota | Must | ✅ Sí | `pet-detail.html`, `pet-profile.html` |
| RF-04 | Buscar y filtrar mascotas | Should | ✅ Sí | `explore.html` |
| RF-05 | Gestionar solicitudes de adopción | Must | ✅ Sí | `request.html` |
| RF-06 | Evaluar compatibilidad entre mascotas para cruza | Must | ✅ Sí (heurística explicable, no ML) | `compatibility.html` |
| RF-07 | Sistema de mensajería entre usuarios | Could | ✅ Sí | `request.html` (panel de chat) |
| RF-08 | Gestionar solicitudes de cruza | Must | ✅ Sí | `request.html` (tipo "Cruza responsable") |
| RF-09 | Validar la información médica de una mascota | Must | ✅ Sí | `vet-panel.html` |
| RF-10 | Gestionar recordatorios de controles preventivos | Should | ✅ Sí (nuevo) | `dashboard.html` (módulo de alertas + simulación de WhatsApp) |
| RF-11 | Administrar la privacidad de la información | Must | ✅ Sí | `pet-profile.html` |
| RF-12 | Verificar la identidad de los usuarios | Must | ✅ Sí (simulado) | `register.html`, `index.html` (login con credenciales) |
| RF-13 | Registrar publicaciones de mascotas | Must | ✅ Sí | `pet-profile.html`, `explore.html` |
| RF-14 | Gestionar carnet de vacunación | Must | ✅ Sí | `pet-add.html`, `pet-profile.html` |
| RF-15 | Consultar el historial de procesos de adopción y cruza | Could | ✅ Sí (nuevo) | `dashboard.html` (sección expandible de solicitudes finalizadas) |
| RF-16 | Gestionar antecedentes genéticos y parentesco de la mascota | Must | ✅ Sí | `pet-add.html`, `pet-profile.html`, `pet-detail.html` |
| RF-17 | Validar imágenes | Should | ✅ Sí (nuevo) | `pet-add.html` (simulación interactiva de escáner IA en el Paso 2) |
| RF-18 | Gestionar el flujo de solicitud de adopción por etapas | Must | ✅ Sí | `request.html` |
| RF-19 | Validar certificados veterinarios antes de habilitar la cruza | Should | ✅ Sí (nuevo) | `pet-profile.html` (bloqueo si no cuenta con certificado validado) |
| RF-20 | Coordinar encuentros de socialización supervisados | Could | ✅ Sí (nuevo) | `encounters.html` |
| RF-21 | Registrar el identificador de microchip de la mascota | Should | ✅ Sí (nuevo) | `pet-add.html`, `pet-profile.html`, `pet-detail.html`, `explore.html` |
| RF-22 | Dar seguimiento post-adopción | Must | ✅ Sí | `post-adoption.html` |
| RF-23 | Emitir alertas de riesgo sanitario o físico en interacciones y cruces | Must | ✅ Sí | `compatibility.html` |
| RF-24 | Registrar trazabilidad de cepa, lote y aplicador de cada vacuna | Should | ✅ Sí (nuevo) | `pet-add.html`, `pet-profile.html` (campos del carnet referencial) |
| RF-25 | Publicar aviso de mascota extraviada | Could | ✅ Sí (nuevo) | `pet-profile.html`, `explore.html` (alerta roja destacada y contacto directo) |
| RF-26 | Habilitar validación médica por segunda opinión veterinaria | Should | ✅ Sí (nuevo) | `vet-panel.html`, `pet-profile.html` (módulo de doble validación y constancia) |
| RF-27 | Controlar y alertar sobre solicitudes repetitivas de cruza | Should | ✅ Sí (nuevo) | `compatibility.html` (alerta automatizada por superación de cruzas semestrales) |

**Resumen:** 27/27 RF cubiertos (100% de cobertura total y 100% de los requisitos *Debe tener*).

> **Nota sobre los componentes de IA e imágenes:** 
> * **RF-06 (Compatibilidad):** Implementado mediante reglas heurísticas explícitas (parentesco, alertas sanitarias, edad y disparidad de tamaño).
> * **RF-17 (Validación de imágenes):** Simulado en el Paso 2 de `pet-add.html` a través de un analizador interactivo que detecta y autoriza/rechaza las fotos (explicabilidad RNF-14).
> * **RF-10 (Notificaciones de WhatsApp):** Simulado mediante un activador emergente que reproduce el envío del mensaje de control al teléfono del usuario.
> * **RF-27 (Uso repetitivo):** Probado y disparado automáticamente en la evaluación de compatibilidad de Toby (`p3`), el cual cuenta con historial de cruzas completadas en su base de datos.
> * **RF-20 (Encuentros de socialización):** Implementado en `encounters.html`; un propietario propone fecha, lugar y mascota/propietario invitado, el otro propietario confirma o rechaza, y el encuentro confirmado queda visible en el historial de interacciones de ambas mascotas (`pet-profile.html`).

## Cuenta de usuario: contraseñas y perfil

- **Registro (`register.html`) y recuperación (`forgot-password.html`)** exigen una contraseña que cumpla la política de seguridad: mínimo 8 caracteres, al menos una mayúscula, una minúscula, un número y un carácter especial. El cumplimiento se valida en vivo mediante un checklist visual (`js/utils.js` → `validatePassword` / `passwordChecklistHtml`), y se vuelve a validar en el servidor (`server.js`) antes de aceptar el registro o el cambio de contraseña.
- **Recuperación de contraseña:** flujo de 3 pasos (correo → código de verificación → nueva contraseña). Como el MVP no tiene backend de correo real, el código de 6 dígitos se simula y se muestra en pantalla con fines de demostración (mismo criterio de simulación usado en RF-10 para WhatsApp).
- **Mostrar/ocultar contraseña:** todos los campos de contraseña de la aplicación incluyen un botón de ojito para alternar su visibilidad (`enablePasswordToggles` en `js/utils.js`).
- **Editar perfil (`profile.html`):** accesible haciendo clic en el nombre/avatar en la barra superior de cualquier pantalla. Permite actualizar nombre, correo y ciudad, y cambiar la contraseña verificando la contraseña actual (endpoint `/api/auth/change-password`).

## Stack técnico

- **Frontend:** HTML5 + CSS3 + JavaScript (vanilla, sin frameworks ni build step).
- **Backend:** [Express](https://expressjs.com/) sobre Node.js (`server.js`), que
  sirve el frontend estático y expone una API REST (`/api/...`).
- **Persistencia:** base de datos **en memoria** dentro del proceso Node (sin
  motor de BD externo, sin Docker), inicializada con el mismo dataset ficticio
  en cada arranque del servidor. Las contraseñas se almacenan con **hash bcrypt**
  (`bcryptjs`), nunca en texto plano ni expuestas por la API.
- Datos ficticios (seed) precargados: 4 usuarios de demostración (Propietario,
  Adoptante, Interesado en cruza, Veterinaria) y 4 mascotas (Firulais, Michi,
  Toby, Luna), inspirados en los mockups de referencia del proyecto.
- Diseño responsivo (mobile / tablet / desktop) mediante CSS Grid/Flexbox y
  media queries en `css/styles.css`.

> **Nota sobre la persistencia:** al ser datos en memoria, se reinician al
> dataset semilla cada vez que el servidor se reinicia (equivalente al botón
> "Restablecer datos de ejemplo" del MVP anterior). Mientras el proceso esté
> activo, los datos se comparten entre todos los usuarios conectados — a
> diferencia de la versión anterior basada en `localStorage`, donde cada
> navegador tenía su propia copia aislada.

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
├── encounters.html             Encuentros de socialización supervisados (RF-20)
├── forgot-password.html        Recuperación de contraseña con política de seguridad
├── profile.html                 Editar perfil y cambiar contraseña
├── css/styles.css               Estilos y diseño responsivo
├── img/logo.svg                 Logo de la marca (pata con corazón)
├── server.js                    Servidor Express: sirve el frontend y expone la API REST
├── package.json                 Dependencias (express, bcryptjs) y script "start"
├── js/db.js                     Cliente API (fetch) con la misma interfaz DB.all/get/insert/update/remove
├── js/auth.js                   Autenticación contra la API (login, registro, recuperación y cambio de contraseña)
└── js/utils.js                  Helpers compartidos (badges, toasts, topbar, política de contraseñas, ojito)
```

## Instrucciones de despliegue local

Requiere [Node.js](https://nodejs.org/) instalado (v18 o superior recomendado).
El sistema se levanta con un solo comando, sin necesidad de Docker ni de
configurar una base de datos:

```bash
cd MVP_MundiPets
npm install
npm start
```

Luego abrir `http://localhost:3000` en el navegador. El servidor Express sirve
tanto el frontend como la API (`/api/...`), por lo que no hace falta levantar
nada más por separado.

Al arrancar, el servidor inicializa automáticamente los datos de ejemplo en
memoria. Para restablecerlos en cualquier momento (sin reiniciar el proceso),
usar el enlace **"Restablecer datos de ejemplo"** en la pantalla de inicio de
sesión, o reiniciar el servidor con `npm start`.

> Variable de entorno opcional: `PORT` (por defecto `3000`), por ejemplo
> `PORT=8080 npm start`.

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


## Advertencia sobre los datos

Todos los usuarios, mascotas, historiales médicos, solicitudes y mensajes de
este MVP son **ficticios**, generados únicamente para fines de demostración
académica. No representan personas, animales ni información sanitaria reales.
