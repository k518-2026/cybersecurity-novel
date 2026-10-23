import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import call_ollama, render_tikz, generate_drawthings_image, CONTENT_DIR, ILLUST_DIR

def run_ep05():
    print("=== Generating Episode 5: CIA Triad & Defense in Depth ===")
    
    # 1. TikZ Figure: CIA Triad & Concentric Defense in Depth
    tikz_ep05 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{ciablue}{RGB}{20, 80, 150}
\definecolor{ciagreen}{RGB}{30, 135, 55}
\definecolor{ciaorange}{RGB}{215, 100, 25}
\definecolor{corebg}{RGB}{245, 248, 255}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % -------------------------------------------------------------
  % 左側：CIAの3要素（情報セキュリティの三位一体）
  % -------------------------------------------------------------
  \node[above, font=\large\bfseries, text=ciablue] at (-5.0, 5.2) {【情報セキュリティの3大要素（CIA）】};

  % 三角形配置の3大要素
  \node[draw=ciablue, fill=blue!10, rounded corners=8pt, line width=1.5pt, minimum width=4.6cm, minimum height=2.2cm, align=center] (c) at (-5.0, 3.8) {
    \textbf{\large Ｃ：機密性}\\[3pt]
    \footnotesize (Confidentiality)\\[3pt]
    \scriptsize 許可された人だけが情報にアクセスできる\\（暗号化、アクセス権限、認証）
  };

  \node[draw=ciagreen, fill=green!10, rounded corners=8pt, line width=1.5pt, minimum width=4.6cm, minimum height=2.2cm, align=center] (i) at (-7.5, 0.4) {
    \textbf{\large Ｉ：完全性}\\[3pt]
    \footnotesize (Integrity)\\[3pt]
    \scriptsize 情報が改ざん・破壊されず正確である\\（ハッシュ値、電子署名、バックアップ）
  };

  \node[draw=ciaorange, fill=orange!10, rounded corners=8pt, line width=1.5pt, minimum width=4.6cm, minimum height=2.2cm, align=center] (a) at (-2.5, 0.4) {
    \textbf{\large Ａ：可用性}\\[3pt]
    \footnotesize (Availability)\\[3pt]
    \scriptsize 必要な時にいつでも情報を使える\\（二重化、DDoS対策、耐障害性）
  };

  \draw[<->, very thick, gray!70] (c.south west) -- (i.north);
  \draw[<->, very thick, gray!70] (c.south east) -- (a.north);
  \draw[<->, very thick, gray!70] (i.east) -- (a.west);

  \node[below, font=\scriptsize, align=center] at (-5.0, -1.0) {
    どれか1つが欠けてもシステムは崩壊する！\\[2pt]
    【例】DDoS攻撃＝可用性破壊、改ざん＝完全性破壊、流出＝機密性破壊
  };

  % -------------------------------------------------------------
  % 右側：多層防御（Defense in Depth）同心円モデル
  % -------------------------------------------------------------
  \node[above, font=\large\bfseries, text=ciablue] at (5.5, 5.2) {【多層防御（Defense in Depth）】};

  % 外側から内側への円
  \fill[blue!8] (5.5, 1.8) circle (3.2cm);
  \draw[blue!60, very thick] (5.5, 1.8) circle (3.2cm);
  \node[above, font=\footnotesize\bfseries, text=blue!80] at (5.5, 4.4) {第1層：入口対策（ファイアウォール・WAF・フィルタ）};

  \fill[blue!18] (5.5, 1.8) circle (2.2cm);
  \draw[blue!80, very thick] (5.5, 1.8) circle (2.2cm);
  \node[above, font=\footnotesize\bfseries, text=blue!90] at (5.5, 3.4) {第2層：内部対策（EDR・最小権限・セグメント）};

  \fill[blue!30] (5.5, 1.8) circle (1.2cm);
  \draw[ciablue, line width=1.5pt] (5.5, 1.8) circle (1.2cm);
  \node[above, font=\footnotesize\bfseries, text=ciablue] at (5.5, 2.4) {第3層：出口対策};

  \node[draw=red!80, fill=white, rounded corners=4pt, thick, align=center, inner sep=3pt] at (5.5, 1.5) {
    \textbf{\textcolor{red!80}{重要データ}}\\[1pt]
    \tiny (暗号化保管)
  };

  \node[below, font=\scriptsize, align=center] at (5.5, -1.0) {
    「1枚の壁」が突破されても次で止める！\\[2pt]
    入口・内部・出口の三位一体で重要資産を護り抜く
  };

