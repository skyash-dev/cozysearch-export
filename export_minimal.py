import os
import shutil
from pathlib import Path

src_dir =  Path("/home/skyash/archivebox/data/archive")
dst_dir =  Path("/home/skyash/Documents/cozysearch-export")
dst_dir.mkdir(parents=True, exist_ok=True)

for folder in src_dir.iterdir():
    if folder.is_dir():
        md = folder / "content.md"
        meta = folder / "metadata.json"
        if md.exists() and meta.exists():
            export_path = dst_dir / folder.name
            export_path.mkdir(exist_ok=True)
            shutil.copy2(md, export_path / "content.md")
            shutil.copy2(meta, export_path / "metadata.json")
