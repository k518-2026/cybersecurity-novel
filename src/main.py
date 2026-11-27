import argparse
import base64
import glob
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from PIL import Image, ImageDraw, ImageFont

JST = timezone(timedelta(hours=9))
logger = logging.getLogger("cybersecurity-novel")

DEFAULT_OLLAMA_HOSTS = [
    os.environ.get("OLLAMA_HOST", "").strip(),
    "http://rtx5060lp:11434",
    "http://192.168.128.62:11434",
]
DEFAULT_DRAW_THINGS_HOSTS = [
    os.environ.get("DRAW_THINGS_HOST", "").strip(),
    "http://kenomac-mini:7860",
    "http://192.168.128.59:7860",
]


def setup_logging(verbose: bool = False) -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )


def resolve_ollama() -> Tuple[Optional[str], List[str]]:
    for host in [h.rstrip("/") for h in DEFAULT_OLLAMA_HOSTS if h]:
        try:
            req = urllib.request.Request(f"{host}/api/tags", method="GET")
            with urllib.request.urlopen(req, timeout=6) as resp:
                data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                models = [m.get("name", "") for m in data.get("models", []) if m.get("name")]
                return host, models
        except Exception:
            continue
    return None, []


def resolve_draw_things() -> Tuple[Optional[str], str]:
    for host in [h.rstrip("/") for h in DEFAULT_DRAW_THINGS_HOSTS if h]:
        try:
            req = urllib.request.Request(f"{host}/sdapi/v1/options", method="GET")
            with urllib.request.urlopen(req, timeout=6) as resp:
                data = json.loads(resp.read().decode("utf-8", errors="ignore"))
                model = str(data.get("sd_model_checkpoint") or data.get("model") or "FLUX.2")
                return host, model
        except Exception:
            try:
                req2 = urllib.request.Request(f"{host}/", method="GET")
                with urllib.request.urlopen(req2, timeout=6) as resp2:
                    if resp2.status == 200:
                        return host, "DrawThings"
            except Exception:
                continue
    return None, ""


def call_ollama_chat(host: str, model: str, system_prompt: str, user_prompt: str, temperature: float = 0.7, num_predict: int = 3500) -> str:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": num_predict,
            "num_ctx": 8192,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(f"{host}/api/chat", data=data, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=600) as resp:
        body = json.loads(resp.read().decode("utf-8", errors="ignore"))
        content = body.get("message", {}).get("content", "")
        return re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()


def scan_existing_episodes(base_dir: Path) -> List[Dict[str, Any]]:
    content_dir = base_dir / "content"
    illust_dir = content_dir / "illustrations"
    fig_dir = content_dir / "figures"
    eps: List[Dict[str, Any]] = []
    for md_path in sorted(content_dir.glob("*_ep*.md")):
        m = re.search(r"_ep(\d+)_([a-zA-Z0-9_-]+)\.md$", md_path.name)
        if not m:
            continue
        ep_num = int(m.group(1))
        slug = m.group(2)
        txt = md_path.read_text(encoding="utf-8", errors="ignore")
        parts = txt.split("---")
        fm = parts[1] if len(parts) >= 3 else ""
        t_m = re.search(r'^title:\s*"?([^"\n]+)"?', fm, re.MULTILINE)
        th_m = re.search(r'^theme:\s*"?([^"\n]+)"?', fm, re.MULTILINE)
        cov_m = re.search(r'^cover_image:\s*"?([^"\n]+)"?', fm, re.MULTILINE)
        fig_m = re.search(r'^figure_image:\s*"?([^"\n]+)"?', fm, re.MULTILINE)
        cov_name = cov_m.group(1).strip() if cov_m else f"ep{ep_num:02d}_4koma.png"
        fig_name = fig_m.group(1).strip() if fig_m else f"fig{ep_num:02d}_{slug}.png"
        eps.append({
            "num": ep_num,
            "id": f"ep{ep_num:02d}",
            "slug": slug,
            "title": t_m.group(1).strip() if t_m else md_path.stem,
            "theme": th_m.group(1).strip() if th_m else "",
            "md_path": md_path,
            "illust_name": cov_name,
            "figure_name": fig_name,
            "has_illust": (illust_dir / cov_name).exists(),
            "has_figure": (fig_dir / fig_name).exists(),
        })
    eps.sort(key=lambda x: x["num"])
    return eps


