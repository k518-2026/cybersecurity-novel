---
title: "第60話 凝縮する鍵と群テストの妙手 〜耐量子有界共謀IDベース暗号（BC-IBE）の極致〜"
episode: 60
arc: 2
category: "spiral_paper"
theme: "横浜国立大学SPIRAL・佐藤慎悟准教授・四方順司教授（NexCrypt Lab）、CANS 2024 / SCIS 2025、組合せ論的群テスト（Group Testing）と格子暗号（Lattice-based Cryptography）を融合したコンパクトな耐量子有界共謀IDベース暗号（BC-IBE: Bounded-Collusion Identity-Based Encryption）の構成"
dss_topic: "耐量子暗号（PQC）・IDベース暗号（IBE）・有界共謀耐性（BC-IBE）・群テスト（Group Testing）・LWE問題"
characters:
  - name: "城崎 悠真"
    role: "横浜国大1年 / SPIRAL学生研究員 / TA"
  - name: "橘 葵"
    role: "高校3年 / 元情報科学部部長"
  - name: "神崎 蓮"
    role: "高校1年 / 情報科学部（IoT・ハード班）"
  - name: "白石 結衣"
    role: "高校1年 / 情報科学部（暗号数理班）"
cover_image: "ep60_4koma.png"
figure_image: "fig60_compact_bc_ibe_group_testing.png"
---

# 第60話 凝縮する鍵と群テストの妙手 〜耐量子有界共謀IDベース暗号（BC-IBE）の極致〜

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

| コマ | シチュエーション | 日本語セリフ | 英語セリフ (English) |
| :--- | :--- | :--- | :--- |
| **1コマ目** | 悠真が「メールアドレスを公開鍵として暗号化できるIDベース暗号（IBE）」の仕組みを提示する | **葵**:「相手のメールアドレスや学籍番号をそのまま公開鍵にして暗号化できるなんて、証明書もいらなくて超便利じゃん！」<br>**悠真**:「でも耐量子（格子暗号）で完全なIBEを作ろうとすると、公開鍵やパラメータが爆発的に巨大化してしまうんだ」 | **Aoi**: "Identity-Based Encryption lets us use email addresses or student IDs directly as public keys without certificates! So convenient!"<br>**Yuma**: "Indeed, but constructing full lattice-based post-quantum IBE blows up the public parameters astronomically!" |
| **2コマ目** | 蓮が「共謀ユーザー数 $k$ の上限（有界共謀）」を設けるBC-IBEのアイデアを出す | **蓮**:「もし悪意のある結託ユーザー数 $k$ に上限がある現実的なモデル（有界共謀BC-IBE）なら、軽量化できるのでは！？」<br>**結衣**:「従来方式でも共謀数 $k$ に比例してマスター公開鍵が肥大化し、IoTや軽量デバイスには載りませんでした……」 | **Ren**: "What if we assume a realistic model bounding malicious colluders up to $k$ (Bounded-Collusion IBE) to slim it down!?"<br>**Yui**: "Even so, conventional schemes scaled linearly with $k$, remaining too heavy for IoT microcontrollers..." |
| **3コマ目** | 結衣が「組合せ論的群テスト（Group Testing）」と格子暗号の融合数理を展開する | **結衣**:「そこで横浜国大SPIRAL・佐藤准教授と四方教授のCANS 2024論文です！ 不良品検査の群テスト行列を格子LWEに統合し、鍵サイズを劇的に圧縮しました！」<br>**葵**:「何十人もの結託者を、たった数個の数理テストパターンで一網打尽に封じ込めるなんて、魔法のパズルみたい！」 | **Yui**: "Enter YNU SPIRAL's CANS 2024 paper by Assoc. Prof. Sato & Prof. Shikata! Integrating combinatorial group testing with lattice LWE drastically compresses parameters!"<br>**Aoi**: "Bounding dozens of colluders with just a handful of mathematical test patterns is pure combinatorial magic!" |
| **4コマ目** | 手のひらサイズの超小型マイコン上で、コンパクトな耐量子IBEが瞬時に復号され、4人が歓喜する | **蓮・結衣**:「理論暗号の洗練が、IoTと次世代ネットの境界を打ち破る！」<br>**全員**:「数理のコンパクト化が、未来のサイバーセキュリティを手のひらに届ける！」 | **Ren & Yui**: "Theoretical cryptographic elegance shatters the boundaries of IoT and next-gen networks!"<br>**All**: "Mathematical compaction brings post-quantum security right into the palm of our hands!" |

---

## 📖 小説本文

「相手の公開鍵証明書（X.509）をCAからダウンロードして、失効リスト（CRL）を確認して……なんて面倒な手続き、全部すっ飛ばせないの？」

橘葵が頬杖をつきながら呟いた。

「葵先輩、それこそが1984年にアディ・シャミア（Adi Shamir）が夢見た**『IDベース暗号（Identity-Based Encryption: IBE）』**の神髄ですよ」

白石結衣が微笑みながらノートPCの画面を向けた。
「IBEでは、受信者のメールアドレス `alice@ynu.ac.jp` や社員番号といった文字列そのものが公開鍵になります。送信者は証明書を一切検証することなく暗号文を送ることができ、受信者は鍵生成センタ（PKG: Private Key Generator）から自分のIDに対応した秘密鍵を受け取るだけで復号できます」

