import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import call_ollama, render_tikz, generate_drawthings_image, CONTENT_DIR, ILLUST_DIR

def run_ep07():
    print("=== Generating Episode 7: Cryptography & Digital Signatures ===")
    
    # 1. TikZ Figure: Public Key Cryptography & Digital Signature Flow
    tikz_ep07 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{keyblue}{RGB}{20, 80, 150}
\definecolor{hashpurple}{RGB}{120, 40, 140}
\definecolor{siggreen}{RGB}{30, 135, 55}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % -------------------------------------------------------------
  % 送信側（葵）：元文書からハッシュ計算 ＆ 秘密鍵で署名作成
  % -------------------------------------------------------------
  \node[draw=keyblue, fill=blue!6, rounded corners=8pt, line width=1.5pt, minimum width=18.5cm, minimum height=3.6cm, align=left] (sender_box) at (0, 3.8) {};
  
  \node[above right, font=\large\bfseries, text=keyblue] at (-9.0, 5.0) {【送信者側】メッセージのハッシュ化 ＆ 送信者の「秘密鍵」によるデジタル署名};

  \node[draw=black!70, fill=white, rounded corners=4pt, thick, align=center, minimum width=3.4cm, minimum height=1.4cm] (doc1) at (-6.8, 3.4) {
    \textbf{送信メッセージ}\\[2pt]
    \footnotesize (元の電子文書)
  };

  \node[draw=hashpurple, fill=purple!10, rounded corners=4pt, thick, align=center, minimum width=3.8cm, minimum height=1.4cm] (hash1) at (-1.4, 3.4) {
    \textbf{一方向ハッシュ関数}\\[2pt]
    \footnotesize (SHA-256で要約生成)
  };

  \node[draw=siggreen, fill=green!15, rounded corners=6pt, very thick, align=center, minimum width=5.6cm, minimum height=1.6cm] (sign) at (5.2, 3.4) {
    \textbf{\textcolor{siggreen}{送信者の「秘密鍵」で暗号化}}\\[2pt]
    \footnotesize $\Rightarrow$ \textbf{\large デジタル署名（電子署名）}の完成！\\[1pt]
    \tiny ※送信者本人しか持たない鍵で署名するため偽造不可能
  };

  \draw[->, very thick] (doc1.east) -- (hash1.west);
  \draw[->, very thick] (hash1.east) -- (sign.west);

  % -------------------------------------------------------------
  % 受信側（悠真）：公開鍵で検証 ＆ 本人証明と非改ざん証明
  % -------------------------------------------------------------
  \node[draw=siggreen, fill=green!6, rounded corners=8pt, line width=1.5pt, minimum width=18.5cm, minimum height=3.8cm, align=left] (recv_box) at (0, -1.2) {};
  
  \node[above right, font=\large\bfseries, text=siggreen] at (-9.0, 0.1) {【受信者側】送信者の「公開鍵」による署名検証 ＆ 改ざん・なりすまし検知};

  \node[draw=siggreen, fill=white, rounded corners=4pt, thick, align=center, minimum width=4.0cm, minimum height=1.4cm] (sig_recv) at (-6.5, -1.6) {
    \textbf{届いたデジタル署名}
  };

  \node[draw=keyblue, fill=blue!15, rounded corners=4pt, very thick, align=center, minimum width=4.4cm, minimum height=1.6cm] (verify) at (-0.8, -1.6) {
    \textbf{送信者の「公開鍵」で復号}\\[2pt]
    \footnotesize (世界中に公開されている鍵)\\[2pt]
    \scriptsize $\Rightarrow$ 復元されたハッシュ値 A
  };

  \node[draw=hashpurple, fill=purple!15, rounded corners=4pt, thick, align=center, minimum width=4.4cm, minimum height=1.6cm] (rehash) at (4.8, -1.6) {
    \textbf{届いた文書から再計算}\\[2pt]
    \footnotesize (SHA-256で再ハッシュ)\\[2pt]
    \scriptsize $\Rightarrow$ 計算されたハッシュ値 B
  };

  \draw[->, very thick] (sig_recv.east) -- (verify.west);

  % 比較判定
  \node[draw=siggreen, fill=green!25, rounded corners=6pt, line width=1.5pt, align=center, minimum width=18.5cm, inner sep=6pt] (verdict) at (0, -3.8) {
    \textbf{\Large ハッシュ値 A ＝ ハッシュ値 B が一致した場合}\\[3pt]
    \small \textbf{① 真正性（送信者本人が書いたこと）} ＆ \textbf{② 完全性（途中で1文字も改ざんされていないこと）} を数学的に完全証明！
  };

  \draw[->, thick, dashed] (verify.south) -- ++(0, -0.4) -| ($(verdict.north) + (-2.8, 0)$);
  \draw[->, thick, dashed] (rehash.south) -- ++(0, -0.4) -| ($(verdict.north) + (2.8, 0)$);

