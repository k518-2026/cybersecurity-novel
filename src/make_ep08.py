import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import call_ollama, render_tikz, generate_drawthings_image, CONTENT_DIR, ILLUST_DIR

def run_ep08():
    print("=== Generating Episode 8: Passkey, FIDO2 & Passwordless ===")
    
    # 1. TikZ Figure: FIDO2 / Passkey Public Key Challenge-Response Architecture
    tikz_ep08 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{fidoamber}{RGB}{215, 120, 20}
\definecolor{goodgreen}{RGB}{30, 135, 55}
\definecolor{clientblue}{RGB}{20, 80, 150}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % 端末側（生体・所持・秘密鍵）
  \node[draw=clientblue, fill=blue!6, rounded corners=8pt, line width=1.5pt, minimum width=9.2cm, minimum height=7.2cm, align=center] (client_box) at (-5.4, 2.0) {};
  \node[above, font=\large\bfseries, text=clientblue] at (-5.4, 4.8) {【ユーザー端末】スマホ・PC（生体認証＋Secure Enclave）};

  \node[draw=clientblue, fill=white, rounded corners=6pt, thick, align=center, minimum width=7.6cm, minimum height=1.5cm] (bio_step) at (-5.4, 3.6) {
    \textbf{ローカル生体認証 (Touch ID / Face ID)}\\[2pt]
    \footnotesize ※生体データは端末外に一切送信されない！
  };

  \node[draw=goodgreen, fill=green!15, rounded corners=6pt, very thick, align=center, minimum width=7.6cm, minimum height=2.2cm] (key_step) at (-5.4, 0.8) {
    \textbf{\textcolor{goodgreen}{\large 端末内チップの「秘密鍵」で署名}}\\[3pt]
    \footnotesize サーバーから届いたランダムな合言葉（Challenge）に\\
    \footnotesize 端末内の秘密鍵でデジタル署名を作成！\\[2pt]
    \scriptsize $\Rightarrow$ 秘密鍵はチップ外に絶対に出ない（流出ゼロ！）
  };

  \draw[->, very thick, goodgreen] (bio_step.south) -- (key_step.north)
    node[midway, right=4pt, font=\scriptsize\bfseries, text=goodgreen] {本人確認完了};

  % サーバー側（公開鍵・チャレンジ生成・署名検証）
  \node[draw=fidoamber, fill=orange!6, rounded corners=8pt, line width=1.5pt, minimum width=9.2cm, minimum height=7.2cm, align=center] (server_box) at (5.4, 2.0) {};
  \node[above, font=\large\bfseries, text=fidoamber] at (5.4, 4.8) {【サービス提供者】Webサーバー・クラウド};

  \node[draw=fidoamber, fill=white, rounded corners=6pt, thick, align=center, minimum width=7.6cm, minimum height=1.5cm] (chal_step) at (5.4, 3.6) {
    \textbf{① 毎回異なる使い捨ての合言葉}\\[2pt]
    \footnotesize (Challenge コードを発行して端末へ送信)
  };

  \node[draw=fidoamber, fill=orange!15, rounded corners=6pt, very thick, align=center, minimum width=7.6cm, minimum height=2.2cm] (verify_step) at (5.4, 0.8) {
    \textbf{\textcolor{fidoamber}{\large ② 登録済みの「公開鍵」で署名検証}}\\[3pt]
    \footnotesize 署名が正しければログイン成功！\\[2pt]
    \scriptsize サーバーには「公開鍵」しか保存されていないため\\
    \scriptsize サーバーがハッキングされてもパスワード流出は原理的に不可能！
  };

  \draw[->, thick, dashed, clientblue] (chal_step.west) -- (bio_step.east)
    node[midway, above=4pt, font=\scriptsize\bfseries, text=clientblue] {Challenge 送信};

  \draw[->, very thick, goodgreen] (key_step.east) -- (verify_step.west)
    node[midway, above=4pt, font=\scriptsize\bfseries, text=goodgreen] {署名付き応答 (Response)};

  % 最下部：フィッシング耐性
  \node[draw=goodgreen, fill=green!25, rounded corners=6pt, line width=1.5pt, align=center, minimum width=20.0cm, inner sep=6pt] at (0, -2.4) {
    \textbf{\Large ★ なぜパスキーは「フィッシング詐欺」を100\%無効化できるのか？}\\[3pt]
    \small 端末はブラウザの正規ドメイン（FQDN）と厳格にバインドして署名するため、偽サイトにいくら騙されても署名が絶対に作成・送信されない！
  };

