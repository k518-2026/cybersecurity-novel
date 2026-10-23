import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import call_ollama, render_tikz, generate_drawthings_image, CONTENT_DIR, ILLUST_DIR

def run_ep03():
    print("=== Generating Episode 3: Free Wi-Fi, MitM & HTTPS/VPN ===")
    
    # 1. TikZ Figure: Man-in-the-Middle Attack vs HTTPS/VPN Encrypted Tunnel
    tikz_ep03 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{userblue}{RGB}{20, 80, 150}
\definecolor{badred}{RGB}{190, 30, 30}
\definecolor{goodgreen}{RGB}{25, 125, 45}
\definecolor{bglight}{RGB}{245, 248, 252}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % -------------------------------------------------------------
  % 上段：公衆Wi-Fiでの暗号化なし通信（中間者攻撃・盗聴）
  % -------------------------------------------------------------
  \node[draw=badred, fill=red!6, rounded corners=8pt, line width=1.5pt, minimum width=18.5cm, minimum height=3.6cm, align=left] (unsec_box) at (0, 3.8) {};
  
  \node[above right, font=\large\bfseries, text=badred] at (-9.0, 5.0) {【危険】暗号化なし公衆Wi-Fi（HTTP通信・なりすましAP）};

  \node[draw=userblue, fill=blue!10, rounded corners=6pt, thick, align=center, minimum width=3.2cm, minimum height=1.6cm] (user1) at (-6.8, 3.4) {
    \textbf{高校生スマホ}\\[2pt]
    \footnotesize (カフェで利用)
  };

  \node[draw=badred, fill=red!15, rounded corners=6pt, very thick, align=center, minimum width=3.8cm, minimum height=1.6cm] (hacker) at (0, 3.4) {
    \textbf{\textcolor{badred}{攻撃者（中間者: MitM）}}\\[2pt]
    \footnotesize 同一Wi-Fi上の盗聴・パケット解析
  };

  \node[draw=black!70, fill=gray!15, rounded corners=6pt, thick, align=center, minimum width=3.2cm, minimum height=1.6cm] (server1) at (6.8, 3.4) {
    \textbf{Webサーバー}\\[2pt]
    \footnotesize (HTTPサービス)
  };

  \draw[->, thick, dashed, red] (user1.east) -- node[above, font=\footnotesize, text=badred] {平文データ (パスワード/閲覧履歴)} (hacker.west);
  \draw[->, thick, dashed, red] (hacker.east) -- node[above, font=\footnotesize, text=badred] {覗き見・改ざん} (server1.west);

  % -------------------------------------------------------------
  % 下段：HTTPS / VPN による暗号化トンネル保護
  % -------------------------------------------------------------
  \node[draw=goodgreen, fill=green!6, rounded corners=8pt, line width=1.5pt, minimum width=18.5cm, minimum height=3.6cm, align=left] (sec_box) at (0, -1.0) {};
  
  \node[above right, font=\large\bfseries, text=goodgreen] at (-9.0, 0.2) {【安全】HTTPS (TLS暗号化) ＆ VPN による強固なシールドトンネル};

  \node[draw=userblue, fill=blue!10, rounded corners=6pt, thick, align=center, minimum width=3.2cm, minimum height=1.6cm] (user2) at (-6.8, -1.4) {
    \textbf{高校生スマホ}\\[2pt]
    \footnotesize (暗号化通信)
  };

  \node[draw=goodgreen, fill=green!20, rounded corners=6pt, very thick, align=center, minimum width=6.5cm, minimum height=1.4cm] (tunnel) at (0, -1.4) {
    \textbf{\textcolor{goodgreen}{TLS / VPN 暗号化トンネル}}\\[2pt]
    \footnotesize \textbf{共通鍵暗号(AES)＋公開鍵暗号(RSA/ECC)のハイブリッド暗号}
  };

  \node[draw=goodgreen, fill=green!15, rounded corners=6pt, thick, align=center, minimum width=3.2cm, minimum height=1.6cm] (server2) at (6.8, -1.4) {
    \textbf{正規Webサーバー}\\[2pt]
    \footnotesize (HTTPSサービス)
  };

  \draw[->, very thick, goodgreen] (user2.east) -- (tunnel.west);
  \draw[->, very thick, goodgreen] (tunnel.east) -- (server2.west);
  
  \node[below, font=\scriptsize, text=black!80] at (0, -2.3) {
    ※電波を傍受されても中身は完全に暗号化されており、攻撃者は一切解読できない！
  };

