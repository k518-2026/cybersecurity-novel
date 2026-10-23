import os
import json
import subprocess
import urllib.request
import re
import base64
import time

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
CONTENT_DIR = os.path.join(BASE_DIR, "content")
FIG_DIR = os.path.join(CONTENT_DIR, "figures")
ILLUST_DIR = os.path.join(CONTENT_DIR, "illustrations")

os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(ILLUST_DIR, exist_ok=True)

OLLAMA_URL = "http://192.168.128.62:11434/api/generate"
DRAW_THINGS_URL = "http://192.168.128.59:7860/sdapi/v1/txt2img"

def call_ollama(model: str, prompt: str, timeout: int = 300) -> str:
    data = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode("utf-8")
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as res:
        res_json = json.loads(res.read().decode("utf-8"))
        return res_json.get("response", "")

def render_tikz(tex_content: str, base_name: str) -> str:
    tex_path = os.path.join(FIG_DIR, f"{base_name}.tex")
    pdf_path = os.path.join(FIG_DIR, f"{base_name}.pdf")
    png_path = os.path.join(FIG_DIR, f"{base_name}.png")
    render_prefix = os.path.join(FIG_DIR, f"{base_name}_render")

    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)

    print(f"[{base_name}] Compiling TikZ with lualatex...")
    res = subprocess.run(["lualatex", "-interaction=nonstopmode", f"{base_name}.tex"], cwd=FIG_DIR, capture_output=True)
    if res.returncode != 0:
        print(f"[{base_name}] lualatex warning/error code:", res.returncode)

    if os.path.exists(pdf_path):
        subprocess.run(["pdftoppm", "-png", "-r", "180", f"{base_name}.pdf", f"{base_name}_render"], cwd=FIG_DIR, capture_output=True)
        rendered_1 = os.path.join(FIG_DIR, f"{base_name}_render-1.png")
        if os.path.exists(rendered_1):
            if os.path.exists(png_path):
                os.remove(png_path)
            os.rename(rendered_1, png_path)
            print(f"[{base_name}] Successfully created figure: {png_path}")
            return png_path
    print(f"[{base_name}] Failed to generate PNG from TikZ!")
    return ""

def generate_drawthings_image(prompt: str, output_path: str, timeout: int = 900) -> bool:
    payload = {
        "prompt": prompt,
        "negative_prompt": "speech bubble, dialogue bubble, text, words, letters, kanji, chinese characters, japanese text, typography, deformed eyes, blurry, gloomy, hat",
        "width": 512,
        "height": 1024,
        "steps": 8,
        "guidance_scale": 3.5,
        "sampler": "Euler A Trailing"
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(DRAW_THINGS_URL, data=data, headers={"Content-Type": "application/json"})
    print(f"Sending prompt to Draw Things: {output_path}...")
    for attempt in range(1, 3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as res:
                body = json.loads(res.read().decode("utf-8"))
                imgs = body.get("images", [])
                if imgs and imgs[0]:
                    b64 = re.sub(r"^data:image/[^;]+;base64,", "", imgs[0])
                    with open(output_path, "wb") as f:
                        f.write(base64.b64decode(b64))
                    print(f"SUCCESS: Saved illustration: {output_path}")
                    return True
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}. Retrying in 5s...")
            time.sleep(5)
    return False

print("Helper functions ready.")
