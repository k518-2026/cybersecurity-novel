---
title: "第59話 幾何に潜む罠と連鎖の暴風 〜古典McEliece暗号におけるマルチユーザー・バックドア解析〜"
episode: 59
arc: 2
category: "spiral_paper"
theme: "横浜国立大学SPIRAL・三浦優樹氏・趙亨騄氏・佐藤慎悟准教授・四方順司教授（NexCrypt Lab）、MobiSec 2024、符号ベース暗号Classic McElieceにおけるバックドア埋め込みの可能性およびマルチユーザー環境下でのバックドア検出・解読脆弱性の数学的解析"
dss_topic: "耐量子暗号（PQC）・符号ベース暗号・Classic McEliece・マルチユーザーセキュリティ・バックドア解析・Goppa符号"
characters:
  - name: "城崎 悠真"
    role: "横浜国大1年 / SPIRAL学生研究員 / TA"
  - name: "橘 葵"
    role: "高校3年 / 元情報科学部部長"
  - name: "神崎 蓮"
    role: "高校1年 / 情報科学部（IoT・ハード班）"
  - name: "白石 結衣"
    role: "高校1年 / 情報科学部（暗号数理班）"
cover_image: "ep59_4koma.png"
figure_image: "fig59_mceliece_multiuser_backdoor.png"
---

# 第59話 幾何に潜む罠と連鎖の暴風 〜古典McEliece暗号におけるマルチユーザー・バックドア解析〜

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

| コマ | シチュエーション | 日本語セリフ | 英語セリフ (English) |
| :--- | :--- | :--- | :--- |
| **1コマ目** | 結衣がホワイトボードに二元Goppa符号の生成行列 $G$ と置換行列 $P$、可逆行列 $S$ を書き連ねる | **結衣**:「NIST耐量子標準化の最終候補『Classic McEliece』は、40年以上破られていない絶対の堅牢性を誇る符号暗号です！」<br>**葵**:「巨大な公開鍵行列の中にランダムな誤りを混ぜて暗号化するんだよね。これなら量子コンピュータでも絶対に破れないの？」 | **Yui**: "A NIST post-quantum finalist, Classic McEliece, is a code-based cipher unbroken for over 40 years!"<br>**Aoi**: "It encrypts by mixing random error vectors into giant generator matrices. Is it truly impregnable even to quantum attacks?" |
| **2コマ目** | 悠真が不敵な笑みを浮かべ、行列のパラメータ生成アルゴリズムに赤ペンで印をつける | **悠真**:「鍵生成器そのものに悪意の設計者が『秘密の数学的トラップドア（バックドア）』を仕込んでいたらどうなると思う？」<br>**蓮**:「えっ！？ 単一のユーザーならランダムに見えても、複数人の鍵が集まると法則が浮き彫りになる……！？」 | **Yuma**: "What if a malicious designer secretly embedded a mathematical trapdoor inside the key generation algorithm itself?"<br>**Ren**: "Wait! Even if it looks pseudo-random for one user, does a hidden pattern emerge once multiple users' keys gather!?" |
| **3コマ目** | 結衣と悠真が「マルチユーザー線形代数攻撃」の連立方程式を導出し、バックドアを無力化する解を提示する | **結衣**:「横浜国大SPIRALの三浦さん・四方教授たちのMobiSec 2024最新論文では、マルチユーザー環境におけるバックドアの相関性を数学的に暴いたのです！」<br>**葵**:「設計者がこっそり全ユーザーの鍵を覗き見しようとしても、数学のメスでその悪意をあぶり出せるんだ！」 | **Yui**: "YNU SPIRAL's MobiSec 2024 paper by Miura and Prof. Shikata mathematically exposes backdoor correlations in multi-user settings!"<br>**Aoi**: "Even if a rogue designer tries to spy on everyone, rigorous linear algebra exposes and neutralizes the hidden malice!" |
| **4コマ目** | 4人が解読方程式を完成させ、ホワイトボードの前でハイタッチを交わす | **蓮・結衣**:「ハードウェアや規格に潜む黒幕の罠すら、理論暗号の力で暴き出す！」<br>**全員**:「幾何と代数の真理を武器に、完全な信頼を築く未来へ進もう！」 | **Ren & Yui**: "Even black-box hardware trapdoors can be laid bare by theoretical cryptography!"<br>**All**: "Armed with the truth of geometry and algebra, we build unbreakable trust for the post-quantum era!" |

---

## 📖 小説本文

「40年間、一度も破られたことがない……！？」

橘葵が思わず身を乗り出した。青葉台高校情報科学部室のホワイトボードには、白石結衣の手によって縦横数百ビットにも及ぶ巨大な二元体上の行列が描かれていた。

「はい、葵先輩」結衣が満足そうに頷く。「1978年にロバート・マックエリス（Robert McEliece）が提案した『McEliece暗号』は、二元Goppa符号（Binary Goppa Code）という誤り訂正符号の復号困難性を安全性の根拠にしています。RSA暗号や楕円曲線暗号がショアの量子アルゴリズムで壊滅するのに対し、符号ベース暗号は量子コンピュータを用いても指数時間の計算量を要するため、NIST（米国国立標準技術研究所）のPQC標準化でも極めて高い信頼を獲得しています」

「格子暗号（Kyber）よりも歴史が古くて実績があるんだよね」神崎蓮が補足する。「公開鍵が数十万バイトから数メガバイトと巨大なのが唯一の欠点だけど、そのぶん暗号文サイズは小さくて、ハードウェアアクセラレータでの復号も爆速なんだ」

