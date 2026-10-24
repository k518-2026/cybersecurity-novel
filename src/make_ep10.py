import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import call_ollama, render_tikz, generate_drawthings_image, CONTENT_DIR, ILLUST_DIR

def run_ep10():
    print("=== Generating Episode 10: Zero-Day & Coordinated Vulnerability Disclosure ===")
    
    # 1. TikZ Figure: Vulnerability Lifecycle & Zero-Day vs Coordinated Disclosure
    tikz_ep10 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{dangerred}{RGB}{200, 30, 30}
\definecolor{cveblue}{RGB}{20, 80, 160}
\definecolor{safeemerald}{RGB}{25, 130, 60}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % タイムライン軸
  \draw[->, line width=2pt, gray!80] (-9.5, 0) -- (9.5, 0)
    node[right, font=\footnotesize\bfseries] {時間経過 $\rightarrow$};

  % ステージ1: 脆弱性発見
  \node[draw=cveblue, fill=blue!10, rounded corners=6pt, thick, align=center, minimum width=4.0cm, minimum height=1.6cm] (s1) at (-7.5, 2.0) {
    \textbf{① 脆弱性の発見}\\[2pt]
    \footnotesize ホワイトハッカーが\\
    \footnotesize ソフトウェアのバグを発見
  };
  \draw[->, thick, cveblue] (s1.south) -- (-7.5, 0.2);

  % 悪夢の分岐：ゼロデイ攻撃
  \node[draw=dangerred, fill=red!15, rounded corners=6pt, very thick, align=center, minimum width=5.0cm, minimum height=2.2cm] (zero_day) at (-2.5, -2.4) {
    \textbf{\textcolor{dangerred}{\large 【脅威】ゼロデイ攻撃 (0-day)}}\\[3pt]
    \footnotesize パッチ（修正プログラム）が\\
    \footnotesize 存在しない「無防備な0日間」に\\
    \footnotesize 攻撃者が極秘に悪用・ハッキング！
  };
  \draw[->, line width=2pt, dashed, red] (-5.0, 0) -- (zero_day.north);

  % 正義の分岐：責任ある協調的開示 (Coordinated Disclosure)
  \node[draw=safeemerald, fill=green!10, rounded corners=6pt, thick, align=center, minimum width=4.8cm, minimum height=1.8cm] (s2) at (-1.8, 2.2) {
    \textbf{② 協調的開示 (CVD)}\\[2pt]
    \footnotesize 開発者へ非公開で報告\\
    \footnotesize JVN / CVE / CISAと連携し\\
    \footnotesize 極秘裏に修正パッチを開発
  };
  \draw[->, thick, safeemerald] (-1.8, 0.2) -- (s2.south);

  % ステージ3: パッチ公開 ＆ KEV / JVN 注意喚起
  \node[draw=safeemerald, fill=green!20, rounded corners=6pt, very thick, align=center, minimum width=5.6cm, minimum height=2.2cm] (s3) at (5.2, 2.2) {
    \textbf{\large ③ パッチ公開と注意喚起}\\[3pt]
    \footnotesize 修正版のリリースと同時に脆弱性を公表\\
    \footnotesize (CVE番号発番・JVN / CISA KEV登録)\\[2pt]
    \scriptsize $\Rightarrow$ 全世界が一斉にアップデート適用！
  };
  \draw[->, line width=2pt, safeemerald] (s2.east) -- (s3.west);
  \draw[->, thick, safeemerald] (5.2, 0.2) -- (s3.south);

  % 最下部注記
  \node[draw=black!70, fill=yellow!15, rounded corners=6pt, line width=1.2pt, align=center, minimum width=19.5cm, inner sep=6pt] at (0, -4.5) {
    \textbf{\Large ★ ホワイトハッカー（Ethical Hacker）の誇りと倫理}\\[3pt]
    \small 脆弱性を発見した際、闇市場に売ったり勝手に悪用すれば犯罪だが、適切に報告して世界を守る力に変えるのが情報倫理の真髄！
  };