def print_status_report(base_dir: Path) -> None:
    eps = scan_existing_episodes(base_dir)
    with_illust = sum(1 for e in eps if e["has_illust"])
    with_fig = sum(1 for e in eps if e["has_figure"])
    print("\n" + "=" * 78)
    print(" 【放課後サイバーディフェンス・ラボ（サイバーセキュリティ小説）公開＆蓄積状況】")
    print("=" * 78)
    print("  ・Webサイト (GitHub Pages) : https://k518-2026.github.io/cybersecurity-novel/")
    print(f"  ・公開済み総エピソード数   : {len(eps)} 話（4コマ漫画あり: {with_illust} 話 / 構造図解あり: {with_fig} 話）")
    if eps:
        print(f"  ・最新エピソード           : {eps[-1]['title']}")
        print("-" * 78)
        for e in eps[-8:]:
            i_mark = "🎨[4コマ有]" if e["has_illust"] else "  [4コマ無]"
            f_mark = "📊[図解有]" if e["has_figure"] else "  [図解無]"
            print(f"  [#{e['num']:02d}] {i_mark} {f_mark} {e['title']} -> {e['md_path'].name}")
    print("=" * 78 + "\n")


def _load_jp_font(size: int, bold: bool = True):
    candidates = (
        [r"C:\Windows\Fonts\BIZ-UDGothicB.ttc", r"C:\Windows\Fonts\YuGothB.ttc", r"C:\Windows\Fonts\meiryob.ttc"]
        if bold
        else [r"C:\Windows\Fonts\BIZ-UDGothicR.ttc", r"C:\Windows\Fonts\YuGothM.ttc", r"C:\Windows\Fonts\meiryo.ttc"]
    )
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size=size)
            except Exception:
                pass
    return ImageFont.load_default()