「無敵じゃん！」葵が胸を張った。「これを使っていれば、量子コンピュータの時代が来ても100%安心ってことね！」

「――もし、その暗号モジュールを作った国家やベンダが、最初から**『秘密の抜け穴（バックドア）』**を仕込んでいたらどうする？」

部室のドアを開けて入ってきた城崎悠真が、静かに問いかけた。

「え……バックドア？ でも、暗号アルゴリズムってオープンソースで数理的に公開されてるんじゃないの？」葵が瞬きする。

「アルゴリズムの仕様書がオープンであっても、**パラメータ生成（鍵生成パラメータの選定）**のプロセスがブラックボックス化されていたら話は別なんだ」悠真がノートPCを開き、横浜国立大学SPIRAL・NexCrypt Lab（四方順司教授・佐藤慎悟准教授ら）の三浦優樹氏らの最新研究論文（MobiSec 2024）をプロジェクターに投影した。

「タイトルは――**『Analysis of Backdoored (Classic) McEliece in a Multi-User Setting（マルチユーザー環境におけるバックドア付きClassic McElieceの解析）』**」

結衣の瞳が、数理的な好奇心でキラリと輝いた。
「McEliece暗号におけるバックドア……！ 設計者が鍵生成器の乱数種やGoppa多項式 $g(z)$ の選定規則に特定の代数幾何的関係性を忍ばせ、設計者だけが効率的に秘密鍵を復元できるようにする攻撃ですね！」

---

## 🔬 技術解説：Classic McEliece暗号とマルチユーザー・バックドア解析

Classic McEliece暗号は、誤り訂正符号の一種であるGoppa符号を利用した公開鍵暗号（KEM）である。

### 1. McEliece暗号の基本構造
- **秘密鍵（Private Key）**:
  有限体 $\mathbb{F}_{2^m}$ 上の次数 $t$ の既約多項式（Goppa多項式）$g(z)$、および $n$ 個の相異なる元からなるサポート集合 $L = (\alpha_1, \alpha_2, \dots, \alpha_n)$。
- **公開鍵（Public Key）**:
  パリティ検査行列 $H$ から導出される組織形式（Systematic Form）の生成行列 $G = [I_k \mid R] \in \mathbb{F}_2^{k \times n}$。
- **暗号化と復号**:
  平文メッセージ $m \in \mathbb{F}_2^k$ に対し、重み $t$ のランダム誤りベクトル $e \in \mathbb{F}_2^n$ を付加して暗号文 $c = mG + e$ を作成する。第三者はランダム線形符号のシンドローム復号問題（NP困難）を解く必要があるが、秘密鍵 $(g(z), L)$ を知る正当な受信者はパターソン（Patterson）のアルゴリズムにより多項式時間で誤り $e$ を特定・除去できる。

### 2. 単一ユーザー環境でのバックドア（Single-User Backdoor）
悪意ある設計者は、Goppa多項式 $g(z)$ やサポート $L$ を生成する際、標準的な擬似乱数生成器ではなく、設計者の秘密鍵 $sk_{adv}$ で暗号化した構造や弱符号（Weak Subcodes）を埋め込むことができる。
単一の公開鍵 $G$ を第三者がいくら検証しても、その統計的分布は真のランダムGoppa符号の公開鍵と区別がつかない（擬似ランダム性）。

### 3. マルチユーザー環境での綻び（Multi-User Correlation）
しかし、現代のインターネットやクラウドシステムでは、何万人、何百万人のユーザーが同じ暗号ライブラリやセキュアチップを用いて鍵を生成する。
YNU SPIRALの三浦・趙・佐藤・四方らは、**「マルチユーザー環境において、悪意の設計者が複数のユーザーに対して共通のマスター・トラップドア構造を再利用せざるを得ない」**という制約に着目した。

各ユーザー $i$ の公開パリティ検査部 $R^{(i)}$ に対し、設計者の埋め込んだトラップドア代数関係が直積空間上で連立代数方程式を構成する：
$$\det \left( \Phi(R^{(1)}, R^{(2)}, \dots, R^{(u)}) \right) = 0$$
SPIRALの研究グループは、単一鍵の検証では決して見抜けなかったバックドアの痕跡が、複数ユーザーの公開鍵をクロス集計・双線形代数解析（Bilinear Algebraic Analysis）することで、悪意の設計者以外の第三者であっても検知・逆コンパイルできる脆弱性の条件を数学的に解明したのである。

---

「鳥肌が立ったよ……！」蓮が唸った。「悪意の設計者が『自分だけが得をする秘密の裏口』を作ったとしても、それが多くのユーザーに配られた瞬間に、数学的な対称性の歪みが生まれて、第三者に裏口の鍵を奪われてしまうんだ！」

「その通り」悠真が笑みを浮かべた。「暗号にバックドアを仕込む行為は、暗号そのものを脆くするだけでなく、敵対者にもその裏口をフリーパスで提供することになる。SPIRALの数理セキュリティ研究は、『いかにバックドアを埋め込ませないか、もし存在したらいかに数学的にあぶり出すか』という、未来の標準化のための防護柵を打ち立てたんだ」

「数学の美しさって、こういうところにあるよね！」葵が満足そうにホワイトボードを拭きながら言った。「どんなに巧みに隠された悪意も、群と体と行列の光を当てれば、影がくっきりと浮かび上がる！」

「はい、葵先輩。私たちの理論暗号班も、さらに高度な数理防壁を追究していきましょう！」結衣が力強く頷いた。

夕暮れが校舎を包み込む中、4人の研究への情熱はますます熱く燃え上がっていた。