\end{tikzpicture}
\end{document}
"""
    render_tikz(tikz_ep10, "fig10_zero_day_coordinated_disclosure")

    # 2. Draw Things Illustration: High-quality 768x1024 single scene
    prompt_ep10 = (
        "1boy, 1girl, smart Japanese high school boy with glasses looking proudly at laptop terminal with green verified security certificate, "
        "cute high school girl with dark ponytail smiling cheerfully beside him with open notebook, "
        "kind elegant female university cybersecurity professor standing warmly with gentle smile in state-of-the-art vulnerability analysis lab, "
        "background showing global threat map monitors and CVE database interface, bright modern sunlit university laboratory, "
        "masterpiece, best quality, beautiful detailed anime art style, Makoto Shinkai style, Kyoto Animation aesthetic, "
        "perfect facial features, beautiful anime eyes, clear pupils, relaxed natural smiles, "
        "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
    )
    img_ep10_path = os.path.join(ILLUST_DIR, "ep10_art.png")
    generate_drawthings_image(prompt_ep10, img_ep10_path)

    # 3. Novel Text via Ollama
    novel_prompt = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生が海外（The Hacker News, BleepingComputer, CISA）や国内（IPA/JVN）で注目される「ゼロデイ脆弱性と協調的開示（Coordinated Vulnerability Disclosure）」、そしてホワイトハッカーの倫理を学ぶ青春ライトノベル第10話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第10話 ゼロの日を越える翼 〜ゼロデイ脆弱性と世界を守るホワイトハッカー〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・部長。オープンソースのコードを読んでいて偶然不審なバグ（脆弱性）の芽を見つける。「これって悪用できちゃうんじゃ…？」と動揺する。
・橘 葵（たちばな あおい）：高校2年・部員。「もし悪いハッカーが先に見つけたら、修正パッチが出る前のゼロデイ攻撃になっちゃうんだよね…！」と真剣に受け止める女子高生。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 准教授。IPA脆弱性関連情報届出制度や米CISAのKEV（既知の悪用脆弱性カタログ）にも精通する専門家。悪用するクラッカーではなく、発見を世界中の盾に変える「協調的開示（CVD）」の崇高な倫理を導く。

【必須要素】
1. ゼロデイ脆弱性（0-day）の恐怖：修正パッチが存在しない期間に悪用される攻撃（海外メディアThe Hacker NewsやBleepingComputerで連日トップニュースとなる脅威）
2. ホワイトハッカー（正義のセキュリティ研究者）がバグを見つけた時の国際ルール「協調的脆弱性開示（Coordinated Vulnerability Disclosure: CVD）」とIPA/JPCERTの届出制度
3. CVE（共通脆弱性識別子）番号の発番、CVSSスコア（深刻度評価）、米CISAのKEV（Known Exploited Vulnerabilities）カタログによる緊急注意喚起の流れ
4. 「知識と技術は人を傷つけるためではなく、世界を支える盾にするためにある」という情報倫理の感動的な結び
5. 大学で学ぶ「高度サイバーセキュリティ技術者・セキュリティアナリスト」への進路の決意

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

    print("Generating Ep10 novel text with shosetsu on 192.168.128.62...")
    novel_body = call_ollama("shosetsu:latest", novel_prompt, timeout=300)

    # 4. Save Markdown
    ep10_md = f"""---
title: "第10話 ゼロの日を越える翼 〜ゼロデイ脆弱性と世界を守るホワイトハッカー〜"
episode_num: 10
date: 2026-10-24
categories: ["高校生向けサイバーセキュリティライトノベル", "大学情報科学入門"]
tags: ["ゼロデイ脆弱性", "ホワイトハッカー", "CVE", "協調的開示", "CISA", "JVN", "情報倫理", "IPAデジタルスキル標準"]
---

# 第10話 ゼロの日を越える翼 〜ゼロデイ脆弱性と世界を守るホワイトハッカー〜

