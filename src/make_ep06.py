import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import call_ollama, render_tikz, generate_drawthings_image, CONTENT_DIR, ILLUST_DIR

def run_ep06():
    print("=== Generating Episode 6: SQL Injection & Web Security ===")
    
    # 1. TikZ Figure: SQL Injection Principle & Prepared Statements (Sanitization)
    tikz_ep06 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{inputred}{RGB}{200, 30, 30}
\definecolor{safegreen}{RGB}{30, 135, 55}
\definecolor{dbblue}{RGB}{20, 80, 150}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % -------------------------------------------------------------
  % 上段：SQLインジェクションの脆弱性（未サニタイズによる命令混入）
  % -------------------------------------------------------------
  \node[draw=inputred, fill=red!6, rounded corners=8pt, line width=1.5pt, minimum width=18.5cm, minimum height=3.6cm, align=left] (vuln_box) at (0, 3.6) {};
  
  \node[above right, font=\large\bfseries, text=inputred] at (-9.0, 4.8) {【脆弱】SQLインジェクション：入力データが「命令（コード）」として解釈される危険};

  \node[draw=inputred, fill=white, rounded corners=4pt, thick, align=center, minimum width=4.8cm, minimum height=1.4cm] (atk_in) at (-6.2, 3.2) {
    \textbf{攻撃者の入力値}\\[2pt]
    \footnotesize \texttt{' OR '1'='1} (常に真になる命令)
  };

  \node[draw=black!70, fill=yellow!15, rounded corners=4pt, align=center, minimum width=6.8cm, minimum height=1.6cm] (app_concat) at (0.2, 3.2) {
    \textbf{脆弱な文字列連結}\\[2pt]
    \scriptsize \texttt{SELECT * FROM users WHERE pass = \textbf{\textcolor{inputred}{'' OR '1'='1}};}
  };

  \node[draw=dbblue, fill=blue!10, rounded corners=4pt, thick, align=center, minimum width=4.0cm, minimum height=1.4cm] (db_leak) at (6.6, 3.2) {
    \textbf{データベース}\\[2pt]
    \footnotesize \textcolor{inputred}{\textbf{全ユーザー情報が漏洩！}}
  };

  \draw[->, very thick, red] (atk_in.east) -- (app_concat.west);
  \draw[->, very thick, red] (app_concat.east) -- (db_leak.west);

  % -------------------------------------------------------------
  % 下段：安全なプレースホルダ（バインド機構・サニタイズ）
  % -------------------------------------------------------------
  \node[draw=safegreen, fill=green!6, rounded corners=8pt, line width=1.5pt, minimum width=18.5cm, minimum height=3.6cm, align=left] (safe_box) at (0, -1.2) {};
  
  \node[above right, font=\large\bfseries, text=safegreen] at (-9.0, 0.0) {【堅牢】プレースホルダ（Prepared Statement）：入力値を「純粋なデータ」として無害化};

  \node[draw=black!70, fill=white, rounded corners=4pt, thick, align=center, minimum width=4.8cm, minimum height=1.4cm] (norm_in) at (-6.2, -1.6) {
    \textbf{悪意ある入力値}\\[2pt]
    \footnotesize \texttt{' OR '1'='1}
  };

  \node[draw=safegreen, fill=green!15, rounded corners=4pt, very thick, align=center, minimum width=6.8cm, minimum height=1.6cm] (app_bind) at (0.2, -1.6) {
    \textbf{\textcolor{safegreen}{プレースホルダによるバインド処理}}\\[2pt]
    \scriptsize \texttt{SELECT * FROM users WHERE pass = \textbf{\textcolor{safegreen}{?}};}\\[1pt]
    \tiny ※入力値はただの「文字列」として厳格に扱われ、命令としては絶対に動かない！
  };

  \node[draw=dbblue, fill=blue!10, rounded corners=4pt, thick, align=center, minimum width=4.0cm, minimum height=1.4cm] (db_safe) at (6.6, -1.6) {
    \textbf{データベース}\\[2pt]
    \footnotesize \textcolor{safegreen}{\textbf{不正認証・漏洩を完全防御！}}
  };

  \draw[->, very thick, safegreen] (norm_in.east) -- (app_bind.west);
  \draw[->, very thick, safegreen] (app_bind.east) -- (db_safe.west);

\end{tikzpicture}
\end{document}
"""
    render_tikz(tikz_ep06, "fig06_sql_injection_defense")

    # 2. Draw Things Illustration: High-quality 768x1024 single scene
    prompt_ep06 = (
        "1boy, 1girl, smart Japanese high school boy with glasses coding web application on dual monitors, "
        "cute high school girl with ponytail pointing excitedly at the database code terminal, "
        "kind stylish female university computer science professor explaining SQL secure database architecture, "
        "modern high school programming computer club room, sunset light glowing through large windows, "
        "clean whiteboards with colorful system diagrams, comfortable high-tech room, "
        "masterpiece, best quality, beautiful detailed anime art style, Kyoto Animation aesthetic, "
        "perfect facial features, beautiful anime eyes, clear pupils, relaxed confident smiles, "
        "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
    )
    img_ep06_path = os.path.join(ILLUST_DIR, "ep06_art.png")
    generate_drawthings_image(prompt_ep06, img_ep06_path)

    # 3. Novel Text via Ollama
    novel_prompt = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生がWebアプリケーションの代表的脆弱性「SQLインジェクション」とセキュアプログラミングの基礎を学ぶ青春ライトノベル第6話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第6話 データベースの合言葉と呪文の罠 〜SQLインジェクションと安全なプログラミング〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・情報科学部長。文化祭用の部活紹介WebサイトとクイズアプリをPythonとSQLで自作開発中。
・橘 葵（たちばな あおい）：高校2年・部員。悠真の作ったログインフォームに、いたずら半分で記号を入力してテストする。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 准教授。悠真のコードを見て「データと命令を混ぜてはいけない」というセキュア開発の大原則を教える。

【必須要素】
1. Webフォームの入力欄に「' OR '1'='1」のような記号とSQL構文を打ち込むと、パスワードを知らなくてもログインできてしまう「SQLインジェクション」の原理
2. なぜ起こるのか？：プログラム内でSQL文を「文字列連結（concat）」で作ってしまうことが根本原因
3. 防ぎ方：プレースホルダ（Prepared Statement / バインド機構）を用いて「データ」と「命令」を物理的に分離する技術
4. サイバーセキュリティ.com等で頻発する、ECサイトの顧客情報・クレジットカード情報漏洩事件の生々しい実例
5. 大学で学ぶ「データベース論・形式言語理論・セキュアソフトウェア工学」への知的好奇心

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

    print("Generating Ep06 novel text with shosetsu on 192.168.128.62...")
    novel_body = call_ollama("shosetsu:latest", novel_prompt, timeout=300)

    # 4. Save Markdown
    ep06_md = f"""---
title: "第6話 データベースの合言葉と呪文の罠 〜SQLインジェクションと安全なプログラミング〜"
episode_num: 6
date: 2026-10-23
categories: ["高校生向けサイバーセキュリティライトノベル", "大学情報科学入門"]
tags: ["SQLインジェクション", "Webセキュリティ", "セキュアプログラミング", "プレースホルダ", "データベース", "IPAデジタルスキル標準"]
---

# 第6話 データベースの合言葉と呪文の罠 〜SQLインジェクションと安全なプログラミング〜

> **【放課後サイバーディフェンス・ラボ】**
> - **舞台**: 県立青葉台高校 情報科学部 ＆ 帝都科学大学
> - **登場人物**: 城崎 悠真（高校2年・部長）、橘 葵（高校2年・部員）、芹沢 涼香 准教授（大学メンター / IPAアドバイザー）
> - **学習テーマ**: SQLインジェクションの脆弱性原理、プレースホルダ（バインド機構）、データとコードの分離思想
> - **参照規格・公式情報**:
>   - [IPA：安全なウェブサイトの作り方（セキュリティ実装ガイダンス）](https://www.ipa.go.jp/security/vuln/websecurity.html)
>   - [OWASP Top 10：インジェクションの脅威](https://owasp.org/www-project-top-ten/)
>   - [サイバーセキュリティ.com：Webサイト改ざん・SQLインジェクション漏洩速報](https://cybersecurity-jp.com/news)

---

## 🎨 ストーリーイラスト (Draw Things 生成)

![第6話 ストーリーイラスト](illustrations/ep06_art.png)

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

### SQLインジェクションの攻撃原理 vs プレースホルダによる無害化防御

![SQLインジェクションとプレースホルダ](figures/fig06_sql_injection_defense.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 「データ」が「命令」に化ける恐怖：SQLインジェクション
Webサイトの検索窓やログインフォームに入力された文字列を、サーバー側でそのままSQL文（データベース操作言語）に文字列結合してしまうと、攻撃者は細工したSQLの欠片（例: `' OR '1'='1`）を送り込むことで、開発者の意図しないSQL命令を実行させてしまいます。
これにより、**「パスワードを知らなくても他人のアカウントで強制ログイン」「顧客データベース全体の不正抜き取り」「データの全削除」**など、壊滅的な被害が発生します。

### 2. 根本的な解決策：「プレースホルダ（Prepared Statement）」
SQLインジェクションを防ぐ世界標準の技術が**「プレースホルダ（バインド機構）」**です。
1. まずSQLの命令構造（骨組み）だけをデータベースにコンパイルさせて確定させる（例: `WHERE pass = ?`）。
2. 後からユーザーの入力値を「純粋なデータ（値）」として後付けで当てはめる。
この仕組みにより、どんなに巧妙なSQL構文が入力値に含まれていても、データベースはそれを**「ただの文字列データ」として機械的に処理するため、命令として暴走することは絶対にありません**。

### 3. 歴史とOWASP Top 10
SQLインジェクションは20年以上前から知られている古典的な脆弱性ですが、国際的なWebセキュリティ推進組織「OWASP（Open Worldwide Application Security Project）」の脅威ランキング（OWASP Top 10）において、常に上位にランクインし続けています。[サイバーセキュリティ.com](https://cybersecurity-jp.com/news)でも、中小ECサイトでの顧客クレジットカード情報漏洩事件の多くがSQLインジェクションを起点としています。

### 4. 大学で学ぶ「プログラミング言語論とデータベース理論」
大学の情報理工学部やコンピュータ科学科では、関係代数（リレーショナル代数）に基づくデータベースの基礎理論や、コンパイラがプログラムの構文木（AST: Abstract Syntax Tree）をどう解析するかという計算機科学の真髄を学びます。単にフレームワークを使うだけでなく、**「コンピュータが言葉をどう解釈しているのか」**を数理的に探求する面白さがここにあります。
"""
    out_file = os.path.join(CONTENT_DIR, "2026-10-23_ep06_sql_injection_and_web_security.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ep06_md)
    print("SUCCESS: Ep06 completed and saved to:", out_file)

if __name__ == "__main__":
    run_ep06()