def render_clean_architecture_diagram(ep_num: int, title: str, nodes: List[Dict[str, str]], fig_path: Path, docs_img_dir: Path) -> None:
    """
    Renders a crisp, zero-overlap high-DPI cybersecurity architecture flowchart PNG (1400x760)
    so figures are guaranteed clean with zero broken arrows or text collisions.
    """
    w, h = 1400, 760
    img = Image.new("RGB", (w, h), (13, 20, 36))
    draw = ImageDraw.Draw(img)

    # Subtle grid
    for gx in range(0, w, 40):
        draw.line([(gx, 0), (gx, h)], fill=(22, 33, 56), width=1)
    for gy in range(0, h, 40):
        draw.line([(0, gy), (w, gy)], fill=(22, 33, 56), width=1)

    font_badge = _load_jp_font(20, bold=True)
    font_title = _load_jp_font(28, bold=True)
    font_box_title = _load_jp_font(22, bold=True)
    font_box_desc = _load_jp_font(17, bold=False)
    font_footer = _load_jp_font(16, bold=False)

    # Header bar
    draw.rounded_rectangle([36, 28, w - 36, 128], radius=16, fill=(24, 38, 66), outline=(56, 189, 248), width=2)
    draw.rounded_rectangle([58, 48, 250, 84], radius=8, fill=(2, 132, 199))
    draw.text((74, 54), f"EPISODE {ep_num:02d} 図解", font=font_badge, fill=(255, 255, 255))
    clean_t = re.sub(r"^第\s*\d+\s*話\s*", "", title).strip()
    if len(clean_t) > 36:
        clean_t = clean_t[:35] + "…"
    draw.text((272, 50), clean_t, font=font_title, fill=(248, 250, 252))
    draw.text((62, 94), "SPIRAL Security Architecture & Defense Verification Flow", font=font_footer, fill=(148, 163, 184))

    # 4 architecture stages arranged in 2x2 clean non-overlapping grid with clear directional arrows
    accents = [
        ((239, 68, 68), (58, 24, 34), "1. 脅威・攻撃ベクトル (Threat)"),
        ((245, 158, 11), (58, 42, 20), "2. 検証・境界制御 (Control)"),
        ((56, 189, 248), (18, 46, 68), "3. 暗号・数理防御機構 (Mechanism)"),
        ((34, 197, 94), (18, 54, 38), "4. 完全性保証・安全運用 (Assurance)"),
    ]
    coords = [
        (60, 175, 650, 415),
        (750, 175, 1340, 415),
        (60, 465, 650, 705),
        (750, 465, 1340, 705),
    ]

    def wrap_text(txt: str, max_chars: int = 26) -> List[str]:
        txt = re.sub(r"\s+", " ", txt).strip()
        return [txt[i : i + max_chars] for i in range(0, len(txt), max_chars)][:4]

    for i in range(4):
        x0, y0, x1, y1 = coords[i]
        border_col, bg_col, default_head = accents[i]
        node = nodes[i] if i < len(nodes) else {}
        n_title = node.get("title") or default_head
        n_desc = node.get("desc") or "多層防御と暗号学的検証によるゼロトラスト保護プロセス"

        draw.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=bg_col, outline=border_col, width=3)
        draw.rounded_rectangle([x0 + 18, y0 + 16, x1 - 18, y0 + 62], radius=8, fill=(15, 23, 42))
        draw.text((x0 + 30, y0 + 26), n_title[:24], font=font_box_title, fill=border_col)

        lines = wrap_text(n_desc, 27)
        cy = y0 + 84
        for ln in lines:
            draw.text((x0 + 30, cy), ln, font=font_box_desc, fill=(226, 232, 240))
            cy += 34

    # Clean non-overlapping arrows: 1 -> 2, 2 -> 3 (diagonal center channel), 3 -> 4
    # Arrow 1 -> 2
    draw.line([(654, 295), (744, 295)], fill=(56, 189, 248), width=5)
    draw.polygon([(748, 295), (730, 283), (730, 307)], fill=(56, 189, 248))
    # Center connector 2 -> 3 via clean middle corridor y=440
    draw.line([(1045, 418), (1045, 440), (355, 440), (355, 460)], fill=(56, 189, 248), width=4)
    draw.polygon([(355, 464), (344, 448), (366, 448)], fill=(56, 189, 248))
    # Arrow 3 -> 4
    draw.line([(654, 585), (744, 585)], fill=(34, 197, 94), width=5)
    draw.polygon([(748, 585), (730, 573), (730, 597)], fill=(34, 197, 94))

    fig_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(fig_path, "PNG", quality=95)
    docs_img_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(fig_path, docs_img_dir / fig_path.name)
    logger.info(f"Saved architecture diagram: {fig_path}")


