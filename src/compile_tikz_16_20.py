import os
import subprocess
import shutil

figs = [
    'fig16_iot_security_mirai',
    'fig17_zero_trust_architecture',
    'fig18_hardware_and_side_channel',
    'fig19_privacy_enhancing_tech',
    'fig20_ot_scada_automotive'
]

DOCS_IMG_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel\docs\assets\images"

for fig in figs:
    tex_path = f"content/figures/{fig}.tex"
    pdf_path = f"content/figures/{fig}.pdf"
    page1_png = f"content/figures/{fig}_page-1.png"
    target_png = f"content/figures/{fig}.png"
    docs_png = os.path.join(DOCS_IMG_DIR, f"{fig}.png")

    print(f"Compiling {tex_path}...")
    res = subprocess.run(
        ["lualatex", "--output-directory=content/figures", tex_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if res.returncode == 0 and os.path.exists(pdf_path):
        print(f"  Compiled PDF. Converting to PNG...")
        subprocess.run(
            ["pdftoppm", "-png", "-r", "200", pdf_path, f"content/figures/{fig}_page"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if os.path.exists(page1_png):
            shutil.copy2(page1_png, target_png)
            shutil.copy2(target_png, docs_png)
            print(f"  Successfully deployed {fig}.png!")
        else:
            print(f"  Warning: {page1_png} not found.")
    else:
        print(f"  Error compiling {tex_path}")

print("ALL TIKZ FIGURES 16-20 COMPILED AND DEPLOYED!")
