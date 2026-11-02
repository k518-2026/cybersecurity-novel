import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")

# Episode 37 Metadata & Deep Dive
ep37_meta = {
    "num": 37,
    "date": "2026-11-02",
    "filename": "2026-11-02_ep37_eol_secondhand_routers.md",
    "title": "第37話 巡る古城と消えぬ記憶 〜中古ルーター流通とサポート終了の落とし穴〜",
    "tags": ["横浜国大SPIRAL", "中古ルーター", "フリマサイト", "EOL", "サポート終了", "個人情報漏洩", "ファクトリーリセット", "CSS2025学生論文賞", "佐々木貴之准教授", "吉岡克成教授"],
    "lead_intro": """帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL IoTセキュリティ実態調査ラボ
神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
横浜国立大学 SPIRAL・佐々木貴之准教授、吉岡克成教授、新堀寛大氏らの先端研究（CSS 2025 学生論文賞）、国内主要フリマサイト（メルカリ・ヤフオク・ラクマ等）における中古家庭用Wi-Fiルーターの流通実態、メーカーのセキュリティサポート終了（EOL: End-of-Life）機器の大量出品と既知脆弱性放置、出品者による初期化（ファクトリーリセット）の不徹底とISP認証情報（PPPoE ID/PW）・Wi-Fi暗号鍵の残存、ボットネット踏み台リスク、サーキュラーエコノミー（循環社会）とセキュリティガバナンス
- [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
- 新堀 寛大, 九鬼 琉, 藤井 翔太, 佐々木 貴之, 小林 信博, 吉岡 克成. 『国内フリマサイトにおけるサポートが終了した中古ルーターの流通状況の調査』. コンピュータセキュリティシンポジウム 2025 (CSS 2025), CSS2025学生論文賞, 2025年10月.""",
    "dialogues": [
        ("第1コマ<br>【起】",
         "蓮のフリマ爆買い自慢：新品の10分の1！中古ルーター最高じゃん！<br>届いたばかりの中古ルーターを掲げ、「フリマなら数百円でルーターが手に入る！安くて動くんだからコスパ最強だろ！」と笑顔の蓮。",
         "蓮: 「フリマなら定価の10分の1以下！安くて普通に動くんだから、中古ルーターこそ最強の選択だろ！」",
         "Ren: 'Flea markets sell routers at a tenth of retail price! Cheap and working—secondhand is hands down the best choice!'"),
        ("第2コマ<br>【承】",
         "結衣の型番調査と戦慄：5年前にサポート終了、しかも前の持ち主のISP情報が残存！<br>ノートPCの脆弱性データベースを指差し、「型番を調べたら5年前にEOL、しかも前の契約情報が丸見えよ！」と警告する結衣。",
         "結衣: 「甘すぎます！5年前にサポート完全終了（EOL）でパッチなし、前の持ち主のプロバイダ認証情報まで残存してます！」",
         "Yui: 'Hopelessly naive! Support ended 5 years ago with zero patches, and previous owner ISP credentials are still wide open!'"),
        ("第3コマ<br>【転】",
         "悠真TAによるCSS 2025受賞論文「国内フリマの中古ルーター実態」解説<br>CSS 2025学生論文賞のデータを投影し、数千台の流通実態調査で浮き彫りになった高いEOL率とリセット不徹底の脅威を解説する悠真。",
         "悠真: 「佐々木准教授・吉岡教授らの研究では、フリマ流通品の多くがEOLで、ファクトリーリセット不徹底が多発していたんだ。」",
         "Yuma: 'Prof. Sasaki & Yoshioka found most flea-market routers were EOL and frequently lacked proper factory resets.'"),
        ("第4コマ<br>【結】",
         "物を大切にする心とサイバー安全の調和を誓う二人<br>初期化ボタンを慎重に確認し、単なる安さではなく製品ライフサイクル全体の安全を見極める責任を胸に刻む蓮と結衣。",
         "蓮: 「安さの裏に放置された穴があったんだな……リサイクルするならセキュリティの寿命も確認しなきゃ！」<br>結衣: 「ええ。物理的な機器が動いても、安全の息が止まっていては使えません。責任ある循環社会を創りましょう。」",
         "Ren: 'Unpatched holes lurked behind that cheap price... recycling hardware means verifying security lifespans too!'<br>Yui: 'Indeed. Hardware may function, but without security life support, it is dead on arrival. Let us champion responsible lifecycles.'")
    ],
    "fig_file": "figures/fig37_eol_secondhand_routers.png",
    "fig_caption": "国内フリマサイトにおけるサポート終了中古ルーター流通リスクとセキュリティガバナンス（CSS 2025）構造図解",
    "column_sections": [
        ("1. C2Cフリマアプリの普及と「中古Wi-Fiルーター」の隠れた爆弾",
         """メルカリ、Yahoo!オークション、楽天ラクマなどのC2Cフリマプラットフォームの爆発的普及により、スマートフォンだけでなく家庭用Wi-Fiルーターやネットワーク機器の中古取引が日常的なものとなりました。
「一人暮らしを始めるから」「自宅のWi-Fiを安く中継したいから」と、新品の数分の一から数百円という破格の値段で中古ルーターを購入するユーザーは後を絶ちません。
しかし、一般の消費者はもちろん、ITに詳しい高校生やエンジニアであっても見落としがちな**「二重のサイバーリスク」**がここに潜んでいます。
1. **セキュリティサポート終了（EOL: End-of-Life / EOS: End-of-Support）機器の蔓延**: メーカーが脆弱性修正パッチの提供を停止しているため、既知のセキュリティホールが永久に塞がれない。
2. **不揮発性メモリ内の個人情報・接続設定の残存**: 前の所有者が適切な「工場出荷時初期化（ファクトリーリセット）」を行わずに売却したため、ISPの接続ID・パスワード、Wi-Fi暗号化キー、VPN設定がそのまま読み出せてしまう。"""),
        ("2. なぜ「動く」のに危険なのか？ 放置された既知脆弱性とボットネット",
         """「電源が入ってインターネットに繋がるなら何の問題もないのでは？」と考えるのは致命的な誤りです。
ルーターは家庭やオフィスの「外の世界（インターネット）」と「中の世界（プライベートLAN）」を隔てる玄関口（ゲートウェイ）です。
ルーターのファームウェアにリモートコード実行（RCE）やDNSキャッシュポイズニング、WebUI認証回避などの脆弱性が存在する場合、攻撃者はインターネット側から数秒で機器を乗っ取ることができます。
- **MiraiやMoziなどのIoTボットネットへの自動編入**: 乗っ取られた中古ルーターは、国家や重要インフラを標的としたDDoS攻撃の踏み台として24時間悪用されます。
- **中間者攻撃とフィッシング誘導**: ルーター内のDNS設定が犯罪者のサーバーに書き換えられると、家庭内のPCやスマホが正規の銀行やショッピングサイトにアクセスしようとした際、本物そっくりの偽サイトへ強制転送されてパスワードやクレジットカード情報を盗まれます。
サポートが終了したルーターは、どんなに外観が綺麗で通信速度が出ていようとも、**「鍵の壊れた玄関ドア」**をネット上に晒しているのと同じなのです。"""),
        ("3. 横浜国大SPIRALの衝撃的実態調査（CSS 2025 学生論文賞）",
         """横浜国立大学 SPIRALの**佐々木貴之 准教授**、**吉岡克成 教授**、**新堀寛大 氏**らの研究チームは、国内シンポジウム **CSS 2025** において論文『*国内フリマサイトにおけるサポートが終了した中古ルーターの流通状況の調査*』を発表し、優れた学術的・社会的価値が認められ**CSS2025学生論文賞**を受賞しました。
- **数千台規模のフリマ出品データを体系的クローリング**:
  国内主要フリマサイトにおける中古Wi-Fiルーターの出品情報を自動収集し、各メーカーの公式サポート状況データベースと照合。その結果、**取引されている中古ルーターの極めて高い割合がすでにサポート終了（EOL）を迎えた危険なモデルである**という実態を初めて定量的に立証しました。
- **実機検証によるファクトリーリセット不徹底の露見**:
  研究チームが実際に流通している機器を抽出調査したところ、前の持ち主のプロバイダ接続情報（PPPoE ID/PW）や宅内SSID・暗号化キーが残存している個体が多数確認されました。悪意ある第三者がこれを購入すれば、元の持ち主のISPアカウントを不正利用してサイバー攻撃の発信元を偽装することも可能です。

サーキュラーエコノミー（資源循環型社会）の推進と、サイバー空間の安全性担保。フリマ事業者によるEOL警告表示の義務化や、ハードウェアの寿命とパッチの責任ある管理（Lifecycle Security）をどう社会実装すべきか、SPIRALの先駆的警鐘は産業界・政策決定者からも熱い注目を集めています。""")
    ]
}

