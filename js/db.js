/*
 * MundiPets MVP - capa de datos sobre localStorage.
 * Simula una base de datos: colecciones, seed ficticio y helpers CRUD.
 * No hay backend real; todo se persiste en el navegador (localStorage).
 */

const DB_KEY = "mundipets_db_v1";
const DB_SESSION_KEY = "mundipets_session_v1";

const SEED = {
  users: [
    { id: "u1", name: "Ana Adoptante", email: "ana.adoptante@ejemplo.com", role: "adoptante", city: "Quevedo", verified: true, docStatus: "Verificado" },
    { id: "u2", name: "Carlos Zambrano", email: "carlos.zambrano@ejemplo.com", role: "propietario", city: "Quevedo", verified: true, docStatus: "Verificado" },
    { id: "u3", name: "Dra. Melissa Vera", email: "melissa.vera@ejemplo.com", role: "veterinaria", city: "Buena Fe", verified: true, docStatus: "Verificado" },
    { id: "u4", name: "Jorge Intriago", email: "jorge.intriago@ejemplo.com", role: "interesado_cruza", city: "Mocache", verified: true, docStatus: "Verificado" }
  ],
  pets: [
    {
      id: "p1", ownerId: "u2", name: "Firulais", species: "Perro", breed: "Mestizo", sex: "Macho",
      age: "2 años", size: "Mediano", city: "Quevedo", reproductiveStatus: "Entero",
      status: "Adopción", photo: "🐕", description: "Perro juguetón y sociable, ideal para casa con patio.",
      privacy: { medicalHistory: "verified", location: "private", contact: "verified", photos: "public", genetics: "private" }
    },
    {
      id: "p2", ownerId: "u4", name: "Michi", species: "Gato", breed: "Siamés", sex: "Hembra",
      age: "1 año", size: "Pequeño", city: "Buena Fe", reproductiveStatus: "Entera",
      status: "Adopción", photo: "🐈", description: "Gata tranquila, acostumbrada a interiores.",
      privacy: { medicalHistory: "verified", location: "private", contact: "verified", photos: "public", genetics: "private" }
    },
    {
      id: "p3", ownerId: "u4", name: "Toby", species: "Perro", breed: "Labrador", sex: "Macho",
      age: "3 años", size: "Grande", city: "Mocache", reproductiveStatus: "Entero",
      status: "Cruza responsable", photo: "🐕‍🦺", description: "Labrador de línea sana, disponible para cruza responsable.",
      privacy: { medicalHistory: "verified", location: "private", contact: "verified", photos: "public", genetics: "verified" }
    },
    {
      id: "p4", ownerId: "u2", name: "Luna", species: "Perro", breed: "Criolla", sex: "Hembra",
      age: "6 meses", size: "Pequeño", city: "Quevedo", reproductiveStatus: "Entera",
      status: "Adopción", photo: "🐶", description: "Cachorra criolla rescatada, muy activa.",
      privacy: { medicalHistory: "pending", location: "private", contact: "verified", photos: "public", genetics: "pending" }
    }
  ],
  medicalRecords: [
    { id: "m1", petId: "p1", type: "Vacuna antirrábica", date: "2025-03-15", status: "Vigente", strain: "Rabisin", applicator: "Dra. Melissa Vera", validated: true },
    { id: "m2", petId: "p1", type: "Desparasitación interna", date: "2025-06-01", status: "Vigente", validated: true },
    { id: "m3", petId: "p1", type: "Certificado veterinario oficial", date: "2025-01-20", status: "Por renovar", validated: false },
    { id: "m4", petId: "p3", type: "Vacuna polivalente", date: "2025-05-10", status: "Vigente", strain: "Nobivac", applicator: "Dra. Melissa Vera", validated: true },
    { id: "m5", petId: "p3", type: "Certificado veterinario oficial", date: "2025-04-02", status: "Vigente", validated: true },
    { id: "m6", petId: "p2", type: "Vacuna antirrábica", date: "2025-02-11", status: "Vigente", validated: true },
    { id: "m7", petId: "p4", type: "Carnet de vacunación", date: "2026-06-29", status: "Por renovar", validated: false }
  ],
  genetics: [
    { id: "g1", petId: "p1", lineage: "Sin registro de pedigrí", hereditaryConditions: "Ninguna reportada", parentage: "Desconocido", notes: "Rescatado adulto, sin historial previo." },
    { id: "g3", petId: "p3", lineage: "Línea Labrador certificada", hereditaryConditions: "Displasia de cadera (bajo riesgo, evaluado)", parentage: "Padres registrados por el criador anterior", notes: "Apto para cruza responsable según evaluación veterinaria." }
  ],
  requests: [
    {
      id: "r1", type: "adopcion", petId: "p1", requesterId: "u1", ownerId: "u2",
      justification: "Vivo en una casa con patio y ya he tenido perros antes. Me encantaría conocerlo.",
      conditions: "Casa con patio, tiempo disponible",
      stage: 2, stages: ["Formulario", "Entrevista", "Visita al hogar", "Periodo de prueba", "Compromiso firmado"],
      status: "en_proceso", createdAt: "2026-07-20"
    }
  ],
  messages: [
    { id: "msg1", requestId: "r1", senderId: "u2", text: "Hola, gracias por tu interés en Firulais. Cuéntame un poco sobre tu hogar y experiencia con mascotas.", time: "10:14" },
    { id: "msg2", requestId: "r1", senderId: "u1", text: "Hola Carlos, vivo en una casa con patio y ya he tenido perros antes. Me encantaría conocerlo.", time: "10:20" },
    { id: "msg3", requestId: "r1", senderId: "u2", text: "Perfecto, revisaré tu solicitud en cuanto la envíes.", time: "10:22" }
  ],
  compatibilityEvaluations: [],
  followUps: [
    { id: "f1", petId: "p1", requestId: "r1", note: "Primer control post-adopción pendiente.", date: "2026-08-15", status: "Pendiente" }
  ]
};

