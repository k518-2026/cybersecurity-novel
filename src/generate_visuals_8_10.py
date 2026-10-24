import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import render_tikz, generate_drawthings_image, ILLUST_DIR

# -------------------------------------------------------------
# Episode 8: Passkey & FIDO2
# -------------------------------------------------------------
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

prompt_ep08 = (
    "1boy, 1girl, smart Japanese high school boy with stylish glasses using fingerprint sensor on thin modern laptop, "
    "cute high school girl with dark ponytail smiling warmly holding a smartphone displaying a glowing green passkey shield icon, "
    "kind elegant female university professor pointing at biometric FIDO2 network diagram on clear digital glass display, "
    "bright futuristic high-tech computer science research seminar room, warm soft ambient lighting, clean desks, "
    "masterpiece, best quality, beautiful detailed anime art style, Makoto Shinkai aesthetic, Kyoto Animation style, "
    "perfect facial features, beautiful anime eyes, clear pupils, relaxed natural smiles, "
    "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
)

# -------------------------------------------------------------
# Episode 9: Supply Chain & SBOM
# -------------------------------------------------------------
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

  % 上段：サプライチェーン攻撃
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

  % 下段：対策（SBOM）
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

# -------------------------------------------------------------
# Episode 10: Zero-Day & Coordinated Disclosure
# -------------------------------------------------------------
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

prompt_ep10 = (
    "1boy, 1girl, smart Japanese high school boy with glasses looking proudly at laptop terminal with green verified security certificate, "
    "cute high school girl with dark ponytail smiling cheerfully beside him with open notebook, "
    "kind elegant female university cybersecurity professor standing warmly with gentle smile in state-of-the-art vulnerability analysis lab, "
    "background showing global threat map monitors and CVE database interface, bright modern sunlit university laboratory, "
    "masterpiece, best quality, beautiful detailed anime art style, Makoto Shinkai style, Kyoto Animation aesthetic, "
    "perfect facial features, beautiful anime eyes, clear pupils, relaxed natural smiles, "
    "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
)

if __name__ == "__main__":
    print("Rendering TikZ figures for Ep08, Ep09, Ep10...")
    render_tikz(tikz_ep08, "fig08_passkey_fido2_architecture")
    render_tikz(tikz_ep09, "fig09_supply_chain_sbom")
    render_tikz(tikz_ep10, "fig10_zero_day_coordinated_disclosure")

    print("Generating Draw Things illustrations (768x1024 / 20 steps)...")
    generate_drawthings_image(prompt_ep08, os.path.join(ILLUST_DIR, "ep08_art.png"))
    generate_drawthings_image(prompt_ep09, os.path.join(ILLUST_DIR, "ep09_art.png"))
    generate_drawthings_image(prompt_ep10, os.path.join(ILLUST_DIR, "ep10_art.png"))
    print("ALL VISUAL ASSETS GENERATED SUCCESSFULLY!")
