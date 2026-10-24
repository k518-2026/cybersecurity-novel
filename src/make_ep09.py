import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import call_ollama, render_tikz, generate_drawthings_image, CONTENT_DIR, ILLUST_DIR

def run_ep09():
    print("=== Generating Episode 9: Supply Chain Attack & SBOM ===")
    
    # 1. TikZ Figure: Supply Chain Attack & SBOM Verification
    tikz_ep09 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{chainblue}{RGB}{20, 80, 150}
\definecolor{badred}{RGB}{190, 30, 30}
\definecolor{goodgreen}{RGB}{30, 135, 55}
\definecolor{sbomgold}{RGB}{205, 120, 20}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % -------------------------------------------------------------
  % 上段：サプライチェーン攻撃（弱小な外部委託先・OSSライブラリ経由の侵入）
  % -------------------------------------------------------------
  \node[draw=badred, fill=red!6, rounded corners=8pt, line width=1.5pt, minimum width=20.0cm, minimum height=3.8cm, align=left] (attack_box) at (0, 3.8) {};
  
  \node[above right, font=\large\bfseries, text=badred] at (-9.8, 5.1) {【脅威】サプライチェーン攻撃：防備の固い本体ではなく「手薄な関連先」を狙う！};

  \node[draw=badred, fill=red!20, rounded corners=6pt, thick, align=center, minimum width=4.2cm, minimum height=1.6cm] (hacker) at (-7.0, 3.2) {
    \textbf{攻撃者}\\[2pt]
    \footnotesize (大企業・官公庁を狙う)
  };

  \node[draw=black!70, fill=white, rounded corners=6pt, thick, align=center, minimum width=5.0cm, minimum height=1.6cm] (supplier) at (-0.8, 3.2) {
    \textbf{外部委託先・関連会社・OSS}\\[2pt]
    \footnotesize (パスワード管理や更新が手薄)
  };

  \node[draw=chainblue, fill=blue!10, rounded corners=6pt, very thick, align=center, minimum width=5.0cm, minimum height=1.6cm] (target) at (6.4, 3.2) {
    \textbf{\Large 本丸の標的組織}\\[2pt]
    \footnotesize (強固な壁を持つ大企業・病院)
  };

  \draw[->, line width=2pt, badred] (hacker.east) -- node[above=2pt, font=\scriptsize\bfseries, text=badred] {手薄な会社を侵略} (supplier.west);
  \draw[->, line width=2pt, badred] (supplier.east) -- node[above=2pt, font=\scriptsize\bfseries, text=badred] {業務ネットワーク経由で侵入！} (target.west);

  % -------------------------------------------------------------
  % 下段：対策（国家サイバー統括室要請＆SBOMによるソフトウェア部品管理）
  % -------------------------------------------------------------
  \node[draw=goodgreen, fill=green!6, rounded corners=8pt, line width=1.5pt, minimum width=20.0cm, minimum height=3.8cm, align=left] (defense_box) at (0, -1.4) {};
  
  \node[above right, font=\large\bfseries, text=goodgreen] at (-9.8, -0.1) {【対策】国家サイバー統括室要請 ＆ SBOM（ソフトウェア部品構成表）による徹底点検};

  \node[draw=sbomgold, fill=orange!15, rounded corners=6pt, thick, align=center, minimum width=5.4cm, minimum height=1.6cm] (sbom) at (-6.4, -2.0) {
    \textbf{\large ＳＢＯＭ (部品構成表)}\\[2pt]
    \footnotesize アプリに含まれる全ての外部ライブラリを\\
    \footnotesize 食品の原材料表示のように可視化！
  };

  \node[draw=goodgreen, fill=green!15, rounded corners=6pt, thick, align=center, minimum width=5.4cm, minimum height=1.6cm] (audit) at (0.0, -2.0) {
    \textbf{\large 委託先セキュリティ審査}\\[2pt]
    \footnotesize 契約基準の統一・多要素認証の義務化\\
    \footnotesize ネットワークアクセスの最小化
  };

  \node[draw=chainblue, fill=blue!15, rounded corners=6pt, very thick, align=center, minimum width=5.4cm, minimum height=1.6cm] (secure_corp) at (6.4, -2.0) {
    \textbf{\large 堅牢なサプライチェーン}\\[2pt]
    \footnotesize どこかに脆弱性が見つかっても\\
    \footnotesize 瞬時に特定して遮断・修復可能！
  };

  \draw[->, very thick, goodgreen] (sbom.east) -- (audit.west);
  \draw[->, very thick, goodgreen] (audit.east) -- (secure_corp.west);

