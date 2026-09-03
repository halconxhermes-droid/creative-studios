# Creative Studios

Estudio creativo multi-agente. Dos filiales especializadas colaboran bajo un Director para producir contenido end-to-end: narrativa (escritores, editores) y producción visual (guionistas, artistas, generadores).

## Cómo crear un proyecto

### Opción 1: directo con el Director

Envía un brief al Director de Estudio (este Hermes). Ejemplo:

> "Quiero un manga cyberpunk de 8 páginas ambientado en Lima 2099, protagonista taxista hacker, tono noir."

El Director orquesta todo el ciclo automáticamente.

### Opción 2: manual

```bash
mkdir -p /data/studios/creative/projects/<proyecto-id>
cp /data/studios/creative/templates/brief.md /data/studios/creative/projects/<proyecto-id>/brief.md
# Edita el brief con tu idea
hermes kanban task-add creative-studios --tenant director --column brief --title "<proyecto-id>"
```

## Cómo seguir un proyecto

```bash
hermes kanban show creative-studios --task <id>          # ver detalle
hermes kanban list creative-studios                      # ver board completo
ls /data/studios/creative/projects/<proyecto-id>/        # ver artefactos
```

## Cómo se entregan los outputs

Los entregables finales viven en `/data/studios/creative/projects/<proyecto-id>/outputs/`. El Director los empaqueta en un bundle con README + créditos.

## Roles y skills

| Filial | Rol | Skill |
|---|---|---|
| Narrativa | Generador de ideas | `idea-generator` |
| Narrativa | Escritor | `escritor` |
| Narrativa | Editor de desarrollo | `editor-desarrollo` |
| Narrativa | Editor de línea | `editor-linea` |
| Narrativa | Lector beta | `lector-beta` |
| Narrativa | Continuista | `continuista` |
| Producción | Guionista manga | `guionista-manga` |
| Producción | Guionista cómic | `guionista-comic` |
| Producción | Guionista video | `guionista-video` |
| Producción | Director de arte | `director-arte` |
| Producción | Generador de imágenes | `generador-imagenes` |
| Producción | Componedor manga | `componedor-manga` |
| Producción | Editor video | `editor-video` |
| Orquestación | Director de estudio | `director-estudio` |
| Orquestación | Evaluación cruzada | `evaluacion-cruzada` |

## Documentación adicional

- `AGENTS.md` — reglas globales
- `CYCLE.md` — flujo de proyecto
- `CONVENTIONS.md` — cómo se hacen las cosas
- `PROCESS.md` — aprobación y rechazo
- `templates/` — plantillas de artefactos
- `/data/.hermes/plans/2026-09-03_040010-creative-studios-multi-agent.md` — plan completo
