import os

CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

def read_raw(ep_num):
    with open(os.path.join(CONTENT_DIR, f"ep{ep_num}_novel_raw.txt"), "r", encoding="utf-8") as f:
        text = f.read().strip()
    return text.replace("* * *", "✦ ✦ ✦")

# Episode 21
ep21_content = f"""---
title: "第21話 甘い偽指の衝撃 〜松本論文「グミ指」と生体検知（Liveness Detection）〜"
episode_num: 21
date: 2026-10-27
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "生体認証", "グミ指", "生体検知", "Liveness Detection", "PAD", "松本勉教授"]
---

# 第21話 甘い偽指の衝撃 〜松本論文「グミ指」と生体検知（Liveness Detection）〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL連携セミナー
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 松本勉教授（現・上席特別教授）の世界的名著『グミ指論文（SPIE 2002）』、人工指による生体認証突破実験、生体情報の本質的脆弱性（Revoke不能性）、なりすまし攻撃検知（PAD / Liveness Detection）、国際規格 ISO/IEC 30107、多要素認証（FIDO2 / パスキー）
> - **探訪・参照研究論文**:
>   - [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
>   - Tsutomu Matsumoto, Hiroyuki Matsumoto, Koji Yamada, Satoshi Hoshino. "Impact of Artificial 'Gummy' Fingers on Fingerprint Systems." *Proceedings of SPIE - Optical Security and Counterfeit Deterrence Techniques IV*, Vol. 4677, pp. 275-289, 2002.
>   - ISO/IEC 30107: Information technology — Biometric presentation attack detection (PAD).

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第21話 4コマ漫画イラスト](illustrations/ep21_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮の生体認証最強論と自慢**<br>スマホの指紋センサーでロック解除し、「偽造不可能で世界最強の鍵！」と豪語する蓮。 | **蓮**: 「見てよ結衣！ 指紋認証ならパスワードと違って絶対盗まれないし、世界最強の鍵だよな！」 | **Ren**: "Look Yui! Unlike passwords, fingerprint auth can never be stolen! It's the ultimate key!" |
| **第2コマ**<br>【承】 | **結衣の冷徹な指摘：生体情報は変えられない**<br>グラスの指紋痕を指差し、「生体情報は秘密情報ではないし一生変更（Revoke）できない」と突く結衣。 | **結衣**: 「甘いです。指紋は毎日ドアノブやグラスに置き忘れていますし、一度流出したら一生変えられません。」 | **Yui**: "Naïve. You leave fingerprints on glasses and doorknobs daily, and unlike passwords, you can never change them." |
| **第3コマ**<br>【転】 | **悠真TAによる伝説の松本論文「グミ指」解説**<br>スーパーのゼラチンで作った人工指が名だたるセンサーの約8割を通過した歴史を披露する悠真。 | **悠真**: 「2002年、横浜国大の松本教授がお菓子のグミで作った人工指でセンサーの約8割を突破したんだ。」 | **Yuma**: "In 2002, Prof. Matsumoto of YNU proved that gelatin gummy fingers fooled about 80% of fingerprint sensors." |
| **第4コマ**<br>【結】 | **生体検知（Liveness）とFIDO2多要素の地平へ**<br>脈拍や血流を検知する生体検知と暗号数理の組み合わせに感銘を受け、先端研究への扉を開く二人。 | **蓮**: 「ゼラチンに負けたからこそ、脈拍検知やAI判定が生まれたんだ！」<br>**結衣**: 「暗号数理と生体検知の融合……これが大学先端研究の凄みですね。」 | **Ren**: "Because sensors were tricked by gelatin, engineers developed pulse detection and smart liveness checks!"<br>**Yui**: "Merging cryptographic math with liveness detection... this is the true brilliance of academic research." |

---

## 📖 小説本文

{read_raw(21)}

---

## 📊 TikZによるセキュリティ構造図解

![松本論文「グミ指」と生体検知（Liveness Detection）の構造図解](figures/fig21_gummy_finger_liveness.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 世界を震撼させた横浜国大・松本論文「グミ指（Gummy Finger）」の衝撃
2002年、横浜国立大学の**松本勉 教授（現・上席特別教授）**らが国際学会SPIEで発表した論文『*Impact of Artificial "Gummy" Fingers on Fingerprint Systems*』は、世界のセキュリティ業界に文字通り激震を走らせました。
スーパーマーケットで手軽に入手できる**ゼラチン粉（お菓子のグミの原料）**と型取り用プラスチックを用い、残留指紋から精巧な「人工指（グミ指）」を作製。これを当時の主要な市販指紋認証センサー（光学式・静電容量式など）に押し当てたところ、なんと**約80%という極めて高い確率で誤認証（正規ユーザーとして突破）**してしまったのです。
ゼラチンは指の微細な凹凸だけでなく、人間の皮膚に近い水分量や電気伝導度を持っていたため、当時の単純な物理センサーをいとも簡単に欺いてしまいました。

### 2. 生体情報（バイオメトリクス）の本質的弱点：「一生変えられない」
この研究が突きつけた最大の教訓は、**「生体認証は万能の銀の弾丸ではない」**という点です。
- **秘密情報ではない**: 人間は日常生活の中で、カフェのグラス、電車のつり革、スマートフォンの画面などに無意識のうちに大量の指紋を付着・放置しています。
- **Revoke（失効・変更）が不可能**: パスワードや秘密鍵が漏洩した場合は新しい文字列に変更できますが、**指紋や虹彩、静脈パターンは一生変更することができません**。一度生体データが漏洩・複製されれば、その人は永久に脅威に晒され続けます。

### 3. なりすまし検知技術（PAD / Liveness Detection）と国際規格 ISO/IEC 30107
松本論文の指摘を受け、世界中の研究者やメーカーは**「生体検知（Liveness Detection / PAD: Presentation Attack Detection）」**の開発に乗り出しました。
単に指紋の模様を見るだけでなく、以下のような「生きた人間である証拠」を同時に検証する多層防御が確立されたのです：
1. **光学式脈波・血流検知（PPG）**: 血液中のヘモグロビンが光を吸収する特性を利用し、心拍に伴う微小な脈動を測定する。
2. **赤外線・真皮層イメージング**: 皮膚表面の角質層だけでなく、偽造が困難な皮膚内部の「真皮層（毛細血管網）」を透過光で撮影する。
3. **生体電気インピーダンス計測**: 生きた人間の皮膚組織特有の高周波交流抵抗や静電容量応答をナノ秒単位で測定する。
4. **AI画像解析**: 皮膚の微細な毛穴、皮膚呼吸による微小な変形、反射スペクトルを機械学習モデルで判別する。

現在では、これらは**国際標準規格「ISO/IEC 30107」**として厳格にテスト基準が定められています。松本教授らの「攻撃研究」があったからこそ、今日の安全なスマートフォン決済やオンライン認証が守られているのです。
"""