def generate_4koma_illustration(dt_host: str, prompts: List[str], out_png: Path, docs_img_dir: Path) -> bool:
    """Generates a clean vertical 4-panel manga strip via Draw Things with gentle eye/eyebrow rules."""
    panel_dir = out_png.parent / "_panels_tmp"
    panel_dir.mkdir(parents=True, exist_ok=True)
    neg = (
        "speech bubble, dialogue bubble, text, words, letters, kanji, chinese characters, japanese text, typography, "
        "deformed eyes, asymmetrical eyes, winking, crossed eyes, weird gaze, creepy eyes, staring eyes, missing pupil, "
        "bad facial anatomy, deformed hands, blurry, dark gloom, watermark, logo"
    )
    style_tail = (
        ", masterpiece Japanese high school tech light novel anime style, bright clean laboratory lighting, "
        "beautiful detailed anime eyes with clear round pupils and iris catchlights, neat delicate thin eyebrows, "
        "soft relaxed eyelids, natural warm friendly expression, pure silent wordless illustration, NO text, NO speech bubbles"
    )

    panel_files: List[Path] = []
    for idx in range(4):
        scene_p = prompts[idx] if idx < len(prompts) else "Japanese high school cybersecurity club members smiling warmly in a bright modern computer lab"
        p_file = panel_dir / f"{out_png.stem}_p{idx + 1}.png"
        payload = {
            "prompt": scene_p.strip().rstrip(".") + style_tail,
            "negative_prompt": neg,
            "width": 512,
            "height": 512,
            "steps": 14,
            "guidance_scale": 4.0,
            "sampler": "Euler A Trailing",
        }
        req = urllib.request.Request(
            f"{dt_host}/sdapi/v1/txt2img",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        ok = False
        for attempt in range(1, 3):
            try:
                logger.info(f"[Draw Things] Rendering panel {idx + 1}/4 for {out_png.name} (attempt {attempt})...")
                with urllib.request.urlopen(req, timeout=600) as resp:
                    body = json.loads(resp.read().decode("utf-8", errors="ignore"))
                    imgs = body.get("images", [])
                    if imgs and imgs[0]:
                        b64 = re.sub(r"^data:image/[^;]+;base64,", "", imgs[0])
                        p_file.write_bytes(base64.b64decode(b64))
                        panel_files.append(p_file)
                        ok = True
                        break
            except Exception as e:
                logger.warning(f"Panel {idx + 1} attempt {attempt} failed: {e}")
                time.sleep(3)
        if not ok:
            return False

    # Combine 4 panels vertically with crisp manga borders
    panel_w, panel_h = 512, 512
    margin_x, margin_top, margin_between, border_w = 24, 28, 24, 4
    canvas_w = panel_w + margin_x * 2
    canvas_h = margin_top * 2 + panel_h * 4 + margin_between * 3
    canvas = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    cy = margin_top
    for pf in panel_files:
        p_img = Image.open(pf).convert("RGB").resize((panel_w, panel_h), Image.Resampling.LANCZOS)
        draw.rectangle([margin_x - border_w, cy - border_w, margin_x + panel_w + border_w - 1, cy + panel_h + border_w - 1], fill=(20, 25, 35))
        canvas.paste(p_img, (margin_x, cy))
        cy += panel_h + margin_between
        try:
            pf.unlink()
        except Exception:
            pass

    out_png.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_png, "PNG", quality=95)
    docs_img_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out_png, docs_img_dir / out_png.name)
    logger.info(f"Saved combined 4-koma illustration: {out_png}")
    return True


def plan_new_episodes(ollama_host: str, planner_model: str, existing_eps: List[Dict[str, Any]], count: int) -> List[Dict[str, Any]]:
    next_num = (max([e["num"] for e in existing_eps]) + 1) if existing_eps else 1
    recent_themes = "\n".join([f"- 第{e['num']}話: {e['title']} ({e['theme'][:60]})" for e in existing_eps[-25:]])
    user_prompt = f"""『放課後サイバーディフェンス・ラボ』（登場人物：城崎悠真・橘葵・神崎蓮・白石結衣）の新作エピソード企画を **{count} 話分**（第{next_num}話〜第{next_num + count - 1}話）作成し、純粋なJSON配列のみで出力してください。

【既存エピソード（これらと重複しない最新・高度なサイバーセキュリティ／暗号数理／AI・クラウド・ハードウェア防衛テーマを選ぶこと）】
{recent_themes}

【出力JSONスキーマ（配列のみ出力・前後の説明不要）】
[
  {{
    "episode_num": {next_num},
    "slug": "english_snake_case_slug",
    "category": "ai_security または crypto または cloud_security または network_security または hardware_security",
    "title": "詩的な副題 〜具体的なセキュリティ技術名〜",
    "theme": "扱う主要技術キーワード5〜7個（カンマ区切り）",
    "panel_prompts": [
      "Panel 1 English scene description:葵 and 結衣 looking at a security alert monitor in a sunlit university lab",
      "Panel 2 English scene description:悠真 explaining cryptographic or security architecture on a glowing holographic display",
      "Panel 3 English scene description:蓮 and 結衣 running defense verification code with green checkmarks on screen",
      "Panel 4 English scene description:All four club members smiling warmly together in celebration in the bright lab"
    ],
    "diagram_nodes": [
      {{"title": "1. 脅威・攻撃手法", "desc": "具体的な攻撃メカニズムの要約（45文字以内）"}},
      {{"title": "2. 検知・境界検証", "desc": "異常検知・ポリシー制御の要約（45文字以内）"}},
      {{"title": "3. 暗号・防御コア技術", "desc": "中核となる数理・システム防御技術（45文字以内）"}},
      {{"title": "4. 安全性の保証・運用", "desc": "検証完了とゼロトラスト運用の効果（45文字以内）"}}
    ]
  }}
]"""
    raw = call_ollama_chat(
        host=ollama_host,
        model=planner_model,
        system_prompt="You output strictly valid JSON arrays only. No markdown code fences.",
        user_prompt=user_prompt,
        temperature=0.7,
        num_predict=2800,
    )
    m = re.search(r"\[\s*\{.*\}\s*\]", raw, flags=re.DOTALL)
    cleaned = m.group(0) if m else raw
    items = json.loads(cleaned, strict=False)
    planned: List[Dict[str, Any]] = []
    for idx, it in enumerate(items[:count]):
        ep_n = next_num + idx
        slug = re.sub(r"[^a-z0-9_]+", "_", str(it.get("slug", f"cyber_defense_{ep_n}")).lower()).strip("_") or f"cyber_defense_{ep_n}"
        it["episode_num"] = ep_n
        it["slug"] = slug
        planned.append(it)
    return planned


