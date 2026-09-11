# Retrospectiva del equipo — MundiPets PFC

Retrospectiva de cierre del equipo, con las acciones concretas acordadas y
su responsable.


## Qué funcionó bien

- El historial de trabajo quedó repartido en más de 25 fechas distintas
  entre el 29 de junio y el 11 de septiembre, con los cinco integrantes
  activos a lo largo de todo el proyecto, no concentrado al final.
- El componente empírico (detector de ambigüedad vs. panel de expertos)
  se ejecutó de principio a fin, con resultados reproducibles por script.
- El equipo respondió rápido a los hallazgos de última hora (`07_Datos`,
  `10_Autoria`, corrección del MVP de submódulo a integración directa).

## Qué no funcionó bien

- Cada integrante usó más de una identidad de Git a lo largo del proyecto,
  lo que obligó a generar un `.mailmap` al cierre en vez de mantener una
  sola cuenta desde el inicio.
- El paquete de datos reproducible (`07_Datos`) y su documentación se
  consolidaron sobre el cierre, no de forma progresiva.

## Acciones concretas con responsable

| Acción | Responsable | Estado |
|---|---|---|
| Verificar que `.mailmap` esté en la raíz del repositorio y que `git log --pretty=format:'%aN'` muestre exactamente 5 identidades | Andy Mendoza | Hecho |
| Confirmar que el tag de línea base apunte al commit final, después de `07_Datos`, `10_Autoria` y `checksums.sha256` regenerado, y que sea anotado | Andy Mendoza | Hecho |
| Verificar sobre un clon limpio que `checksums.sha256` y `checksums_datos.sha256` no den error | Jimmy Nieves | Hecho |
| Cerrar la clasificación de riesgo del componente de IA con su base legal explícita en el ERS | Genesis Gutierrez | Hecho |
| Revisar y completar la doble codificación (A7) si se necesita una ronda de calibración adicional | Edson Daniel Fuertes Arraes | Hecho |
| Actualizar los diagramas UML de `03_Modelado` si algo cambió tras las últimas correcciones del ERS | Gary Morales | Hecho |
| Ensayar la defensa individual con base en el guion de `09_Defensa/`, cada quien su propia parte | Los cinco integrantes | Hecho |

## Valoración general del proceso

El proyecto se desarrolló durante aproximadamente tres meses, con trabajo
distribuido entre los cinco integrantes y una fase final de consolidación
de evidencia y corrección de hallazgos antes del cierre.

---

## Firma

| Integrante | Confirmación | Fecha |
|---|---|---|
| Andy Mendoza | Confirmo que esta retrospectiva refleja lo acordado por el equipo — Andy Mendoza | 2026-09-11 |
| Edson Daniel Fuertes Arraes |  | 2026-09-11 |
| Genesis Gutierrez | Confirmo que esta retrospectiva refleja lo acordado por el equipo — Genesis Gutierrez | 2026-09-11 |
| Gary Morales |  | 2026-09-11 |
| Jimmy Nieves |  | 2026-09-11 |
