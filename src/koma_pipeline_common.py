import os
import json
import time
import base64
import shutil
import urllib.request
from PIL import Image, ImageDraw

DRAW_THINGS_URL = "http://192.168.128.59:7860/sdapi/v1/txt2img"
WORK_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(WORK_DIR)
ILLUST_DIR = os.path.join(BASE_DIR, "content", "illustrations")
DOCS_IMG_DIR = os.path.join(BASE_DIR, "docs", "assets", "images")
BRAIN_DIR = r"C:\Users\k\.gemini\antigravity\brain\b164408c-44fc-48cc-9938-3c3604d5617b"

neg_common = (
    "bad eyes, deformed eyes, missing eyes, closed eyes, crossed eyes, melted face, no pupils, no eyes, "
    "sunglasses, opaque glasses, blindfold, deformed anatomy, bad hands, blurry, ugly, text, watermark, speech bubble"
)

def generate_panel(prompt, output_file):
    if os.path.exists(output_file) and os.path.getsize(output_file) > 10000:
        print(f"  [Cached] Panel exists: {os.path.basename(output_file)} ({os.path.getsize(output_file)} bytes)")
        return True
    
    payload = {
        "prompt": prompt,
        "negative_prompt": neg_common,
        "width": 512,
        "height": 512,
        "steps": 12,
        "guidance_scale": 4.0,
        "sampler": "Euler A Trailing"
    }
    req = urllib.request.Request(
        DRAW_THINGS_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    t0 = time.time()
    for attempt in range(1, 4):
        try:
            print(f"  Generating {os.path.basename(output_file)} (attempt {attempt})...")
            with urllib.request.urlopen(req, timeout=400) as res:
                body = json.loads(res.read().decode("utf-8"))
                imgs = body.get("images", [])
                if imgs and imgs[0]:
                    with open(output_file, "wb") as f:
                        f.write(base64.b64decode(imgs[0]))
                    print(f"  [Saved] {output_file} in {time.time()-t0:.2f}s ({os.path.getsize(output_file)} bytes)")
                    return True
        except Exception as e:
            print(f"  Attempt {attempt} failed: {e}. Retrying in 5s...")
            time.sleep(5)
    return False

def combine_4koma(panel_files, final_output_path):
    print(f"Combining {len(panel_files)} panels into: {os.path.basename(final_output_path)}...")
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
    print(f"Combined 4-koma saved: {final_output_path} ({manga_img.size})")

def process_episode_4koma(ep_num, panels_data):
    ep_str = f"ep{ep_num:02d}"
    print(f"\n=======================================================")
    print(f"=== PROCESSING {ep_str.upper()} 4-KOMA MANGA PIPELINE ===")
    print(f"=======================================================")
    
    temp_dir = os.path.join(ILLUST_DIR, f"temp_{ep_str}")
    os.makedirs(temp_dir, exist_ok=True)
    
    panel_files = []
    for p_info in panels_data:
        p_file = os.path.join(temp_dir, f"p{p_info['panel_num']}.png")
        print(f"\n--- {ep_str.upper()} Panel {p_info['panel_num']}: {p_info['name']} ---")
        ok = generate_panel(p_info["prompt"], p_file)
        if not ok:
            print(f"Warning: Failed to generate {p_file}")
        panel_files.append(p_file)
        
    final_filename = f"{ep_str}_4koma.png"
    out_illust = os.path.join(ILLUST_DIR, final_filename)
    docs_illust = os.path.join(DOCS_IMG_DIR, final_filename)
    brain_illust = os.path.join(BRAIN_DIR, final_filename)
    
    combine_4koma(panel_files, out_illust)
    
    shutil.copy2(out_illust, docs_illust)
    try:
        shutil.copy2(out_illust, brain_illust)
    except Exception as e:
        pass
    print(f"SUCCESS: {final_filename} deployed to content and docs assets!")
