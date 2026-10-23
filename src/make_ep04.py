import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import call_ollama, render_tikz, generate_drawthings_image, CONTENT_DIR, ILLUST_DIR

def run_ep04():
    print("=== Generating Episode 4: Malware & Security Patch ===")
    
    # 1. TikZ Figure: Vulnerability & Security Patch Defense
    tikz_ep04 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{wallgray}{RGB}{120, 130, 140}
\definecolor{badred}{RGB}{190, 30, 30}
\definecolor{goodblue}{RGB}{20, 90, 160}
\definecolor{patchgreen}{RGB}{30, 140, 50}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % -------------------------------------------------------------
  % 左側：脆弱性（セキュリティホール）を突くマルウェアの侵入
  % -------------------------------------------------------------
  \node[draw=badred, fill=red!6, rounded corners=8pt, line width=1.5pt, minimum width=8.8cm, minimum height=6.0cm, align=center] (left_box) at (-4.8, 2.0) {};
  
  \node[above, font=\large\bfseries, text=badred] at (-4.8, 4.3) {【危険】脆弱性を放置したシステム};

  % 壁（城壁）に穴がある
  \fill[wallgray!40] (-8.5, -0.2) rectangle (-7.0, 3.8);
  \fill[wallgray!40] (-2.6, -0.2) rectangle (-1.1, 3.8);
  
  \node[draw=badred, fill=red!20, dashed, very thick, minimum width=4.4cm, minimum height=1.6cm, align=center] (hole) at (-4.8, 1.8) {
    \textbf{\textcolor{badred}{脆弱性 (Security Hole)}}\\[2pt]
    \footnotesize プログラムの設計ミス・不具合
  };

  \node[draw=badred, fill=red!30, rounded corners=4pt, align=center] (malware) at (-4.8, 3.5) {
    \textbf{マルウェア / ランサムウェア}\\[2pt]
    \footnotesize (未修正の穴を狙って侵入！)
  };

  \draw[->, very thick, badred] (malware.south) -- (hole.north);
  \node[below, font=\scriptsize, text=badred] at (-4.8, 0.4) {
    【結果】データ暗号化・身代金要求・情報漏洩！
  };

  % -------------------------------------------------------------
  % 右側：セキュリティパッチによる修復と多層防御
  % -------------------------------------------------------------
  \node[draw=goodblue, fill=blue!6, rounded corners=8pt, line width=1.5pt, minimum width=8.8cm, minimum height=6.0cm, align=center] (right_box) at (4.8, 2.0) {};

  \node[above, font=\large\bfseries, text=goodblue] at (4.8, 4.3) {【安全】更新（パッチ適用）後の堅牢なシステム};

  % 壁が修復されている
  \fill[wallgray!40] (1.1, -0.2) rectangle (2.6, 3.8);
  \fill[patchgreen!40, draw=patchgreen, very thick] (2.6, 1.0) rectangle (7.0, 2.6);
  \fill[wallgray!40] (7.0, -0.2) rectangle (8.5, 3.8);

  \node[align=center] at (4.8, 1.8) {
    \textbf{\textcolor{patchgreen}{\Large 堅牢なパッチ (修正済)}}\\[2pt]
    \footnotesize OS・アプリの最新アップデート
  };

  \node[draw=badred, fill=red!15, rounded corners=4pt, align=center] (blocked_malware) at (4.8, 3.5) {
    \textbf{マルウェアの攻撃}\\[2pt]
    \footnotesize (侵入経路が完全に塞がれている)
  };

  \draw[->, very thick, badred] (blocked_malware.south) -- ++(0, -0.4);
  \node[font=\Large\bfseries, text=patchgreen] at (4.8, 2.8) {× 侵入阻止};

  \node[below, font=\scriptsize, text=goodblue] at (4.8, 0.4) {
    【結果】ゼロデイ攻撃リスクを最小化しデータを保護！
  };

\end{tikzpicture}
\end{document}
"""
    render_tikz(tikz_ep04, "fig04_malware_vulnerability_patch")

    # 2. Draw Things Illustration (Boy + Girl in server/security lab)
    prompt_ep04 = (
        "Vertical four-panel comic strip, Japanese yonkoma manga layout, "
        "4 rectangular panels stacked vertically from top to bottom with clean white borders, full color Japanese anime art style. "
        "Panel 1: A smart Japanese high school boy in uniform showing a pop-up software update alert on his laptop to a curious high school girl. "
        "Panel 2: Female university professor illustrating software security patches and castle wall defenses on a whiteboard with colorful markers. "
        "Panel 3: The high school boy smiling as a system security scan shows 100 percent green shield protection status on screen. "
        "Panel 4: High school boy, high school girl, and female professor standing side by side smiling happily in high-tech university cybersecurity center. "
        "Masterpiece anime comic strip, clean panel division, rich vibrant colors, high contrast, crisp lineart, completely pure illustration, "
        "detailed anime eyes, soft relaxed expression, natural warm smiles, NO speech bubbles, NO text, NO words, NO letters, NO Japanese text."
    )
    img_ep04_path = os.path.join(ILLUST_DIR, "ep04_4koma.png")
    generate_drawthings_image(prompt_ep04, img_ep04_path)

    # 3. Novel Text via Ollama
    novel_prompt = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生がサイバーセキュリティ（マルウェアの種類とソフトウェア更新・脆弱性パッチの重要性）を学ぶ青春ライトノベル第4話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第4話 忍び寄るトロイの木馬 〜マルウェアの種類とソフトウェア更新の真実〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・部長。理系男子。パソコンのOSアップデート通知を「面倒だから後で」と先延ばしにしがちな葵を諭す。
・橘 葵（たちばな あおい）：高校2年・部員。「アップデートしたら動かなくなるかも…」と更新を躊躇していた女子高生。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 サイバーセキュリティ研究室 准教授。脆弱性（セキュリティホール）と城壁の修復を例えに、パッチの真髄を教える。

【必須要素】
1. マルウェアの分類：ウイルス（宿主が必要）、ワーム（自己増殖）、トロイの木馬（無害を装う）、ランサムウェア（身代金要求型）
2. 脆弱性（セキュリティホール）とは何か（ソフトウェアのバグや設計ミス）
3. なぜ「OSやアプリのアップデート通知」を放置してはいけないのか（攻撃者は公開された脆弱性情報を元に即座に攻撃ツールを作る）
4. サイバーセキュリティ.com等で報じられる医療機関や中小企業のランサムウェア被害の現実
5. 大学で学ぶ「セキュアプログラミングとシステムアーキテクチャ」の奥深さ

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

    print("Generating Ep04 novel text with shosetsu on 192.168.128.62...")
    novel_body = call_ollama("shosetsu:latest", novel_prompt, timeout=300)

    # 4. Save Markdown
    ep04_md = f"""---
