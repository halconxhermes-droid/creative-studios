# Creative Studios — Kanban Configuration

Board: `creative-studios`

## Columnas (lifecycle del proyecto)

| Columna | Descripción | Acción esperada |
|---|---|---|
| `brief` | Brief del usuario, ingresado | Validar con Director |
| `pitch` | Pitch propuesto, listo para aprobación | Aprobado → narrativa |
| `narrativa` | Manuscrito redactado | Enviar a edición |
| `edicion` | Revisado por editores (desarrollo + línea) | Aprobado → guion |
| `guion` | Guion técnico producido | Enviar a producción |
| `produccion` | Renders, audio, storyboard | Listo para revisión |
| `revision` | Evaluación cruzada | Aprobado → entregado / Rechazado → corrección |
| `entregado` | Entregable final empaquetado | Archivado |

## Tenants (filiales)

| Tenant | Path workspace | Skills |
|---|---|---|
| `narrativa` | `/data/studios/creative/projects` | `idea-generator`, `escritor`, `editor-desarrollo`, `editor-linea`, `lector-beta`, `continuista` |
| `produccion` | `/data/studios/creative/projects` | `guionista-manga`, `guionista-comic`, `guionista-video`, `director-arte`, `generador-imagenes`, `componedor-manga`, `editor-video` |
| `director` | `/data/studios/creative/projects` | `director-estudio`, `evaluacion-cruzada` |

## Cómo crear una tarea

```bash
hermes kanban create "<título>" \
  --body "<descripción completa>" \
  --tenant narrativa \
  --project "<proyecto-id>"
```

## Cómo listar

```bash
hermes kanban list                        # tasks listos/todo
hermes kanban list --assignee narrativa   # tasks de la filial narrativa
hermes kanban show <task-id>              # detalle + comentarios
```

## Cómo comentar (para reportar progreso)

```bash
hermes kanban comment <task-id> --message "<mensaje>"
```