# Episode 38 Metadata & Deep Dive
ep38_meta = {
    "num": 38,
    "date": "2026-11-02",
    "filename": "2026-11-02_ep38_darknet_thirdparty_dependencies.md",
    "title": "第38話 闇市を支える蜘蛛の糸 〜ダークネットの外部依存性とLLMシグネチャ〜",
    "tags": ["横浜国大SPIRAL", "ダークネット", "ダークウェブ", "Tor", "Onionサービス", "第三者依存性", "単一障害点", "LLM", "シグネチャ生成", "CSS2025", "インミンパパ特任准教授", "吉岡克成教授"],
    "lead_intro": """帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL サイバーインテリジェンス研究室
神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
横浜国立大学 SPIRAL・イン・ミンパパ特任准教授、吉岡克成教授、内野彰紀氏らの先端研究（CSS 2025）、Torオニオンルーティングによるダークネットマーケット（DNM: Darknet Market）の実態、外界と完全遮断されているという「完全匿名性の神話」の崩壊、現代Webサイトとしての外部サービス依存（DDoS防御CAPTCHA、CDN、暗号資産決済API、外部ホスティング）、クリアネット（表層Web）依存がもたらす単一障害点（SPOF）とIPアドレス漏洩リスク、大規模言語モデル（LLM）を用いたOnion DOM構造の自動意味解析と第三者依存シグネチャ自動生成、国際法執行機関（ユーロポール・FBI等）によるサプライチェーン遮断捜査
- [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
- 内野 彰紀, イン ミンパパ, 吉岡 克成. 『ダークネットマーケットの第三者サービス依存性調査：LLMによる検知とシグネチャ生成』. コンピュータセキュリティシンポジウム 2025 (CSS 2025), 2025年10月.""",
    "dialogues": [
        ("第1コマ<br>【起】",
         "蓮のダークウェブ幻想：Torの闇市は外界から遮断された無敵の要塞だろ！<br>Onionブラウザの画面を指差し、「ダークウェブの闇市は表のネットと完全に切り離された無敵の匿名要塞だろ！」と興奮する蓮。",
         "蓮: 「Torのダークネットマーケットは、表のネットから完全に隔離された無敵の匿名要塞だろ！」",
         "Ren: 'Darknet markets on Tor are invincible anonymous fortresses completely severed from the clearnet!'"),
        ("第2コマ<br>【承】",
         "結衣の冷徹な指摘：CAPTCHAや決済APIなど外部サービスなしに運営不可能！<br>Webインスペクターのコードを示し、「CAPTCHAや暗号資産決済など、表のクリアネットAPIに依存しているわ」と看破する結衣。",
         "結衣: 「幻想です。DDoS対策のCAPTCHAや暗号資産決済APIなど、表のサービスを繋がなければ動かないわ。」",
         "Yui: 'Pure fantasy. Without external DDoS CAPTCHAs and crypto payment APIs, they cannot function for a second.'"),
        ("第3コマ<br>【転】",
         "悠真TAによるCSS 2025論文「LLMによる外部依存検知とシグネチャ生成」解説<br>CSS 2025論文の相関図を投影し、LLMでOnionサイトのDOMを解析して外部依存の単一障害点を特定するSPIRALの手法を語る悠真。",
         "悠真: 「イン特任准教授らはLLMでOnionサイトの依存関係を暴き、闇市のアキレス腱を突くシグネチャを作ったんだ。」",
         "Yuma: 'Assoc. Prof. Yin used LLMs to map onion dependencies and generate signatures targeting darknet Achilles heels.'"),
        ("第4コマ<br>【結】",
         "闇を支える蜘蛛の糸を断つ！真のインテリジェンスへの目覚め<br>巨大な脅威マップを見つめ、要塞そのものではなくそれを支える外部サプライチェーンを見抜く洞察力に感動する蓮と結衣。",
         "蓮: 「要塞を正面から叩くんじゃなく、外から支えてる蜘蛛の糸を断ち切る……インテリジェンスって奥が深い！」<br>結衣: 「ええ。複雑なネットワークの依存構造を暴く数理とAIこそ、悪の根を断つ真の力ですね。」",
         "Ren: 'Don\\'t breach the fortress walls—sever the invisible web threads holding it up! Intelligence is brilliant!'<br>Yui: 'Indeed. Tracing complex dependency graphs with AI is the true power that uproots cybercrime.'")
    ],
    "fig_file": "figures/fig38_darknet_thirdparty_dependencies.png",
    "fig_caption": "ダークネットマーケットの第三者サービス依存性調査とLLMシグネチャ生成（CSS 2025）構造図解",
    "column_sections": [
        ("1. 「無敵の孤島」ではないダークネットマーケット（DNM）の現実",
         """違法薬物、不正取得されたクレジットカード情報、サイバー攻撃ツールやゼロデイエクスプロイトが売買される「ダークネットマーケット（DNM: Darknet Market）」。
これらはTor（The Onion Router）やI2Pなどの暗号化匿名通信ネットワーク上で運用される「Hidden Services（Onionサービス）」として構築されており、一般的なWebブラウザからはアクセスできず、サーバーの物理的なIPアドレスや設置場所は多重の暗号化によって隠蔽されています。
そのため、一般には「表層のインターネット（クリアネット）とは完全に切り離された孤立無援のブラックボックス要塞」であるかのように錯覚されがちです。
しかし、現実のDNMは数千〜数万人のユーザーが売買を行う**極めて複雑で高度な「現代のWebアプリケーション」**です。自分たちだけの閉じたサーバーだけで完結させることは技術的にもコスト的にも不可能であり、表層のクリアネットや外部の第三者サービスに深く依存しています。"""),
        ("2. 外部依存がもたらす「単一障害点（SPOF）」と匿名性の崩壊",
         """DNMが依存している主な外部第三者サービスには以下のようなものがあります。
- **DDoS防御とCAPTCHA（画像認証）**: ライバル組織や法執行機関からの妨害DDoS攻撃を防ぐため、外部のアンチDDoSプロバイダやCAPTCHA検証サーバーを利用。
- **暗号資産（ビットコイン・Monero等）決済APIとミキシングサービス**: トランザクションの着金確認やブロックチェーン追跡を難読化するための外部ウォレットAPI。
- **CDN（コンテンツ配信網）や外部ホスティング・アナリティクス**: サイトのロードを高速化するための画像キャッシュやアクセス解析スクリプト。

ここに、犯罪インフラの**「アキレス腱（単一障害点: Single Point of Failure）」**が存在します。
もし依存している外部のCAPTCHAプロバイダがダウンしたり、法執行機関に押収されれば、ダークネットマーケット全体がログイン不能となって取引が停止します。
さらに、ブラウザが外部サービスと通信する際に発生する「クリアネットへのIPパケットリーク」「タイミング解析」「クロスサイト・フィンガープリント」によって、Torの暗号化のベールが剥がされ、サーバーの真のIPアドレスや管理者の足跡が特定される契機となるのです。"""),
        ("3. 横浜国大SPIRALの革新：LLMによるDOM構造の自動意味解析とシグネチャ生成（CSS 2025）",
         """横浜国立大学 SPIRALの**イン・ミンパパ 特任准教授**、**吉岡克成 教授**、**内野彰紀 氏**らは、**CSS 2025** において論文『*ダークネットマーケットの第三者サービス依存性調査：LLMによる検知とシグネチャ生成*』を発表しました。
- **手作業の限界を超える「LLM意味解析エンジン」**:
  ダークウェブ上のサイトは、解析や摘発を妨害するためにHTMLのソースコードや難読化JavaScriptが極めて複雑に入り組んでいます。研究チームは、クローリングした膨大なOnionサイトのDOM（Document Object Model）構造を、最新の**大規模言語モデル（LLM）**に読み込ませ、外部サービスへの通信やAPI呼び出しを行っているコード箇所を文脈から高精度に自動検出する枠組みを開発しました。
- **検知シグネチャの自動生成とサプライチェーン・マッピング**:
  LLMは単に検出するだけでなく、侵入検知システム（IDS）や脅威インテリジェンス（CTI）プラットフォームで即座に利用可能な「正規表現シグネチャ」や「YARAルール」を自動生成。どの闇市場がどの外部インフラを共有しているかという**「地下サプライチェーンの全体相関図」**を世界で初めて可視化しました。

正面から要塞の扉を叩くのではなく、要塞を外側から支えている細い蜘蛛の糸（外部依存）を断ち切る。国際警察機構やセキュリティベンダーと連携し、サイバー犯罪エコシステムの中枢を兵站から制圧する最先端サイバーインテリジェンスの神髄がここにあります。""")
    ]
}

