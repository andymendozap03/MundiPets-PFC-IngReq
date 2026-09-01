/*
 * MundiPets MVP - cliente de datos sobre el API REST de server.js.
 * Antes esta capa persistía en localStorage; ahora delega en el backend
 * Express (datos en memoria en el servidor), por lo que todas las
 * operaciones son asíncronas y se comparten entre todos los usuarios.
 */

const API_BASE = "/api";

async function apiRequest(method, path, body) {
  const res = await fetch(API_BASE + path, {
    method,
    headers: body !== undefined ? { "Content-Type": "application/json" } : undefined,
    body: body !== undefined ? JSON.stringify(body) : undefined
  });
  if (!res.ok) {
    let message = "Error de comunicación con el servidor";
    try {
      const data = await res.json();
      message = data.message || data.error || message;
    } catch (e) { /* respuesta sin cuerpo JSON */ }
    const err = new Error(message);
    err.status = res.status;
    throw err;
  }
  if (res.status === 204) return null;
  return res.json();
}

const DB = {
  all(collection) {
    return apiRequest("GET", "/" + collection);
  },
  async get(collection, id) {
    try {
      return await apiRequest("GET", "/" + collection + "/" + id);
    } catch (e) {
      if (e.status === 404) return null;
      throw e;
    }
  },
  insert(collection, item) {
    return apiRequest("POST", "/" + collection, item);
  },
  update(collection, id, patch) {
    return apiRequest("PATCH", "/" + collection + "/" + id, patch);
  },
  remove(collection, id) {
    return apiRequest("DELETE", "/" + collection + "/" + id);
  },
  reset() {
    return apiRequest("POST", "/db/reset");
  }
};

window.DB = DB;
window.apiRequest = apiRequest;
