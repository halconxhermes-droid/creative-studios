# Creative Studios — Convenciones

## Convenciones globales

| Convención | Valor / Ejemplo |
|---|---|
| **Idioma por defecto** | Español |
| **Nombres de proyectos** | `kebab-case` → `novela-el-taxi-de-la-memoria` |
| **Nombres de carpetas** | `snake_case` → `narrativa/`, `produccion/` |
| **Sufijos de archivo** | `snake_case` con versión → `pitch_v1.md`, `capitulo_01.md` |
| **Artefactos finales sin versión** | `manga.pdf`, `video.mp4` |
| **Tono editorial** | Profesional, claro, sin jerga gratuita |
| **Commits** | `tipo(scope): descripción` (conventional commits) |
| **Tags de release** | `v1.0`, `v1.1`, etc. (semantic versioning) |
| **Ramas** | `proyecto/<id>` cuando hay proyectos simultáneos |
| **No borrar artefactos intermedios** | Versionar, no sobrescribir |
| **Emojis** | Ninguno en manuscritos finales; sí en kanban/comunicación interna |
| **Criterios de evaluación** | Directos, con feedback accionable |

## Estructura obligatoria por proyecto

Cada proyecto en `projects/<proyecto-id>/` debe tener:

```
brief.md                    # input del usuario (inmutable)
kanban.json                 # snapshot del board
wiki/
├── mundo.md
├── personajes.md
└── linea_tiempo.md
narrativa/
├── pitch.md                # propuesta aprobada
├── borrador/               # versiones iniciales
├── ediciones/              # manuscritos editados
└── final.md                # versión aprobada para producción
produccion/
├── guion.json              # guion técnico (manga/comic/video)
├── storyboard.md           # storyboard visual
├── brief_artistico.md      # estilo visual
├── prompts/
│   └── <panel>_v1.yaml     # prompts de generación visual
├── renders/                # imágenes/videos generados
├── manga/                  # componentes manga
├── comic/                  # componentes cómic
├── video/                  # componentes video
└── audio/                  # música, voces, SFX
outputs/                    # entregables finales (al usuario)
```

## Tareas Kanban: flujo por columnas

| Columna | Tenant principal | Qué se hace |
|---|---|---|
| `brief` | `director` | Usuario envía brief; Director valida |
| `pitch` | `narrativa` | Generador de ideas produce pitch |
| `narrativa` | `narrativa` | Escritor escribe capítulo/manuscrito |
| `edicion` | `narrativa` | Editor desarrollo + editor línea pulen |
| `guion` | `produccion` | Guionista adapta → guion técnico |
| `produccion` | `produccion` | Generador de imágenes/audio/renders |
| `revision` | `director` + otra filial | Evaluación cruzada |
| `entregado` | `director` | Bundle empaquetado + entregado al usuario |

## Reglas de tenencia (filiales)

| Tenant | Autoridad | Skills obligatorias |
|---|---|---|
| `narrativa` | Continuista es la autoridad de mundo | `idea-generator`, `escritor`, `editor-desarrollo`, `editor-linea`, `lector-beta`, `continuista` |
| `produccion` | Director de arte es autoridad visual | `guionista-manga`, `guionista-comic`, `guionista-video`, `director-arte`, `generador-imagenes`, `componedor-manga`, `editor-video` |
| `director` | Coordinador general, última palabra | `director-estudio`, `evaluacion-cruzada` |

## Cuándo se mueve tarea en el kanban

1. Brief válido → movimiento a `pitch`
2. Pitch aprobado por Director → movimiento a `narrativa`
3. Manuscrito completado → movimiento a `edicion`
4. Edición aprobada (sin rechazos críticos) → movimiento a `guion`
5. Guión técnico aprobado → movimiento a `produccion`
6. Producción completada → movimiento a `revision`
7. Evaluación cruzada aprobada → movimiento a `entregado`
8. Rechazo en cualquier paso → retroceso a columna anterior con `kanban_comment` y tag `[rewrite]`

## Feedback de rechazo: plantilla obligatoria

```markdown
### 📝 Rechazo: <razón corta>

**Qué falló:** <qué aspecto concreto no funciona>

**Qué falta o es débil:**
1. <punto 1 específico, con referencia página/panel>
2. <punto 2>

**Cómo arreglarlo:**
1. <acción concreta para el agente que rehaga>
2. <ejemplo o referencia>

**Plazo estimado:** <horas o "próxima iteración">
```

## Versionado de artefactos

- **Commit tras aprobación:** cada entregable aprobado se commitea con tag `vN.M`.
- **Git message:** `tipo(scope): descripción del entregable` (feat, fix, docs, style, refactor, test, chore).
- **Tag:** `projects/<proyecto-id>/releases/<tag>`.
- **No sobrescribir:** si hay que cambiar algo, crear nueva versión con sufijo.

## Pantallas prohibidas en trabajos finales

- `emoji` decorativos en manuscritos, guiones, storyboards (sí en comunicación interna en kanban).
- `TXT-speak` (ej. "u" por "you", "q" por "que") salvo en diálogos donde el personaje lo usa intencionalmente.
- "info-dumping" sin setup previo. El continuista debe haber marcado la información antes.
- Resolver conflictos sin setup previo.

## Prioridades de tokens / costo

Para el Director:
1. **Primer paso:** usar modelo barato (ej. `hermes-3-8b-openhermes`) para tasks mecánicas (formateo JSON, validación, resúmenes).
2. **Paso creativo:** usar modelo de calidad para escritura, guion, edición.
3. **Generación visual:** usar ComfyUI local si hay GPU; si no, API con límite presupuestario.