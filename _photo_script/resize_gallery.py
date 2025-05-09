from PIL import Image
import os

input_dir = r"C:\Users\ioman\OneDrive\Documents\Work\Portfolio\Test_gpt\photo-portfolio\assets\images\gallery"
output_dir = r"C:\Users\ioman\OneDrive\Documents\Work\Portfolio\Test_gpt\photo-portfolio\assets\images\gallery_light"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        try:
            with Image.open(input_path) as img:
                img.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                img.save(output_path, format="JPEG", quality=70)
                print(f"Saved: {filename}")
        except Exception as e:
            print(f"Failed: {filename} ({e})")