\end{tikzpicture}
\end{document}
"""
    render_tikz(tikz_ep03, "fig03_wifi_mitm_encryption_tunnel")

    # 2. Draw Things Illustration (Boy + Girl + Mentor in cafe/lab setting)
    prompt_ep03 = (
        "Vertical four-panel comic strip, Japanese yonkoma manga layout, "
        "4 rectangular panels stacked vertically from top to bottom with clean white borders, full color Japanese anime art style. "
        "Panel 1: A cool high school boy with glasses studying with a cute high school girl at a cafe table with laptops, noticing an open free Wi-Fi network popup. "
        "Panel 2: Female university professor sitting across from them, holding up a smartphone and explaining data packet eavesdropping with a hand gesture. "
        "Panel 3: The high school boy confidently setting up a secure VPN and HTTPS connection on his laptop, showing the green lock icon to the girl. "
        "Panel 4: High school boy, high school girl, and female professor all smiling happily and relaxed in the warm sunlit campus cafe. "
        "Masterpiece anime comic strip, clean panel division, rich vibrant colors, high contrast, crisp lineart, completely pure illustration, "
        "detailed anime eyes, soft relaxed expression, natural warm smiles, NO speech bubbles, NO text, NO words, NO letters, NO Japanese text."
    )
    img_ep03_path = os.path.join(ILLUST_DIR, "ep03_4koma.png")
    generate_drawthings_image(prompt_ep03, img_ep03_path)

    # 3. Novel Text via Ollama
    novel_prompt = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生がサイバーセキュリティ（公衆無線LANの危険性と通信の暗号化HTTPS・VPNの仕組み）を学ぶ青春ライトノベル第3話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第3話 街角の電波は誰のもの？ 〜公衆無線LANの危険性と通信の暗号化（HTTPS）〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・情報科学部長。ノートPCでプログラミングに熱中する理系男子。街中のカフェの野良Wi-Fiの危険性を察知する。
・橘 葵（たちばな あおい）：高校2年・部員。「ギガが減らないから便利！」と街のパスワードなし無料Wi-Fiにすぐ飛びつこうとする女子高生。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 サイバーセキュリティ研究室 准教授。カフェに偶然現れ、電波の不可視性と暗号化トンネルの美しさを語る。

【必須要素】
1. 街中の暗号化されていない公衆無線LAN（野良Wi-Fi・悪意あるなりすましアクセスポイント「Evil Twin」）の危険性
2. パケット盗聴と「中間者攻撃（Man-in-the-Middle: MitM）」の原理（電波は誰でも拾えるという事実）
3. なぜHTTPS（TLS）通信やVPNがデータを守れるのか（共通鍵暗号の高速性と公開鍵暗号の安全性を組み合わせたハイブリッド暗号方式）
4. カフェオレの香り、キーボードの打鍵音、画面に走る緑色のシールドサインなど五感描写
5. 大学で学ぶ「暗号数学・情報理論」への知的好奇心

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

    print("Generating Ep03 novel text with shosetsu on 192.168.128.62...")
    novel_body = call_ollama("shosetsu:latest", novel_prompt, timeout=300)

    # 4. Save Markdown
    ep03_md = f"""---
title: "第3話 街角の電波は誰のもの？ 〜公衆無線LANの危険性と通信の暗号化（HTTPS）〜"
episode_num: 3
date: 2026-10-23
categories: ["高校生向けサイバーセキュリティライトノベル", "大学情報科学入門"]
tags: ["公衆無線LAN", "フリーWi-Fi", "中間者攻撃", "HTTPS", "TLS", "VPN", "暗号化通信", "IPAデジタルスキル標準"]
---

