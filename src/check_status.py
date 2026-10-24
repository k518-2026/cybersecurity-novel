import glob
import re

for path in sorted(glob.glob("content/2026*.md")):
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    m_title = re.search(r'title:\s*"([^"]+)"', c)
    title = m_title.group(1) if m_title else path
    has_script = "## 💬 4コマ漫画キャラクターセリフ" in c
    has_4koma = bool(re.search(r"ep\d+_4koma\.png", c))
    print(f"{path[-35:]} | 4koma_img: {has_4koma} | script: {has_script} | {title}")