# Episode 39 Metadata & Deep Dive
ep39_meta = {
    "num": 39,
    "date": "2026-11-02",
    "filename": "2026-11-02_ep39_homomorphic_signature_designated_evaluator.md",
    "title": "第39話 託された演算と選ばれし証 〜指定評価者付き準同型署名の奇跡〜",
    "tags": ["横浜国大SPIRAL", "準同型署名", "指定評価者", "HS-DE", "NexCrypt Lab", "IEEE Access", "四方順司教授", "高機能暗号", "プライバシー保護計算", "真正性保証"],
    "lead_intro": """帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 次世代暗号ラボ（NexCrypt Lab）
神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
横浜国立大学 SPIRAL・四方順司教授（NexCrypt Lab長）、白石和真氏、原啓祐氏らの国際学術論文（IEEE Access 2025 / Vol. 13）、スマートグリッドや医療AI・IoTビッグデータにおけるクラウド計算委託の安全性、従来のデジタル署名の限界（データ加工で署名が壊れる問題）、署名された生データから直接演算（平均・総和・線形変換）を行い計算結果に対する正当な署名を秘密鍵なしで導出できる「準同型署名（Homomorphic Signature: HS）」、従来の準同型署名における「誰でも勝手に評価・改ざん演算ができてしまう」未認可計算リスク、特定の正規トークンを持つ評価者のみに演算を許可する「指定評価者付き準同型署名（HS-DE: Homomorphic Signature with Designated Evaluator）」の世界初の厳密モデル化と安全な暗号構成法
- [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
- Kazuma Shiraishi, Keisuke Hara, Toi Tomita, Kyosuke Yamashita, Junji Shikata. "Homomorphic Signature with Designated Evaluator." *IEEE Access*, Vol. 13, pp. 23950-23958, 2025.""",
    "dialogues": [
        ("第1コマ<br>【起】",
         "蓮のクラウド委託論：電子署名をつけてクラウドに送れば改ざんされないだろ！<br>電力メーターの模型を掲げ、「電子署名をつけてクラウドに計算を任せれば、改ざんも防げて完璧だろ！」と自信満々の蓮。",
         "蓮: 「IoTデータをクラウドに集計させるなら、普通の電子署名をつけておけば改ざんされないから完璧だろ！」",
         "Ren: 'If we outsource IoT data aggregation to the cloud, standard digital signatures will block tampering completely!'"),
        ("第2コマ<br>【承】",
         "結衣の署名破壊と秘密鍵漏洩リスクの指摘<br>破損した署名アイコンを示し、「普通の署名は平均値を求めた瞬間に無効化し、秘密鍵を渡せば偽造し放題よ」と指摘する結衣。",
         "結衣: 「無知すぎます。普通の署名は計算加工された瞬間に無効化し、秘密鍵を預ければデータ偽造し放題です。」",
         "Yui: 'Utterly ignorant. Standard signatures break the instant you compute averages, and giving private keys invites total forgery.'"),
        ("第3コマ<br>【転】",
         "悠真TAによる四方教授らのIEEE Access 2025論文「指定評価者付き準同型署名」解説<br>IEEE Access 2025論文の数理モデルを投影し、署名を生かしたまま計算でき、かつ「指定評価者」のみに演算を許可する四方教授らの画期的暗号を説く悠真。",
         "悠真: 「四方教授らは、許可された指定評価者だけが署名データ上で演算できる新暗号HS-DEを世界で初めて確立したんだ！」",
         "Yuma: 'Prof. Shikata pioneered HS-DE, a breakthrough cipher allowing only authorized designated evaluators to compute over signed data!'"),
        ("第4コマ<br>【結】",
         "データの信頼を数理で託す！プライバシーと真正性の調和に感動する二人<br>複雑な格子数式が輝くディスプレイを見つめ、計算の正しさとデータのプライバシーを同時に守り抜く数学の極致に心震わせる蓮と結衣。",
         "蓮: 「秘密鍵を渡さなくても、選ばれたサーバーだけが正しく計算したことを数学が証明してくれるなんて……凄すぎる！」<br>結衣: 「真正性とプライバシーの究極の調和……これぞ現代暗号数理が切り拓く知のフロンティアですね。」",
         "Ren: 'Without giving away private keys, math proves only the chosen server computed faithfully... pure genius!'<br>Yui: 'The ultimate harmony of authenticity and privacy... this is the true frontier forged by cryptographic mathematics.'")
    ],
    "fig_file": "figures/fig39_homomorphic_signature_designated_evaluator.png",
    "fig_caption": "指定評価者付き準同型署名（HS-DE, IEEE Access 2025）の数理構造と安全なクラウド計算委託モデル図解",
    "column_sections": [
        ("1. クラウド計算委託が直面する「署名が壊れる」ジレンマ",
         """スマートシティのスマートメーター（電力計）、コネクテッドカーの走行ログ、病院の電子カルテなど、膨大なIoTデバイスから収集されるデータは、リソースの限られた端末単体では処理しきれないため、外部のクラウドサーバーに送って集計・統計解析・機械学習を行わせるのが一般的です。
しかし、ここで暗号技術の根本的なジレンマに直面します。
- **普通の電子署名（RSAやECDSA）の限界**:
  デジタル署名は「データが1ビットでも改ざんされていないこと」を保証する仕組みです。そのため、クラウドサーバーが生データを集計して「全体の平均値」や「合計値」を計算した瞬間、元の署名は完全に壊れてしまい、第三者からは「正しく計算された結果なのか、悪意あるクラウドが改ざんした結果なのか」を検証することができなくなります。
- **秘密鍵を預ける危険性**:
  かといって、クラウドに集計結果に対する署名を生成させるためにデバイスの署名用秘密鍵を預けてしまえば、万が一クラウドがハッキングされた際に、過去・現在・未来のすべてのデータを無制限に偽造されてしまいます。"""),
        ("2. 準同型署名（Homomorphic Signature）の登場と「誰でも計算できる」落とし穴",
         """この難問を解決するために考案された高機能暗号が**「準同型署名（Homomorphic Signature: HS）」**です。
準同型署名では、元の生データに対する署名を持っていれば、**署名秘密鍵を持たない外部の計算サーバーであっても、データ同士の演算（足し算や線形結合など）を行い、その『計算結果に対する正当な署名』を数学的に直接導出**することができます。
データの受け取り手（検証者）は、元の生データを見ることなく、「この平均値は、正当なデバイス群から送信されたデータから間違いなく計算されたものである」と数学的に100%検証できます。

しかし、従来の標準的な準同型署名には、実用上の重大なセキュリティ上の死角が存在していました。
それは**「公開鍵さえあれば、世界の誰であっても勝手に準同型演算を行えてしまう」**という点です。
悪意ある第三者や無許可の外部ノードが、中間データを勝手に組み合わせた無意味な計算結果をでっち上げたり、意図しない計算を行わせることで元データの機微なパターンを逆算・漏洩させてしまうリスクを排除できなかったのです。"""),
        ("3. 横浜国大・四方順司教授が切り拓いた「指定評価者付き準同型署名（HS-DE）」（IEEE Access 2025）",
         """横浜国立大学 SPIRALの次世代暗号ラボ（NexCrypt Lab）長を務める**四方順司 教授**、**白石和真 氏**、**原啓祐 氏**らの研究チームは、国際学術誌 **IEEE Access 2025**（Vol. 13）において論文『*Homomorphic Signature with Designated Evaluator*』を発表し、この限界を打ち破る世界初の画期的暗号モデルを提案・証明しました。
- **「指定評価者（Designated Evaluator）」による演算権限の暗号的制御**:
  研究チームは、準同型演算を行える主体を、特定の評価鍵（Evaluation Key）を正当に付与された「指定された評価者」だけに厳密に制限する新しい暗号プリミティブ**「HS-DE（Homomorphic Signature with Designated Evaluator）」**を定式化しました。
- **未認可ノードによる不正演算・情報漏洩の完全遮断**:
  評価鍵を持たない第三者は、公開鍵や署名データを持っていても準同型演算を行うことが一切できません。これにより、信頼できない分散クラウド環境やマルチテナント環境においても、契約した特定の計算サーバーだけが正当な演算を行える安全なデータパイプラインが保証されます。
- **厳密なセキュリティ証明と構成法の提示**:
  暗号学的なゲームベース安全モデルにおいて、「指定されていない者による計算の偽造不可能性」と「真正性の保持」を数学的に厳密に証明し、標準的な暗号仮定から安全に実装できる具体的なアルゴリズム構成を世界で初めて提示しました。

信頼できないクラウドやAIワーカーにデータを委託しながら、その計算の正しさと機密性を数学的に両立する。横浜国大SPIRALの先端数理は、次代の安全なデータ駆動型社会を支える不可視の強靭な礎を築いています。""")
    ]
}