> **【放課後サイバーディフェンス・ラボ】**
> - **舞台**: 県立青葉台高校 情報科学部 ＆ 帝都科学大学 先端脆弱性解析センター
> - **登場人物**: 城崎 悠真（高校2年・部長）、橘 葵（高校2年・部員）、芹沢 涼香 准教授（大学メンター / IPAアドバイザー）
> - **学習テーマ**: ゼロデイ（0-day）脆弱性の脅威、協調的脆弱性開示（CVD）、CVE/CVSS、ホワイトハッカーの情報倫理
> - **参照規格・国内外ニュース情報**:
>   - [IPA / JPCERT/CC：ソフトウエア等の脆弱性関連情報届出制度](https://www.ipa.go.jp/security/vuln/report/)
>   - [米CISA：Known Exploited Vulnerabilities Catalog (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
>   - [The Hacker News / BleepingComputer：国際的ゼロデイ攻撃・緊急脆弱性速報](https://thehackernews.com/)
>   - [内閣官房 国家サイバー統括室：脆弱性情報流通と官民連携方針](https://www.cyber.go.jp/)

---

## 🎨 ストーリーイラスト (Draw Things 生成)

![第10話 ストーリーイラスト](illustrations/ep10_art.png)

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

### 脆弱性のライフサイクル：ゼロデイ攻撃 vs 協調的開示（CVD）

![ゼロデイ脆弱性と協調的開示](figures/fig10_zero_day_coordinated_disclosure.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 防御側の準備が「ゼロ日」：ゼロデイ（0-day）攻撃とは？
ソフトウェアに未知の脆弱性（バグ）が見つかったとき、開発者が修正プログラム（パッチ）を公開する前、あるいは公開と同時に攻撃者がその穴を悪用することを**「ゼロデイ攻撃（Zero-Day Exploit）」**と呼びます。
防御側にとって「対策を打つ猶予期間が0日（ゼロ日）」であることからこの名がついています。海外の大手セキュリティメディア（*The Hacker News*や*BleepingComputer*）が連日速報する重大インシデントの多くが、このゼロデイ脆弱性を起点としています。

### 2. 世界を守る国際ルール：協調的脆弱性開示（CVD）
正義の研究者（ホワイトハッカー）が脆弱性を発見したとき、勝手にSNSで公開したりダークウェブで売却することは厳禁です。
1. **非公開での通報**: まず開発者（ベンダー）または各国の調整機関（日本のIPA/JPCERT・米国のCERT/CC等）に極秘裏に報告します。
2. **パッチの共同開発**: 開発者が修正プログラムを完成させるまで、情報は厳重に秘密に保たれます。
3. **同時公開**: パッチの配布準備が整った日に初めて、脆弱性の情報（CVE番号）と対策方法が世界へ一斉に公表されます。
この世界規模の協力体制を**「協調的脆弱性開示（Coordinated Vulnerability Disclosure: CVD）」**と呼びます。

### 3. CVEと米CISAの「KEVカタログ」
世界中で発見された脆弱性には、重複を防ぐため一意の識別番号**「CVE（Common Vulnerabilities and Exposures）」**が付与されます（例: CVE-2026-xxxxx）。さらに米CISA（サイバーセキュリティ・社会基盤安全保障庁）は、実際にサイバー攻撃で悪用されている深刻な脆弱性を**「KEV（既知の悪用脆弱性）カタログ」**に登録し、政府機関や民間企業へ強制的なパッチ適用期限を設けて注意を促しています。

### 4. 大学で学ぶ「リバースエンジニアリングとホワイトハッカーの倫理」
大学の情報理工学部や高度サイバー人材育成プログラムでは、バイナリ解析やファジング（自動バグ検出技術）といった高度な攻撃分析手法を学びます。強大な力を持つからこそ、**「技術を正義のために行使する倫理観（情報モラル・サイバー法）」**を身につけたホワイトハッカーは、国家やグローバル社会から今もっとも求められている守護者です。
"""
    out_file = os.path.join(CONTENT_DIR, "2026-10-24_ep10_zero_day_and_white_hackers.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ep10_md)
    print("SUCCESS: Ep10 completed and saved to:", out_file)

if __name__ == "__main__":
    run_ep10()
