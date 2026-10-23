import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import call_ollama, render_tikz, generate_drawthings_image, CONTENT_DIR, ILLUST_DIR

def run_ep02():
    print("=== Generating Episode 2: Phishing & Domain/Certificates ===")
    
    # 1. TikZ Figure
    tikz_ep02 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{goodblue}{RGB}{20, 80, 140}
\definecolor{badred}{RGB}{190, 30, 30}
\definecolor{bgblue}{RGB}{236, 246, 255}
\definecolor{bgred}{RGB}{255, 238, 238}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % 正規URLの解剖
  \node[draw=goodblue, fill=bgblue, rounded corners=8pt, line width=1.5pt, minimum width=18.5cm, minimum height=2.8cm, align=left] (real) at (0, 4.0) {
    \textbf{\Large 【正規のURL構造とSSL/TLS証明書】}\\[4pt]
    \large \texttt{https://\textbf{\textcolor{goodblue}{bank.example.co.jp}}/login/}\\[5pt]
    \footnotesize
    \begin{tabular}{lll}
      \textbf{プロトコル:} \texttt{https://} (暗号化通信) & \textbf{組織名:} \texttt{bank.example} & \textbf{国・属性ドメイン:} \texttt{.co.jp} (日本法人厳格審査)
    \end{tabular}\\[3pt]
    \footnotesize \textbf{\textcolor{goodblue}{鍵マークの真実:}} 通信は暗号化されているが、「サイト運営者が本物か」はドメイン名（FQDN）で確認！
  };

  % 偽URL（フィッシング）の罠
  \node[draw=badred, fill=bgred, rounded corners=8pt, line width=1.5pt, minimum width=18.5cm, minimum height=2.8cm, align=left] (fake) at (0, 0.4) {
    \textbf{\Large 【フィッシング詐欺サイトの巧妙な偽装URL】}\\[4pt]
    \large \texttt{https://\textbf{\textcolor{badred}{bank.example.co.jp.sec-update.xyz}}/login/}\\[5pt]
    \footnotesize
    \begin{tabular}{lll}
      \textbf{プロトコル:} \texttt{https://} (無料証明書で偽装) & \textbf{騙しのサブドメイン:} \texttt{bank.example.co.jp.} & \textbf{真のドメイン:} \texttt{\textbf{\textcolor{badred}{sec-update.xyz}}}
    \end{tabular}\\[3pt]
    \footnotesize \textbf{\textcolor{badred}{危険な誤認:}} 「httpsや鍵マークがあるから安全」は大間違い！ 攻撃者も証明書を取得して罠を張る！
  };

  % チェックポイント
  \node[draw=black!70, fill=yellow!15, rounded corners=6pt, line width=1.2pt, minimum width=18.5cm, minimum height=1.8cm, align=center] (point) at (0, -2.6) {
    \textbf{\large ★ フィッシング詐欺を見抜く3原則（IPA デジタルスキル標準）}\\[3pt]
    \small 1. メールのリンクではなく\textbf{公式ブックマークや公式アプリ}からアクセスする\\[2pt]
    \small 2. 末尾のドメイン（トップレベル〜セカンドレベル）が本物の企業と一致しているか確認する
  };

  \draw[->, very thick, red] (real.south) -- (fake.north);

\end{tikzpicture}
\end{document}
"""
    render_tikz(tikz_ep02, "fig02_phishing_domain_structure")

    # 2. Draw Things Illustration (Boy + Girl + Mentor)
    prompt_ep02 = (
        "Vertical four-panel comic strip, Japanese yonkoma manga layout, "
        "4 rectangular panels stacked vertically from top to bottom with clean white borders, full color Japanese anime art style. "
        "Panel 1: A smart Japanese high school boy with short black hair and glasses showing a suspicious delivery SMS on his smartphone to a cute high school girl in high school computer room. "
        "Panel 2: A stylish, cool female university professor pointing at domain structure on digital screen, explaining fake phishing URLs to the boy and girl. "
        "Panel 3: The high school boy nodding with deep understanding while typing on laptop terminal, comparing real vs fake domain names. "
        "Panel 4: High school boy, high school girl, and female professor all smiling together proudly and warmly in sunny modern computer lab. "
        "Masterpiece anime comic strip, clean panel division, rich vibrant colors, high contrast, crisp lineart, completely pure illustration, "
        "detailed anime eyes, soft relaxed expression, natural warm smiles, NO speech bubbles, NO text, NO words, NO letters, NO Japanese text."
    )
    img_ep02_path = os.path.join(ILLUST_DIR, "ep02_4koma.png")
    generate_drawthings_image(prompt_ep02, img_ep02_path)

    # 3. Novel Text via Ollama
    novel_prompt = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生がサイバーセキュリティ（フィッシング詐欺とURL・電子証明書の仕組み）を学ぶ青春ライトノベル第2話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第2話 偽りの手紙と本物の目印 〜フィッシング詐欺の見抜き方とURLの秘密〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・情報科学部長。冷静沈着で理系男子。スマホに届いた怪しい不在通知SMSの不審点に気づく。
・橘 葵（たちばな あおい）：高校2年・情報科学部員。元気な女子高生。あやうくURLをタップしそうになる。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 サイバーセキュリティ研究室 准教授。IPAアドバイザー。

【必須要素】
1. 宅配便や金融機関を装うスミッシング（SMSフィッシング）の手口と心理誘導（ソーシャルエンジニアリング：緊急性・不安を煽る手口）
2. URL・ドメイン名（FQDN）の右から左へ読む階層構造（ccTLD, gTLD, 組織ドメイン, サブドメインの罠）
3. 「HTTPS（鍵マーク）があるから安全」という高校生が陥りがちな誤解と、SSL/TLS証明書が保証する「暗号化」と「身元確認」の真実
4. サイバーセキュリティ.com等で頻発するフィッシング詐欺被害のリアルな事例
5. 大学で情報科学・ネットワーク技術を学ぶ魅力

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

    print("Generating Ep02 novel text with shosetsu on 192.168.128.62...")
    novel_body = call_ollama("shosetsu:latest", novel_prompt, timeout=300)

    # 4. Save Markdown
    ep02_md = f"""---
title: "第2話 偽りの手紙と本物の目印 〜フィッシング詐欺の見抜き方とURLの秘密〜"
episode_num: 2
date: 2026-10-23
categories: ["高校生向けサイバーセキュリティライトノベル", "大学情報科学入門"]
tags: ["フィッシング詐欺", "ソーシャルエンジニアリング", "URL構造", "SSL/TLS電子証明書", "IPAデジタルスキル標準", "国家サイバー統括室"]
---

# 第2話 偽りの手紙と本物の目印 〜フィッシング詐欺の見抜き方とURLの秘密〜

> **【放課後サイバーディフェンス・ラボ】**
> - **舞台**: 県立青葉台高校 情報科学部 ＆ 帝都科学大学 情報科学部 サイバーセキュリティ研究室
> - **登場人物**: 城崎 悠真（高校2年・部長）、橘 葵（高校2年・部員）、芹沢 涼香 准教授（大学メンター / IPAアドバイザー）
> - **学習テーマ**: スミッシングとソーシャルエンジニアリング、URLの階層構造、電子証明書（HTTPS）の真実
> - **参照規格・公式情報**:
>   - [IPA 独立行政法人 情報処理推進機構：デジタルスキル標準（DSS）](https://www.ipa.go.jp/jinzai/skill-standard/dss/index.html)
>   - [内閣官房 国家サイバー統括室：フィッシング対策方針](https://www.cyber.go.jp/)
>   - [サイバーセキュリティ.com：フィッシング詐欺・偽装サイト被害速報](https://cybersecurity-jp.com/news)

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第2話 4コマ漫画イラスト](illustrations/ep02_4koma.png)

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

### 正規URL vs フィッシング詐欺サイトのドメイン構造比較

![正規URL vs フィッシングサイトのURL構造](figures/fig02_phishing_domain_structure.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 「人の心の隙」を突くソーシャルエンジニアリング
フィッシング詐欺（Phishing）やスミッシング（SMSフィッシング）は、高度なコンピュータ攻撃というよりも、「緊急！荷物のお届け」「24時間以内に確認しないとアカウント凍結」など、**人間の恐怖や焦燥感・好奇心を利用して冷静な判断を奪う「ソーシャルエンジニアリング」**です。

### 2. URLを「右から左」に読む技術
URLのホスト名部分は、ピリオドで区切られた右側から階層が上がっていきます。
- 例: `login.example.co.jp` の場合、本体は `.co.jp` の中にある `example` という企業組織です。
- 詐欺サイトの手口: `example.co.jp.sec-login.xyz` のように、左側に有名企業の名前を並べて安心させ、**真のドメイン末尾を怪しい文字列（`.xyz` 等）に偽装**します。必ず「プロトコル（https://）の直後ではなく、最初のスラッシュ（/）の直前」に注目する習慣をつけましょう。

### 3. 「鍵マーク（HTTPS）があるから安心」は時代遅れ？
かつて「通信が暗号化されている（HTTPS）＝ 安全なサイト」と言われた時代もありましたが、現在は攻撃者自身も無料のSSL/TLS証明書を簡単に取得できます。
- **HTTPSが保証すること**: 端末とサーバー間の通信が途中で盗聴・改ざんされていないこと。
- **HTTPSが保証しないこと**: そのサーバーの運営者が詐欺師ではないこと。
「鍵マークがある詐欺サイト」が当たり前になった現代だからこそ、ドメイン名そのものを確かめるリテラシーが不可欠です。

### 4. 大学で学ぶ「ネットワーク工学と暗号技術」
大学の情報系学部では、インターネットの名前解決を支える「DNS（Domain Name System）」の階層アーキテクチャや、第三者認証機関（CA）による公開鍵暗号基盤（PKI）の数学的証明、Webアプリケーションの脆弱性検出を体系的に学びます。ネットの土台を理解することで、巧妙な詐欺攻撃の構造が手にとるように見えてくる面白さがあります。
"""
    out_file = os.path.join(CONTENT_DIR, "2026-10-23_ep02_phishing_and_social_engineering.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ep02_md)
    print("SUCCESS: Ep02 completed and saved to:", out_file)

if __name__ == "__main__":
    run_ep02()