def format_novel_body(raw_text):
    raw_text = raw_text.replace("\r\n", "\n")
    parts = [p.strip() for p in raw_text.split("* * *") if p.strip()]
    if len(parts) == 1:
        parts = [p.strip() for p in raw_text.split("***") if p.strip()]
    return "\n\n✦ ✦ ✦\n\n".join(parts)

def build_markdown(meta):
    raw_path = os.path.join(CONTENT_DIR, f"ep{meta['num']}_novel_raw.txt")
    if not os.path.exists(raw_path):
        print(f"Warning: {raw_path} not found yet.")
        return False
    with open(raw_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    
    novel_body = format_novel_body(raw_text)
    
    # build table
    table_rows = []
    for item in meta["dialogues"]:
        panel_name, situation, ja, en = item
        table_rows.append(f"| **{panel_name}** | **{situation}** | **{ja}** | **{en}** |")
    dialogue_table = "\n".join(table_rows)
    
    # build column sections
    column_texts = []
    for title, body in meta["column_sections"]:
        column_texts.append(f"### {title}\n\n{body}")
    column_block = "\n\n".join(column_texts)
    
    md_content = f"""---
title: "{meta['title']}"
episode_num: {meta['num']}
date: {meta['date']}
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: {json.dumps(meta['tags'], ensure_ascii=False)}
---

# {meta['title']}

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: {meta['lead_intro'].splitlines()[0]}
> - **登場人物**: {meta['lead_intro'].splitlines()[1]}
> - **学習テーマ**: {meta['lead_intro'].splitlines()[2]}
> - **探訪・参照研究論文**:
{chr(10).join('>   ' + line for line in meta['lead_intro'].splitlines()[3:])}

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第{meta['num']}話 4コマ漫画イラスト](illustrations/ep{meta['num']}_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
{dialogue_table}

---

## 📖 小説本文

{novel_body}

---

## 📊 TikZによるセキュリティ構造図解

![{meta['fig_caption']}]({meta['fig_file']})

---

## 💡 高校生のためのセキュリティ深掘りコラム

{column_block}
"""
    out_path = os.path.join(CONTENT_DIR, meta["filename"])
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Created: {out_path} ({len(md_content)} chars)")
    return True

if __name__ == "__main__":
    for meta in [ep37_meta, ep38_meta, ep39_meta]:
        build_markdown(meta)
    print("Markdown assembly check complete.")