\end{tikzpicture}
\end{document}
"""
    render_tikz(tikz_ep08, "fig08_passkey_fido2_architecture")

    # 2. Draw Things Illustration: High-quality 768x1024 single scene
    prompt_ep08 = (
        "1boy, 1girl, smart Japanese high school boy with stylish glasses using fingerprint sensor on thin modern laptop, "
        "cute high school girl with dark ponytail smiling warmly holding a smartphone displaying a glowing green passkey shield icon, "
        "kind elegant female university professor pointing at biometric FIDO2 network diagram on clear digital glass display, "
        "bright futuristic high-tech computer science research seminar room, warm soft ambient lighting, clean desks, "
        "masterpiece, best quality, beautiful detailed anime art style, Makoto Shinkai aesthetic, Kyoto Animation style, "
        "perfect facial features, beautiful anime eyes, clear pupils, relaxed natural smiles, "
        "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
    )
    img_ep08_path = os.path.join(ILLUST_DIR, "ep08_art.png")
    generate_drawthings_image(prompt_ep08, img_ep08_path)

    # 3. Novel Text via Ollama
    novel_prompt = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生がデジタル庁・総務省の推進する最新のパスワードレス認証「パスキー（FIDO2）」の仕組みを学ぶ青春ライトノベル第8話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第8話 覚えない合言葉と手のひらの証明 〜パスキー（FIDO2）とパスワードのない未来〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・部長。「パスワードを長く複雑にするのに疲れた…そもそも覚える必要があること自体が人間の限界なのでは？」と悩む。
・橘 葵（たちばな あおい）：高校2年・部員。「スマホの指紋や顔認証でポチッと押すだけでログインできるパスキーって、裏で何が起きてるの？」と興味津々な女子高生。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 准教授。デジタル庁や総務省の認証ガイドライン検討にも関わる研究者。「覚えるパスワード」から「公開鍵暗号による数学的証明」への歴史的転換を優しく解説。

【必須要素】
1. デジタル庁の本人確認ガイドラインや総務省が推進する「パスキー（FIDO2）」の国家的な普及の背景
2. パスキーの仕組み：端末内のセキュアチップに「秘密鍵」を厳重保管し、生体認証（Touch ID/Face ID）で解錠、サーバーには「公開鍵」だけを預けるチャレンジ＆レスポンス認証
3. なぜ「サーバー攻撃」にも「フィッシング詐欺」にも無敵なのか？（サーバーには秘密情報がないため漏洩しない、ドメインと鍵が自動バインドされるため偽サイトには鍵が反応しない）
4. 海外ニュース（CISAやFIDOアライアンス）で数十億アカウントへ拡大する世界のパスワードレス潮流
5. 大学で学ぶ「暗号プロトコル検証・ハードウェアセキュリティ」への知的好奇心

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

    print("Generating Ep08 novel text with shosetsu on 192.168.128.62...")
    novel_body = call_ollama("shosetsu:latest", novel_prompt, timeout=300)

    # 4. Save Markdown
    ep08_md = f"""---
title: "第8話 覚えない合言葉と手のひらの証明 〜パスキー（FIDO2）とパスワードのない未来〜"
episode_num: 8
date: 2026-10-24
categories: ["高校生向けサイバーセキュリティライトノベル", "大学情報科学入門"]
tags: ["パスキー", "FIDO2", "パスワードレス", "デジタル庁", "総務省", "公開鍵暗号", "フィッシング耐性"]
---

# 第8話 覚えない合言葉と手のひらの証明 〜パスキー（FIDO2）とパスワードのない未来〜