\end{tikzpicture}
\end{document}
"""
    render_tikz(tikz_ep09, "fig09_supply_chain_sbom")

    # 2. Draw Things Illustration: High-quality 768x1024 single scene
    prompt_ep09 = (
        "1boy, 1girl, smart Japanese high school boy with glasses pointing at interactive digital supply chain tree diagram on laptop, "
        "cute high school girl with dark ponytail listening attentively with bright understanding expression, "
        "kind stylish female university cybersecurity professor holding a glowing digital blueprint symbol representing software bill of materials, "
        "modern university cybersecurity operations center, large transparent network status monitors on wall, "
        "soft clean blue ambient lighting, wooden research desks, bright sunny windows, "
        "masterpiece, best quality, beautiful detailed anime art style, Makoto Shinkai style, Kyoto Animation aesthetic, "
        "perfect facial features, beautiful anime eyes, clear pupils, relaxed natural smiles, "
        "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
    )
    img_ep09_path = os.path.join(ILLUST_DIR, "ep09_art.png")
    generate_drawthings_image(prompt_ep09, img_ep09_path)

    # 3. Novel Text via Ollama
    novel_prompt = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生が国内政府機関（国家サイバー統括室・警察庁）や海外（CISA）が最重要警戒する「サプライチェーン攻撃」と「ソフトウェア部品管理（SBOM）」を学ぶ青春ライトノベル第9話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第9話 見えない裏口と材料の目録 〜サプライチェーン攻撃とソフトウェアの原材料表示〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・部長。部活のアプリ開発で世界中のオープンソース（OSS）ライブラリを組み込んでいたが、「もしこの部品の1つに悪意があったら？」と戦慄する。
・橘 葵（たちばな あおい）：高校2年・部員。「大企業やお医者さんの病院がハッキングされたニュース、直接攻撃されたんじゃなくて、取引先の小さな会社から侵入されたんだって…！」と驚く女子高生。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 准教授。内閣官房国家サイバー統括室の緊急注意喚起を題材に、食品のアレルギー表示に似た「SBOM（ソフトウェア部品構成表）」の重要性を解き明かす。

【必須要素】
1. 2026年10月に内閣官房国家サイバー統括室や警察庁サイバー警察局が一斉に発出した「委託先等のサプライチェーンを経由した不正アクセス・情報漏洩事案」の注意喚起
2. サプライチェーン攻撃の構造：本丸の要塞（大企業や重要インフラ）ではなく、セキュリティ対策が手薄な子会社・下請け業者・取引先のリモート接続を足がかりに侵入する手口
3. ソフトウェアサプライチェーンの危機：プログラムに組み込まれるオープンソース（OSS）の依存関係の複雑化と、食品の原材料表示に例えられる「SBOM（Software Bill of Materials）」の役割
4. 海外ニュース（CISAのKEVカタログやオープンソース脆弱性）との連動
5. 大学で学ぶ「ソフトウェアエンジニアリング・信頼性工学」の社会的重要性と魅力

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

    print("Generating Ep09 novel text with shosetsu on 192.168.128.62...")
    novel_body = call_ollama("shosetsu:latest", novel_prompt, timeout=300)

    # 4. Save Markdown
    ep09_md = f"""---
title: "第9話 見えない裏口と材料の目録 〜サプライチェーン攻撃とソフトウェアの原材料表示〜"
episode_num: 9
date: 2026-10-24
categories: ["高校生向けサイバーセキュリティライトノベル", "大学情報科学入門"]
tags: ["サプライチェーン攻撃", "国家サイバー統括室", "警察庁", "SBOM", "オープンソース", "CISA", "IPAデジタルスキル標準"]
---

# 第9話 見えない裏口と材料の目録 〜サプライチェーン攻撃とソフトウェアの原材料表示〜

