import os
import sys

BASE_DIR = r"e:\GoogleAntigravity\books\cybersecurity-novel"
sys.path.append(BASE_DIR)
from src.generator_pipeline import render_tikz, generate_drawthings_image, call_ollama, CONTENT_DIR, ILLUST_DIR

# -------------------------------------------------------------
# Episode 11: Digital Forensics & Cyber Law (不正アクセス禁止法)
# -------------------------------------------------------------
tikz_ep11 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{lawnavy}{RGB}{20, 60, 130}
\definecolor{auditgreen}{RGB}{25, 125, 50}
\definecolor{alertred}{RGB}{190, 30, 30}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % -------------------------------------------------------------
  % 上段：インシデント発生時の証拠保全（デジタル・フォレンジックの黄金律）
  % -------------------------------------------------------------
  \node[draw=lawnavy, fill=blue!6, rounded corners=8pt, line width=1.5pt, minimum width=20.0cm, minimum height=3.8cm, align=left] (forensics_box) at (0, 3.8) {};
  
  \node[above right, font=\large\bfseries, text=lawnavy] at (-9.8, 5.1) {【技術】デジタル・フォレンジック（電子鑑識）：サイバー空間の現場検証};

  \node[draw=alertred, fill=red!15, rounded corners=6pt, thick, align=center, minimum width=5.2cm, minimum height=1.6cm] (step1) at (-6.5, 3.2) {
    \textbf{① 証拠の保全（書き込み禁止）}\\[2pt]
    \footnotesize ライトブロッカー経由で接続\\
    \footnotesize 電源を切らず揮発性メモリ(RAM)も回収
  };

  \node[draw=lawnavy, fill=white, rounded corners=6pt, thick, align=center, minimum width=5.2cm, minimum height=1.6cm] (step2) at (0.0, 3.2) {
    \textbf{② ビット単位の完全複製（Image）}\\[2pt]
    \footnotesize オリジナルを触らずクローンを作成\\
    \footnotesize SHA-256ハッシュ値で同一性を証明
  };

  \node[draw=auditgreen, fill=green!15, rounded corners=6pt, very thick, align=center, minimum width=5.2cm, minimum height=1.6cm] (step3) at (6.5, 3.2) {
    \textbf{\large ③ タイムライン復元・解析}\\[2pt]
    \footnotesize 削除された痕跡や通信ログを復元\\
    \footnotesize 不正侵入の経路と時刻を完全特定！
  };

  \draw[->, very thick, lawnavy] (step1.east) -- (step2.west);
  \draw[->, very thick, lawnavy] (step2.east) -- (step3.west);

  % -------------------------------------------------------------
  % 下段：不正アクセス禁止法と法執行・キャリア
  % -------------------------------------------------------------
  \node[draw=auditgreen, fill=green!6, rounded corners=8pt, line width=1.5pt, minimum width=20.0cm, minimum height=3.8cm, align=left] (law_box) at (0, -1.4) {};
  
  \node[above right, font=\large\bfseries, text=auditgreen] at (-9.8, -0.1) {【法律・職業】不正アクセス禁止法（第3条）とサイバー鑑識官・セキュリティ捜査官};

  \node[draw=lawnavy, fill=blue!15, rounded corners=6pt, thick, align=center, minimum width=9.0cm, minimum height=1.8cm] (law_def) at (-4.8, -2.0) {
    \textbf{\large 不正アクセス行為の3大類型}\\[3pt]
    \footnotesize ① 他人のパスワード・識別符号を無断入力する行為\\
    \footnotesize ② セキュリティホールを突いて制限を免れる行為\\
    \footnotesize ③ 他人のパスワードを不正に取得・提供する行為
  };

  \node[draw=auditgreen, fill=green!20, rounded corners=6pt, very thick, align=center, minimum width=9.0cm, minimum height=1.8cm] (career) at (4.8, -2.0) {
    \textbf{\Large 未来の仕事：デジタル捜査官＆CSIRT}\\[3pt]
    \footnotesize 警察サイバー犯罪対策課・民間インシデント対応チーム\\
    \small \textbf{\textcolor{lawnavy}{数学・PCアーキテクチャ・法律を駆使して社会の正義を守る！}}
  };

  \draw[->, very thick, auditgreen] (law_def.east) -- (career.west);

