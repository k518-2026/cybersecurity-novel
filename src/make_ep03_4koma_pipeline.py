import os
import json
import time
import base64
import urllib.request
from PIL import Image, ImageDraw

DRAW_THINGS_URL = "http://192.168.128.59:7860/sdapi/v1/txt2img"
WORK_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(WORK_DIR)
TEMP_PANELS_DIR = os.path.join(BASE_DIR, "content", "illustrations", "temp_ep03")
os.makedirs(TEMP_PANELS_DIR, exist_ok=True)

neg_common = (
    "bad eyes, deformed eyes, missing eyes, closed eyes, crossed eyes, melted face, no pupils, no eyes, "
    "sunglasses, opaque glasses, blindfold, deformed anatomy, bad hands, blurry, ugly, text, watermark, speech bubble"
)

# 4 specific panel prompts focusing on expressions and gestures (Ki-Shō-Ten-Ketsu) for Episode 03: Free Wi-Fi & Encryption
panels_config = [
    {
        "panel_num": 1,
        "name": "起: カフェで野良フリーWi-Fiを見つけて喜ぶ葵",
        "file": os.path.join(TEMP_PANELS_DIR, "p1.png"),
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of cute Japanese high school girl with dark ponytail sitting at a cozy modern cafe table, "
            "holding her smartphone excitedly, cheerful naive smile, wide sparkling hazel anime eyes, "
            "coffee cup on wooden table, warm ambient cafe lighting, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真が危険な電波傍受を真剣に警告",
        "file": os.path.join(TEMP_PANELS_DIR, "p2.png"),
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear transparent glasses, "
            "calm serious warning expression, perfectly drawn beautiful dark anime eyes, clear defined pupils, "
            "reaching hand gently out across cafe table to stop connecting, pointing to laptop screen showing unencrypted packet warning, "
            "cafe atmosphere, clean lines, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生が安全な暗号化トンネル（VPN/HTTPS）を解説",
        "file": os.path.join(TEMP_PANELS_DIR, "p3.png"),
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant stylish female university professor smiling warmly, "
            "gentle confident wise smile, beautiful expressive purple-brown anime eyes, "
            "holding a glowing transparent cryptographic tunnel shield model with small padlock icon, "
            "bright modern seminar room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 安全な通信で安心してカフェ学習を楽しむ二人",
        "file": os.path.join(TEMP_PANELS_DIR, "p4.png"),
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl with ponytail smiling with immense relief and peaceful joy, "
            "bright joyful hazel anime eyes, coffee cup in hand, nodding happily, "
            "smart high school boy with glasses smiling gently beside her while typing on laptop, "
            "cozy sunlit cafe window table, warm safe relaxed atmosphere, wordless, no text, no speech bubble"
        )
    }
]

def generate_panel(prompt, output_file):
    if os.path.exists(output_file) and os.path.getsize(output_file) > 10000:
        print(f"Skipping already generated panel: {output_file}")
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
    print(f"Generating panel -> {output_file}...")
    t0 = time.time()
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=360) as res:
                body = json.loads(res.read().decode("utf-8"))
                imgs = body.get("images", [])
                if imgs and imgs[0]:
                    with open(output_file, "wb") as f:
                        f.write(base64.b64decode(imgs[0]))
                    print(f"Saved {output_file} in {time.time()-t0:.2f}s ({os.path.getsize(output_file)} bytes)")
                    return True
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}. Retrying in 5s...")
            time.sleep(5)
    return False

def combine_4koma(panel_files, final_output_path):
    print("Combining 4 panels into a vertical 4-koma manga...")
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
    print(f"Combined 4-koma saved successfully: {final_output_path} ({manga_img.size})")

if __name__ == "__main__":
    panel_files = []
    for cfg in panels_config:
        print(f"\n--- Processing Panel {cfg['panel_num']}: {cfg['name']} ---")
        ok = generate_panel(cfg["prompt"], cfg["file"])
        if not ok:
            print(f"Warning: Failed to generate panel {cfg['panel_num']}")
        panel_files.append(cfg["file"])
        
    out_illust = os.path.join(BASE_DIR, "content", "illustrations", "ep03_4koma.png")
    docs_illust = os.path.join(BASE_DIR, "docs", "assets", "images", "ep03_4koma.png")
    
    combine_4koma(panel_files, out_illust)
    
    import shutil
    shutil.copy2(out_illust, docs_illust)
    shutil.copy2(out_illust, r"C:\Users\k\.gemini\antigravity\brain\b164408c-44fc-48cc-9938-3c3604d5617b\ep03_4koma.png")
    print("EPISODE 03 4-KOMA REGENERATED WITH PERFECT EYES AND SAVED TO ALL ASSETS!")
