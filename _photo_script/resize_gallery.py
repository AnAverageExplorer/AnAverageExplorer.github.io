from PIL import Image
import os
from pathlib import Path

# Set relative paths from script directory
base_dir = Path(__file__).resolve().parents[1]  # goes up from _photo_script
gallery_dir = base_dir / "assets" / "images" / "gallery"
light_dir = base_dir / "assets" / "images" / "gallery_light"
info_dir = base_dir / "_image_info"

# Ensure output directories exist
light_dir.mkdir(parents=True, exist_ok=True)
info_dir.mkdir(parents=True, exist_ok=True)

template = '''---
filename: "{filename}"
title: "{title}"
description:
tags:

project: null
display: true
---
'''

# Process images
for image_file in gallery_dir.iterdir():
    if image_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
        filename = image_file.name
        webp_filename = image_file.stem + ".webp"
        light_path = light_dir / webp_filename
        md_path = info_dir / f"{image_file.stem}.md"

        # Create resized .webp image only if not present or source is newer
        if not light_path.exists() or os.path.getmtime(image_file) > os.path.getmtime(light_path):
            try:
                with Image.open(image_file) as img:
                    img.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                    img.save(light_path, format="WEBP", quality=75)
                    print(f"Created/updated light version: {webp_filename}")
            except Exception as e:
                print(f"Image failed: {filename} — {e}")

        # Create .md metadata file if not present
        if not md_path.exists():
            title = image_file.stem.replace('_', ' ').title()
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(template.format(filename=filename, title=title))
                print(f"Created metadata: {md_path.name}")