\end{tikzpicture}
\end{document}
"""

prompt_ep11 = (
    "1boy, 1girl, smart Japanese high school boy with glasses analyzing forensic timeline logs on dual monitors, "
    "cute high school girl with ponytail pointing enthusiastically at a reconstructed network packet chart on digital tablet, "
    "kind stylish female university professor explaining digital forensic evidence procedures and cyber law, "
    "modern high-tech cyber defense command room, clean wooden desks, digital whiteboard with evidence chain diagrams, "
    "warm afternoon sunlight through windows, collaborative studying, teamwork, active learning, "
    "masterpiece, best quality, beautiful detailed anime art style, Kyoto Animation aesthetic, "
    "perfect facial features, beautiful anime eyes, clear pupils, relaxed confident smiles, "
    "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
)

# -------------------------------------------------------------
# Episode 12: LAN, Routers & Network Troubleshooting
# -------------------------------------------------------------
tikz_ep12 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{privgreen}{RGB}{30, 130, 60}
\definecolor{pubblue}{RGB}{20, 80, 160}
\definecolor{routerorange}{RGB}{215, 110, 20}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % -------------------------------------------------------------
  % 左側：家庭・学校のプライベートLAN
  % -------------------------------------------------------------
  \node[draw=privgreen, fill=green!6, rounded corners=8pt, line width=1.5pt, minimum width=8.8cm, minimum height=7.2cm, align=center] (lan_box) at (-5.4, 2.0) {};
  \node[above, font=\large\bfseries, text=privgreen] at (-5.4, 4.8) {【プライベートLAN】学校・自宅のネットワーク};

  \node[draw=privgreen, fill=white, rounded corners=4pt, thick, align=center, minimum width=7.2cm, minimum height=1.3cm] (lan_pc) at (-5.4, 3.8) {
    \textbf{高校生パソコン (DHCPで自動割当)}\\[2pt]
    \footnotesize IP: \texttt{192.168.1.15} / MAC: \texttt{00:1A:2B:...}
  };

  \node[draw=privgreen, fill=white, rounded corners=4pt, thick, align=center, minimum width=7.2cm, minimum height=1.3cm] (lan_phone) at (-5.4, 2.0) {
    \textbf{高校生スマホ}\\[2pt]
    \footnotesize IP: \texttt{192.168.1.24}
  };

  \node[draw=black!70, fill=yellow!15, rounded corners=4pt, align=center, minimum width=7.2cm, minimum height=1.5cm] (lan_dns) at (-5.4, 0.0) {
    \textbf{DNSキャッシュサーバー}\\[2pt]
    \footnotesize \texttt{www.example.com} $\rightarrow$ \texttt{203.0.113.80}\\
    \scriptsize ドメイン名をIPアドレスに電話帳のように変換！
  };

  % -------------------------------------------------------------
  % 中央：ルーター（NAT / NAPT：ポート番号で振り分け）
  % -------------------------------------------------------------
  \node[draw=routerorange, fill=orange!20, rounded corners=8pt, line width=2pt, align=center, minimum width=4.0cm, minimum height=4.2cm] (router) at (0.0, 2.0) {
    \textbf{\Large ルーター}\\[4pt]
    \textbf{\large (NAT / NAPT)}\\[4pt]
    \footnotesize プライベートIP と\\
    \footnotesize グローバルIP を\\
    \footnotesize 相互変換！\\[3pt]
    \scriptsize 内外を遮断する\\
    \scriptsize 最初のファイアウォール
  };

  % -------------------------------------------------------------
  % 右側：グローバルインターネット
  % -------------------------------------------------------------
  \node[draw=pubblue, fill=blue!6, rounded corners=8pt, line width=1.5pt, minimum width=8.8cm, minimum height=7.2cm, align=center] (wan_box) at (5.4, 2.0) {};
  \node[above, font=\large\bfseries, text=pubblue] at (5.4, 4.8) {【グローバルWAN】世界中のインターネット};

  \node[draw=pubblue, fill=white, rounded corners=4pt, thick, align=center, minimum width=7.2cm, minimum height=1.5cm] (pub_ip) at (5.4, 3.6) {
    \textbf{契約プロバイダ割当のグローバルIP}\\[2pt]
    \footnotesize IP: \texttt{198.51.100.42} (世界で唯一の宛先)
  };

  \node[draw=pubblue, fill=blue!15, rounded corners=4pt, very thick, align=center, minimum width=7.2cm, minimum height=2.2cm] (web_srv) at (5.4, 0.8) {
    \textbf{\large 目的のWebサーバー}\\[3pt]
    \footnotesize IP: \texttt{203.0.113.80} (Port: 443 HTTPS)\\[2pt]
    \scriptsize パケットがルーターを経由してバケツリレーで届く！
  };

  \draw[->, very thick, privgreen] (lan_pc.east) -- (router.west |- lan_pc.east);
  \draw[->, very thick, privgreen] (lan_phone.east) -- (router.west |- lan_phone.east);
  \draw[->, very thick, pubblue] (router.east) -- (pub_ip.west);
  \draw[->, very thick, pubblue] (pub_ip.south) -- (web_srv.north);

  % 下部まとめ
  \node[draw=black!70, fill=green!20, rounded corners=6pt, line width=1.2pt, align=center, minimum width=20.0cm, inner sep=6pt] at (0, -2.4) {
    \textbf{\Large ★ ネットワークが分かるとセキュリティの「どこを守るべきか」が見えてくる！}\\[3pt]
    \small IPアドレス（住所）、MACアドレス（機器識別）、ポート番号（部屋番号）、DNS（案内所）の連携がインターネットの基礎！
  };

\end{tikzpicture}
\end{document}
"""