# Episode 22
ep22_content = f"""---
title: "第22話 蜜壺が暴く暗黒生態系 〜吉岡研「IoTPOT」とIoTマルウェアの進化〜"
episode_num: 22
date: 2026-10-27
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "吉岡克成教授", "IoTPOT", "ハニーポット", "IoTマルウェア", "Mirai", "脅威インテリジェンス"]
---

# 第22話 蜜壺が暴く暗黒生態系 〜吉岡研「IoTPOT」とIoTマルウェアの進化〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 共同観測ルーム
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 吉岡克成教授（SPIRALセンター長）らの先駆的論文『IoTPOT（USENIX WOOT 2015）』、IoTハニーポットの二段階協調アーキテクチャ、異種CPUアーキテクチャ（ARM/MIPS等）サンドボックス、IoTマルウェア生態系の解明、脅威インテリジェンスエコシステム
> - **探訪・参照研究論文**:
>   - [横浜国立大学 SPIRAL：吉岡克成研究室（CyRaP Lab）](https://spiral.ynu.ac.jp/)
>   - Pa Pa Yin Minn, Shogo Suzuki, Katsunari Yoshioka, Tsutomu Matsumoto, Takahiro Kasama, Christian Rossow. "IoTPOT: A Novel Honeypot with Analyzing Various Architectural Malware." *Proceedings of the 9th USENIX Workshop on Offensive Technologies (WOOT 15)*, 2015.
>   - 吉岡克成, 鈴木将吾, イン ミンパパ, 笠間貴弘, 松本勉. 「IoTPOT：未知のIoTマルウェア動態を解明するハニーポットシステム」, *情報処理学会論文誌*, Vol. 57, No. 9, pp. 2098-2109, 2016.

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第22話 4コマ漫画イラスト](illustrations/ep22_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮の困惑：自作マイコンに届く謎のバイナリ**<br>Raspberry Piに世界中から届く攻撃パケットを眺め、PC用（x86）と全く違う構造に頭を抱える蓮。 | **蓮**: 「うわっ、自作ルーターに謎のバイナリが送り込まれてる！ でもx86じゃなくてARMやMIPS向けだ……！？」 | **Ren**: "Whoa, weird binaries are raining down on my custom router! But they aren't x86, they're for ARM and MIPS...!?" |
| **第2コマ**<br>【承】 | **結衣の洞察：従来のハニーポットでは追えない**<br>端末ログを分析し、シェルを真似るだけの低対話ハニーポットではIoTマルウェアの深層挙動が暴けないと気づく結衣。 | **結衣**: 「一般的なハニーポットでは、攻撃者がダウンロードさせる多種多様なバイナリを実行・解析できません。」 | **Yui**: "Standard honeypots only mimic a shell. They cannot execute and analyze binaries across diverse architectures." |
| **第3コマ**<br>【転】 | **悠真TAが解説するSPIRAL「IoTPOT」の二重構造**<br>フロントエンドで罠を張り、バックエンドの仮想QEMU群で多種CPUマルウェアを動かす吉岡研のシステムを紹介。 | **悠真**: 「そこで横浜国大の吉岡教授たちが開発したのが『IoTPOT』だ。8種類以上のCPU環境で安全に挙動を暴くんだ。」 | **Yuma**: "That's why Prof. Yoshioka's team at YNU created 'IoTPOT', safely revealing malware behaviors across 8+ CPU architectures." |
| **第4コマ**<br>【結】 | **暗黒生態系の解明とプロアクティブ防衛の誓い**<br>Mirai出現の前年から世界を救う脅威観測網を築いたSPIRALの偉業に圧倒され、守備範囲を広げる二人。 | **蓮**: 「敵の攻撃手法を隅々まで解明するからこそ、完璧な対策が打てるんだな！」<br>**結衣**: 「観測という名の灯火で闇を照らす……まさに本物のサイバー防衛研究です。」 | **Ren**: "By thoroughly deciphering the adversary's playbook, we can build flawless countermeasures!"<br>**Yui**: "Illuminating the darkness through relentless observation... this is true cybersecurity science." |

---

## 📖 小説本文

{read_raw(22)}

---

## 📊 TikZによるセキュリティ構造図解

![吉岡研「IoTPOT」とIoTマルウェア生態系の構造図解](figures/fig22_iotpot_threat_intelligence.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. IoTマルウェアの特殊性と「CPUアーキテクチャの多様性」
一般的なパソコンやクラウドサーバーは、IntelやAMDの「x86 / x86_64」という共通の命令セット（CPUアーキテクチャ）で動いています。
しかし、家庭用Wi-Fiルーター、ネットワークカメラ（Webcam）、スマートテレビ、温湿度センサーなどの**IoT（Internet of Things）機器**は、消費電力や製造コストを抑えるため、**ARM、MIPS、PowerPC、SuperH、SPARC、Motorola 68000**など、驚くほど多様なCPUを採用しています。
攻撃者もこの環境に合わせて、同一のマルウェアソースコードから8〜10種類以上の異なるCPU向けバイナリを一斉にクロスコンパイルしてばら撒くという、PCとは全く異なる攻撃手口を発達させました。

### 2. 横浜国大・吉岡教授らの金字塔「IoTPOT」の画期的構造
2015年、横浜国立大学の**吉岡克成 教授（現・SPIRALセンター長）**らの研究チームは、この多種多様なIoTマルウェアの生態系を暴く画期的なハニーポットシステム**「IoTPOT」**を国際学会 USENIX WOOT 2015 で発表しました。
IoTPOTの最大の特徴は、**「フロントエンド（Frontend）」と「バックエンド（Backend: IoTBOX）」を鮮やかに分離した二段階協調アーキテクチャ**にあります：
- **フロントエンド（Low-Interaction）**: インターネット上に数万個の無防備なIoT機器を装った低負荷な罠を展開。Telnet辞書攻撃に対して実機のプロンプトを巧みにシミュレートし、攻撃者が送り込んでくるマルウェアのダウンロードURLや生バイナリを確実に捕捉する。
- **バックエンド（IoTBOX: High-Interaction）**: 捕捉した未知バイナリを、QEMU仮想環境上に構築された**8種類以上の異種CPUサンドボックス**へ自動転送。実際にマルウェアを動作させ、C2（指令サーバー）への通信、他端末へのスキャン、DDoS攻撃のパケット送信挙動を完全隔離された環境で詳細に記録する。

### 3. Miraiボットネット出現を予見した「脅威インテリジェンス」の先駆
2016年秋、世界中のDNSサービス（Dyn）を麻痺させ米国の東海岸全域でTwitterやNetflixをダウンさせた悪名高い**「Miraiボットネット」**。
しかし吉岡教授らのIoTPOTは、Miraiが世界を騒がせる**1年以上も前の2015年春の時点で、すでに前身となるBashliteなどのIoTボットが世界中で激しい感染競争を繰り広げている実態を学術的に可視化**していました。
敵がどのような手口で機器を乗っ取り、どのように勢力を拡大しているのか――「敵の生態系を誰よりも早く観測し、社会全体に先手（プロアクティブ）の防御策を提供する」というSPIRALの脅威インテリジェンス研究は、世界中のセキュリティ機関から最高峰の評価を受けています。
"""