> **【放課後サイバーディフェンス・ラボ】**
> - **舞台**: 県立青葉台高校 情報科学部 ＆ 帝都科学大学 ソフトウェア信頼性研究室
> - **登場人物**: 城崎 悠真（高校2年・部長）、橘 葵（高校2年・部員）、芹沢 涼香 准教授（大学メンター / IPAアドバイザー）
> - **学習テーマ**: サプライチェーン攻撃（委託先経由の侵害）、OSS依存関係リスク、SBOM（ソフトウェア部品構成表）、最小権限アクセス
> - **参照規格・政府公式情報**:
>   - [内閣官房 国家サイバー統括室：不正アクセス事案を踏まえた委託先等のサプライチェーン対策要請](https://www.cyber.go.jp/)
>   - [警察庁サイバー警察局：サイバー警察局だより・情報流出への緊急注意喚起](https://www.npa.go.jp/cyber/)
>   - [経済産業省：ソフトウェア管理に向けたSBOMの導入に関する手引](https://www.meti.go.jp/)
>   - [CISA：Secure by Demand and Software Supply Chain Security](https://www.cisa.gov/)

---

## 🎨 ストーリーイラスト (Draw Things 生成)

![第9話 ストーリーイラスト](illustrations/ep09_art.png)

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

### サプライチェーン攻撃の侵入経路 vs SBOMによる部品管理・防御

![サプライチェーン攻撃とSBOM](figures/fig09_supply_chain_sbom.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 本丸ではなく「脇道」を突く：サプライチェーン攻撃
大企業や重要インフラ組織は、厳重なセキュリティ投資を行っており正面突破は容易ではありません。そこで攻撃者が目をつけたのが、業務で繋がっている**「中小の下請け企業」「海外現地法人」「外部委託先」「取引先の保守端末」**です。
防備の薄い委託先のVPNやID・パスワードを突破し、そこから信頼関係（ネットワークの接続許可）を悪用して本丸の重要データを盗み出す手口を「サプライチェーン攻撃」と呼びます。2026年10月にも、内閣官房国家サイバー統括室や警察庁が事業者に向けた緊急対策要請を一斉に発出しています。

### 2. ソフトウェアの原材料表示：SBOM（Software Bill of Materials）とは？
私たちが日々利用している現代のアプリケーションは、開発者がゼロから書いたコードだけでなく、世界中の開発者が公開している**膨大な数のオープンソース（OSS）ライブラリやフレームワーク**が積み木のように組み合わさって動いています。
- もし、その中にある無名のライブラリ1つに致命的な脆弱性（セキュリティホール）が混入していたらどうなるでしょうか？
- どのアプリにどのバージョンの部品が使われているかを瞬時に把握するために生まれたのが**「SBOM（ソフトウェア部品構成表）」**です。
食品のパッケージに「小麦・大豆・卵」と原材料が明記されているように、ソフトウェアの全構成部品を機械可読な形式（SPDXやCycloneDX）で一覧化することで、海外で新たな脆弱性が公表された際も数分で影響範囲を特定できます。

### 3. 海外（米CISA）の動向：「Secure by Design」
米国CISA（サイバーセキュリティ・社会基盤安全保障庁）も、製品の設計段階から安全性を組み込む「Secure by Design」を強く提唱し、政府調達においてSBOMの提出を義務付けるなど、世界中でサプライチェーン全体の安全保障が国際ルールとなりつつあります。

### 4. 大学で学ぶ「ソフトウェア工学と信頼性数理」
大学の情報理工学部やシステム工学科では、複雑に絡み合うソフトウェアの依存関係グラフを数理的に分析し、脆弱性の波及経路を特定するアルゴリズムや、安全なソフトウェアサプライチェーンを構築するための自動検証技術を学びます。単なるプログラミングにとどまらず、**「社会を支える巨大システムの信頼性を数学的に保証する」**現代最先端の工学分野です。
"""
    out_file = os.path.join(CONTENT_DIR, "2026-10-24_ep09_supply_chain_attack_and_sbom.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ep09_md)
    print("SUCCESS: Ep09 completed and saved to:", out_file)

if __name__ == "__main__":
    run_ep09()