prompt_ep12 = (
    "1boy, 1girl, smart Japanese high school boy with glasses configuring a clean Wi-Fi router on a workbench with blue ethernet LAN cables, "
    "cute high school girl with ponytail happily inspecting IP address configurations and packet flows on her laptop, "
    "kind stylish female university professor guiding them with a warm smile pointing at network routing architecture on blackboard, "
    "modern school network laboratory, bright sunshine through large windows, shelves of networking gear, clean wooden desks, "
    "active teamwork, hands-on learning, collaborative problem solving, "
    "masterpiece, best quality, beautiful detailed anime art style, Kyoto Animation aesthetic, "
    "perfect facial features, beautiful anime eyes, clear pupils, relaxed confident smiles, "
    "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
)

# -------------------------------------------------------------
# Episode 13: Cyber Defense Competition (CTF) & Future Careers
# -------------------------------------------------------------
tikz_ep13 = r"""\documentclass[tikz,border=18pt]{standalone}
\usepackage{luatexja}
\usepackage{tikz}
\usetikzlibrary{shapes.geometric,arrows.meta,positioning,calc}

\definecolor{ctfgold}{RGB}{210, 130, 20}
\definecolor{ctfblue}{RGB}{20, 80, 160}
\definecolor{ctfgreen}{RGB}{25, 125, 50}

\begin{document}
\begin{tikzpicture}[>=Stealth, font=\small]

  % -------------------------------------------------------------
  % 上段：CTF（Capture The Flag）競技の主要5大ジャンル
  % -------------------------------------------------------------
  \node[draw=ctfgold, fill=orange!6, rounded corners=8pt, line width=1.5pt, minimum width=20.0cm, minimum height=3.8cm, align=left] (ctf_box) at (0, 3.8) {};
  
  \node[above right, font=\large\bfseries, text=ctfgold] at (-9.8, 5.1) {【競技】サイバーセキュリティ競技 CTF（Capture The Flag）の主要ジャンル};

  \node[draw=ctfblue, fill=blue!10, rounded corners=4pt, thick, align=center, minimum width=3.5cm, minimum height=1.6cm] (c1) at (-7.2, 3.2) {
    \textbf{\large Web}\\[2pt]
    \footnotesize SQLi, XSS, 認証回避\\
    \tiny Webアプリの欠陥を突く
  };

  \node[draw=ctfblue, fill=blue!10, rounded corners=4pt, thick, align=center, minimum width=3.5cm, minimum height=1.6cm] (c2) at (-3.6, 3.2) {
    \textbf{\large Crypto}\\[2pt]
    \footnotesize RSA暗号, 共通鍵\\
    \tiny 暗号の数学的弱点を解読
  };

  \node[draw=ctfblue, fill=blue!10, rounded corners=4pt, thick, align=center, minimum width=3.5cm, minimum height=1.6cm] (c3) at (0.0, 3.2) {
    \textbf{\large Reversing}\\[2pt]
    \footnotesize 逆アセンブル, 逆コンパイル\\
    \tiny バイナリプログラムを解析
  };

  \node[draw=ctfblue, fill=blue!10, rounded corners=4pt, thick, align=center, minimum width=3.5cm, minimum height=1.6cm] (c4) at (3.6, 3.2) {
    \textbf{\large Forensics}\\[2pt]
    \footnotesize パケット解析, 隠しデータ\\
    \tiny 消された痕跡から旗を探す
  };

  \node[draw=ctfblue, fill=blue!10, rounded corners=4pt, thick, align=center, minimum width=3.5cm, minimum height=1.6cm] (c5) at (7.2, 3.2) {
    \textbf{\large Pwn}\\[2pt]
    \footnotesize メモリ破壊, バッファ溢れ\\
    \tiny システムの制御権を奪取
  };

  % -------------------------------------------------------------
  % 下段：大学進学とセキュリティプロフェッショナルの輝く未来
  % -------------------------------------------------------------
  \node[draw=ctfgreen, fill=green!6, rounded corners=8pt, line width=1.5pt, minimum width=20.0cm, minimum height=3.8cm, align=left] (career_box) at (0, -1.4) {};
  
  \node[above right, font=\large\bfseries, text=ctfgreen] at (-9.8, -0.1) {【進路】大学情報学部での高度研究から広がるサイバーセキュリティのキャリア};

  \node[draw=ctfgreen, fill=white, rounded corners=6pt, thick, align=center, minimum width=6.0cm, minimum height=1.8cm] (car1) at (-6.2, -2.0) {
    \textbf{\large セキュリティエンジニア}\\[2pt]
    \footnotesize 堅牢なクラウド・Webを設計\\
    \footnotesize 守りのアーキテクトとして活躍！
  };

  \node[draw=ctfgold, fill=orange!15, rounded corners=6pt, thick, align=center, minimum width=6.0cm, minimum height=1.8cm] (car2) at (0.0, -2.0) {
    \textbf{\large ホワイトハッカー / ペンテスター}\\[2pt]
    \footnotesize 模擬攻撃で企業の弱点を診断\\
    \footnotesize 悪用される前に社会を守る！
  };

  \node[draw=ctfblue, fill=blue!15, rounded corners=6pt, thick, align=center, minimum width=6.0cm, minimum height=1.8cm] (car3) at (6.2, -2.0) {
    \textbf{\large セキュリティアナリスト / CISO}\\[2pt]
    \footnotesize 組織全体の危機管理と戦略立案\\
    \footnotesize 国家・企業のデジタル信頼を指揮！
  };

  \draw[->, very thick, ctfgreen] (car1.east) -- (car2.west);
  \draw[->, very thick, ctfgreen] (car2.east) -- (car3.west);

\end{tikzpicture}
\end{document}
"""

