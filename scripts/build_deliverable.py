#!/usr/bin/env python3
"""
build_deliverable.py — Genera el bundle final de un proyecto creativo.

Usage:
    python3 build_deliverable.py <proyecto-id> [--version v1.0]

Por qué existe (CONVENTIONS.md §"Versionado de artefactos"):
    Cada entrega aprobada se empaqueta en un bundle con:
    - README.md (descripción y guía)
    - manuscrito_final.md (narrativa aprobada)
    - pitch.md (propuesta original)
    - guion.json (guion técnico, si aplica)
    - brief_artistico.md (paleta/tipografías/moodboard, si aplica)
    - evaluacion_cruzada.md (veredicto final)
    - wiki/ (bible del mundo)
    - CREDITOS.md (roles y skills utilizadas)

El bundle se comprime en <proyecto-id>-bundle.zip en outputs/.

Luego intenta hacer `git commit` + `git tag` semántico en la raíz del repo
de estudios (si es un repositorio git). Si el tag ya existe, lo sobrescribe
con `-f` solo si se pasa --force.
"""

import argparse
import sys
import zipfile
import subprocess
from pathlib import Path
from datetime import datetime, timezone

STUDIOS = Path("/data/studios/creative")
OUTPUTS = STUDIOS / "outputs"


def build(proyecto_id: str, version: str = "v1.0", force: bool = False) -> Path:
    """Empaqueta un proyecto en outputs/<proyecto-id>/ y devuelve la ruta."""
    proyecto_path = STUDIOS / "projects" / proyecto_id
    if not proyecto_path.exists():
        print(f"ERROR: proyecto '{proyecto_id}' no encontrado en {proyecto_path}")
        sys.exit(1)

    bundle_dir = OUTPUTS / proyecto_id
    bundle_dir.mkdir(parents=True, exist_ok=True)

    # 1. README del bundle
    readme = f"""# {proyecto_id} — Entregable Final

**Fecha:** {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
**Versión:** {version}
**Generado por:** Creative Studios (Hermes Agent)

## Contenido del bundle

- `manuscrito_final.md` — Manuscrito narrativo aprobado
- `pitch.md` — Propuesta original
- `guion.json` — Guion técnico (manga/cómic/video), si aplica
- `brief_artistico.md` — Paleta, tipografías y moodboard, si aplica
- `evaluacion_cruzada.md` — Veredicto de aprobación final
- `wiki/` — Biblia del mundo
- `CREDITOS.md` — Roles y skills utilizadas

## Créditos

Generado con Creative Studios — estudio creativo multi-agente.
Director de Estudio: Hermes Agent (Nous Research)
"""
    readme_path = bundle_dir / "README.md"
    readme_path.write_text(readme, encoding="utf-8")
    print(f"OK: README.md → {readme_path}")

    # 2. Copiar outputs/ existentes (si los hay)
    src_outputs = proyecto_path / "outputs"
    if src_outputs.exists():
        for f in src_outputs.rglob("*"):
            if f.is_file():
                rel = f.relative_to(src_outputs)
                dst = bundle_dir / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(f.read_bytes())
                print(f"  + {rel}")

    # 3. Manuscrito final (preferir narrativa/final.md; fallback a ediciones/)
    final_md = proyecto_path / "narrativa" / "final.md"
    if not final_md.exists():
        final_md = proyecto_path / "narrativa" / "ediciones" / "manuscrito_editado.md"
    if final_md.exists():
        dst = bundle_dir / "manuscrito_final.md"
        dst.write_bytes(final_md.read_bytes())
        print("  + manuscrito_final.md")

    # 4. Pitch
    pitch_md = proyecto_path / "narrativa" / "pitch.md"
    if pitch_md.exists():
        dst = bundle_dir / "pitch.md"
        dst.write_bytes(pitch_md.read_bytes())
        print("  + pitch.md")

    # 5. Guion técnico (manga/cómic/video)
    guion_json = proyecto_path / "produccion" / "guion.json"
    if guion_json.exists():
        dst = bundle_dir / "guion.json"
        dst.write_bytes(guion_json.read_bytes())
        print("  + guion.json")

    # 6. Brief artístico
    brief_art = proyecto_path / "produccion" / "brief_artistico.md"
    if brief_art.exists():
        dst = bundle_dir / "brief_artistico.md"
        dst.write_bytes(brief_art.read_bytes())
        print("  + brief_artistico.md")

    # 7. Evaluación cruzada
    eval_cruz = proyecto_path / "produccion" / "evaluacion_cruzada.md"
    if eval_cruz.exists():
        dst = bundle_dir / "evaluacion_cruzada.md"
        dst.write_bytes(eval_cruz.read_bytes())
        print("  + evaluacion_cruzada.md")

    # 8. Wiki
    wiki_src = proyecto_path / "wiki"
    if wiki_src.exists():
        wiki_dst = bundle_dir / "wiki"
        wiki_dst.mkdir(parents=True, exist_ok=True)
        for f in wiki_src.rglob("*.md"):
            dst = wiki_dst / f.name
            dst.write_bytes(f.read_bytes())
        print("  + wiki/")

    # 9. Créditos
    creditos = proyecto_path / "CREDITOS.md"
    if creditos.exists():
        dst = bundle_dir / "CREDITOS.md"
        dst.write_bytes(creditos.read_bytes())
        print("  + CREDITOS.md")

    # 10. ZIP del bundle
    zip_path = bundle_dir.parent / f"{proyecto_id}-bundle.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(bundle_dir.rglob("*")):
            if f.is_file():
                arcname = f"{proyecto_id}/" + str(f.relative_to(bundle_dir))
                zf.write(f, arcname)
    print(f"\nOK: Bundle → {zip_path} ({zip_path.stat().st_size // 1024} KB)")

    # 11. Git commit + tag en el repo del proyecto (no en studios/)
    tag_name = f"{proyecto_id}/{version}"
    try:
        subprocess.run(["git", "add", "-A"], cwd=proyecto_path,
                       check=True, capture_output=True)
        commit_msg = f"feat({proyecto_id}): entrega {version}"
        result = subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=proyecto_path, capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"OK: git commit en {proyecto_path}")
        elif "nothing to commit" in (result.stdout + result.stderr):
            print(f"INFO: sin cambios que commitear en {proyecto_path}")
        else:
            print(f"WARN: git commit: {result.stderr.strip()}")

        tag_args = ["git", "tag", "-a", tag_name, "-m", f"Release {version} — {proyecto_id}"]
        if force:
            tag_args.insert(2, "-f")
        result = subprocess.run(tag_args, cwd=proyecto_path,
                               capture_output=True, text=True)
        if result.returncode == 0:
            print(f"OK: git tag {tag_name}")
        else:
            print(f"WARN: git tag: {result.stderr.strip()}")
    except FileNotFoundError:
        print("INFO: git no disponible, saltando commit/tag")
    except subprocess.CalledProcessError as e:
        print(f"WARN: git falló: {e}")

    return bundle_dir


def main():
    parser = argparse.ArgumentParser(
        description="Empaqueta un proyecto de Creative Studios en un bundle final."
    )
    parser.add_argument("proyecto_id", help="ID del proyecto (kebab-case)")
    parser.add_argument("--version", default="v1.0",
                        help="Etiqueta de versión (default: v1.0)")
    parser.add_argument("--force", action="store_true",
                        help="Sobrescribe el tag git si ya existe")
    args = parser.parse_args()
    build(args.proyecto_id, args.version, args.force)


if __name__ == "__main__":
    main()