\end{tikzpicture}
\end{document}
"""
    render_tikz(tikz_ep05, "fig05_cia_and_defense_in_depth")

    # 2. Draw Things Illustration: High-quality 768x1024 single scene
    prompt_ep05 = (
        "1boy, 1girl, smart Japanese high school boy with stylish glasses and school blazer, "
        "cute high school girl with dark brown ponytail smiling happily, "
        "kind elegant female university professor holding a glowing holographic pyramid model representing security CIA triad, "
        "high-tech university cybersecurity command center, transparent glass boards with system network graphs, "
        "soft futuristic blue ambient lighting, clean modern desks, sunlit windows in background, "
        "masterpiece, best quality, beautiful detailed anime art style, Makoto Shinkai style, Kyoto Animation aesthetic, "
        "perfect facial features, beautiful anime eyes, clear pupils, relaxed warm smiles, "
        "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
    )
    img_ep05_path = os.path.join(ILLUST_DIR, "ep05_art.png")
    generate_drawthings_image(prompt_ep05, img_ep05_path)

    # 3. Novel Text via Ollama
    novel_prompt = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生がサイバーセキュリティの根幹概念（情報セキュリティの3要素CIAと多層防御）を学ぶ青春ライトノベル第5話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第5話 三つの宝珠を守る城壁 〜情報セキュリティの3大要素（CIA）と多層防御〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・情報科学部長。冷静沈着で理系男子。「データを暗号化して鍵を厳重にすれば完璧なのでは？」と考えていた。
・橘 葵（たちばな あおい）：高校2年・部員。「暗号化しても、学校のサーバーが落ちて成績表が見られなくなったら大問題だよね！」と直感的に気づく女子高生。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 サイバーセキュリティ研究室 准教授。CIA（機密性・完全性・可用性）のバランスと、城郭建築のような「多層防御」の哲学を説く。

【必須要素】
1. セキュリティの3大要素「CIA」：
   - 機密性（Confidentiality）：許可された人だけが見られる（暗号化、アクセス制限）
   - 完全性（Integrity）：改ざんされず正しい状態が保たれている（ハッシュ、デジタル署名）
   - 可用性（Availability）：必要な時にいつでも使える（DDoS対策、二重化、バックアップ）
2. なぜ「機密性」だけではダメなのか？（可用性が破壊されるランサムウェアやDDoS攻撃、完全性が破壊されるWeb改ざんの恐怖）
3. 多層防御（Defense in Depth）：外壁（入口対策）、内郭（内部対策・EDR）、天守閣（出口対策・データ暗号化）という何重もの防壁
4. サイバーセキュリティ.com等で報じられるDDoS攻撃によるサービス停止事件やバックアップ破壊のリアル
5. 大学で学ぶ「セキュリティガバナンスとシステム設計論」への知的な憧れ

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

    print("Generating Ep05 novel text with shosetsu on 192.168.128.62...")
    novel_body = call_ollama("shosetsu:latest", novel_prompt, timeout=300)

    # 4. Save Markdown
    ep05_md = f"""---
title: "第5話 三つの宝珠を守る城壁 〜情報セキュリティの3大要素（CIA）と多層防御〜"
episode_num: 5
date: 2026-10-23
categories: ["高校生向けサイバーセキュリティライトノベル", "大学情報科学入門"]
tags: ["CIAの3要素", "機密性", "完全性", "可用性", "多層防御", "DDoS攻撃", "IPAデジタルスキル標準", "国家サイバー統括室"]
---

# 第5話 三つの宝珠を守る城壁 〜情報セキュリティの3大要素（CIA）と多層防御〜

