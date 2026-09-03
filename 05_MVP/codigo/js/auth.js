/*
 * Autenticacion sobre el API REST de server.js: las contrasenas se
 * verifican en el backend con bcrypt (nunca en el cliente). El
 * navegador solo persiste el id del usuario activo en localStorage
 * como sesion simple, y consulta al servidor el resto del perfil.
 */

const SESSION_KEY = "mundipets_session_v3";

const ROLE_LABELS = {
  propietario: "Propietario de mascota",
  adoptante: "Adoptante",
  interesado_cruza: "Interesado en cruza",
  veterinaria: "Veterinaria"
};

const Auth = {
  async current() {
    const raw = localStorage.getItem(SESSION_KEY);
    if (!raw) return null;
    try {
      const session = JSON.parse(raw);
      return await DB.get("users", session.userId);
    } catch (e) {
      return null;
    }
  },
  async loginWithCredentials(email, password) {
    try {
      const res = await apiRequest("POST", "/auth/login", { email, password });
      this.login(res.user.id);
      return { success: true, user: res.user };
    } catch (e) {
      return { success: false, message: e.message };
    }
  },
  async register(payload) {
    try {
      const res = await apiRequest("POST", "/auth/register", payload);
      this.login(res.user.id);
      return { success: true, user: res.user };
    } catch (e) {
      return { success: false, message: e.message };
    }
  },
  login(userId) {
    localStorage.setItem(SESSION_KEY, JSON.stringify({ userId }));
  },
  logout() {
    localStorage.removeItem(SESSION_KEY);
    window.location.href = "index.html";
  },
  async requireLogin() {
    const user = await this.current();
    if (!user) {
      window.location.href = "index.html";
      return null;
    }
    return user;
  },
  roleLabel(role) {
    return ROLE_LABELS[role] || role;
  },
  async requestPasswordReset(email) {
    try {
      const res = await apiRequest("POST", "/auth/forgot-password", { email });
      return { success: true, code: res.code };
    } catch (e) {
      return { success: false, message: e.message };
    }
  },
  async verifyResetCode(email, code) {
    try {
      await apiRequest("POST", "/auth/verify-code", { email, code });
      return { success: true };
    } catch (e) {
      return { success: false, message: e.message };
    }
  },
  async resetPassword(email, code, newPassword) {
    try {
      await apiRequest("POST", "/auth/reset-password", { email, code, newPassword });
      return { success: true };
    } catch (e) {
      return { success: false, message: e.message };
    }
  },
  async changePassword(userId, currentPassword, newPassword) {
    try {
      await apiRequest("POST", "/auth/change-password", { userId, currentPassword, newPassword });
      return { success: true };
    } catch (e) {
      return { success: false, message: e.message };
    }
  }
};

window.Auth = Auth;
window.ROLE_LABELS = ROLE_LABELS;