title: "第4話 忍び寄るトロイの木馬 〜マルウェアの種類とソフトウェア更新の真実〜"
episode_num: 4
date: 2026-10-23
categories: ["高校生向けサイバーセキュリティライトノベル", "大学情報科学入門"]
tags: ["マルウェア", "ランサムウェア", "トロイの木馬", "脆弱性", "セキュリティパッチ", "IPAデジタルスキル標準", "JVN"]
---

# 第4話 忍び寄るトロイの木馬 〜マルウェアの種類とソフトウェア更新の真実〜

> **【放課後サイバーディフェンス・ラボ】**
> - **舞台**: 県立青葉台高校 情報科学部 ＆ 帝都科学大学先端セキュリティラボ
> - **登場人物**: 城崎 悠真（高校2年・部長）、橘 葵（高校2年・部員）、芹沢 涼香 准教授（大学メンター / IPAアドバイザー）
> - **学習テーマ**: マルウェアの種類と生態、脆弱性（セキュリティホール）の原理、セキュリティアップデート（パッチ）の必須性
> - **参照規格・公式情報**:
>   - [IPA / JPCERT/CC：Japan Vulnerability Notes (JVN)](https://jvn.jp/)
>   - [IPA：サイバーセキュリティ注意喚起（ランサムウェア対策）](https://www.ipa.go.jp/security/anshin/measures/ransomware.html)
>   - [サイバーセキュリティ.com：ランサムウェア感染・サプライチェーン攻撃速報](https://cybersecurity-jp.com/news)

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第4話 4コマ漫画イラスト](illustrations/ep04_4koma.png)

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

### 脆弱性の放置リスク vs セキュリティパッチによる修復・防御モデル

![脆弱性とセキュリティパッチ](figures/fig04_malware_vulnerability_patch.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 「悪意あるソフトウェア」マルウェアの4大分類
- **コンピュータウイルス**: 他の正常な実行ファイルやマクロに寄生（感染）して悪さを働くプログラム。
- **ワーム**: 宿主ファイルを必要とせず、ネットワーク経由で自分自身の複製を勝手に拡散させる自立型プログラム。
- **トロイの木馬**: 有用なゲームや便利ツールに見せかけてユーザーに自ら実行させ、裏でバックドアを開く罠。
- **ランサムウェア**: 端末内の写真や文書ファイルを勝手に強力な暗号でロックし、「元に戻したければ身代金を払え」と脅迫する極めて悪質なマルウェア。

### 2. 脆弱性（セキュリティホール）とは何か？
プログラムは人間が書いたもの（数百万行〜数千万行のコード）であるため、どうしても「メモリ管理のミス」や「入力チェックの漏れ」などの欠陥（バグ）が生まれます。このうち、**外部から不正操作や情報奪取に悪用できてしまうバグを「脆弱性（セキュリティホール）」**と呼びます。

### 3. なぜ「アップデートの先延ばし」が最も危険なのか？
セキュリティパッチ（修正プログラム）が公開された瞬間、攻撃者は「どんな穴が塞がれたのか」を逆アセンブル（リバースエンジニアリング）して解析し、**パッチを当てていない無防備な端末を狙い撃ちにする攻撃コード（エクスプロイト）**を瞬時に作成・ばら撒きます。
「後でやろう」と数日間放置するだけで、ネットに繋がっている端末は世界中の自動スキャンボットの標的になってしまいます。

### 4. 大学で学ぶ「システム安全工学とリバースエンジニアリング」
大学の計算機科学科・情報工学科では、プログラムがOSのメモリ（スタック領域やヒープ領域）をどのように使用するかというコンピュータアーキテクチャの根底を学びます。バッファオーバーフローなどの脆弱性がなぜ発生するのか、そして**「欠陥の出ない安全なプログラム（セキュアコーディング）」**をどう構築するかを学ぶことは、最高峰のエンジニアになるための必須教養です。
"""
    out_file = os.path.join(CONTENT_DIR, "2026-10-23_ep04_malware_and_vulnerabilities.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ep04_md)
    print("SUCCESS: Ep04 completed and saved to:", out_file)

if __name__ == "__main__":
    run_ep04()