\end{tikzpicture}
\end{document}
"""
    render_tikz(tikz_ep07, "fig07_digital_signature_pki")

    # 2. Draw Things Illustration: High-quality 768x1024 single scene
    prompt_ep07 = (
        "1boy, 1girl, smart Japanese high school boy with glasses holding a glowing golden digital key, "
        "cute high school girl with ponytail happily inspecting an encrypted holographic seal on a tablet screen, "
        "kind female university cryptography professor smiling warmly in modern university mathematics and informatics seminar room, "
        "background showing beautiful mathematical blackboard equations, warm soft ambient lighting, clean wooden desks, "
        "masterpiece, best quality, beautiful detailed anime art style, Kyoto Animation aesthetic, "
        "perfect facial features, beautiful anime eyes, clear pupils, relaxed natural smiles, "
        "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
    )
    img_ep07_path = os.path.join(ILLUST_DIR, "ep07_art.png")
    generate_drawthings_image(prompt_ep07, img_ep07_path)

    # 3. Novel Text via Ollama
    novel_prompt = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生が暗号理論の金字塔「公開鍵暗号とデジタル署名（電子署名）」の仕組みを学ぶ青春ライトノベル第7話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第7話 割れない南京錠と魔法の印鑑 〜公開鍵暗号とデジタル署名の数理〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・部長。「誰にでも配っていい公開鍵と、自分だけが持つ秘密鍵のペア」という公開鍵暗号の美しさに魅了される。
・橘 葵（たちばな あおい）：高校2年・部員。「暗号化って、相手に鍵を送ったらその鍵を途中で盗まれちゃうんじゃないの？」という素朴な疑問を持つ。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 准教授。「開いた南京錠を配る」という日常の例えから、デジタル署名がなぜ「なりすまし」と「改ざん」を同時に防げるのかを解き明かす。

【必須要素】
1. 共通鍵暗号の「鍵配送問題」（鍵を安全に送る難しさ）
2. 公開鍵暗号（RSA・楕円曲線暗号）の発想：誰でも施錠できるが、解錠できるのは持ち主だけの鍵ペア
3. デジタル署名（電子署名）の逆転の発想：本人しか持たない「秘密鍵」で暗号化し、全員が持っている「公開鍵」で復号することで、世界で唯一の本人証明・改ざん検知を行う仕組み
4. 一方向ハッシュ関数（SHA-256など）によるダイジェスト生成の役割
5. サイバーセキュリティ.com等で報じられる電子署名・偽造メール（SPF/DKIM/DMARC）やソフトウェアサプライチェーン改ざん事件の教訓
6. 数学（素数・合同式・離散対数問題）が社会の信頼インフラを支えているという深い感動

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

    print("Generating Ep07 novel text with shosetsu on 192.168.128.62...")
    novel_body = call_ollama("shosetsu:latest", novel_prompt, timeout=300)

    # 4. Save Markdown
    ep07_md = f"""---
title: "第7話 割れない南京錠と魔法の印鑑 〜公開鍵暗号とデジタル署名の数理〜"
episode_num: 7
date: 2026-10-23
categories: ["高校生向けサイバーセキュリティライトノベル", "大学情報科学入門"]
tags: ["暗号理論", "公開鍵暗号", "デジタル署名", "ハッシュ関数", "PKI", "電子署名", "IPAデジタルスキル標準"]
---

