import os
import sys
import json
import time
import base64
import urllib.request
import subprocess
import shutil
from PIL import Image, ImageDraw

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
CONTENT_DIR = os.path.join(BASE_DIR, "content")
FIG_DIR = os.path.join(CONTENT_DIR, "figures")
ILLUST_DIR = os.path.join(CONTENT_DIR, "illustrations")
DOCS_IMG_DIR = os.path.join(BASE_DIR, "docs", "assets", "images")

DRAW_THINGS_URL = "http://192.168.128.59:7860/sdapi/v1/txt2img"
neg_common = (
    "bad eyes, deformed eyes, missing eyes, closed eyes, deformed anatomy, bad hands, blurry, ugly, "
    "text, watermark, speech bubble, dialogue, words, letters, kanji, japanese text, font, subtitles"
)

def generate_panel(prompt, output_file, timeout=300):
    if os.path.exists(output_file) and os.path.getsize(output_file) > 10000:
        print(f"Panel exists: {output_file}")
        return True
    payload = {
        "prompt": prompt + ", masterpiece, clean manga anime style, Kyoto Animation, sharp lineart, wordless, NO text, NO speech bubbles, pure silent comic art",
        "negative_prompt": neg_common,
        "width": 512,
        "height": 512,
        "steps": 8,
        "guidance_scale": 3.5,
        "sampler": "Euler A Trailing"
    }
    req = urllib.request.Request(DRAW_THINGS_URL, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
    for attempt in range(1, 4):
        try:
            print(f"Generating {output_file} (attempt {attempt})...")
            with urllib.request.urlopen(req, timeout=timeout) as res:
                body = json.loads(res.read().decode("utf-8"))
                imgs = body.get("images", [])
                if imgs and imgs[0]:
                    with open(output_file, "wb") as fp:
                        fp.write(base64.b64decode(imgs[0]))
                    print(f"Saved {output_file}")
                    return True
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(5)
    return False

def combine_4koma(panel_files, final_output_path):
    panel_w, panel_h = 512, 512
    margin_x = 24
    margin_top = 28
    margin_between = 24
    border_thickness = 4
    
    canvas_w = panel_w + (margin_x * 2)
    canvas_h = margin_top + (panel_h * 4) + (margin_between * 3) + margin_top
    
    manga_img = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    draw = ImageDraw.Draw(manga_img)
    
    current_y = margin_top
    for idx, p_path in enumerate(panel_files):
        p_img = Image.open(p_path).convert("RGB")
        if p_img.size != (panel_w, panel_h):
            p_img = p_img.resize((panel_w, panel_h), Image.LANCZOS)
        
        box_x0 = margin_x - border_thickness
        box_y0 = current_y - border_thickness
        box_x1 = margin_x + panel_w + border_thickness - 1
        box_y1 = current_y + panel_h + border_thickness - 1
        draw.rectangle([box_x0, box_y0, box_x1, box_y1], fill=(20, 25, 35))
        
        manga_img.paste(p_img, (margin_x, current_y))
        current_y += panel_h + margin_between
        
    manga_img.save(final_output_path, "PNG", quality=95)
    print(f"Combined 4-koma saved: {final_output_path}")

def compile_tikz(base_name):
    print(f"Compiling TikZ {base_name}...")
    res = subprocess.run(["lualatex", "-interaction=nonstopmode", f"{base_name}.tex"], cwd=FIG_DIR, capture_output=True)
    pdf_path = os.path.join(FIG_DIR, f"{base_name}.pdf")
    png_path = os.path.join(FIG_DIR, f"{base_name}.png")
    render_prefix = os.path.join(FIG_DIR, f"{base_name}_render")
    if os.path.exists(pdf_path):
        subprocess.run(["pdftoppm", "-png", "-r", "150", f"{base_name}.pdf", render_prefix], cwd=FIG_DIR, capture_output=True)
        rendered_1 = os.path.join(FIG_DIR, f"{base_name}_render-1.png")
        if os.path.exists(rendered_1):
            if os.path.exists(png_path):
                os.remove(png_path)
            os.rename(rendered_1, png_path)
            shutil.copy2(png_path, os.path.join(DOCS_IMG_DIR, f"{base_name}.png"))
            print(f"Successfully compiled TikZ: {png_path}")
            return True
    print(f"Failed to compile TikZ: {base_name}")
    return False

if __name__ == "__main__":
    print("Pipeline helper ready.")
