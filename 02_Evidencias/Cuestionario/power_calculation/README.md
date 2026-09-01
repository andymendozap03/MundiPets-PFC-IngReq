# Power calculation — Cuestionario v2.0 (perfil dominante)

## Por qué existe esta carpeta

El cuestionario v2.0 reunió **61 respuestas válidas**, distribuidas en 47
propietarios de mascota, 7 interesados en adopción y 7 interesados en cruza.
El perfil dominante (propietario de mascota) no alcanza el mínimo de
**n ≥ 60 respuestas por perfil** establecido en la guía de la Entrega 4 (2B).

Como alternativa admitida explícitamente por la guía cuando el mínimo por
perfil no se alcanza (Sección 5, Tabla de evidencia mínima terminal, y
gatekeeper G5), se documenta aquí un **cálculo de potencia estadística**
específico para el cuestionario, con:

- α = 0,05
- 1 − β (potencia mínima exigida) = 0,80
- d de Cohen = 0,5 (tamaño de efecto mediano)

Este cálculo es **independiente** del cálculo de potencia ya reportado para
el componente empírico del Enfoque 2 (detector de ambigüedad vs. consenso
experto, en `06_Experimento/scripts_analisis/`), que corresponde a un
análisis distinto sobre el corpus de requisitos y no sobre las respuestas
de campo del cuestionario.

## Resultado

Con el n disponible del perfil dominante (n = 47), la prueba t de una
muestra alcanza una **potencia estadística real de 91,86 %**, muy por
encima del 80 % mínimo exigido. El tamaño de muestra mínimo teórico
requerido para alcanzar esa potencia con d = 0,5 y α = 0,05 es de 34
respuestas — el n disponible (47) lo supera con margen.

El detalle completo del resultado se encuentra en
`tabla_power_cuestionario.csv`, generada automáticamente por el script
(ninguna cifra se calculó o editó manualmente).

## Cómo ejecutar el script

Requiere Python 3 y la librería `statsmodels`:

```bash
pip install statsmodels
python 06_calcular_power_cuestionario.py
```

El script imprime el resultado en consola y escribe (o sobrescribe)
`tabla_power_cuestionario.csv` en esta misma carpeta.

## Archivos de esta carpeta

| Archivo | Contenido |
|---|---|
| `06_calcular_power_cuestionario.py` | Script que calcula el n mínimo requerido y la potencia real alcanzada con n=47 |
| `tabla_power_cuestionario.csv` | Salida reproducible del script, con todas las métricas del cálculo |
| `README.md` | Este archivo |
