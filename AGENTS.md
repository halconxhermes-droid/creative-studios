# Creative Studios — Reglas Globales

> Este archivo es la constitución del estudio. Todo agente (humano o IA) que trabaje aquí debe leerlo antes de actuar.

## Idioma

- **Por defecto: español.** Salvo brief explícito que pida otro idioma.
- Nombres de archivos, commits y mensajes en español (excepto términos técnicos universales como `JSON`, `PDF`, `commit`).

## Convenciones de nombres

- **Proyectos:** `kebab-case` → `novela-el-taxi-de-la-memoria`
- **Carpetas internas:** `snake_case` → `narrativa/`, `produccion/`
- **Archivos:** `snake_case` con sufijo de versión → `pitch_v1.md`, `capitulo_01.md`
- **Artefactos finales:** siempre sin versión → `manga.pdf`, `video.mp4`

## Estructura obligatoria de cada proyecto

```
projects/<proyecto-id>/
├── brief.md                  # input del usuario (inmutable una vez creado)
├── kanban.json               # snapshot del board
├── wiki/                     # bible del mundo (source of truth)
│   ├── mundo.md
│   ├── personajes.md
│   └── linea_tiempo.md
├── narrativa/
│   ├── pitch.md              # propuesta aprobada
│   ├── borrador/             # versiones iniciales
│   ├── ediciones/            # manuscritos editados
│   └── final.md              # versión aprobada para producción
├── produccion/
│   ├── guion.json            # guion técnico (manga/comic/video)
│   ├── storyboard.md         # storyboard visual
│   ├── brief_artistico.md    # estilo visual
│   ├── prompts/              # prompts de generación visual
│   ├── renders/              # imágenes/videos generados
│   ├── manga/                # componentes manga
│   ├── comic/                # componentes cómic
│   ├── video/                # componentes video
│   └── audio/                # música, voces, SFX
└── outputs/                  # entregables finales (al usuario)
```

## Reglas de versionado

- **Commits:** cada entregable aprobado se commitea con mensaje `tipo(scope): descripción`.
- **Tags:** entregable final lleva tag semántico `v1.0`, `v1.1`, etc. (Mayor.Minor).
- **Rama:** un proyecto vive en su propia rama (`proyecto/<id>`) cuando hay múltiples proyectos simultáneos.
- **No borrar artefactos intermedios** — son trazabilidad. Si un entregable cambia, se versiona, no se sobrescribe.

## Tono editorial

- Profesional, claro, sin jerga gratuita.
- Crítico directo en evaluaciones (mejor feedback doloroso temprano que pulido tarde).
- Respetuoso con el trabajo ajeno: cada cambio sugiere el porqué.
- Sin emojis decorativos en manuscritos finales (sí en kanban y comunicación interna).

## Cuando un agente entra al estudio

1. Lee este `AGENTS.md` (constitución).
2. Lee `CYCLE.md` (flujo de proyecto).
3. Lee `CONVENTIONS.md` (cómo se hacen las cosas).
4. Revisa el kanban (`hermes kanban list creative-studios`) para ver el estado actual.
5. Carga la skill específica de su rol.
6. Reporta en kanban con `kanban_comment` lo que va haciendo.

## Restricciones absolutas

- **No modificar `brief.md` después de creado.** Si el brief cambia, se crea un nuevo proyecto.
- **No saltarse pasos del ciclo.** La evaluación cruzada es obligatoria para entregables que cruzan filiales.
- **No destruir trabajo.** Rechazos = nueva versión, no borrado.
- **No inventar datos del mundo.** El continuista es la autoridad; cualquier inconsistencia se reporta, no se "arregla" silenciosamente.
