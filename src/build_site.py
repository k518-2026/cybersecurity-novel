import os
import re
import glob
import shutil
import html

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
CONTENT_DIR = os.path.join(BASE_DIR, "content")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
STORIES_DIR = os.path.join(DOCS_DIR, "stories")
IMAGES_DIR = os.path.join(DOCS_DIR, "assets", "images")

os.makedirs(STORIES_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# Copy all images
for p in glob.glob(os.path.join(CONTENT_DIR, "figures", "*.png")):
    shutil.copy2(p, IMAGES_DIR)
for p in glob.glob(os.path.join(CONTENT_DIR, "illustrations", "*.png")):
    shutil.copy2(p, IMAGES_DIR)

episodes = [
    {
        "num": 1,
        "id": "ep01",
        "title": "秘密の合言葉と見えない鍵 〜パスワード認証と多要素認証の仕組み〜",
        "theme": "認証の3要素（知識・所持・生体）、多要素認証（MFA）、アカウントリスト攻撃",
        "md_file": "2026-10-23_ep01_passwords_and_authentication.md",
        "illust": "ep01_4koma.png",
        "figure": "fig01_mfa_principles.png"
    },
    {
        "num": 2,
        "id": "ep02",
        "title": "偽りの手紙と本物の目印 〜フィッシング詐欺の見抜き方とURLの秘密〜",
        "theme": "スミッシング、ソーシャルエンジニアリング、URL階層構造、電子証明書（HTTPS）の真実",
        "md_file": "2026-10-23_ep02_phishing_and_social_engineering.md",
        "illust": "ep02_4koma.png",
        "figure": "fig02_phishing_domain_structure.png"
    },
    {
        "num": 3,
        "id": "ep03",
        "title": "街角の電波は誰のもの？ 〜公衆無線LANの危険性と通信の暗号化（HTTPS）〜",
        "theme": "フリーWi-Fi、盗聴と中間者攻撃（MitM）、TLS暗号化トンネル、VPN",
        "md_file": "2026-10-23_ep03_free_wifi_and_encryption.md",
        "illust": "ep03_4koma.png",
        "figure": "fig03_wifi_mitm_encryption_tunnel.png"
    },
    {
        "num": 4,
        "id": "ep04",
        "title": "忍び寄るトロイの木馬 〜マルウェアの種類とソフトウェア更新の真実〜",
        "theme": "マルウェア4分類（ウイルス・ワーム・トロイ・ランサムウェア）、脆弱性とパッチ適用",
        "md_file": "2026-10-23_ep04_malware_and_vulnerabilities.md",
        "illust": "ep04_4koma.png",
        "figure": "fig04_malware_vulnerability_patch.png"
    },
    {
        "num": 5,
        "id": "ep05",
        "title": "三つの宝珠を守る城壁 〜情報セキュリティの3大要素（CIA）と多層防御〜",
        "theme": "CIA（機密性・完全性・可用性）、DDoS攻撃、多層防御の同心円モデル",
        "md_file": "2026-10-23_ep05_cia_triad_and_defense_in_depth.md",
        "illust": "ep05_art.png",
        "figure": "fig05_cia_and_defense_in_depth.png"
    },
    {
        "num": 6,
        "id": "ep06",
        "title": "データベースの合言葉と呪文の罠 〜SQLインジェクションと安全なプログラミング〜",
        "theme": "SQLインジェクション攻撃、文字列連結の脆弱性、プレースホルダ（バインド機構）",
        "md_file": "2026-10-23_ep06_sql_injection_and_web_security.md",
        "illust": "ep06_art.png",
        "figure": "fig06_sql_injection_defense.png"
    },
    {
        "num": 7,
        "id": "ep07",
        "title": "割れない南京錠と魔法の印鑑 〜公開鍵暗号とデジタル署名の数理〜",
        "theme": "鍵配送問題、公開鍵暗号の鍵ペア、デジタル署名（電子署名）、SHA-256ハッシュ関数",
        "md_file": "2026-10-23_ep07_cryptography_and_digital_signatures.md",
        "illust": "ep07_art.png",
        "figure": "fig07_digital_signature_pki.png"
    },
    {
        "num": 8,
        "id": "ep08",
        "title": "覚えない合言葉と手のひらの証明 〜パスキー（FIDO2）とパスワードのない未来〜",
        "theme": "パスキー（FIDO2/WebAuthn）、端末セキュアエレメント、チャレンジ＆レスポンス、フィッシング耐性",
        "md_file": "2026-10-24_ep08_passkey_and_fido2_passwordless.md",
        "illust": "ep08_art.png",
        "figure": "fig08_passkey_fido2_architecture.png"
    },
    {
        "num": 9,
        "id": "ep09",
        "title": "見えない裏口と材料の目録 〜サプライチェーン攻撃とソフトウェアの原材料表示〜",
        "theme": "サプライチェーン攻撃（委託先経由侵害）、国家サイバー統括室要請、SBOM（ソフトウェア部品構成表）、CISA",
        "md_file": "2026-10-24_ep09_supply_chain_attack_and_sbom.md",
        "illust": "ep09_art.png",
        "figure": "fig09_supply_chain_sbom.png"
    },
    {
        "num": 10,
        "id": "ep10",
        "title": "ゼロの日を越える翼 〜ゼロデイ脆弱性と世界を守るホワイトハッカー〜",
        "theme": "ゼロデイ攻撃（0-day）、協調的脆弱性開示（CVD）、CVE/CVSS、米CISA KEV、ホワイトハッカー倫理",
        "md_file": "2026-10-24_ep10_zero_day_and_white_hackers.md",
        "illust": "ep10_art.png",
        "figure": "fig10_zero_day_coordinated_disclosure.png"
    }
]

def parse_markdown(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    parts = text.split("---", 2)
    body = parts[2] if len(parts) >= 3 else text

    novel_match = re.search(r"## 📖 小説本文\s*(.*?)\s*## 📊 TikZ", body, re.DOTALL)
    novel_text = novel_match.group(1).strip() if novel_match else ""

    col_match = re.search(r"## 💡 高校生のためのセキュリティ深掘りコラム\s*(.*)$", body, re.DOTALL)
    col_text = col_match.group(1).strip() if col_match else ""

    meta_match = re.search(r"> \*\*【放課後サイバーディフェンス・ラボ】\*\*\s*(.*?)\s*---", body, re.DOTALL)
    meta_text = meta_match.group(1).strip() if meta_match else ""

    return meta_text, novel_text, col_text

def format_novel_paragraphs(text):
    paras = text.split("\n\n")
    html_out = []
    for p in paras:
        p = p.strip()
        if not p:
            continue
        if "* * *" in p or "＊＊＊" in p or "---" in p:
            html_out.append('<div class="scene-divider">✦ ✦ ✦</div>')
        else:
            lines = p.split("\n")
            p_clean = "<br>".join([html.escape(l) for l in lines if l.strip()])
            html_out.append(f"<p>{p_clean}</p>")
    return "\n".join(html_out)

def format_column_markdown(text):
    lines = text.split("\n")
    html_out = []
    in_list = False
    for line in lines:
        line_s = line.strip()
        if line_s.startswith("### "):
            if in_list: html_out.append("</ul>"); in_list = False
            html_out.append(f"<h3>{html.escape(line_s[4:])}</h3>")
        elif line_s.startswith("- ") or line_s.startswith("* "):
            if not in_list: html_out.append("<ul>"); in_list = True
            l_body = line_s[2:]
            l_body = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", l_body)
            html_out.append(f"<li>{l_body}</li>")
        elif line_s.startswith("1. ") or line_s.startswith("2. ") or line_s.startswith("3. ") or line_s.startswith("4. "):
            if not in_list: html_out.append("<ol>"); in_list = True
            l_body = line_s[3:]
            l_body = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", l_body)
            html_out.append(f"<li>{l_body}</li>")
        elif line_s == "":
            if in_list: html_out.append("</ul>"); in_list = False
        else:
            if in_list: html_out.append("</ul>"); in_list = False
            l_body = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html.escape(line_s))
            html_out.append(f"<p>{l_body}</p>")
    if in_list: html_out.append("</ul>")
    return "\n".join(html_out)

# Build Story Detail Pages
for ep in episodes:
    md_path = os.path.join(CONTENT_DIR, ep["md_file"])
    if not os.path.exists(md_path):
        continue
    meta_txt, novel_txt, col_txt = parse_markdown(md_path)
    novel_html = format_novel_paragraphs(novel_txt)
    col_html = format_column_markdown(col_txt)

    meta_lines = [l.replace("> -", "").replace(">", "").strip() for l in meta_txt.split("\n") if l.strip()]
    meta_html = "<br>".join([re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", l) for l in meta_lines])

    story_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>第{ep['num']:02d}話 {html.escape(ep['title'])} | 放課後サイバーディフェンス・ラボ</title>
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Shippori+Mincho:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>

  <header class="site-header">
    <div class="site-title">放課後サイバーディフェンス・ラボ</div>
    <div class="site-subtitle">〜高校生からはじめるサイバーセキュリティと大学情報科学の扉〜</div>
    <div class="nav-badges">
      <span class="badge">IPA デジタルスキル標準 (DSS) 準拠</span>
      <span class="badge">国家サイバー統括室 (cyber.go.jp) 啓発方針</span>
      <span class="badge">デジタル庁・総務省ガイドライン</span>
      <span class="badge">米CISA / 国際セキュリティ基準</span>
    </div>
  </header>

  <main class="container">
    <a href="../index.html" class="back-link">← エピソード一覧に戻る</a>

    <article class="story-article">
      <div class="story-header">
        <div class="story-ep-num">Episode {ep['num']:02d}</div>
        <h1 class="story-title">{html.escape(ep['title'])}</h1>
        <div class="story-meta-box">
          {meta_html}
        </div>
      </div>

      <div class="art-center">
        <img src="../assets/images/{ep['illust']}" alt="第{ep['num']:02d}話 ストーリーイラスト" loading="lazy">
      </div>

      <div class="novel-body">
        {novel_html}
      </div>

      <div class="art-center">
        <h2 style="font-size: 1.4rem; color: var(--secondary); margin-bottom: 1.2rem;">📊 TikZ セキュリティ構造図解</h2>
        <img src="../assets/images/{ep['figure']}" alt="第{ep['num']:02d}話 セキュリティ構造図" loading="lazy">
      </div>

      <div class="column-box">
        <h2>💡 高校生のためのセキュリティ深掘りコラム</h2>
        {col_html}
      </div>

      <div style="text-align: center; margin-top: 3rem;">
        <a href="../index.html" class="card-btn" style="padding: 0.8rem 2rem;">エピソード一覧に戻る</a>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <p>© 2026 放課後サイバーディフェンス・ラボ (Cybersecurity Novel Library)</p>
    <p>Repository: <a href="https://github.com/k518-2026/cybersecurity-novel" target="_blank" rel="noopener" style="color: var(--primary);">k518-2026/cybersecurity-novel</a></p>
  </footer>

</body>
</html>
"""
    out_html = os.path.join(STORIES_DIR, f"{ep['id']}.html")
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(story_html)
    print("Created story page:", out_html)

# Build Top Index Page (docs/index.html)
cards_html = []
for ep in episodes:
    card = f"""
    <div class="card">
      <img src="assets/images/{ep['illust']}" alt="第{ep['num']:02d}話 挿絵" class="card-thumb" loading="lazy">
      <div class="card-body">
        <div class="card-ep">Episode {ep['num']:02d}</div>
        <h2 class="card-title">{html.escape(ep['title'])}</h2>
        <p class="card-theme"><strong>学習テーマ:</strong> {html.escape(ep['theme'])}</p>
        <a href="stories/{ep['id']}.html" class="card-btn">小説と図解を読む →</a>
      </div>
    </div>
    """
    cards_html.append(card)

index_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>放課後サイバーディフェンス・ラボ 〜高校生からはじめるサイバーセキュリティと大学情報科学の扉〜</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Shippori+Mincho:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>

  <header class="site-header">
    <div class="site-title">放課後サイバーディフェンス・ラボ</div>
    <div class="site-subtitle">〜高校生からはじめるサイバーセキュリティと大学情報科学の扉〜</div>
    <div class="nav-badges">
      <span class="badge">IPA デジタルスキル標準 (DSS) 準拠</span>
      <span class="badge">国家サイバー統括室 (cyber.go.jp) 啓発方針</span>
      <span class="badge">デジタル庁・総務省ガイドライン</span>
      <span class="badge">米CISA / 国際セキュリティ基準</span>
      <span class="badge">大学情報科学・工学進学ガイド</span>
    </div>
  </header>

  <main class="container">
    <section style="background: white; border-radius: 1rem; padding: 2rem; margin-bottom: 2.5rem; border: 1px solid var(--border-color); box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
      <h2 style="font-size: 1.4rem; color: var(--secondary); margin-bottom: 0.8rem;">🛡️ このライブラリについて</h2>
      <p style="color: #475569; font-size: 0.98rem; line-height: 1.8;">
        高校生がサイバーセキュリティの面白さや重要性に触れ、将来の情報科学系・工学系大学への進学やセキュリティ専門職を目指すための入門ライトノベルです。<br>
        男子高校生（城崎 悠真 部長）と女子高校生（橘 葵）が、国内外の最新サイバー脅威ニュースや政府機関（デジタル庁・国家サイバー統括室・米CISA等）の公式情報を題材に、大学の芹沢 涼香 准教授と共にセキュリティの仕組みを優しく・正確に探求していきます。
      </p>
    </section>

    <h2 style="font-size: 1.5rem; color: var(--secondary); margin-bottom: 1.5rem; border-left: 4px solid var(--primary); padding-left: 0.8rem;">📚 収録エピソード一覧（全10話）</h2>

    <div class="episodes-grid">
      {''.join(cards_html)}
    </div>
  </main>

  <footer class="site-footer">
    <p>© 2026 放課後サイバーディフェンス・ラボ (Cybersecurity Novel Library)</p>
    <p>Repository: <a href="https://github.com/k518-2026/cybersecurity-novel" target="_blank" rel="noopener" style="color: var(--primary);">k518-2026/cybersecurity-novel</a></p>
  </footer>

</body>
</html>
"""

index_path = os.path.join(DOCS_DIR, "index.html")
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
print("Updated top index page for all 10 episodes:", index_path)