# Episode 23
ep23_content = f"""---
title: "第23話 闇夜の反射鏡を砕け 〜ダークネットとDNSアンプ攻撃事前観測〜"
episode_num: 23
date: 2026-10-27
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "牧田大佑准教授", "吉岡克成教授", "ダークネット", "DNSアンプ攻撃", "DDoS事前対策", "AmpPot"]
---

# 第23話 闇夜の反射鏡を砕け 〜ダークネットとDNSアンプ攻撃事前観測〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL ネットワーク監視室
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 牧田大佑准教授・吉岡克成教授らの特選論文『DNSアンプDDoS攻撃の事前対策に向けたDNSハニーポットとダークネットの相関分析』、DNSアンプ（増幅）攻撃の物理的メカニズム、UDPの送信元IP偽装（IP Spoofing）、オープンリゾルバ問題、ダークネット（未使用IP空間）観測、攻撃予兆の事前検知
> - **探訪・参照研究論文**:
>   - [横浜国立大学 SPIRAL：サイバー空間観測・分析研究グループ](https://spiral.ynu.ac.jp/)
>   - 牧田大佑, 吉岡克成, イン ミンパパ, 鈴木将吾, 松本勉. 「DNSアンプDDoS攻撃の事前対策に向けたDNSハニーポットとダークネットの相関分析」, *情報処理学会論文誌*, Vol. 56, No. 9, pp. 1827-1837, 2015. (情報処理学会特選論文)
>   - Daisuke Makita, Katsunari Yoshioka, et al. "Analyzing and Mitigating DNS Amplification DDoS Attacks via Coordinated Honeypot and Darknet Monitoring." *NATO CCDCOE International Conference on Cyber Conflict (CyCon)*.

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第23話 4コマ漫画イラスト](illustrations/ep23_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮の衝撃：数十バイトが数百倍のメガトン兵器へ**<br>DNSパケットのシミュレーションを見つめ、たった1行の問い合わせが巨大な津波に化ける怪異に目を見張る蓮。 | **蓮**: 「なんだこれ！？ たった60バイトの問い合わせを送っただけで、4,000バイト以上の巨大応答が返ってくるのか！？」 | **Ren**: "What is this!? A tiny 60-byte query generates an enormous 4,000-byte response back!?" |
| **第2コマ**<br>【承】 | **結衣の数理分析：UDP送信元偽装とオープンリゾルバ**<br>ホワイトボードにパケット構造を描き、UDPのコネクションレス特性とIP偽装による反射の仕組みを看破する結衣。 | **結衣**: 「UDPはハンドシェイクがありません。送信元IPを標的のアドレスに偽装すれば、巨大応答が標的に集中砲火されます。」 | **Yui**: "UDP lacks handshakes. If attackers spoof the source IP with the victim's, massive responses crush the victim." |
| **第3コマ**<br>【転】 | **悠真TAが語る「ダークネット」とSPIRAL牧田論文**<br>宇宙のブラックホールのように誰も使っていない未使用IP空間に降り注ぐパケット観測とハニーポット連携を解説。 | **悠真**: 「横浜国大の牧田・吉岡先生たちは、ダークネットとDNSハニーポットを連携させて攻撃の予兆を捉えたんだ。」 | **Yuma**: "Professors Makita and Yoshioka at YNU correlated darknet scans with DNS honeypots to detect attack preparations." |
| **第4コマ**<br>【結】 | **受動的対処から能動的予知へ！二人の未来構想**<br>攻撃が起きてから耐えるのではなく、ダークネットの予兆分析で先手を打つ研究の真価に胸を高鳴らせる二人。 | **蓮**: 「攻撃が始まる前に準備運動を見つけ出すなんて、まさに未来予知ディフェンスだ！」<br>**結衣**: 「ビッグデータ数理がインターネットの平和を守る……素晴らしい研究の領域です。」 | **Ren**: "Spotting their warm-up scans before the assault even begins... it's literally precognitive cyber defense!"<br>**Yui**: "Big data mathematics guarding the peace of the internet... what an inspiring research frontier." |

---

## 📖 小説本文

{read_raw(23)}

---

## 📊 TikZによるセキュリティ構造図解

![ダークネットとDNSアンプDDoS攻撃の相関分析構造図解](figures/fig23_darknet_ddos_correlation.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 「DNSアンプ攻撃（DNS Amplification Attack）」の原理
インターネットの住所録である**DNS（Domain Name System）**。通常は「`example.com` のIPアドレスを教えて」と尋ねると、サーバーが数十バイトでIPアドレスを返してくれます。
しかし攻撃者は、暗号鍵や長大なレコードを含むドメインに対して「すべての情報（`ANY` クエリやDNSSECクエリ）」を要求します。
すると、**わずか60バイト程度の要求パケットに対して、3,000〜4,000バイト以上（約50〜70倍）の巨大な応答パケット**が生成されます。これが「アンプ（増幅器）」と呼ばれる理由です。

### 2. なぜ標的に届くのか？：UDPと「送信元IP偽装（IP Spoofing）」
Web閲覧で使われるTCP通信では、通信開始前に必ず**「3ウェイハンドシェイク（SYN ➡ SYN/ACK ➡ ACK）」**を行って相手が実在するか確認するため、送信元を偽装することは極めて困難です。
しかし、DNSやNTPで使われる**UDP（User Datagram Protocol）**は、事前確認なしに一方的にパケットを送りつける「コネクションレス型」です。
攻撃者は、パケットの送信元IPアドレスを「標的（攻撃したい企業やサーバー）のIP」に書き換えて（偽装して）、世界中に存在する無防備なDNSサーバー（**オープンリゾルバ**）へ一斉にクエリを投げます。すると、数千台のDNSサーバーから標的へ向かって巨大な応答パケットの津波が一瞬で集中し、標的の回線とサーバーを完全にパンク（DDoS）させてしまうのです。

### 3. 横浜国大・牧田大佑准教授らの先駆的功績：ダークネットとの相関分析
横浜国立大学 SPIRALの**牧田大佑 准教授・吉岡克成 教授**らは、この深刻なDDoS攻撃に対して画期的な解決策を提示し、情報処理学会論文誌の**「特選論文」**を受賞しました。
- **ダークネット（Darknet）とは**: インターネット上で正式に割り当てられているものの、実際にはコンピュータやサーバーが接続されていない「未使用のIPアドレス空間（ブラックホール）」のこと。正常な通信ならパケットが届くはずがないため、ここに届くパケットはすべて**「世界中を徘徊する不正なスキャンや探索活動」**であることが分かります。
- **事前対策の相関メカニズム**:
  攻撃者は、本番のDDoS攻撃を発動する数時間〜数日前に、まず「世界中のどのDNSサーバーを踏み台（アンプの反射鏡）に使えるか」を探すための**「予備探索スキャン」**をインターネット全体に仕掛けます。
  牧田教授らは、SPIRALが運用する**DNSハニーポット（AmpPot等）に届いた問い合わせ**と、NICT等の**ダークネットに届いた無差別スキャンパケット**を時系列で高精度に照合・相関分析しました。
  その結果、**「攻撃者がどのオープンリゾルバを踏み台として選別したか」「どの標的を狙おうとしているか」をDDoS攻撃の発動前に察知し、事前に踏み台リストの遮断や標的への警告を行うという、能動的（プロアクティブ）な事前防御エコシステム**を世界で初めて実証したのです。
"""

