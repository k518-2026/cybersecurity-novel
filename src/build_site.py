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
        "title": "秘密の合言葉と見えない壁 〜パスワード認証と多要素認証の仕組み〜",
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
        "title": "三つの宝玉を守る城壁 〜情報セキュリティの3大要素（CIA）と多層防御〜",
        "theme": "CIA（機密性・完全性・可用性）、DDoS攻撃、多層防御の同心円モデル",
        "md_file": "2026-10-23_ep05_cia_triad_and_defense_in_depth.md",
        "illust": "ep05_4koma.png",
        "figure": "fig05_cia_and_defense_in_depth.png"
    },
    {
        "num": 6,
        "id": "ep06",
        "title": "データベースの合言葉と呪文の罠 〜SQLインジェクションと安全なプログラミング〜",
        "theme": "SQLインジェクション攻撃、文字列連結の脆弱性、プレースホルダ（バインド機構）",
        "md_file": "2026-10-23_ep06_sql_injection_and_web_security.md",
        "illust": "ep06_4koma.png",
        "figure": "fig06_sql_injection_defense.png"
    },
    {
        "num": 7,
        "id": "ep07",
        "title": "割れない南京錠と魔法の印鑑 〜公開鍵暗号とデジタル署名の数理〜",
        "theme": "鍵配送問題、公開鍵暗号の鍵ペア、デジタル署名（電子署名）、SHA-256ハッシュ関数",
        "md_file": "2026-10-23_ep07_cryptography_and_digital_signatures.md",
        "illust": "ep07_4koma.png",
        "figure": "fig07_digital_signature_pki.png"
    },
    {
        "num": 8,
        "id": "ep08",
        "title": "パスワードを捨てる日 〜生体認証とパスキー（FIDO2）が拓く未来〜",
        "theme": "パスキー（Passkey）、FIDO2 / WebAuthn、公開鍵認証、Secure Enclave、パスワードレス認証",
        "md_file": "2026-10-24_ep08_passkey_and_fido2_passwordless.md",
        "illust": "ep08_art.png",
        "figure": "fig08_passkey_fido2_architecture.png"
    },
    {
        "num": 9,
        "id": "ep09",
        "title": "見えない鎖の綻び 〜サプライチェーン攻撃とソフトウェアの原材料表示（SBOM）〜",
        "theme": "サプライチェーン攻撃、委託先経由侵入、オープンソース汚染、SBOM（ソフトウェア部品構成表）",
        "md_file": "2026-10-24_ep09_supply_chain_attack_and_sbom.md",
        "illust": "ep09_art.png",
        "figure": "fig09_supply_chain_sbom.png"
    },
    {
        "num": 10,
        "id": "ep10",
        "title": "ゼロの日を越える翼 〜ゼロデイ脆弱性と世界を守るホワイトハッカー〜",
        "theme": "ゼロデイ攻撃（0-day）、協調的脆弱性開示（CVD）、CVE番号、米CISA KEVカタログ、倫理的ハッカー",
        "md_file": "2026-10-24_ep10_zero_day_and_white_hackers.md",
        "illust": "ep10_art.png",
        "figure": "fig10_zero_day_coordinated_disclosure.png"
    },
    {
        "num": 11,
        "id": "ep11",
        "title": "砂浜の足跡と電子の鑑識官 〜デジタル・フォレンジックと不正アクセス禁止法〜",
        "theme": "デジタル・フォレンジック、ライトブロッカー、ハッシュ値照合、不正アクセス禁止法、サイバー警察・CSIRT",
        "md_file": "2026-10-24_ep11_digital_forensics_and_cyber_law.md",
        "illust": "ep11_art.png",
        "figure": "fig11_digital_forensics_law.png"
    },
    {
        "num": 12,
        "id": "ep12",
        "title": "世界を繋ぐバケツリレー 〜家庭・学校のLAN、ルーターとDNSの秘密〜",
        "theme": "LANとWAN、プライベートIPとグローバルIP、ルーター（NAT/NAPT）、DNS名前解決、初期ファイアウォール",
        "md_file": "2026-10-24_ep12_lan_routers_and_dns_basics.md",
        "illust": "ep12_art.png",
        "figure": "fig12_lan_router_dns.png"
    },
    {
        "num": 13,
        "id": "ep13",
        "title": "旗を掲げる守護者たち 〜サイバーセキュリティ競技（CTF）と未来への扉〜",
        "theme": "CTF（Capture The Flag）競技、5大ジャンル（Web, Crypto, Reversing, Forensics, Pwn）、大学情報学部進路、CISO",
        "md_file": "2026-10-24_ep13_ctf_competition_and_future_careers.md",
        "illust": "ep13_art.png",
        "figure": "fig13_ctf_and_careers.png"
    },
    {
        "num": 14,
        "id": "ep14",
        "title": "見えない空の保管庫 〜クラウドセキュリティと責任共有モデル〜",
        "theme": "クラウドサービス（IaaS/PaaS/SaaS）、責任共有モデル、IAM最小権限の原則、公開バケット設定ミス防止",
        "md_file": "2026-10-24_ep14_cloud_security_and_shared_responsibility.md",
        "illust": "ep14_art.png",
        "figure": "fig14_cloud_shared_responsibility.png"
    },
    {
        "num": 15,
        "id": "ep15",
        "title": "知性をまとう盾と矛 〜人工知能（AI）の悪用脅威と防衛の未来（第1部 完結）〜",
        "theme": "AI時代の脅威（プロンプト注入・ディープフェイク・データ汚染） vs AI自律防御、人間の倫理と知性、第1部堂々完結",
        "md_file": "2026-10-24_ep15_ai_security_and_future_frontiers.md",
        "illust": "ep15_art.png",
        "figure": "fig15_ai_security_deepfake.png"
    }
]

