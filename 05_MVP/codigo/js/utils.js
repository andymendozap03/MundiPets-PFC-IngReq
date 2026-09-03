/* Helpers compartidos: topbar, badges, toast, inicializacion comun. */

function initials(name) {
  return (name || "?")
    .split(" ")
    .map((p) => p[0])
    .slice(0, 2)
    .join("")
    .toUpperCase();
}

const BRAND_LOGO = `<img src="img/logo.svg" class="brand-logo" alt=""> <span class="brand-text">MundiPets</span>`;

function renderTopbar(activeUser) {
  const el = document.getElementById("topbar");
  if (!el) return;
  if (!activeUser) {
    el.innerHTML = `<a href="index.html" class="brand">${BRAND_LOGO}</a>`;
    return;
  }
  el.innerHTML = `
    <a href="dashboard.html" class="brand">${BRAND_LOGO}</a>
    <div class="topbar-right">
      <a href="profile.html" class="user-menu-link" title="Ver mi perfil">
        <span class="user-menu-name">${activeUser.name}</span>
        <span class="avatar" title="${Auth.roleLabel(activeUser.role)}">${initials(activeUser.name)}</span>
      </a>
      <button class="btn btn-secondary btn-sm" onclick="Auth.logout()">Salir</button>
    </div>
  `;
}

function toast(message) {
  let el = document.getElementById("toast");
  if (!el) {
    el = document.createElement("div");
    el.id = "toast";
    document.body.appendChild(el);
  }
  el.textContent = message;
  el.classList.add("show");
  clearTimeout(window.__toastTimer);
  window.__toastTimer = setTimeout(() => el.classList.remove("show"), 2600);
}

function badgeForMedicalStatus(status) {
  if (status === "Vigente") return `<span class="badge badge-green">Vigente</span>`;
  if (status === "Por renovar") return `<span class="badge badge-amber">Por renovar</span>`;
  return `<span class="badge badge-gray">${status}</span>`;
}

function badgeForRequestStatus(status) {
  const map = {
    en_proceso: '<span class="badge badge-amber">En proceso</span>',
    aceptada: '<span class="badge badge-green">Aceptada</span>',
    rechazada: '<span class="badge badge-red">Rechazada</span>',
    completada: '<span class="badge badge-green">Completada</span>'
  };
  return map[status] || `<span class="badge badge-gray">${status}</span>`;
}

function badgeForPetStatus(status) {
  if (status === "Adopción") return `<span class="badge badge-green">Adopción</span>`;
  if (status === "Cruza responsable") return `<span class="badge badge-purple">Cruza responsable</span>`;
  return `<span class="badge badge-gray">${status}</span>`;
}

function escapeHtml(str) {
  const div = document.createElement("div");
  div.textContent = str == null ? "" : String(str);
  return div.innerHTML;
}

function qs(name) {
  return new URLSearchParams(window.location.search).get(name);
}

function attachResetButton() {
  const btn = document.getElementById("resetDataBtn");
  if (!btn) return;
  btn.addEventListener("click", async () => {
    if (confirm("Esto restablecera todos los datos de ejemplo (mascotas, solicitudes, mensajes) y cerrara tu sesion. ¿Continuar?")) {
      await DB.reset();
      localStorage.removeItem("mundipets_session_v3");
      window.location.href = "index.html";
    }
  });
}

/* Política de contraseñas: mínimo 8 caracteres, mayúscula, minúscula, número y carácter especial. */
const PASSWORD_POLICY = [
  { key: "length", label: "Mínimo 8 caracteres", test: (pw) => pw.length >= 8 },
  { key: "upper", label: "Al menos una letra mayúscula (A-Z)", test: (pw) => /[A-Z]/.test(pw) },
  { key: "lower", label: "Al menos una letra minúscula (a-z)", test: (pw) => /[a-z]/.test(pw) },
  { key: "number", label: "Al menos un número (0-9)", test: (pw) => /[0-9]/.test(pw) },
  { key: "special", label: "Al menos un carácter especial (!@#$%...)", test: (pw) => /[^A-Za-z0-9]/.test(pw) }
];

function validatePassword(pw) {
  pw = pw || "";
  const checks = PASSWORD_POLICY.map((rule) => ({ ...rule, ok: rule.test(pw) }));
  return { valid: checks.every((c) => c.ok), checks };
}

function passwordChecklistHtml(pw) {
  const { checks } = validatePassword(pw);
  return `
    <ul class="password-checklist">
      ${checks.map((c) => `<li class="${c.ok ? "ok" : ""}"><span class="check-icon">${c.ok ? "✓" : "○"}</span>${c.label}</li>`).join("")}
    </ul>
  `;
}

/* Conecta un input de contraseña con un contenedor que muestra la política en vivo. */
function attachPasswordChecklist(inputId, checklistId) {
  const input = document.getElementById(inputId);
  const box = document.getElementById(checklistId);
  if (!input || !box) return;
  const update = () => { box.innerHTML = passwordChecklistHtml(input.value); };
  input.addEventListener("input", update);
  update();
}

const EYE_ICON_SHOW = `<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"/><circle cx="12" cy="12" r="3"/></svg>`;
const EYE_ICON_HIDE = `<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.94 10.94 0 0 1 12 19c-7 0-11-7-11-7a18.5 18.5 0 0 1 5.06-5.94M9.9 4.24A10.94 10.94 0 0 1 12 4c7 0 11 7 11 7a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>`;

/* Agrega un botón de ojito a los campos de contraseña para mostrar/ocultar el valor. */
function enablePasswordToggles(root) {
  (root || document).querySelectorAll('input[type="password"]').forEach((input) => {
    if (input.dataset.toggleAttached) return;
    input.dataset.toggleAttached = "true";

    const wrapper = document.createElement("div");
    wrapper.className = "password-field";
    input.parentNode.insertBefore(wrapper, input);
    wrapper.appendChild(input);

    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "password-toggle";
    btn.setAttribute("aria-label", "Mostrar contraseña");
    btn.innerHTML = EYE_ICON_SHOW;
    wrapper.appendChild(btn);

    btn.addEventListener("click", () => {
      const willShow = input.type === "password";
      input.type = willShow ? "text" : "password";
      btn.innerHTML = willShow ? EYE_ICON_HIDE : EYE_ICON_SHOW;
      btn.setAttribute("aria-label", willShow ? "Ocultar contraseña" : "Mostrar contraseña");
    });
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", () => enablePasswordToggles());
} else {
  enablePasswordToggles();
}
