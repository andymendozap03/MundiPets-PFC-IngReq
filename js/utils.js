/* Helpers compartidos: topbar, badges, toast, inicializacion comun. */

function initials(name) {
  return (name || "?")
    .split(" ")
    .map((p) => p[0])
    .slice(0, 2)
    .join("")
    .toUpperCase();
}

function renderTopbar(activeUser) {
  const el = document.getElementById("topbar");
  if (!el) return;
  if (!activeUser) {
    el.innerHTML = `<div class="brand">MundiPets</div>`;
    return;
  }
  el.innerHTML = `
    <a href="dashboard.html" class="brand">MundiPets</a>
    <div class="topbar-right">
      <span class="user-menu-name">${activeUser.name}</span>
      <span class="avatar" title="${Auth.roleLabel(activeUser.role)}">${initials(activeUser.name)}</span>
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
  btn.addEventListener("click", () => {
    if (confirm("Esto restablecera todos los datos de ejemplo (mascotas, solicitudes, mensajes) y cerrara tu sesion. ¿Continuar?")) {
      DB.reset();
      window.location.href = "index.html";
    }
  });
}