prompt_ep13 = (
    "1boy, 1girl, smart Japanese high school boy with glasses and cute high school girl with ponytail celebrating with joyful smiles, "
    "looking at laptop screen showing solved CTF cybersecurity challenge scoreboard with green flags, "
    "kind female university professor clapping and congratulating them with a warm proud smile, "
    "high school computer room decorated with colorful celebration banners, trophies and certificates on desk, "
    "bright glowing sunlight filling the classroom, hope, accomplishment, bright future, "
    "masterpiece, best quality, beautiful detailed anime art style, Kyoto Animation aesthetic, "
    "perfect facial features, beautiful expressive anime eyes, natural happy smiles, "
    "cinematic lighting, sharp focus, harmonious color grading, single scene illustration"
)

# Text generation prompts
P11 = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生が「デジタル・フォレンジック（電子鑑識）」と「不正アクセス禁止法」を学び、正義を守る職業の魅力に目覚める青春ライトノベル第11話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第11話 砂浜の足跡と電子の鑑識官 〜デジタル・フォレンジックと不正アクセス禁止法〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・部長。文化祭用の部活サーバーで誰かがログインを試みた不審なログを発見し、「これって警察や法律ではどう扱われるんだろう？」と考える。
・橘 葵（たちばな あおい）：高校2年・部員。「映画の鑑識課みたいに、パソコンの中にも犯人の足跡が残るの？」と興味津々な女子高生。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 准教授。警察や裁判所での証拠能力を持つ「デジタル・フォレンジック（証拠保全・ハッシュ値の一致・タイムライン解析）」と「不正アクセス禁止法」の法的位置づけを優しく解説。

