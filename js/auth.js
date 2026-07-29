/*
 * Sesion simulada por rol. No hay autenticacion real con contrasena
 * (es una demo de MVP con datos ficticios); se persiste el usuario activo
 * en localStorage para simular RF-12 (verificar la identidad de los usuarios).
 */

const SESSION_KEY = "mundipets_session_v1";

const ROLE_LABELS = {
  propietario: "Propietario de mascota",
  adoptante: "Adoptante",
  interesado_cruza: "Interesado en cruza",
  veterinaria: "Veterinaria"
};

const Auth = {
  current() {
    const raw = localStorage.getItem(SESSION_KEY);
    if (!raw) return null;
    try {
      const session = JSON.parse(raw);
      return DB.get("users", session.userId);
    } catch (e) {
      return null;
    }
  },
  login(userId) {
    localStorage.setItem(SESSION_KEY, JSON.stringify({ userId }));
  },
  logout() {
    localStorage.removeItem(SESSION_KEY);
    window.location.href = "index.html";
  },
  requireLogin() {
    const user = this.current();
    if (!user) {
      window.location.href = "index.html";
      return null;
    }
    return user;
  },
  roleLabel(role) {
    return ROLE_LABELS[role] || role;
  }
};

window.Auth = Auth;
window.ROLE_LABELS = ROLE_LABELS;
