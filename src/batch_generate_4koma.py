import os
import json
import base64
import urllib.request
import time
import shutil
from PIL import Image, ImageDraw

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
DRAW_THINGS_URL = "http://192.168.128.59:7860/sdapi/v1/txt2img"
DOCS_IMG_DIR = os.path.join(BASE_DIR, "docs", "assets", "images")
CONTENT_ILLUST = os.path.join(BASE_DIR, "content", "illustrations")

neg_common = (
    "bad eyes, deformed eyes, missing eyes, closed eyes, deformed anatomy, bad hands, blurry, ugly, "
    "text, watermark, speech bubble, dialogue, words, letters, kanji, japanese text, font, subtitles"
)

def make_panel(prompt, out_path):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
        print(f"Panel cached: {out_path}")
        return True
    payload = {
        "prompt": prompt + ", masterpiece, high quality anime manga art, Kyoto Animation, clean fine linework, completely wordless, NO text, NO speech bubbles, pure silent comic art",
        "negative_prompt": neg_common,
        "width": 512,
        "height": 512,
        "steps": 6,
        "guidance_scale": 3.0,
        "sampler": "Euler A Trailing"
    }
    req = urllib.request.Request(DRAW_THINGS_URL, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
    for attempt in range(1, 4):
        try:
            print(f"Rendering {out_path} (try {attempt})...")
            with urllib.request.urlopen(req, timeout=120) as res:
                body = json.loads(res.read().decode("utf-8"))
                imgs = body.get("images", [])
                if imgs and imgs[0]:
                    with open(out_path, "wb") as fp:
                        fp.write(base64.b64decode(imgs[0]))
                    print(f"Saved panel: {out_path}")
                    return True
        except Exception as e:
            print(f"Attempt {attempt} error: {e}")
            time.sleep(4)
    return False

def combine_4koma(panel_paths, out_path):
    panel_w, panel_h = 512, 512
    margin_x, margin_top, margin_between, border_thickness = 24, 28, 24, 4
    canvas_w = panel_w + (margin_x * 2)
    canvas_h = margin_top + (panel_h * 4) + (margin_between * 3) + margin_top
    
    manga_img = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    draw = ImageDraw.Draw(manga_img)
    
    curr_y = margin_top
    for p_path in panel_paths:
        p_img = Image.open(p_path).convert("RGB")
        if p_img.size != (panel_w, panel_h):
            p_img = p_img.resize((panel_w, panel_h), Image.LANCZOS)
        
        box = [margin_x - border_thickness, curr_y - border_thickness, margin_x + panel_w + border_thickness - 1, curr_y + panel_h + border_thickness - 1]
        draw.rectangle(box, fill=(20, 25, 35))
        manga_img.paste(p_img, (margin_x, curr_y))
        curr_y += panel_h + margin_between
        
    manga_img.save(out_path, "PNG", quality=95)
    print(f"Saved 4koma: {out_path}")

tasks = [
    {
        "ep": "ep79",
        "panels": [
            "smart high school boy and girl looking closely at a semiconductor wafer under a laboratory microscope",
            "oscilloscope screen showing a suspicious power fluctuation spike in a hardware circuit",
            "female scientist explaining silicon PUF fingerprint concept pointing to a clean glowing circuit diagram",
            "boy and girl smiling cheerfully giving a thumbs up with a verified secure microchip on desk"
        ]
    },
    {
        "ep": "ep80",
        "panels": [
            "cybersecurity researcher looking at a futuristic quantum computing cloud server rack",
            "entangled photon laser beam traveling into a secure optical quantum cryostat",
            "smart girl in high school uniform sending blind encrypted quantum measurement instructions from laptop",
            "researchers smiling happily celebrating secure blind quantum computation output on screen"
        ]
    },
    {
        "ep": "ep81",
        "panels": [
            "young female student looking worried at a large neural network graph on a monitor with data leaks",
            "smart boy with glasses calculating mathematical influence function gradients on a digital tablet",
            "holographic neural network node turning into gentle sparkling dust in a clean unlearning process",
            "boy and girl giving high-five smiling peacefully in a bright AI laboratory"
        ]
    }
]

if __name__ == "__main__":
    for item in tasks:
        ep_name = item["ep"]
        temp_dir = os.path.join(CONTENT_ILLUST, f"temp_{ep_name}")
        os.makedirs(temp_dir, exist_ok=True)
        panel_files = []
        for i, prompt in enumerate(item["panels"]):
            p_file = os.path.join(temp_dir, f"p{i+1}.png")
            make_panel(prompt, p_file)
            panel_files.append(p_file)
        
        final_file = os.path.join(CONTENT_ILLUST, f"{ep_name}_4koma.png")
        combine_4koma(panel_files, final_file)
        shutil.copy2(final_file, os.path.join(DOCS_IMG_DIR, f"{ep_name}_4koma.png"))
        print(f"Finished {ep_name} 4koma successfully!")