function loadDb() {
  const raw = localStorage.getItem(DB_KEY);
  if (!raw) {
    const fresh = JSON.parse(JSON.stringify(SEED));
    localStorage.setItem(DB_KEY, JSON.stringify(fresh));
    return fresh;
  }
  try {
    return JSON.parse(raw);
  } catch (e) {
    const fresh = JSON.parse(JSON.stringify(SEED));
    localStorage.setItem(DB_KEY, JSON.stringify(fresh));
    return fresh;
  }
}

function saveDb(db) {
  localStorage.setItem(DB_KEY, JSON.stringify(db));
}

function resetDb() {
  localStorage.removeItem(DB_KEY);
  localStorage.removeItem(DB_SESSION_KEY);
  return loadDb();
}

function uid(prefix) {
  return prefix + "_" + Math.random().toString(36).slice(2, 9);
}

const DB = {
  all(collection) {
    const db = loadDb();
    return db[collection] || [];
  },
  get(collection, id) {
    return this.all(collection).find((item) => item.id === id) || null;
  },
  insert(collection, item) {
    const db = loadDb();
    if (!db[collection]) db[collection] = [];
    if (!item.id) item.id = uid(collection.slice(0, 2));
    db[collection].push(item);
    saveDb(db);
    return item;
  },
  update(collection, id, patch) {
    const db = loadDb();
    const list = db[collection] || [];
    const idx = list.findIndex((item) => item.id === id);
    if (idx === -1) return null;
    list[idx] = { ...list[idx], ...patch };
    saveDb(db);
    return list[idx];
  },
  remove(collection, id) {
    const db = loadDb();
    db[collection] = (db[collection] || []).filter((item) => item.id !== id);
    saveDb(db);
  },
  reset() {
    return resetDb();
  }
};

window.DB = DB;
window.MUNDIPETS_UID = uid;