> **【放課後サイバーディフェンス・ラボ】**
> - **舞台**: 県立青葉台高校 情報科学部 ＆ 帝都科学大学先端サイバー防衛指令室
> - **登場人物**: 城崎 悠真（高校2年・部長）、橘 葵（高校2年・部員）、芹沢 涼香 准教授（大学メンター / IPAアドバイザー）
> - **学習テーマ**: CIAの3要素（機密性・完全性・可用性）、真正性と責任追跡性、多層防御（入口・内部・出口対策）
> - **参照規格・公式情報**:
>   - [IPA 独立行政法人 情報処理推進機構：デジタルスキル標準（DSS）セキュリティアーキテクチャ](https://www.ipa.go.jp/jinzai/skill-standard/dss/index.html)
>   - [内閣官房 国家サイバー統括室：サイバーセキュリティ基本法と重要インフラ防護](https://www.cyber.go.jp/)
>   - [サイバーセキュリティ.com：DDoS攻撃・システムダウン・Web改ざん被害速報](https://cybersecurity-jp.com/news)

---

## 🎨 ストーリーイラスト (Draw Things 生成)

![第5話 ストーリーイラスト](illustrations/ep05_art.png)

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

### CIAの3大要素と多層防御（同心円モデル）

![CIAの3大要素と多層防御](figures/fig05_cia_and_defense_in_depth.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. セキュリティの土台を支える「CIA」とは？
情報セキュリティとは、単に「パスワードをかけて漏洩を防ぐ（機密性）」ことだけではありません。国際標準（ISO/IEC 27001）やIPAでも定義される以下の3本柱がバランスよく満たされて初めて、安全なシステムと言えます。
- **C（Confidentiality: 機密性）**: 適切な権限を持つ人だけが情報にアクセスできること。（漏洩防止・暗号化）
- **I（Integrity: 完全性）**: 情報が正確であり、改ざんや欠落がないこと。（改ざん検知・ハッシュ値）
- **A（Availability: 可用性）**: 必要な時に、いつでも遅延なくサービスを利用できること。（二重化・耐障害性）

### 2. 「可用性」を狙い撃ちにするDDoS攻撃
大量のパソコンやIoT機器を乗っ取って一斉に標的サーバーへ無駄な通信を送りつける**「DDoS（分散型サービス不能）攻撃」**は、機密性を盗むのではなく**「可用性をゼロにして業務を停止させる」攻撃**です。チケット予約サイトやオンラインゲーム、自治体サイトがアクセス集中でダウンさせられるのは、まさに可用性が脅かされた実例です。

### 3. お城に学ぶ「多層防御（Defense in Depth）」の極意
中世の堅牢な城は、一本の堀や一つの門だけで守られていたわけではありません。
- **入口対策（外堀・大手門）**: ファイアウォールやWAFで不正侵入を水際でブロック。
- **内部対策（城内の迷路・内郭）**: たとえ門が破られても、EDR（エンドポイント検知）やネットワーク分離で被害拡大を防ぐ。
- **出口対策（天守閣の宝物庫）**: 侵入者がデータを持ち出そうとしても暗号化や持ち出し遮断（DLP）で阻止する。
「100%破られない壁はない」という前提に立ち、何重もの盾を用意するのが現代サイバーセキュリティの神髄です。

### 4. 大学で学ぶ「セキュリティガバナンスとリスクマネジメント」
大学の情報社会科学部や経営情報学科、先端工学部では、技術的なプログラミングだけでなく、「限られた予算と時間の中で、どの資産をどう多層防御で守るべきか」という**リスク分析手法やセキュリティガバナンス**を学びます。社会全体の重要インフラを俯瞰し、守護の戦略を立てる「セキュリティストラテジスト（CISO）」への道が開かれています。
"""
    out_file = os.path.join(CONTENT_DIR, "2026-10-23_ep05_cia_triad_and_defense_in_depth.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ep05_md)
    print("SUCCESS: Ep05 completed and saved to:", out_file)

if __name__ == "__main__":
    run_ep05()