def write_episode_markdown(ollama_host: str, writer_model: str, planner_model: str, plan: Dict[str, Any], out_md: Path) -> None:
    ep_num = plan["episode_num"]
    slug = plan["slug"]
    raw_title = re.sub(r"^第\s*\d+\s*話\s*", "", str(plan.get("title", "")).strip())
    full_title = f"第{ep_num}話 {raw_title}"
    theme = str(plan.get("theme", "先端サイバーセキュリティ"))
    category = str(plan.get("category", "ai_security"))

    story_prompt = f"""以下の企画に基づき、『放課後サイバーディフェンス・ラボ』第{ep_num}話の小説本文・4コマセリフ表・高校生向け深掘りコラムを執筆してください。

- タイトル: {full_title}
- テーマ: {theme}
- 登場人物:
  - 城崎 悠真（横浜国大1年 / SPIRAL学生研究員 / TA・頼れる理論派メンター）
  - 橘 葵（高校3年 / 元情報科学部部長・洞察力と倫理観に優れたヒロイン）
  - 神崎 蓮（高校1年 / IoT・システム実装班・元気な実践派）
  - 白石 結衣（高校1年 / 暗号数理班・数理と論理に強いクールで優しい後輩）

【厳守する出力構成（見出しを正確に一致させること）】
## 💬 4コマ漫画キャラクターセリフ（日・英対訳）
| コマ | シチュエーション | 日本語セリフ | English Dialogue |
| :--- | :--- | :--- | :--- |
| **1コマ目（起）** | 導入場面の描写 | **葵**: 「…」<br>**結衣**: 「…」 | **Aoi**: "..."<br>**Yui**: "..." |
| **2コマ目（承）** | 原因分析場面 | **悠真**: 「…」 | **Yuma**: "..." |
| **3コマ目（転）** | 防御実装・検証場面 | **蓮**: 「…」<br>**結衣**: 「…」 | **Ren**: "..."<br>**Yui**: "..." |
| **4コマ目（結）** | 解決と未来への展望 | **葵**: 「…」<br>**悠真**: 「…」 | **Aoi**: "..."<br>**Yuma**: "..." |

## 📖 小説本文
（ここに3,000〜4,000文字程度で、緊迫感あるサイバー事案の導入、数理・アーキテクチャの丁寧な解明、検証コマンドや防御実装による解決、温かいエピローグを小説として豊かに描くこと。シーン区切りは `* * *` を使用）

## 💡 高校生のためのセキュリティ深掘りコラム
### 1. 今回の脅威と背景メカニズム
（わかりやすく解説）
### 2. 防御アーキテクチャと数理・技術ポイント
（箇条書きを交えて解説）
### 3. 私たちが今日から実践できるセキュリティの視点
（進路や実践のヒントを解説）"""

    active_writer = writer_model if writer_model else planner_model
    body = call_ollama_chat(
        host=ollama_host,
        model=active_writer,
        system_prompt="あなたは情報セキュリティと暗号数理に精通した青春ライトノベル作家です。正確でわかりやすくドラマチックな日本語で執筆してください。",
        user_prompt=story_prompt,
        temperature=0.72,
        num_predict=4500,
    )

    safe_title = full_title.replace('"', '\\"')
    safe_theme = theme.replace('"', '\\"')
    frontmatter = f"""---
title: "{safe_title}"
episode: {ep_num}
arc: 2
category: "{category}"
theme: "{safe_theme}"
characters:
  - name: "城崎 悠真"
    role: "横浜国大1年 / SPIRAL学生研究員 / TA"
  - name: "橘 葵"
    role: "高校3年 / 元情報科学部部長"
  - name: "神崎 蓮"
    role: "高校1年 / 情報科学部（IoT・ハード班）"
  - name: "白石 結衣"
    role: "高校1年 / 情報科学部（暗号数理班）"
cover_image: "ep{ep_num:02d}_4koma.png"
figure_image: "fig{ep_num:02d}_{slug}.png"
---

"""
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(frontmatter + body.strip() + "\n", encoding="utf-8")
    logger.info(f"Saved episode Markdown: {out_md} ({len(body)} chars)")