> **【放課後サイバーディフェンス・ラボ】**
> - **舞台**: 県立青葉台高校 情報科学部 ＆ 帝都科学大学 次世代認証アーキテクチャ研究室
> - **登場人物**: 城崎 悠真（高校2年・部長）、橘 葵（高校2年・部員）、芹沢 涼香 准教授（大学メンター / IPAアドバイザー）
> - **学習テーマ**: パスキー（Passkey / FIDO2）の仕組み、チャレンジ＆レスポンス認証、フィッシング耐性、セキュアエレメント
> - **参照規格・政府公式情報**:
>   - [デジタル庁：本人確認ガイドライン・デジタル認証標準](https://www.digital.go.jp/)
>   - [総務省：パスキー普及促進方針・テレワークセキュリティガイドライン](https://www.soumu.go.jp/)
>   - [FIDO Alliance：FIDO2 / WebAuthn 仕様標準](https://fidoalliance.org/)
>   - [CISA（米国サイバーセキュリティ・社会基盤安全保障庁）：Phishing-Resistant MFA ガイダンス](https://www.cisa.gov/)

---

## 🎨 ストーリーイラスト (Draw Things 生成)

![第8話 ストーリーイラスト](illustrations/ep08_art.png)

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

### パスキー（FIDO2）の公開鍵チャレンジ＆レスポンス認証フロー

![パスキーとFIDO2の仕組み](figures/fig08_passkey_fido2_architecture.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. なぜ「パスワードを覚える時代」は終わるのか？
長年、私たちは「12文字以上で大文字・小文字・記号を混ぜ、使い回さず、定期的に変更する」という不可能な要求を強いられてきました。その結果、メモ帳への平文保存や簡単なパスワードの使い回しが蔓延し、多くの漏洩事件を引き起こしました。
これに対し、**デジタル庁や総務省、さらには米CISAが強力に推進しているのが「パスキー（Passkey / FIDO2）」**です。「人間が秘密を記憶する」のではなく、**「端末の安全なチップ（Secure Enclave等）に強固な暗号鍵を持たせ、本人は指紋や顔認証でそれを解錠するだけ」**という根本的なパラダイムシフトです。

### 2. パスキーが誇る2大絶対防御
- **① サーバー流出への耐性**:
  サービス事業者のサーバーに預けるのは「公開鍵」だけです。万一事業者のデータベースがハッキングされても、公開鍵は誰に見られても安全な鍵であるため、**パスワードのように不正ログインに使われることは原理的に不可能です**。
- **② フィッシング詐欺（偽サイト）への耐性**:
  パスキーはOSとブラウザが連携し、現在アクセスしている正規のWebサイトドメイン（例: `bank.example.co.jp`）と厳格にペアリングされています。もしユーザーがスミッシング等に騙されて巧妙な偽サイト（例: `bank.example.co.jp.scam.xyz`）を開いてしまっても、**ブラウザがドメイン不一致を検知して鍵署名を一切拒絶するため、フィッシング詐欺が100%成立しません**。

### 3. グローバル標準「FIDO2 / WebAuthn」の広がり
Apple、Google、Microsoftが全面協力し、2026年現在、世界で50億個以上のパスキーが稼働しています。金融機関や証券会社、通信キャリアでも「パスキー必須化」の動きが加速しており、パスワードレス認証は次世代社会の当たり前のインフラとなりつつあります。

### 4. 大学で学ぶ「耐タンパー性ハードウェアとプロトコル検証」
大学の情報工学部やハードウェアセキュリティ研究室では、暗号鍵を物理的なサイドチャネル攻撃（消費電力や電磁波の解析）から守る「耐タンパー（Tamper-resistant）技術」や、数理論理学を用いて暗号プロトコルに欠陥がないかを自動証明する「形式手法（Formal Methods）」を学びます。ソフトウェアとハードウェアが融合する最先端のセキュリティ工学の世界です。
"""
    out_file = os.path.join(CONTENT_DIR, "2026-10-24_ep08_passkey_and_fido2_passwordless.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(ep08_md)
    print("SUCCESS: Ep08 completed and saved to:", out_file)

if __name__ == "__main__":
    run_ep08()
