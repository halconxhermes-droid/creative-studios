# Creative Studios — Proceso de Aprobación y Rechazo

Estándares para que el Director y las filiales aprueben o rechacen trabajo.

---

## Tipos de decisión

| Tipo | Quién decide | Cuándo se aplica |
|---|---|---|
| **Aprobación rápida** | Director solo | Cuando hay criterios objetivos claros (pitch cumple rúbrica, JSON valida, PDF generado) |
| **Aprobación con revisión** | Director + lectura del artefacto | Manuscrito completo, entregable final |
| **Rechazo con feedback** | Director + filial responsable | Cuando un entregable no cumple estándares |
| **Evaluación cruzada** | Ambas filiales (rúbrica 1-5) | Antes de entregar, siempre |

---

## Criterios de aprobación rápida

Se aprueba sin leer el artefacto completo cuando:

- ✅ `idea-generator` → pitch con rúbrica ≥ 3.5/5 por criterio
- ✅ `escritor` → mínimo de palabras cumplido + beats marcados
- ✅ `editor-linea` → diff muestra mejoras verificables
- ✅ `guionista-manga/comic` → JSON valida contra schema
- ✅ `generador-imagenes` → todos los YAML tienen los 7 campos
- ✅ `componedor-manga` → PDF existe + tiene el nº de páginas correcto

---

## Criterios de aprobación con revisión

Se requiere leer el artefacto cuando:

- ✅ Manuscrito final: leer los primeros 2 y últimos 2 párrafos + 1 capítulo aleatorio
- ✅ Entregable final: abrir/verificar que existe y es reproducible
- ✅ Brief artístico: verificar que paleta tiene hex concretos (no "azul genérico")

---

## Plantilla de rechazo (obligatoria)

Todo rechazo debe usar esta plantilla en el `kanban_comment`:

```markdown
## Rechazo: <nombre-del paso>

**Qué se evaluó:** <skill + artefacto>
**Veredicto:** ❌ RECHAZADO

### Qué falló
1. <criterio>: <descripción concreta con referencia a página/panel/viñeta>
2. <...>

### Qué falta o es débil
- <observación 1>
- <observación 2>

### Cómo arreglarlo (prioridad)
**[P1 - Crítico]** <acción concreta>
**[P2 - Importante]** <acción>
**[P3 - Opcional]** <acción>

### Iteración
Intento N de 3 máximo. Tras el 3er rechazo, escalar al usuario.
```

---

## Criterios de evaluación cruzada

Rúbrica en `evaluacion-cruzada/SKILL.md`. Resumen:

| Score | Significado |
|---|---|
| 1 | Muy malo — bloquea |
| 2 | Deficiente — requiere mucho trabajo |
| 3 | Aceptable — cumple mínimos |
| 4 | Bueno — supera expectativas |
| 5 | Excelente — referente |

**Veredicto:**
- ≥ 28/40 → APROBADO
- 20-27/40 → REQUIERE CAMBIOS (lista cambios)
- < 20/40 → RECHAZADO (reescritura desde punto indicado)

---

## Escala de severidad

| Severidad | Descripción | Acción |
|---|---|---|
| **[P1]** | Crítico — sin resolver, no se puede avanzar | Reescribir obligatoriamente |
| **[P2]** | Importante — afecta calidad significativamente | Reescribir recomendado |
| **[P3]** | Opcional — mejora marginal | Aceptable sin cambio |

---

## Aprobación tácita

Si el Director no responde en 24 horas (en un contexto cronjob), se considera aprobación tácita del último entregable y se avanza al siguiente paso. Para evitar esto, el agente que completó un paso debe marcar claramente `¿LISTO PARA APROBACIÓN?` en el kanban comment.

---

## Protocolo de escalado

1. **1er rechazo:** agente recibe feedback y reintenta.
2. **2º rechazo:** agente recibe feedback detallado + ejemplo de lo que se espera.
3. **3er rechazo:** Director informa al usuario con resumen del problema y opciones:
   - Reescribir con guidance más específica.
   - Abandonar el proyecto.
   - Cambiar de agente (si hay alternativa disponible).
