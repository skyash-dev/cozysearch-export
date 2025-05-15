import os
import shutil
from pathlib import Path

src_dir = Path("/home/skyash/archivebox/data/archive")
dst_dir = Path("/home/skyash/Documents/cozysearch-export")
dst_dir.mkdir(parents=True, exist_ok=True)

for folder in src_dir.iterdir():
    if folder.is_dir():
        output_html = folder / "output.html"
        content_md = folder / "content.md"
        metadata = folder / "metadata.json"
        screenshot = folder / "screenshot.png"

        if output_html.exists() and metadata.exists():
            export_path = dst_dir / folder.name
            export_path.mkdir(exist_ok=True)

            shutil.copy2(output_html, export_path / "output.html")
            shutil.copy2(metadata, export_path / "metadata.json")

            if content_md.exists():
                shutil.copy2(content_md, export_path / "content.md")
            if screenshot.exists():
                shutil.copy2(screenshot, export_path / "screenshot.png")
