#!/usr/bin/env python3
"""
build_deliverable.py — Genera el bundle final de un proyecto creativo.
Usage: python3 build_deliverable.py <proyecto-id>
"""

import sys
import zipfile
import subprocess
from pathlib import Path
from datetime import datetime

STUDIOS = Path("/data/studios/creative")
OUTPUTS = STUDIOS / "outputs"


def build(proyecto_id: str) -> Path:
    proyecto_path = STUDIOS / "projects" / proyecto_id
    if not proyecto_path.exists():
        print(f"ERROR: proyecto '{proyecto_id}' no encontrado en {proyecto_path}")
        sys.exit(1)

    bundle_dir = OUTPUTS / proyecto_id
    bundle_dir.mkdir(parents=True, exist_ok=True)

    # README del bundle
    readme = f"""# {proyecto_id.title()} — Entregable Final

**Fecha:** {datetime.utcnow().strftime('%Y-%m-%d')}
**Generado por:** Creative Studios (Hermes Agent)

## Contenido del bundle

- `manga.pdf` — Manga formato B5, {proyecto_id}
- `video.mp4` — Video, si fue solicitado
- `manuscrito_final.md` — Manuscrito narrativo aprobado
- `pitch.md` — Propuesta original
- `wiki/` — Biblia del mundo

## Créditos

Generado con Creative Studios — estudio creativo multi-agente.
Director de Estudio: Hermes Agent (Nous Research)
Filial Narrativa: idea-generator, escritor, editor-desarrollo,
                  editor-linea, lector-beta, continuista
Filial Producción: director-arte, guionista-manga, generador-imagenes,
                   componedor-manga, editor-video
"""
    readme_path = bundle_dir / "README.md"
    readme_path.write_text(readme, encoding="utf-8")
    print(f"OK: README.md → {readme_path}")

    # Copiar entregables
    src_outputs = proyecto_path / "outputs"
    if src_outputs.exists():
        for f in src_outputs.rglob("*"):
            if f.is_file():
                rel = f.relative_to(src_outputs)
                dst = bundle_dir / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(f.read_bytes())
                print(f"  + {rel}")
    else:
        # Buscar entregables sueltos
        for pattern in ["*.pdf", "*.mp4", "*.zip"]:
            for f in proyecto_path.rglob(pattern):
                dst = bundle_dir / f.name
                dst.write_bytes(f.read_bytes())
                print(f"  + {f.name} (from {f.parent.name}/)")

    # Copiar manuscrito final y pitch
    final_md = proyecto_path / "narrativa" / "final.md"
    if not final_md.exists():
        final_md = proyecto_path / "narrativa" / "ediciones" / "manuscrito_editado.md"
    if final_md.exists():
        dst = bundle_dir / "manuscrito_final.md"
        dst.write_bytes(final_md.read_bytes())
        print(f"  + manuscrito_final.md")

    pitch_md = proyecto_path / "narrativa" / "pitch.md"
    if pitch_md.exists():
        dst = bundle_dir / "pitch.md"
        dst.write_bytes(pitch_md.read_bytes())
        print(f"  + pitch.md")

    # Copiar wiki
    wiki_src = proyecto_path / "wiki"
    if wiki_src.exists():
        wiki_dst = bundle_dir / "wiki"
        wiki_dst.mkdir(parents=True, exist_ok=True)
        for f in wiki_src.rglob("*.md"):
            dst = wiki_dst / f.name
            dst.write_bytes(f.read_bytes())
        print(f"  + wiki/")

    # ZIP del bundle
    zip_path = bundle_dir.parent / f"{proyecto_id}-bundle.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in bundle_dir.rglob("*"):
            if f.is_file():
                arcname = f"{proyecto_id}/" + str(f.relative_to(bundle_dir))
                zf.write(f, arcname)
    print(f"\nOK: Bundle → {zip_path} ({zip_path.stat().st_size // 1024} KB)")

    # Git commit + tag
    git_dir = proyecto_path
    try:
        subprocess.run(["git", "add", "-A"], cwd=git_dir, check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", f"feat({proyecto_id}): entrega v1.0"],
            cwd=git_dir, check=True, capture_output=True, text=True
        )
        subprocess.run(
            ["git", "tag", "-a", f"v1.0", "-m", f"Release v1.0 — {proyecto_id}"],
            cwd=git_dir, check=True, capture_output=True
        )
        print(f"OK: git commit + tag v1.0 en {git_dir}")
    except subprocess.CalledProcessError as e:
        print(f"WARN: git commit failed: {e.stderr.decode()}")

    return bundle_dir


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 build_deliverable.py <proyecto-id>")
        sys.exit(1)
    build(sys.argv[1])