def rebuild_pages(base_dir: Path) -> None:
    logger.info("Rebuilding GitHub Pages (docs/) via src/build_site.py...")
    subprocess.run([sys.executable, str(base_dir / "src" / "build_site.py")], cwd=str(base_dir), check=True)


def git_sync_and_push(base_dir: Path, count_label: str) -> bool:
    try:
        subprocess.run(["git", "add", "content/", "docs/", "src/build_site.py"], cwd=str(base_dir), check=True)
        diff = subprocess.run(["git", "diff", "--staged", "--quiet"], cwd=str(base_dir))
        if diff.returncode == 0:
            logger.info("No staged changes to commit.")
            return True
        subprocess.run(
            ["git", "commit", "-m", f"feat(episodes): Add {count_label} cybersecurity novel episode(s) & update GitHub Pages"],
            cwd=str(base_dir),
            check=True,
        )
        git_env = {**os.environ, "GIT_EDITOR": "true"}
        subprocess.run(["git", "fetch", "origin", "main"], cwd=str(base_dir), check=False, env=git_env)
        subprocess.run(["git", "merge", "--no-edit", "-X", "ours", "origin/main"], cwd=str(base_dir), check=False, env=git_env)
        subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=str(base_dir), check=True)
        logger.info("Successfully pushed cybersecurity novel assets & docs/ to origin/main!")
        return True
    except Exception as e:
        logger.error(f"Git sync/push failed: {e}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Cybersecurity Novel Autonomous Orchestrator (Ollama + Draw Things + GitHub Pages)")
    parser.add_argument("-n", "--stock-count", type=int, default=0, help="Generate N new cybersecurity novel episodes")
    parser.add_argument("--work-id", default=None, help="Target episode ID (e.g., ep87 or 87) for image regeneration")
    parser.add_argument("--generate-images", action="store_true", help="Generate or replace 4-koma / figure images")
    parser.add_argument("--build-pages", action="store_true", help="Rebuild GitHub Pages (docs/)")
    parser.add_argument("--status-report", action="store_true", help="Show current episode & asset status")
    parser.add_argument("--push", action="store_true", help="Commit and push changes to origin/main")
    parser.add_argument("--force", action="store_true", help="Force overwrite when regenerating images")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose logging")
    args = parser.parse_args()

    setup_logging(args.verbose)
    base_dir = Path(__file__).resolve().parent.parent
    docs_img_dir = base_dir / "docs" / "assets" / "images"

    if args.status_report:
        print_status_report(base_dir)
        return

    if args.build_pages:
        rebuild_pages(base_dir)
        if args.push:
            git_sync_and_push(base_dir, "rebuilt")
        print_status_report(base_dir)
        return

    if args.generate_images:
        dt_host, dt_model = resolve_draw_things()
        if not dt_host:
            logger.error("Draw Things server is offline or unreachable.")
            sys.exit(1)
        logger.info(f"Draw Things online: {dt_host} ({dt_model})")
        eps = scan_existing_episodes(base_dir)
        target_norm = str(args.work_id).strip().lower() if args.work_id else None
        updated = 0
        for e in eps:
            if target_norm and target_norm not in (e["id"].lower(), str(e["num"]), e["md_path"].stem.lower()):
                continue
            illust_path = base_dir / "content" / "illustrations" / e["illust_name"]
            if not illust_path.exists() or args.force:
                ok = generate_4koma_illustration(
                    dt_host=dt_host,
                    prompts=[
                        f"Japanese high school girl Aoi and Yui in a sunlit cybersecurity lab investigating {e['slug'].replace('_', ' ')}",
                        "University mentor Yuma explaining cryptographic network defense on a glowing monitor",
                        "High school boy Ren and girl Yui verifying green security checkmarks on terminal screens",
                        "All four club members smiling warmly together in the bright university research lab",
                    ],
                    out_png=illust_path,
                    docs_img_dir=docs_img_dir,
                )
                if ok:
                    updated += 1
        if updated > 0:
            rebuild_pages(base_dir)
            if args.push:
                git_sync_and_push(base_dir, f"{updated} updated image")
        print_status_report(base_dir)
        return

    if args.stock_count > 0:
        if args.push:
            git_env = {**os.environ, "GIT_EDITOR": "true"}
            subprocess.run(["git", "fetch", "origin", "main"], cwd=str(base_dir), check=False, env=git_env)
            subprocess.run(["git", "merge", "--no-edit", "-X", "ours", "origin/main"], cwd=str(base_dir), check=False, env=git_env)

        ollama_host, models = resolve_ollama()
        if not ollama_host:
            logger.error("Ollama server is offline or unreachable.")
            sys.exit(1)
        dt_host, dt_model = resolve_draw_things()
        if not dt_host:
            logger.error("Draw Things server is offline or unreachable.")
            sys.exit(1)

        planner_model = "qwen3.5:9b" if "qwen3.5:9b" in models else (models[0] if models else "qwen3.5:9b")
        writer_model = "qwen3.5:9b" if "qwen3.5:9b" in models else ("shosetsu:latest" if "shosetsu:latest" in models else planner_model)
        logger.info(f"Servers OK | Ollama: {ollama_host} (planner={planner_model}, writer={writer_model}) | DrawThings: {dt_host} ({dt_model})")

        existing_eps = scan_existing_episodes(base_dir)
        plans = plan_new_episodes(ollama_host, planner_model, existing_eps, args.stock_count)
        today_str = datetime.now(JST).strftime("%Y-%m-%d")

        for idx, plan in enumerate(plans, start=1):
            ep_num = plan["episode_num"]
            slug = plan["slug"]
            logger.info(f"\n=== [{idx}/{len(plans)}] Generating Episode #{ep_num:02d}: {plan.get('title')} ===")
            out_md = base_dir / "content" / f"{today_str}_ep{ep_num:02d}_{slug}.md"
            write_episode_markdown(ollama_host, writer_model, planner_model, plan, out_md)

            fig_path = base_dir / "content" / "figures" / f"fig{ep_num:02d}_{slug}.png"
            render_clean_architecture_diagram(
                ep_num=ep_num,
                title=str(plan.get("title", "")),
                nodes=plan.get("diagram_nodes") or [],
                fig_path=fig_path,
                docs_img_dir=docs_img_dir,
            )

            illust_path = base_dir / "content" / "illustrations" / f"ep{ep_num:02d}_4koma.png"
            generate_4koma_illustration(
                dt_host=dt_host,
                prompts=plan.get("panel_prompts") or [],
                out_png=illust_path,
                docs_img_dir=docs_img_dir,
            )

            rebuild_pages(base_dir)
            if args.push:
                git_sync_and_push(base_dir, f"ep{ep_num:02d}")

        print_status_report(base_dir)
        return

    print_status_report(base_dir)


if __name__ == "__main__":
    main()