# 第7話 割れない南京錠と魔法の印鑑 〜公開鍵暗号とデジタル署名の数理〜

> **【放課後サイバーディフェンス・ラボ】**
> - **舞台**: 県立青葉台高校 情報科学部 ＆ 帝都科学大学 数理情報セキュリティ研究室
> - **登場人物**: 城崎 悠真（高校2年・部長）、橘 葵（高校2年・部員）、芹沢 涼香 准教授（大学メンター / IPAアドバイザー）
> - **学習テーマ**: 共通鍵暗号の鍵配送問題、公開鍵暗号の鍵ペア、デジタル署名の数理モデル、ハッシュ関数
> - **参照規格・公式情報**:
>   - [IPA 独立行政法人 情報処理推進機構：暗号技術ガイドライン（CRYPTREC）](https://www.ipa.go.jp/security/cryptrec/)
>   - [内閣官房 国家サイバー統括室：暗号政策と耐量子計算機暗号（PQC）の展望](https://www.cyber.go.jp/)
>   - [サイバーセキュリティ.com：ソフトウェア署名改ざん・送信元なりすまし速報](https://cybersecurity-jp.com/news)

---

## 🎨 ストーリーイラスト (Draw Things 生成)

![第7話 ストーリーイラスト](illustrations/ep07_art.png)

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

### デジタル署名（電子署名）の作成と検証フロー

![デジタル署名の仕組みとPKI](figures/fig07_digital_signature_pki.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 「鍵配送問題」を打ち破った公開鍵暗号の革命
古くからの「共通鍵暗号（シーザー暗号やAES）」は、暗号化と復号に同じ鍵を使うため、「その鍵をどうやって安全に相手に渡すか」という**鍵配送問題**に直面します。
1970年代に発明された**「公開鍵暗号（Public Key Cryptography）」**は、この常識を覆しました。
- **公開鍵（Public Key）**: 誰に配っても良い鍵（開いた南京錠のようなもの）。
- **秘密鍵（Private Key）**: 本人だけが厳重に隠し持つ鍵（解錠用の専用キー）。
誰もが公開鍵で箱をロック（暗号化）できますが、その箱を開けられるのは世界でただ一人、秘密鍵を持つ受取人だけです。

### 2. 「逆転の発想」で生まれるデジタル署名
この鍵ペアの仕組みを**逆向き**に使ったのが「デジタル署名」です。
1. 送信者が、自分だけの**「秘密鍵」で暗号化**したデータ（署名）を作成する。
2. 受信者は、世界中に配られている送信者の**「公開鍵」で復号**を試みる。
もし送信者の公開鍵で綺麗に復号できれば、**「この署名は世界で唯一、秘密鍵を持っている本人しか作れなかった」**ことが数学的に証明されます（真正性・否認防止）。

### 3. ハッシュ関数（SHA-256）との二人三脚
大きな電子文書全体を直接暗号化すると計算に時間がかかるため、実際には**一方向ハッシュ関数（SHA-256など）**を用いて文書を短い固定長データ（ハッシュ値）に圧縮してから秘密鍵で署名します。
もし途中で文書が1文字でも書き換えられると、ハッシュ値が雪崩のように全く別の値に変化するため、**「途中で改ざんされていないこと（完全性）」**も瞬時に判定できます。

### 4. 大学で学ぶ「数理情報科学・数論・現代暗号」
大学の数学科や情報科学科では、フェルマーの小定理やオイラーの定理、巨大な素数を使ったRSA暗号の構成、そして楕円曲線上の群論を学びます。さらに近年では、将来の量子コンピュータでも解読できない**「耐量子計算機暗号（PQC: Post-Quantum Cryptography）」**の研究が世界中で熱狂的に進められています。数学という純粋な真理が、世界中の金融や国家インフラを守る最強の盾になる感動を味わえる学問です。
"""
    out_file = os.path.join(CONTENT_DIR, "2026-10-23_ep07_cryptography_and_digital_signatures.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ep07_md)
    print("SUCCESS: Ep07 completed and saved to:", out_file)

if __name__ == "__main__":
    run_ep07()