「それ、最高じゃん！」葵が身を乗り出す。「全人類がIBEを使えば、PKI（公開鍵基盤）の複雑なトラブルから解放されるよ！」

「ところが、ポスト量子（耐量子）の世界になると、途端に分厚い壁が立ちはだかるんだ」

大学の講義を終えて駆けつけた城崎悠真が、黒板に格子暗号のLWE（Learning With Errors）問題を書き連ねた。
「従来のIBEはペアリング写像（楕円曲線の双線形写像）に依存していたけれど、ペアリングはショアの量子アルゴリズムで完全に破られてしまう。そこで格子暗号に基づく耐量子IBE（LWEベース）が研究されてきた。でも、完全な格子IBEはトラップドア生成行列や基底のサイズが巨大で、計算コストも膨大なんだ」

「そこで登場したのが、**有界共謀耐性（Bounded-Collusion Resistance）**という実用的な割り切りなんだね」神崎蓮が指をパチンと鳴らした。

「そう」悠真が頷く。「現実の社内ネットワークや組織において、100万人全員が結託して暗号系を攻撃することはまず考えにくい。せいぜい『悪意のある攻撃者が最大 $k$ 人の不正ユーザーの秘密鍵を買い集めて結託（Collusion）する』というシナリオを防げれば十分なケースが多い。これが**BC-IBE（Bounded-Collusion IBE）**だ。しかし……従来のBC-IBE方式でも、結託許容数 $k$ を大きくすると、マスター公開鍵（MPK）のサイズが $O(k)$ またはそれ以上に急拡大してしまうという致命的な弱点があった」

「そのボトルネックを根底から覆したのが、横浜国立大学SPIRALの佐藤慎悟准教授と四方順司教授の国際会議論文（CANS 2024 / SCIS 2025）なんだ」

---

## 🔬 技術解説：組合せ論的群テストとコンパクト格子BC-IBE

### 1. 課題：従来の格子BC-IBEのパラメータ肥大化
標準的な格子暗号系（LWE問題に基づく暗号系）において、有界共謀耐性を持たせる場合、マスター公開鍵 $MPK$ には多数のランダム行列 $A_i \in \mathbb{Z}_q^{n \times m}$ を並べる必要があった。
結託数 $k$ の攻撃者が秘密鍵 $sk_{ID_1}, \dots, sk_{ID_k}$ を合成して未認可のID $ID^*$ の秘密鍵を偽造できないようにするためには、独立な次元を確保するためにマスター公開鍵サイズが $k$ に対して線形に増大していた。

### 2. 救世主：非適応的群テスト（Non-Adaptive Group Testing）の導入
SPIRALの研究グループは、感染症検査や不良品スクリーニングで発展した離散数学理論**「群テスト（Group Testing）」**を暗号構造に組み込んだ。
- **群テストとは**:
  $N$ 個の検体の中に最大 $k$ 個の陽性検体（欠陥品）が含まれているとき、それらを個別に $N$ 回検査するのではなく、複数の検体を混ぜ合わせたプール検査を $M \ll N$ 回行うことで、すべての陽性検体を特定する理論。
- **$d$-disjunct 行列の特性**:
  バイナリ検査行列 $M \in \{0, 1\}^{t \times N}$ において、任意の $d$ 本の列ベクトルの論理和（OR）が、他のいかなる列ベクトルも包含しない（coverしない）とき、その行列を $d$-disjunct 行列と呼ぶ。

### 3. 格子LWEと群テストの直積統合
佐藤准教授・四方教授らは、$d$-disjunct 行列の行ベクトルの配置規則を利用して、LWEのマスター公開鍵行列の成分を共有・圧縮する新技術を開発した。
- ユーザーID $ID \in \{1, \dots, N\}$ に対し、$d$-disjunct 行列の第 $ID$ 列ベクトル $v_{ID} \in \{0, 1\}^t$ を対応付ける。
- 最大 $k$ 人のユーザーが結託しても、$d$-disjunct 行列の組合せ論的独立性により、未認可のターゲットID $ID^*$ に対応する格子部分空間を張ることが情報理論的に不可能となる。
- これにより、マスター公開鍵サイズを従来の $O(k \cdot \log N)$ から、劇的に圧縮されたサイズ $O(k^2 \cdot \log N)$ かつ定数倍を大幅に削減した**コンパクト耐量子BC-IBE**の構成に成功した。

---

「うわあ……！ まるでPCR検査のプール検診のアイデアが、最先端の耐量子格子暗号の鍵サイズを削ぎ落とすために使われているなんて！」葵は目を丸くして感嘆の声を上げた。

「情報理論と離散数学、そして代数的格子理論の美しい融合です」結衣が胸元で手を組んだ。「このSPIRALの研究成果によって、今まで処理能力の低さから耐量子暗号を諦めていた車載ネットワーク（CAN）やスマートメーター、超小型センサー端末でも、安全にIDベース暗号が使える道が拓かれたのです」

「数理の力で、重くて扱いにくかった耐量子暗号が、こんなに身近でコンパクトになるんだね」蓮が小型マイコンボードを愛おしそうに眺めた。

「暗号の世界は、ただ頑丈にするだけじゃない。『使いやすさ』と『小ささ』を数学的に極めることも、同じくらい崇高な科学なんだ」悠真が力強く語りかけた。

情報科学部室の窓からは、横浜の街のきらめく夜景が見え始めていた。4人の瞳には、次世代のセキュアな社会を支える技術への確信が宿っていた。