# 第3話 街角の電波は誰のもの？ 〜公衆無線LANの危険性と通信の暗号化（HTTPS）〜

> **【放課後サイバーディフェンス・ラボ】**
> - **舞台**: 駅前カフェ「テラス・サイバネティクス」 ＆ 帝都科学大学
> - **登場人物**: 城崎 悠真（高校2年・部長）、橘 葵（高校2年・部員）、芹沢 涼香 准教授（大学メンター / IPAアドバイザー）
> - **学習テーマ**: 公衆無線LANのパケット傍受リスク、中間者攻撃（MitM）、TLS暗号化トンネルとVPNの仕組み
> - **参照規格・公式情報**:
>   - [IPA 独立行政法人 情報処理推進機構：公衆無線LAN利用時のセキュリティ対策](https://www.ipa.go.jp/security/anshin/measures/wireless_lan.html)
>   - [総務省：Wi-Fi提供者向け・利用者向けセキュリティガイドライン](https://www.soumu.go.jp/)
>   - [サイバーセキュリティ.com：公衆Wi-Fi情報詐取・中間者攻撃ニュース](https://cybersecurity-jp.com/news)

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第3話 4コマ漫画イラスト](illustrations/ep03_4koma.png)

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

### 中間者攻撃（MitM）の脅威とTLS/VPN暗号化トンネルの保護

![中間者攻撃とTLS/VPN暗号化トンネル](figures/fig03_wifi_mitm_encryption_tunnel.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 「電波は空中に撒き散らされている」という事実
有線LANケーブルと異なり、無線LAN（Wi-Fi）の電波は周囲数十メートルに同心円状に広がっています。暗号化キー（鍵マーク）が設定されていない無料Wi-Fiでは、**同じ電波を受信できる誰でも特殊なツールを使ってパケット（通信データ）を傍受可能**です。さらに、実在するカフェや駅の名前を騙った「悪魔の双子（Evil Twin）アクセスポイント」を攻撃者が設置しているケースもあります。

### 2. 中間者攻撃（Man-in-the-Middle: MitM）とは？
端末と本来の通信相手（サーバー）の間に攻撃者が割り込み、双方になりすまして通信を中継・盗聴・改ざんする手口です。平文通信（HTTP）の場合、閲覧中のWebサイトや入力したID・パスワード、プライベートなやり取りが筒抜けになってしまいます。

### 3. HTTPSとVPNがデータを不可視化する仕組み
- **HTTPS（TLS 1.3など）**:
  ブラウザとWebサーバーの間で、最初に「公開鍵暗号」を使って秘密の鍵を安全に共有し、以降のやり取りを高速な「共通鍵暗号（AESなど）」で暗号化します。これにより、たとえ電波を傍受されても、第三者には「意味不明なランダム文字列」にしか見えません。
- **VPN（Virtual Private Network）**:
  端末とVPNサーバーの間に強固な仮想暗号化トンネルを作り、Wi-Fi区間のすべての通信をまるごと包み込んで隠蔽します。公衆Wi-Fiを利用する際の強力な盾となります。

### 4. 大学で学ぶ「情報セキュリティと暗号理論」
大学の情報通信学科や数学科・情報数理工学科では、素因数分解の困難さに基づくRSA暗号や、楕円曲線暗号（ECC）、さらに量子コンピュータでも解読できない「耐量子計算機暗号（PQC）」などの最先端数学を学びます。単なるルールを守るだけでなく、**「数学という絶対の法則で世界を守る技術」**を学ぶことができる非常にエキサイティングな分野です。
"""
    out_file = os.path.join(CONTENT_DIR, "2026-10-23_ep03_free_wifi_and_encryption.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ep03_md)
    print("SUCCESS: Ep03 completed and saved to:", out_file)

if __name__ == "__main__":
    run_ep03()