# Episode 24
ep24_content = f"""---
title: "第24話 量子の嵐と格子の盾 〜四方研究室と耐量子計算機暗号数理〜"
episode_num: 24
date: 2026-10-27
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "四方順司教授", "NexCrypt", "耐量子計算機暗号", "PQC", "格子暗号", "匿名同報認証"]
---

# 第24話 量子の嵐と格子の盾 〜四方研究室と耐量子計算機暗号数理〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 NexCrypt 研究室
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 四方順司教授（SPIRAL副センター長・NexCrypt Lab長）らの耐量子計算機暗号数理、ショアのアルゴリズムによるRSA・ECC解読危機、格子暗号（ML-KEM / ML-DSA）、Harvest Now, Decrypt Later（HNDL）脅威、匿名同報認証、集約メッセージ認証コード（Aggregate MAC）
> - **探訪・参照研究論文**:
>   - [横浜国立大学 SPIRAL：四方順司研究室（NexCrypt Lab）](https://spiral.ynu.ac.jp/)
>   - Junji Shikata, et al. "Post-Quantum Cryptography and Mathematical Foundations for Information Security." *IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences*, 2023.
>   - 四方順司. 「耐量子計算機暗号と次世代暗号数理の展望」, *電子情報通信学会論文誌*, 2024.
>   - NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA): Post-Quantum Cryptography Standards.

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第24話 4コマ漫画イラスト](illustrations/ep24_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮のパニック：量子コンピュータで暗号全滅！？**<br>「量子計算機が実用化されたらネット社会の暗号が全部破られる」という噂記事を読み青ざめる蓮。 | **蓮**: 「おい結衣！ 量子コンピュータが来たらRSA暗号も全部解読されて、ネットが終わるって本当か！？」 | **Ren**: "Hey Yui! If quantum computers arrive, will RSA encryption be shattered and end the internet!?" |
| **第2コマ**<br>【承】 | **結衣の歓喜：量子の嵐を阻む「格子暗号」の幾何学**<br>瞳を輝かせ、高次元空間に広がる「格子問題（Lattice）」の美しさと強固さをスケッチする結衣。 | **結衣**: 「終わりません。ショアのアルゴリズムでも解けない高次元幾何学『格子暗号（PQC）』が存在します。」 | **Yui**: "It won't end. There is 'Lattice Cryptography'—high-dimensional geometry that Shor's algorithm cannot solve." |
| **第3コマ**<br>【転】 | **悠真TAが語る横浜国大・四方教授の次世代暗号数理**<br>SPIRALのNexCrypt研究室が創り出す格子暗号や匿名同報認証、集約MACなどの最先端数理を紹介する悠真。 | **悠真**: 「横浜国大の四方順司教授は、PQCだけでなくプライバシーを守る匿名同報認証の数理も極めているんだ。」 | **Yuma**: "Prof. Junji Shikata at YNU masters not just PQC, but advanced math for anonymous broadcast authentication." |
| **第4コマ**<br>【結】 | **100年先の未来を守る数理の盾！結衣の決意**<br>暗号数理が人類の自由を守る最強の盾であると確信し、蓮も数理の圧倒的な美しさに引き込まれる。 | **蓮**: 「数学者って未来の盾を何十年も前から準備してるんだな……！」<br>**結衣**: 「はい。数理の美しさこそ、量子の嵐をも跳ね返す人類最強の砦です。」 | **Ren**: "Mathematicians prepare our future shields decades in advance... unbelievable!"<br>**Yui**: "Yes. Mathematical elegance is humanity's greatest fortress against even quantum storms." |

---

## 📖 小説本文

{read_raw(24)}

---

## 📊 TikZによるセキュリティ構造図解

![四方研究室と耐量子計算機暗号（PQC）数理の構造図解](figures/fig24_pqc_lattice_shikata.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 「量子コンピュータの脅威」の真実：ショアのアルゴリズム
現在、Webサイトの保護（HTTPS/TLS）や電子署名、ビットコインなどで使われている暗号は、主に**RSA暗号（素因数分解の難しさ）**や**楕円曲線暗号（離散対数問題の難しさ）**に依存しています。
従来のスーパーコンピュータでは、これらを解くのに宇宙の年齢（何百億年）以上かかります。
しかし、1994年にピーター・ショアが発見した**「ショアのアルゴリズム（Shor's Algorithm）」**を大規模な誤り耐性型汎用量子コンピュータ（FTQC）で実行すると、量子の「重ね合わせ」と「量子もつれ・干渉」を利用して周期性を瞬時に特定し、**数分〜数時間という多項式時間で素因数分解や離散対数を解いてしまいます**。

### 2. 「今盗んで将来解読する（HNDL: Harvest Now, Decrypt Later）」の危機
「量子コンピュータが完成するのはまだ先だから大丈夫」という考えは致命的な誤りです。
国家支援型ハッカーや諜報機関は、**「今インターネット上を流れている高度な暗号化通信データをそのまま丸ごと記録・保存（Harvest）し、10年後や20年後に量子コンピュータが完成した瞬間に一斉解読（Decrypt）する」**という「HNDL攻撃」を現在進行形で行っています。
国家機密、個人のゲノム医療データ、外交記録などは数十年間にわたって機密を守らなければならないため、**「今すぐ」量子耐性を持つ暗号へ移行する必要がある**のです。

### 3. 格子暗号（Lattice-based Cryptography）と横浜国大・四方順司教授の研究
米国NISTは2024年に耐量子計算機暗号（PQC）の公式標準規格（FIPS 203: ML-KEM、FIPS 204: ML-DSAなど）を制定しましたが、その中核を占めるのが**「格子暗号（Lattice-based Cryptography）」**です。
- **格子の難しさ**: 2次元や3次元の升目なら最も近い格子点はすぐ見つかりますが、**数百次元という途方もない高次元空間**にランダムに歪んだ格子点を敷き詰めると、量子の並列計算をもってしても「ある点に最も近い格子点を見つける問題（SVP/LWE問題）」は指数関数的な時間がかかり、解くことができません。
- **横浜国大 SPIRAL・四方順司 教授（NexCrypt Lab長）の先駆的暗号数理**:
  四方教授らは、単に鍵を安全に共有するだけでなく、高度な次世代社会を見据えた高機能暗号数理を開拓しています：
  1. **匿名同報認証（Anonymous Broadcast Authentication）**: 自動運転車やスマートシティにおいて、「誰が送ったかという個人のプライバシーや位置情報を完全に秘匿したまま、送信者が正当な車両であることを全員が数学的に検証できる」画期的な認証方式。
  2. **集約メッセージ認証コード（Aggregate MAC）**: 何万台ものIoTセンサーや車載ECUから送られてくる大量の署名を、通信帯域を圧迫することなく「1つの短いコードに圧縮・集約して一括検証」する数理技術。
  3. **情報理論的安全性（Information-Theoretic Security）**: 計算能力が無限にある敵に対しても物理層のノイズや乱数性によって絶対に破られない究極の安全基準の追求。

数学という最も純粋な学問が、未来の社会インフラと人々の尊厳を守る強固な盾となっているのです。
"""

