# Creative Studios — Ciclo de Proyecto

Flujo de vida completo de un proyecto, desde el brief hasta la entrega.

---

## Mapa del ciclo

```
┌─────────────────────────────────────────────────────────────┐
│  brief ──► pitch ──► narrativa ──► edicion ──► gui        │
│    │           │            │            │        │        │
│    ▼           ▼            ▼            ▼        ▼        │
│  VALIDAR   APROBAR    COMPLETAR    APROBAR   APROBAR     │
│                                                             │
│  gui ──► produccion ──► revision ──► entregado            │
│    │           │              │             │              │
│    ▼           ▼              ▼             ▼              │
│  APROBAR   COMPLETAR   EVAL-CRUZADA   BUNDLE+ENVIO        │
└─────────────────────────────────────────────────────────────┘
```

---

## Paso 1: brief → pitch

**Actor:** `director` + `narrativa`
**Skill:** `idea-generator`
**Input:** `brief.md`
**Output:** `narrativa/pitch.md`
**Kanban:** `brief` → `pitch`

El Director recibe el brief y delega a `idea-generator`. Se generan 3 pitches, se elige el mejor según la rúbrica. El Director aprueba o rechaza el pitch.

- **Aprobar:** mover a `pitch` en kanban, avanzar.
- **Rechazar:** comentario en kanban con razones específicas, re-delegar `idea-generator`.

---

## Paso 2: pitch → narrativa

**Actor:** `narrativa`
**Skill:** `escritor` + `continuista`
**Input:** `pitch.md` + `wiki/` (vacia al inicio)
**Output:** `narrativa/borrador/capitulo_NN.md`
**Kanban:** `pitch` → `narrativa`

El escritor produce los capítulos según la longitud del brief. El continuista actualiza la wiki con cada capítulo. Se escribe 1 capítulo → se actualiza wiki → se escribe el siguiente.

---

## Paso 3: narrativa → edicion

**Actor:** `narrativa`
**Skills:** `editor-desarrollo` + `editor-linea` + `lector-beta` (en paralelo)
**Input:** `narrativa/borrador/*.md`
**Output:** `narrativa/ediciones/informe_estructura.md`, `manuscrito_editado.md`, `informe_beta.md`
**Kanban:** `narrativa` → `edicion`

Los tres agentes revisan en paralelo. El Director evalúa el resultado:

- **Beta = PUBLICABLE:** aprobar y avanzar a `guion`.
- **Beta = REQUIERE TRABAJO:** volver al `escritor` con el feedback del editor beta.
- **Beta = DESCARTAR:** informar al usuario y abortar proyecto.

---

## Paso 4: edicion → guion

**Actor:** `produccion`
**Skills:** `director-arte` + `guionista-manga` / `guionista-comic` / `guionista-video`
**Input:** `narrativa/final.md` (o `manuscrito_editado.md`)
**Output:** `produccion/brief_artistico.md` + `produccion/guion.json` (o `storyboard_video.md`)
**Kanban:** `edicion` → `guion`

El director de arte define el estilo. El guionista adapta el manuscrito al formato pedido.

---

## Paso 5: guion → produccion

**Actor:** `produccion`
**Skill:** `generador-imagenes`
**Input:** `produccion/guion.json` + `produccion/brief_artistico.md`
**Output:** `produccion/prompts/*.yaml` + `produccion/renders/` (si GPU disponible)
**Kanban:** `guion` → `produccion`

Se generan los prompts. Si hay GPU local o API, se generan los renders. Si no, los prompts quedan listos para generación manual.

---

## Paso 6: produccion → composicion

**Actor:** `produccion`
**Skills:** `componedor-manga` / `editor-video`
**Input:** `produccion/guion.json` + `produccion/renders/` + `produccion/brief_artistico.md`
**Output:** `outputs/<proyecto>/manga.pdf` o `video.mp4`
**Kanban:** `produccion` → `revision`

Se maquetan las páginas o se compite el video. Si falta algún render o audio, se reporta como `[blocker]` en kanban.

---

## Paso 7: revision → evaluacion cruzada

**Actor:** `director` + filiales
**Skill:** `evaluacion-cruzada`
**Input:** narrativa final + produccion
**Output:** `produccion/evaluacion_cruzada.md`
**Kanban:** `revision`

La filial de producción evalúa la narrativa (adaptabilidad, claridad visual, ritmo). La filiales devuelve su evaluación. El Director aplica la rúbrica:

- **≥ 28/40:** APROBADO → avanzar.
- **20-27/40:** REQUIERE CAMBIOS → volver al paso correspondiente.
- **< 20/40:** RECHAZADO → informar al usuario.

---

## Paso 8: entrega

**Actor:** `director`
**Skills:** `build_deliverable` (script)
**Input:** `outputs/<proyecto>/`
**Output:** `outputs/<proyecto>/bundle.zip` + commit + tag `v1.0`
**Kanban:** `revision` → `entregado`

El Director empaqueta todo: entregable final + manuscrito + pitch + wiki + créditos. Se commitea con tag semántico. Se informa al usuario.

---

## Reglas de rollback

| Paso donde se rechaza | Vuelve a |
|---|---|
| `pitch` rechazado | `idea-generator` |
| `narrativa` incompleta | `escritor` |
| `edicion` falla | `escritor` (con feedback) |
| `guion` no adaptable | `escritor` + `editor-desarrollo` |
| `produccion` (renders) | `generador-imagenes` |
| `evaluacion-cruzada` < 20 | Reescribir desde el paso indicado en el reporte |

Tras 3 rechazos consecutivos en el mismo paso: informar al usuario antes de reintentar.
