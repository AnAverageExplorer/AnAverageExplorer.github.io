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

def get_aspect_ratio(path):
    try:
        with Image.open(path) as img:
            width, height = img.size
            return round(width / height, 3)
    except Exception as e:
        print(f"Error reading {path.name}: {e}")
        return None

def update_md_file(md_path, ratio_value, filename, title):
    ratio_line = f"ratio: {ratio_value}"
    if md_path.exists():
        with open(md_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if any("ratio:" in line for line in lines):
            # Update existing ratio
            lines = [ratio_line + "\n" if line.startswith("ratio:") else line for line in lines]
        else:
            # Insert ratio before closing ---
            for i, line in enumerate(lines):
                if line.strip() == "---" and i != 0:
                    lines.insert(i, ratio_line + "\n")
                    break

        with open(md_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
            print(f"Updated ratio in: {md_path.name}")
    else:
        # Create new .md with ratio
        template = f'''---
filename: "{filename}"
title: "{title}"
description:
tags:

project: null
display: true
{ratio_line}
---
'''
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(template)
            print(f"Created metadata: {md_path.name}")

# Process images
for image_file in gallery_dir.iterdir():
    if image_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
        filename = image_file.name
        webp_filename = image_file.stem + ".webp"
        light_path = light_dir / webp_filename
        md_path = info_dir / f"{image_file.stem}.md"

        # Create resized .webp image only if not present or outdated
        if not light_path.exists() or os.path.getmtime(image_file) > os.path.getmtime(light_path):
            try:
                with Image.open(image_file) as img:
                    img.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                    img.save(light_path, format="WEBP", quality=75)
                    print(f"Created/updated light version: {webp_filename}")
            except Exception as e:
                print(f"Image failed: {filename} — {e}")

        # Calculate aspect ratio and update/create .md
        ratio = get_aspect_ratio(image_file)
        if ratio:
            title = image_file.stem.replace('_', ' ').title()
            update_md_file(md_path, ratio, filename, title)