# Episode 25
ep25_content = f"""---
title: "第25話 賢者の檻と化かす影 〜LLMが暴くサンドボックス回避の迷宮〜"
episode_num: 25
date: 2026-10-27
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "伊藤曜助教", "吉岡克成教授", "サンドボックス回避", "LLMセキュリティ", "CyRaP", "AI防御"]
---

# 第25話 賢者の檻と化かす影 〜LLMが暴くサンドボックス回避の迷宮〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL CyRaP / CyAPEX 実習環境
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 伊藤曜助教・吉岡克成教授らの最新研究『大規模言語モデル（LLM）によるサンドボックス回避耐性強化支援』、マルウェアのサンドボックス検出・環境擬態テクニック（Evasion Attacks）、環境アーティファクトの自動探索、AIによる自律的セキュリティ検証、第2部先進研究編の壮大な結び
> - **探訪・参照研究論文**:
>   - [横浜国立大学 SPIRAL：吉岡研究室（CyRaP Lab）](https://spiral.ynu.ac.jp/)
>   - 伊藤曜, 吉岡克成. 「大規模言語モデルを用いたマルウェア解析用サンドボックスの回避耐性強化支援」, *コンピュータセキュリティシンポジウム（CSS 2025）*, 情報処理学会, 2025. (情報処理学会 ICSS研究賞 受賞)
>   - Yo Ito, Katsunari Yoshioka, et al. "Enhancing Sandbox Robustness against Evasive Malware via Large Language Models." *Journal of Information Processing / IEEE Transactions on Dependable and Secure Computing*.

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第25話 4コマ漫画イラスト](illustrations/ep25_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮の勘違い：サンドボックスで動いた無害なプログラム？**<br>解析用仮想環境で怪しい検体を実行したところ何のエラーも出ず、「安全なファイルだったよ！」と胸を撫で下ろす蓮。 | **蓮**: 「隔離環境で動かしてみたけど、何もしないで終了したよ！ なーんだ、無害な安全ファイルだったんだな！」 | **Ren**: "I ran it in the sandbox, but it did nothing and exited! Phew, turns out it's completely harmless!" |
| **第2コマ**<br>【承】 | **結衣と悠真のタネ明かし：それは「死んだふり」！**<br>画面のレジストリやマウス移動履歴を指差し、マルウェアが檻を察知して攻撃を封印した（回避行動）と指摘する結衣。 | **結衣**: 「騙されてはいけません。マルウェアが仮想環境特有の痕跡を察知して『死んだふり』をしているだけです。」 | **Yui**: "Don't be fooled. The malware detected the virtual environment and is simply playing dead to deceive us." |
| **第3コマ**<br>【転】 | **悠真TAが解説するSPIRAL伊藤・吉岡論文のブレイクスルー**<br>横浜国大の伊藤曜助教らが開発した「LLMを使ってサンドボックスの弱点を自動発見・修復する」最新論文を紹介。 | **悠真**: 「そこで横浜国大の伊藤・吉岡先生たちは、LLMを活用して檻の擬態漏れを自律的に強化する技術を生み出したんだ。」 | **Yuma**: "That's why Dr. Ito and Prof. Yoshioka at YNU created an LLM framework to automatically detect and patch sandbox leaks." |
| **第4コマ**<br>【結】 | **第2部先進研究編完結！大学先端の地平へ**<br>AIと数理が交差する最前線の学術研究に圧倒され、いつか自分たちも世界を守る論文を書く研究者になると誓う二人。 | **蓮**: 「AIで攻撃を見破り、AIで檻を完璧にするのか！ 俺、絶対にこの研究の最前線へ進むぞ！」<br>**結衣**: 「ええ。巨人の肩の上に立ち、未来の安全を拓く研究者を目指しましょう！」 | **Ren**: "Using AI to anticipate attacks and perfect the sandbox! I'm definitely heading to the frontier of this research!"<br>**Yui**: "Yes. Standing on the shoulders of giants, let us become researchers who forge future security!" |

---

## 📖 小説本文

{read_raw(25)}

---

## 📊 TikZによるセキュリティ構造図解

![LLMによるサンドボックス回避耐性強化支援の構造図解](figures/fig25_llm_sandbox_spiral.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. マルウェアの狡猾な知恵「サンドボックス回避（Evasion Attack）」
セキュリティ企業や研究機関は、不審なプログラムを見つけると**「サンドボックス（解析用仮想マシン環境）」**の中で安全に実行し、どのような悪事（ファイルの暗号化、外部通信、パスワード窃取など）を働くかを動的解析します。
しかし、現代の高度なマルウェアは**「自分が檻（サンドボックス）の中にいるかどうか」を極めて狡猾に確認**します：
- **ユーザー操作の不在**: マウスカーソルが一定時間全く動いていない、キーボード入力がない。
- **ハードウェアの不自然さ**: CPUコア数が1個しかない、RAMが極端に小さい、画面解像度が800x600など不自然。
- **仮想環境特有の痕跡（アーティファクト）**: VMwareやVirtualBox特有のデバイスドライバ、レジストリキー、MACアドレスのOUI（ベンダー識別子）が存在する。
- **時間の引き伸ばし（Time Acceleration検知）**: スリープ関数を呼び出した際、解析ツールが時間を早送りしたことを高精度タイマーで検知する。

檻の中にいると判断したマルウェアは、攻撃コードを一切実行せずに**正常なプログラムのふりをして終了（擬死）**し、解析者を欺いて「安全なファイル」と判定させようとします。

### 2. 防御側の苦悩：果てしない「モグラ叩き」
サンドボックスを開発するセキュリティ研究者は、マルウェアに「本物の人間のパソコンだ」と信じ込ませるために、無数のシステム設定やレジストリ、ダミーファイル、マウス移動エミュレーションなどを手作業で組み込んできました。
しかし、Windows OSやLinux OSの内部仕様は膨大であり、攻撃者が次々と見つけ出す「新たな環境識別トリガー」を手作業で網羅し続けることには物理的な限界がありました。

### 3. 横浜国大・伊藤曜助教と吉岡克成教授の革新（CSS 2025 / ICSS研究賞）
このモグラ叩きに終止符を打つべく、横浜国立大学 SPIRALの**伊藤曜 助教・吉岡克成 教授**らが提案したのが、**「大規模言語モデル（LLM）を活用したサンドボックス回避耐性の自律的強化支援技術」**です。
- **アプローチの革新性**:
  LLMは、膨大なオープンソースコード、マルウェア解析レポート、Windows API仕様書、リバースエンジニアリング文献の知識を保持しています。
  研究チームは、LLMに対してマルウェアアナリストと回避攻撃者の双方の視点を与え、**「あるサンドボックス設定に対して、攻撃者ならどのAPIやレジストリをチェックして仮想環境だと見破るか」を自律的に推論・列挙**させました。
- **自動検証とパッチ適用**:
  LLMが提案した回避ロジックを実際のサンドボックス上で動的テストし、実際に回避に使われうる「設定の隙（アーティファクト漏れ）」をピンポイントで特定。さらに、その漏れを塞ぐためのOS設定スクリプトやダミー環境パッチを自動生成させることに成功しました。

この成果は情報処理学会の**コンピュータセキュリティシンポジウム（CSS 2025）において「ICSS研究賞」**を受賞し、AIとサイバーセキュリティが融合した最先端の学術成果として国内外で絶賛されています。
大学の研究室では、このように日夜、世界を守るための最先端の知性が生み出され続けているのです。
"""

files_to_write = {
    "2026-10-27_ep21_gummy_finger_and_liveness_detection.md": ep21_content,
    "2026-10-27_ep22_iotpot_and_iot_malware_ecosystem.md": ep22_content,
    "2026-10-27_ep23_darknet_and_dns_amplification_prevention.md": ep23_content,
    "2026-10-27_ep24_pqc_lattice_cryptography_shikata_lab.md": ep24_content,
    "2026-10-27_ep25_llm_sandbox_evasion_robustness_spiral.md": ep25_content,
}

for fname, content in files_to_write.items():
    path = os.path.join(CONTENT_DIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created {path} ({len(content)} chars)")

print("ALL EP21-25 MARKDOWN FILES CREATED SUCCESSFULLY!")
