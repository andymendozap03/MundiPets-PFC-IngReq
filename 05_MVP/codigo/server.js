/*
 * MundiPets MVP — servidor Express.
 * Sirve el frontend estático y expone una API REST respaldada por una
 * base de datos en memoria (sin motor de BD externo, apta para el MVP
 * académico). Las contraseñas se guardan con hash bcrypt, nunca en
 * texto plano ni se exponen en las respuestas de la API.
 */

const express = require("express");
const bcrypt = require("bcryptjs");
const path = require("path");

const PORT = process.env.PORT || 3000;
const SALT_ROUNDS = 8;

function uid(prefix) {
  return prefix + "_" + Math.random().toString(36).slice(2, 9);
}

function genResetCode() {
  return String(Math.floor(100000 + Math.random() * 900000));
}

const PASSWORD_POLICY_RE = { upper: /[A-Z]/, lower: /[a-z]/, number: /[0-9]/, special: /[^A-Za-z0-9]/ };
function isPasswordValid(pw) {
  pw = pw || "";
  return pw.length >= 8 && PASSWORD_POLICY_RE.upper.test(pw) && PASSWORD_POLICY_RE.lower.test(pw)
    && PASSWORD_POLICY_RE.number.test(pw) && PASSWORD_POLICY_RE.special.test(pw);
}

/* ---------------------------------------------------------------------- */
/* Datos semilla (misma estructura que el antiguo js/db.js del cliente)   */
/* ---------------------------------------------------------------------- */

const SEED_USERS_PLAIN = [
  { id: "u1", name: "Ana Adoptante", email: "ana.adoptante@ejemplo.com", password: "Ana#2026", role: "adoptante", city: "Quevedo", verified: true, docStatus: "Verificado" },
  { id: "u2", name: "Carlos Zambrano", email: "carlos.zambrano@ejemplo.com", password: "Carlos#2026", role: "propietario", city: "Quevedo", verified: true, docStatus: "Verificado" },
  { id: "u3", name: "Dra. Melissa Vera", email: "melissa.vera@ejemplo.com", password: "Melissa#2026", role: "veterinaria", city: "Buena Fe", verified: true, docStatus: "Verificado" },
  { id: "u4", name: "Jorge Intriago", email: "jorge.intriago@ejemplo.com", password: "Jorge#2026", role: "interesado_cruza", city: "Mocache", verified: true, docStatus: "Verificado" }
];

const SEED_REST = {
  pets: [
    {
      id: "p1", ownerId: "u2", name: "Firulais", species: "Perro", breed: "Mestizo", sex: "Macho",
      age: "2 años", size: "Mediano", city: "Quevedo", reproductiveStatus: "Entero",
      status: "Adopción", photo: "🐕", description: "Perro juguetón y sociable, ideal para casa con patio.",
      microchip: "981022300456128",
      privacy: { medicalHistory: "verified", location: "private", contact: "verified", photos: "public", genetics: "private" }
    },
    {
      id: "p2", ownerId: "u4", name: "Michi", species: "Gato", breed: "Siamés", sex: "Hembra",
      age: "1 año", size: "Pequeño", city: "Buena Fe", reproductiveStatus: "Entera",
      status: "Adopción", photo: "🐈", description: "Gata tranquila, acostumbrada a interiores.",
      microchip: "",
      privacy: { medicalHistory: "verified", location: "private", contact: "verified", photos: "public", genetics: "private" }
    },
    {
      id: "p3", ownerId: "u4", name: "Toby", species: "Perro", breed: "Labrador", sex: "Macho",
      age: "3 años", size: "Grande", city: "Mocache", reproductiveStatus: "Entero",
      status: "Cruza responsable", photo: "🐕‍🦺", description: "Labrador de línea sana, disponible para cruza responsable.",
      microchip: "981022300789456",
      privacy: { medicalHistory: "verified", location: "private", contact: "verified", photos: "public", genetics: "verified" }
    },
    {
      id: "p4", ownerId: "u2", name: "Luna", species: "Perro", breed: "Criolla", sex: "Hembra",
      age: "6 meses", size: "Pequeño", city: "Quevedo", reproductiveStatus: "Entera",
      status: "Adopción", photo: "🐶", description: "Cachorra criolla rescatada, muy activa.",
      microchip: "",
      privacy: { medicalHistory: "pending", location: "private", contact: "verified", photos: "public", genetics: "pending" }
    }
  ],
  medicalRecords: [
    { id: "m1", petId: "p1", type: "Vacuna antirrábica", date: "2025-03-15", status: "Vigente", strain: "Rabisin", Lote: "R-90812", applicator: "Dra. Melissa Vera", validated: true },
    { id: "m2", petId: "p1", type: "Desparasitación interna", date: "2025-06-01", status: "Vigente", strain: "Drontal", Lote: "D-445", applicator: "Dra. Melissa Vera", validated: true },
    { id: "m3", petId: "p1", type: "Certificado veterinario oficial", date: "2025-01-20", status: "Por renovar", validated: false },
    { id: "m4", petId: "p3", type: "Vacuna polivalente", date: "2025-05-10", status: "Vigente", strain: "Nobivac", Lote: "N-7890", applicator: "Dra. Melissa Vera", validated: true },
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
    },
    {
      id: "r2", type: "cruza", petId: "p3", requesterId: "u1", ownerId: "u4",
      justification: "Cruza controlada anterior.", conditions: "Casa con patio",
      stage: 5, stages: ["Formulario", "Entrevista", "Visita al hogar", "Periodo de prueba", "Compromiso firmado"],
      status: "completada", createdAt: "2026-05-10"
    },
    {
      id: "r3", type: "cruza", petId: "p3", requesterId: "u1", ownerId: "u4",
      justification: "Cruza controlada anterior 2.", conditions: "Casa con patio",
      stage: 5, stages: ["Formulario", "Entrevista", "Visita al hogar", "Periodo de prueba", "Compromiso firmado"],
      status: "completada", createdAt: "2026-06-15"
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
  ],
  reminders: [
    { id: "rem1", petId: "p1", type: "Vacuna contra Parvovirus", date: "2026-08-24", status: "Pendiente", description: "Dosis anual de refuerzo requerida." },
    { id: "rem2", petId: "p2", type: "Control de Desparasitación", date: "2026-08-20", status: "Pendiente", description: "Tratamiento trimestral preventivo." }
  ],
  encounters: [
    {
      id: "enc1", petAId: "p1", ownerAId: "u2", petBId: "p2", ownerBId: "u4",
      date: "2026-09-10", place: "Parque Central de Quevedo", notes: "Encuentro de socialización previo a evaluar una posible adopción conjunta.",
      status: "pendiente", createdAt: "2026-09-01"
    }
  ],
  passwordResets: []
};