def parse_markdown_to_html(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split frontmatter
    parts = content.split("---")
    if len(parts) >= 3:
        body = "---".join(parts[2:]).strip()
    else:
        body = content.strip()

    # Extract 4-Koma Script if present
    script_match = re.search(r"## 💬 4コマ漫画キャラクターセリフ（日・英対訳）\s*\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    script_raw = script_match.group(1).strip() if script_match else ""
    script_html = ""
    if script_raw:
        # Parse table rows
        rows = [r.strip() for r in script_raw.split("\n") if r.strip().startswith("|") and not "---" in r and not "シチュエーション" in r]
        items_html = []
        for r in rows:
            cols = [c.strip() for c in r.split("|")[1:-1]]
            if len(cols) >= 4:
                koma_num_raw, situ_raw, ja_raw, en_raw = cols[0], cols[1], cols[2], cols[3]
                # clean formatting
                koma_label = re.sub(r"<br>", " ", koma_num_raw).replace("**", "").strip()
                situ_text = re.sub(r"<br>", "<br>", situ_raw).replace("**", "<strong>").replace("</strong>", "</strong>") # preserve simple tags
                
                # Format character dialogues
                ja_formatted = ja_raw.replace("<br>", "<br>")
                ja_formatted = re.sub(r"\*\*(.*?)\*\*:", r'<span class="koma-char-name">[\1]</span>', ja_formatted)
                
                en_formatted = en_raw.replace("<br>", "<br>")
                en_formatted = re.sub(r"\*\*(.*?)\*\*:", r'<span class="koma-char-name">[\1]</span>', en_formatted)

                item = f"""
                <div class="koma-panel-item">
                  <div class="koma-panel-badge">{html.escape(koma_label)}</div>
                  <div class="koma-panel-body">
                    <div class="koma-situation">{situ_text}</div>
                    <div class="koma-dialogue-ja">🗣️ {ja_formatted}</div>
                    <div class="koma-dialogue-en">🌐 {en_formatted}</div>
                  </div>
                </div>
                """
                items_html.append(item)
        
        if items_html:
            script_html = f"""
            <div class="koma-script-box">
              <div class="koma-script-header">
                <h3>💬 4コマ漫画キャラクターセリフ (Story Dialogue Script)</h3>
                <span class="lang-tag">日・英バイリンガル (JA / EN)</span>
              </div>
              <div class="koma-panels-list">
                {''.join(items_html)}
              </div>
            </div>
            """

    # Extract novel
    novel_match = re.search(r"## 📖 小説本文\s*\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    novel_raw = novel_match.group(1).strip() if novel_match else ""

    # Extract column
    column_match = re.search(r"## 💡 高校生のためのセキュリティ深掘りコラム\s*\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    column_raw = column_match.group(1).strip() if column_match else ""

    # Convert novel paragraphs
    novel_paragraphs = []
    for para in novel_raw.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        if para == "***" or para == "* * *":
            novel_paragraphs.append('<div class="scene-break">✦ ✦ ✦</div>')
        elif para.startswith("「") or para.startswith("『"):
            novel_paragraphs.append(f'<p class="dialogue">{html.escape(para)}</p>')
        else:
            novel_paragraphs.append(f'<p>{html.escape(para)}</p>')
    novel_html = "\n".join(novel_paragraphs)

    # Convert column subsections
    column_html_parts = []
    col_sections = re.split(r"### (.*?)\n", column_raw)
    if len(col_sections) > 1:
        for i in range(1, len(col_sections), 2):
            sec_title = col_sections[i].strip()
            sec_body = col_sections[i+1].strip() if i+1 < len(col_sections) else ""
            
            lines = []
            for line in sec_body.split("\n"):
                line = line.strip()
                if not line:
                    continue
                line = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", line)
                line = re.sub(r"`(.*?)`", r"<code>\1</code>", line)
                if line.startswith("- "):
                    lines.append(f"<li>{line[2:]}</li>")
                elif re.match(r"^\d+\.\s", line):
                    lines.append(f"<li>{line[3:]}</li>")
                else:
                    lines.append(f"<p>{line}</p>")
            
            body_html = "\n".join(lines)
            if "<li>" in body_html:
                body_html = f"<ul>{body_html}</ul>"

            column_html_parts.append(f"""
            <div class="column-box">
              <h3>💡 {html.escape(sec_title)}</h3>
              <div class="column-content">
                {body_html}
              </div>
            </div>
            """)
    column_html = "\n".join(column_html_parts)

    return script_html, novel_html, column_html

# Build each episode page
for idx, ep in enumerate(episodes):
    prev_ep = episodes[idx-1] if idx > 0 else None
    next_ep = episodes[idx+1] if idx < len(episodes)-1 else None

    script_html, novel_html, column_html = parse_markdown_to_html(os.path.join(CONTENT_DIR, ep["md_file"]))

    prev_link = f'<a href="{prev_ep["id"]}.html" class="nav-btn">← 第{prev_ep["num"]:02d}話: {html.escape(prev_ep["title"][:18])}...</a>' if prev_ep else '<span class="nav-disabled">最初のエピソード</span>'
    next_link = f'<a href="{next_ep["id"]}.html" class="nav-btn next">第{next_ep["num"]:02d}話: {html.escape(next_ep["title"][:18])}... →</a>' if next_ep else '<span class="nav-disabled">最新エピソード</span>'

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

  <header class="story-header">
    <div class="container">
      <div class="breadcrumb">
        <a href="../index.html">トップ (目次)</a> &gt; <span>第{ep['num']:02d}話</span>
      </div>
      <div class="story-ep-tag">Episode {ep['num']:02d}</div>
      <h1 class="story-main-title">{html.escape(ep['title'])}</h1>
      <div class="story-meta">
        <span>📚 学習テーマ: <strong>{html.escape(ep['theme'])}</strong></span>
        <span>🏫 登場人物: 城崎悠真（部長・高2）、橘葵（部員・高2）、芹沢涼香准教授（大学メンター）</span>
      </div>
    </div>
  </header>

  <main class="container story-container">

    <!-- ストーリーイラスト (4コマ漫画) -->
    <section class="visual-card">
      <div class="visual-header">
        <h2>🎨 4コマ漫画挿絵（文字なし）</h2>
        <span class="visual-badge">AI高解像度生成</span>
      </div>
      <div class="visual-body">
        <img src="../assets/images/{ep['illust']}" alt="第{ep['num']:02d}話 ストーリーイラスト" class="responsive-img">
        <p class="caption">▲ 【挿絵】青葉台高校 情報科学部＆帝都科学大学サイバーディフェンス・ラボでの実践シーン</p>
      </div>
    </section>

    <!-- 4コマ漫画セリフ（日・英バイリンガル）※存在する場合 -->
    {script_html}

    <!-- 小説本文 -->
    <section class="novel-section">
      <div class="section-title">
        <h2>📖 小説本文</h2>
      </div>
      <div class="novel-body">
        {novel_html}
      </div>
    </section>

    <!-- TikZ 技術構造図解 -->
    <section class="visual-card">
      <div class="visual-header">
        <h2>📊 セキュリティ構造図解 (TikZ LuaLaTeX生成)</h2>
        <span class="visual-badge">国家安全基準・工学図解</span>
      </div>
      <div class="visual-body">
        <img src="../assets/images/{ep['figure']}" alt="第{ep['num']:02d}話 セキュリティ構造図解" class="responsive-img">
        <p class="caption">▲ 【技術構造図】IPAデジタルスキル標準・国際規格に準拠した仕組みのモデル化</p>
      </div>
    </section>

    <!-- 深掘りコラム -->
    <section class="column-section">
      <div class="section-title">
        <h2>💡 高校生のためのセキュリティ深掘りコラム ＆ 大学進路ガイド</h2>
      </div>
      {column_html}
    </section>

    <!-- 前後ナビゲーション -->
    <nav class="episode-nav">
      {prev_link}
      <a href="../index.html" class="nav-btn center">目次に戻る</a>
      {next_link}
    </nav>

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
      <h2 style="font-size: 1.4rem; color: var(--secondary); margin-bottom: 0.8rem;">📖 このライブラリについて</h2>
      <p style="color: #475569; font-size: 0.98rem; line-height: 1.8;">
        高校生がサイバーセキュリティの面白さや重要性に触れ、将来の情報科学系・工学系大学への進学やセキュリティ専門職を目指すための入門ライトノベルです。<br>
        男子高校生（城崎 悠真 部長）と女子高校生（橘 葵）が、国内外の最新サイバー脅威ニュースや政府機関（デジタル庁・国家サイバー統括室・米CISA等）の公式情報を題材に、大学の芹沢 涼香 准教授と共にセキュリティの仕組みを優しく・正確に探求していきます。
      </p>
    </section>

    <h2 style="font-size: 1.5rem; color: var(--secondary); margin-bottom: 1.5rem; border-left: 4px solid var(--primary); padding-left: 0.8rem;">📑 収録エピソード一覧（第1部 全15話）</h2>

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
print("Updated top index page and story pages for all 13 episodes:", index_path)