【必須要素】
1. 不審アクセスがあった際、やってはいけないこと（不用意に再起動したりファイルを上書きすると証拠が消える）
2. デジタル・フォレンジックの基本手順：ライトブロッカー（書き込み防止装置）、ビット単位の完全クローン、SHA-256ハッシュ値による同一性証明、タイムライン復元
3. 日本の法律「不正アクセス行為の禁止等に関する法律（不正アクセス禁止法）」の基本（他人のID・パスワード無断入力、脆弱性を突く不正侵入、パスワード不正取得の禁止）
4. 警察のサイバー犯罪対策課や企業のCSIRT（インシデント対応チーム）で活躍する鑑識官・セキュリティ調査員のやりがい
5. 「コンピュータの仕組みと法律を知ることで、社会の不正に立ち向かう力になる」という前向きなメッセージ

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

P12 = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生が「家庭・学校のLANとルーター、IPアドレスとDNSの基本」を学び、ネットワークの基礎がセキュリティに直結する面白さを知る青春ライトノベル第12話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第12話 世界を繋ぐバケツリレー 〜家庭・学校のLAN、ルーターとDNSの秘密〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・部長。部室のWi-FiルーターとLANケーブルを整理しながら、IPアドレスの割り当てやポート開放について葵に説明する。
・橘 葵（たちばな あおい）：高校2年・部員。「プライベートIPとグローバルIPって何が違うの？」「URLを入れたらなんで目的のサーバーに繋がるの？」と素朴な疑問をぶつける女子高生。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 准教授。手紙の住所や電話帳に例えて、ルーター（NAT/NAPT）とDNSのバケツリレーの仕組み、そしてルーターが果たす「最初のファイアウォール」の役割を解き明かす。

【必須要素】
1. LAN（Local Area Network）とWAN（Wide Area Network）の違い
2. プライベートIPアドレス（192.168.x.x 等の家庭・学校内アドレス）と、世界で唯一のグローバルIPアドレス
3. ルーターのNAT/NAPT機能：外のインターネットと家庭内をつなぎ、ポート番号で宛先を振り分ける仕組み。外部からの無差別侵入を防ぐ防波堤の役割
4. DNS（Domain Name System）：人間が読みやすいドメイン名を機械が理解できるIPアドレスに瞬時に変換する「インターネットの電話帳」の役割
5. ネットワークの基本構造を理解することが、将来のネットワークエンジニアやセキュリティアーキテクトへの第一歩であるという明るい励まし

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

P13 = """あなたは情景豊かで生き生きとした会話を描くライトノベル作家です。
以下の構成プロットをもとに、高校生が「サイバーセキュリティ競技（CTF: Capture The Flag）」に初挑戦し、大学進学や将来のセキュリティ職業への大きな夢を抱く青春ライトノベル第13話（第1シーズン完結編）の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第13話 旗を掲げる守護者たち 〜サイバーセキュリティ競技（CTF）と未来への扉〜
【登場人物】
・城崎 悠真（きのさき ゆうま）：高校2年・部長。葵と共に高校生向けCTF競技大会にオンライン参加。暗号（Crypto）やWeb問題に挑み、学んできた知識を武器に最後の旗（Flag）を勝ち取る。
・橘 葵（たちばな あおい）：高校2年・部員。最初はパスワードの使い回しをしていた少女が、フォレンジック問題でパケット解析を成功させ、チームの勝利に大貢献する。
・芹沢 涼香（せりざわ すずか）：大学情報科学部 准教授。見事に完走した2人を温かく称え、大学での研究生活、そしてホワイトハッカー・セキュリティエンジニア・CISOとして広がる輝かしい未来を語る。

【必須要素】
1. セキュリティ競技「CTF（Capture The Flag）」の楽しさ：隠された「flag{...}」という文字列を探し出す知的な謎解きゲーム
2. これまで学んだ全知識の総動員（認証、暗号、パケット、Web脆弱性、フォレンジック）
3. 制限時間ギリギリで2人が協力して最後の問題を解き明かすカタルシス
4. 「セキュリティは怖いものではなく、人々が安心してデジタル社会を生きるための優しい盾」という主題の回収
5. 高校2年生の2人が「大学の情報学部でサイバーセキュリティを本格的に学び、世界を守るエンジニアになる」と晴れやかな笑顔で未来へ踏み出す感動のエンディング

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""

print("Episode 11-13 assets and prompts prepared.")