function buildSeed() {
  const users = SEED_USERS_PLAIN.map((u) => {
    const { password, ...rest } = u;
    return { ...rest, password: bcrypt.hashSync(password, SALT_ROUNDS) };
  });
  return { users, ...JSON.parse(JSON.stringify(SEED_REST)) };
}

let db = buildSeed();

function sanitizeUser(u) {
  if (!u) return u;
  const { password, ...rest } = u;
  return rest;
}

function collectionOf(name) {
  if (!db[name]) db[name] = [];
  return db[name];
}

/* ---------------------------------------------------------------------- */
/* App Express                                                            */
/* ---------------------------------------------------------------------- */

const app = express();
app.use(express.json());
app.use(express.static(__dirname));

/* --- Autenticación --- */

app.post("/api/auth/login", (req, res) => {
  const { email, password } = req.body || {};
  const user = db.users.find((u) => u.email.trim().toLowerCase() === String(email || "").trim().toLowerCase());
  if (!user) return res.status(401).json({ success: false, message: "El correo electrónico no está registrado." });
  if (!bcrypt.compareSync(String(password || ""), user.password)) {
    return res.status(401).json({ success: false, message: "La contraseña es incorrecta." });
  }
  res.json({ success: true, user: sanitizeUser(user) });
});

app.post("/api/auth/register", (req, res) => {
  const { name, email, password, role, city } = req.body || {};
  if (!name || !email || !password) {
    return res.status(400).json({ success: false, message: "Completa nombre, correo y contraseña." });
  }
  if (db.users.some((u) => u.email.toLowerCase() === String(email).toLowerCase())) {
    return res.status(409).json({ success: false, message: "Ya existe una cuenta con ese correo." });
  }
  if (!isPasswordValid(password)) {
    return res.status(400).json({ success: false, message: "La contraseña no cumple con la política de seguridad requerida." });
  }
  const user = {
    id: uid("us"), name, email, role: role || "adoptante", city: city || "Quevedo",
    verified: false, docStatus: "Pendiente", password: bcrypt.hashSync(password, SALT_ROUNDS)
  };
  db.users.push(user);
  res.status(201).json({ success: true, user: sanitizeUser(user) });
});

app.post("/api/auth/forgot-password", (req, res) => {
  const { email } = req.body || {};
  const user = db.users.find((u) => u.email.trim().toLowerCase() === String(email || "").trim().toLowerCase());
  if (!user) return res.status(404).json({ success: false, message: "No existe ninguna cuenta registrada con ese correo electrónico." });
  const code = genResetCode();
  db.passwordResets = db.passwordResets.filter((p) => p.email !== user.email);
  db.passwordResets.push({ email: user.email, code, createdAt: Date.now() });
  res.json({ success: true, code });
});

app.post("/api/auth/verify-code", (req, res) => {
  const { email, code } = req.body || {};
  const entry = db.passwordResets.find((p) => p.email.toLowerCase() === String(email || "").trim().toLowerCase());
  if (!entry) return res.status(400).json({ success: false, message: "Primero solicita un código de recuperación." });
  if (entry.code !== String(code || "").trim()) return res.status(400).json({ success: false, message: "El código ingresado no es válido." });
  res.json({ success: true });
});

app.post("/api/auth/reset-password", (req, res) => {
  const { email, code, newPassword } = req.body || {};
  const entry = db.passwordResets.find((p) => p.email.toLowerCase() === String(email || "").trim().toLowerCase());
  if (!entry || entry.code !== String(code || "").trim()) {
    return res.status(400).json({ success: false, message: "El código ingresado no es válido." });
  }
  if (!isPasswordValid(newPassword)) {
    return res.status(400).json({ success: false, message: "La contraseña no cumple con la política de seguridad requerida." });
  }
  const user = db.users.find((u) => u.email.trim().toLowerCase() === String(email).trim().toLowerCase());
  if (!user) return res.status(404).json({ success: false, message: "No existe ninguna cuenta registrada con ese correo electrónico." });
  user.password = bcrypt.hashSync(newPassword, SALT_ROUNDS);
  db.passwordResets = db.passwordResets.filter((p) => p.email.toLowerCase() !== String(email).toLowerCase());
  res.json({ success: true });
});

app.post("/api/auth/change-password", (req, res) => {
  const { userId, currentPassword, newPassword } = req.body || {};
  const user = db.users.find((u) => u.id === userId);
  if (!user) return res.status(404).json({ success: false, message: "Usuario no encontrado." });
  if (!bcrypt.compareSync(String(currentPassword || ""), user.password)) {
    return res.status(401).json({ success: false, message: "La contraseña actual es incorrecta." });
  }
  if (!isPasswordValid(newPassword)) {
    return res.status(400).json({ success: false, message: "La contraseña no cumple con la política de seguridad requerida." });
  }
  user.password = bcrypt.hashSync(newPassword, SALT_ROUNDS);
  res.json({ success: true });
});

/* --- Reinicio de datos de ejemplo --- */

app.post("/api/db/reset", (req, res) => {
  db = buildSeed();
  res.json({ success: true });
});

/* --- CRUD genérico para el resto de colecciones --- */

app.get("/api/:collection", (req, res) => {
  const { collection } = req.params;
  let list = collectionOf(collection);
  if (collection === "users") list = list.map(sanitizeUser);
  res.json(list);
});

app.get("/api/:collection/:id", (req, res) => {
  const { collection, id } = req.params;
  const item = collectionOf(collection).find((x) => x.id === id);
  if (!item) return res.status(404).json({ error: "No encontrado" });
  res.json(collection === "users" ? sanitizeUser(item) : item);
});

app.post("/api/:collection", (req, res) => {
  const { collection } = req.params;
  if (collection === "users") {
    return res.status(400).json({ error: "Usa /api/auth/register para crear usuarios" });
  }
  const item = { ...req.body };
  if (!item.id) item.id = uid(collection.slice(0, 2));
  collectionOf(collection).push(item);
  res.status(201).json(item);
});

app.patch("/api/:collection/:id", (req, res) => {
  const { collection, id } = req.params;
  const list = collectionOf(collection);
  const idx = list.findIndex((x) => x.id === id);
  if (idx === -1) return res.status(404).json({ error: "No encontrado" });
  const patch = { ...req.body };
  if (collection === "users") {
    delete patch.password;
    if (patch.email) {
      const emailTaken = list.some((u) => u.id !== id && u.email.toLowerCase() === String(patch.email).toLowerCase());
      if (emailTaken) return res.status(409).json({ error: "Ya existe una cuenta con ese correo." });
    }
  }
  list[idx] = { ...list[idx], ...patch };
  res.json(collection === "users" ? sanitizeUser(list[idx]) : list[idx]);
});

app.delete("/api/:collection/:id", (req, res) => {
  const { collection, id } = req.params;
  db[collection] = collectionOf(collection).filter((x) => x.id !== id);
  res.status(204).end();
});

app.listen(PORT, () => {
  console.log(`MundiPets escuchando en http://localhost:${PORT}`);
});
