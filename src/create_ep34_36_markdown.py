import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")

# Episode 34 Metadata & Deep Dive
ep34_meta = {
    "num": 34,
    "date": "2026-11-01",
    "filename": "2026-11-01_ep34_ethical_humint_telegram.md",
    "title": "第34話 潜入の影と倫理の光 〜Telegram犯罪捜査とインフォームド・コンセントのジレンマ〜",
    "tags": ["横浜国大SPIRAL", "HUMINT", "Telegram潜入", "メンロレポート", "インフォームドコンセント", "研究倫理", "CSS2025", "吉岡克成教授", "インミンパパ特任准教授"],
    "lead_intro": """帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL サイバー犯罪インテリジェンス研究室
神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
横浜国立大学 SPIRAL・吉岡克成教授、イン・ミンパパ特任准教授、久保颯汰氏らの先端研究（CSS 2025）、暗号化メッセージングアプリ（Telegram）上での脅威アクターに対する人的情報収集（HUMINT）、サイバー脅威インテリジェンス（CTI）における研究倫理原則「メンロレポート（Menlo Report）」、インフォームド・コンセント（事前説明と同意）の必然性と実施困難性、身分偽装によるおとり捜査リスク、段階的合意形成モデル（Phased Informed Consent）、倫理監視LLMによるリアルタイム・コンプライアンス検証
- [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
- 久保 颯汰, イン ミンパパ, 吉岡 克成, ほか. 『インフォームド・コンセントに基づくTelegram上の人的情報収集の実施可能性の検証』. コンピュータセキュリティシンポジウム 2025 (CSS 2025), 2025年10月.""",
    "dialogues": [
        ("第1コマ<br>【起】",
         "蓮の潜入捜査論：悪人を騙して捕まえるなら偽アカウント潜入も当然！<br>Telegramのチャット画面を掲げ、「犯罪者を捕まえるためなら偽アカウントで騙して情報を引き出せば手っ取り早いだろ！」と意気込む蓮。",
         "蓮: 「悪人を捕まえるためなら、裏垢で騙して潜入して情報を引き出すのが手っ取り早いだろ！」",
         "Ren: 'To catch bad guys, going undercover with burner accounts and extracting intel is the fastest way!'"),
        ("第2コマ<br>【承】",
         "結衣の倫理的指摘：メンロレポートとインフォームド・コンセントの原則<br>倫理指針の資料を広げ、「研究対象が人間である以上、事前の説明と同意（インフォームド・コンセント）が必須です」と冷徹に戒める結衣。",
         "結衣: 「甘いです。研究対象が人間である以上、メンロレポートの原則に従い同意を得る義務があります。」",
         "Yui: 'Naïve. As long as humans are research subjects, the Menlo Report mandates informed consent.'"),
        ("第3コマ<br>【転】",
         "悠真TAによるCSS 2025論文のHUMINTジレンマと倫理監視LLM解説<br>CSS 2025論文の図を指差しながら、正直に名乗れば逃げられ偽れば倫理違反になるジレンマと、段階的同意およびLLM監視のブレークスルーを解説する悠真。",
         "悠真: 「名乗れば逃亡、偽れば倫理違反。SPIRALの研究チームは段階的告知とLLM監視で突破口を開いたんだ。」",
         "Yuma: 'Confess and they flee, conceal and you violate ethics. SPIRAL cracked this via phased consent and LLM monitoring.'"),
        ("第4コマ<br>【結】",
         "正義の手段を選び抜く！真のサイバー守護者への誇りを誓う二人<br>透明な監査ログが流れる画面を見つめ、犯罪者と同じ闇に堕ちることなく、法の光の下で戦う誇りと覚悟を胸に刻む蓮と結衣。",
         "蓮: 「目的が正義でも、汚い手段じゃ悪党と同じだ……倫理の光の下で戦ってこそ真のディフェンダーだな！」<br>結衣: 「ええ。高い倫理観を胸に刻んでこそ、私たちは胸を張って科学の刃を振るえます。」",
         "Ren: 'Even for justice, foul means make us no better than villains. We must defend in the light of ethics!'<br>Yui: 'Indeed. With unyielding ethical integrity, we wield the blade of science with unwavering pride.'")
    ],
    "fig_file": "figures/fig34_ethical_humint_telegram.png",
    "fig_caption": "Telegram上の人的情報収集（HUMINT）におけるインフォームド・コンセントと倫理監視LLM（CSS 2025）構造図解",
    "column_sections": [
        ("1. サイバー犯罪の温床「Telegram」とHUMINT（人的情報収集）の最前線",
         """近年、ランサムウェア組織、初期アクセスブローカー（IAB）、マルウェア開発者などのサイバー犯罪者は、追跡が容易な従来の掲示板から、暗号化チャットアプリ「Telegram」や「Discord」のクローズドな地下コミュニティへと活動拠点を急速に移行させています。
こうした地下チャットルームでは、攻撃ツールの売買、標的企業の脆弱性情報、盗み出されたクレデンシャル（認証情報）がリアルタイムに取引されています。
外部からのクローリングや自動スクレイピング（OSINT）だけでは全体像の把握が難しいため、研究者や捜査官が自らアカウントを作成し、アクターと直接コミュニケーションをとって脅威インテリジェンス（CTI）を収集する**「HUMINT（Human Intelligence: 人的情報収集）」**が不可欠な手法となっています。"""),
        ("2. Menlo Report（メンロレポート）が突きつける「HUMINTの根本的ジレンマ」",
         """しかし、大学や公的研究機関がHUMINTを行う場合、避けて通れないのが**「研究倫理原則」**です。
情報通信技術（ICT）研究における国際的な倫理ガイドラインである**「メンロレポート（Menlo Report）」**では、医療研究におけるベルモントレポートの精神を継承し、以下の4大原則を定めています。
- **人々の尊重（Respect for Persons）**: 被験者の自律性を尊重し、調査目的やリスクを開示して**「インフォームド・コンセント（事前説明と同意）」**を得ること。
- **善行（Beneficence）**: 社会的利益を最大化し、被験者や社会への危害（プライバシー侵害や身体的危険）を最小化すること。
- **正義（Justice）**: 研究の負担と利益が特定集団に不当に偏らないこと。
- **法と公共利益の尊重（Respect for Law and Public Interest）**: 法令を遵守し、透明性と説明責任を果たすこと。

ここで絶望的な**「HUMINTのジレンマ」**が発生します。
サイバー犯罪者に「こんにちは、私は大学の研究者です。学術調査のためにあなたの発言を記録・分析させてください」と正直に告知（インフォームド・コンセント）すれば、犯罪者は即座にチャットから研究者をブロック・追放し、別のチャンネルへと逃亡します。
一方で、身分を偽り「同業のハッカー」や「ツールの買い手」になりすまして情報を引き出せば、それは**被験者を欺く違法なおとり捜査や倫理違反**に直結し、学術論文として発表することもできなくなってしまうのです。"""),
        ("3. 横浜国大SPIRALのブレークスルー：段階的合意形成と「倫理監視LLM」（CSS 2025）",
         """横浜国立大学 SPIRALの**吉岡克成 教授**、**イン・ミンパパ 特任准教授**、**久保颯汰 氏**らの研究チームは、国内最高峰の暗号・情報セキュリティシンポジウム **CSS 2025** において論文『*インフォームド・コンセントに基づくTelegram上の人的情報収集の実施可能性の検証*』を発表し、この極めて困難なジレンマに世界初の工学的・倫理的ブレークスルーを提示しました。
- **段階的インフォームド・コンセント（Phased Informed Consent）のモデル検証**:
  最初からすべてを開示して即座に遮断されるのを防ぎつつ、欺瞞を最小限に抑えるため、「対話の初期フェーズ」「信頼関係構築フェーズ」「核心的脅威情報の聴取フェーズ」のどの段階でどのように研究目的を開示すべきか、受容性と情報収集効率の境界線を厳密に実験検証しました。
- **HUMINT対話における「倫理監視LLM（Ethical Guardrail LLM）」**:
  対話を行う研究者が感情や功名心に流され、犯罪行為の教唆・幇助や、相手の人権を侵害する発言をしてしまわないよう、バックエンドのLLMが対話ログをリアルタイムに監視。メンロレポートのチェックリストに照らして「越えてはならない一線」を判定し、警告を発する先駆的セーフガード技術を導入しました。

目的が正義であっても、手段が不当であってはならない――。犯罪者と同じ闇に堕ちることなく、法の光と高い倫理観を堅持しながらサイバー社会の深淵に挑む、学術研究の崇高なプライドがここに確立されています。""")
    ]
}

# Episode 35 Metadata & Deep Dive
ep35_meta = {
    "num": 35,
    "date": "2026-11-01",
    "filename": "2026-11-01_ep35_pqc_identity_based_encryption.md",
    "title": "第35話 証明書なき星群と格子の絆 〜耐量子IDベース暗号と群テストの奇跡〜",
    "tags": ["横浜国大SPIRAL", "耐量子暗号", "PQC", "IDベース暗号", "IBE", "BC-IBE", "群テスト", "CANS2024", "四方順司教授", "NexCrypt Lab"],
    "lead_intro": """帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 次世代暗号ラボ（NexCrypt Lab）
神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
横浜国立大学 SPIRAL・四方順司教授（NexCrypt Lab長）、佐藤慎悟氏らの国際会議論文（CANS 2024 / LNCS 14905）、数十億台のIoT・自動運転スマートシティにおける公開鍵暗号基盤（PKI）の限界、デジタル証明書発行・失効リスト（CRL/OCSP）の通信・管理ボトルネック、相手の識別子（メールアドレスや機器ID）そのものを公開鍵として使うIDベース暗号（IBE）、量子コンピュータの脅威とペアリング暗号の終焉、耐量子計算機暗号（PQC / 格子暗号）、悪意ある共謀に対抗する有界共謀耐性IBE（BC-IBE）、情報理論・組合せ数学の「群テスト（Group Testing）」による公開パラメータの極限小型化（Compact IBE）
- [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
- Shingo Sato, Junji Shikata. "Compact Post-Quantum Bounded-Collusion Identity-based Encryption." *Cryptology and Network Security (CANS 2024)*, Lecture Notes in Computer Science (LNCS), Vol. 14905, pp. 119-139, Springer, 2024.""",
    "dialogues": [
        ("第1コマ<br>【起】",
         "蓮の証明書万能論：数十億のIoTに全部証明書を配れば解決だろ！<br>街灯やセンサーの模型を指差し、「数億台のIoT機器すべてに電子証明書を配って管理すれば安心だろ！」と主張する蓮。",
         "蓮: 「数十億台のIoT機器すべてに電子証明書（PKI）を発行して配れば、身元確認なんて完璧だろ！」",
         "Ren: 'If we just issue digital certificates (PKI) to billions of IoT devices, identity verification is totally solved!'"),
        ("第2コマ<br>【承】",
         "結衣の証明書管理破綻と量子の壁の指摘<br>サーバーパンクのグラフを示し、「失効管理（CRL）でインフラが破綻し、量子コンピュータで既存暗号は破られます」と論破する結衣。",
         "結衣: 「甘すぎます。失効リストの配信でサーバーはパンクし、量子マシンが来れば既存証明書は全滅です。」",
         "Yui: 'Hopelessly naive. Certificate revocation will choke the servers, and quantum computers will crush legacy PKI.'"),
        ("第3コマ<br>【転】",
         "悠真TAによる四方教授らのCANS 2024論文「群テストによる超コンパクト耐量子IBE」解説<br>CANS 2024論文の格子数理スライドを投影し、相手のIDがそのまま鍵になるIBEを群テスト理論で超小型化した四方教授らの偉業を熱く語る悠真。",
         "悠真: 「四方教授らは『群テスト』の数理を融合し、耐量子環境で公開鍵サイズを極限まで小型化したんだ！」",
         "Yuma: 'Prof. Shikata merged Group Testing math to achieve ultra-compact public parameters under post-quantum IBE!'"),
        ("第4コマ<br>【結】",
         "証明書のない星群に咲き誇る数学の絆に感動する二人<br>証明書の問い合わせなしにIDだけで瞬時に暗号通信を確立するスマートシティの未来図を見つめ、数学の美しさに目を輝かせる蓮と結衣。",
         "蓮: 「証明書サーバーがなくても、相手のIDだけで瞬時に安全に通信できるなんて……未来すぎる！」<br>結衣: 「幾何学と組合せ論の奇跡……これこそが未来のスマート社会を支える不可視の礎ですね。」",
         "Ren: 'Instant, secure communication using just IDs, completely free of certificate servers... mind blown!'<br>Yui: 'A miracle of geometry and combinatorics... the invisible foundation empowering future smart societies.'")
    ],
    "fig_file": "figures/fig35_pqc_identity_based_encryption.png",
    "fig_caption": "耐量子有界共謀IDベース暗号（Compact Post-Quantum BC-IBE, CANS 2024）の構造図解",
    "column_sections": [
        ("1. 「証明書の海」で溺れるIoT社会と公開鍵暗号基盤（PKI）の限界",
         """スマートシティ、自動運転車、ドローン、スマートグリッドなど、無数のIoT機器が瞬時に連携し合う現代社会において、長年サイバー空間を支えてきた**「公開鍵基盤（PKI: Public Key Infrastructure）」**が悲鳴を上げています。
PKIでは、各機器が本物であることを証明するために、認証局（CA）が発行した「電子証明書」を保持し、通信相手に提示します。
しかし、デバイスが数十億台規模に爆発すると、以下の深刻な問題に直面します。
- **証明書失効リスト（CRL / OCSP）のパンク**: 万が一デバイスが故障やハッキングを受け、証明書を失効（Revocation）させた場合、世界中の通信端末がその最新失効情報を頻繁に問い合わせるため、ネットワーク帯域とCAサーバーが瞬時に飽和します。
- **証明書検証の遅延**: コンマ数秒の遅れが人命に関わる自動運転（V2X通信）において、重厚な証明書チェーンを検証する処理時間は致命的なボトルネックとなります。"""),
        ("2. 夢の「IDベース暗号（IBE）」と耐量子（PQC）の厚い壁",
         """そこで1984年にシャミア（Shamir）によって提唱された究極の暗号技術が**「IDベース暗号（IBE: Identity-Based Encryption）」**です。
IBEでは、相手の**「メールアドレス」「IPアドレス」「MACアドレス」「ドメイン名」といった任意の識別子（ID）そのものが公開鍵**になります。送信者は相手の証明書を取り寄せて検証する必要が一切なく、IDを指定するだけで暗号文を送信できます。
しかし、従来のIBE（Boneh-Franklin等）は「楕円曲線上のペアリング暗号」に強く依存しており、**量子コンピュータが実用化されるとショアのアルゴリズムによって完全に解読されてしまう**という致命的な弱点を抱えていました。
量子耐性を持つ「格子暗号（Lattice-based Cryptography）」を用いてIBEを構築する研究も進められてきましたが、悪意あるユーザー複数人が秘密鍵を持ち寄ってマスター鍵を不正に復元しようとする「共謀攻撃（Collusion Attack）」を防ぐため、**公開パラメータのサイズが数ギガバイトにも巨大化してしまう**という致命的な壁に阻まれていました。"""),
        ("3. 横浜国大・四方順司教授が証明した「群テスト×耐量子BC-IBE」（CANS 2024）",
         """横浜国立大学 SPIRALの次世代暗号ラボ（NexCrypt Lab）長を務める**四方順司 教授**と**佐藤慎悟 氏**は、暗号・ネットワークセキュリティの国際シンポジウム **CANS 2024**（Lecture Notes in Computer Science 14905）において、論文『*Compact Post-Quantum Bounded-Collusion Identity-based Encryption*』を発表しました。
本研究は、共謀可能な攻撃者の上限数を設定した「有界共謀耐性IBE（BC-IBE）」において、公開鍵サイズを劇的に小型化する世界初の汎用理論を打ち立てました。
- **情報数学「群テスト（Group Testing）」の融合**:
  従来のエラー訂正符号を用いるアプローチでは、パラメータサイズが共謀者数に対して指数関数的に肥大化していました。四方教授らは、多数の検体から少数の感染者を効率的に特定する組合せ数学理論である「非適応的群テスト（Non-Adaptive Group Testing）」の概念を暗号パラメータの設計に導入しました。
- **NIST標準の汎用PQC暗号から直接構成**:
  格子暗号をはじめとするNIST選定の耐量子公開鍵暗号（PKE）をブラックボックスとして利用し、量子耐性を完全に維持しながら、公開パラメータサイズを従来比で劇的に圧縮（Compact化）することに成功しました。

認証局（CA）への問い合わせを一切不要にし、相手のIDだけで瞬時に安全な暗号通信を可能にするこの数理のブレークスルーは、未来の超巨大スマート社会や宇宙通信インフラを根底から支える最強の防盾となります。""")
    ]
}

# Episode 36 Metadata & Deep Dive
ep36_meta = {
    "num": 36,
    "date": "2026-11-01",
    "filename": "2026-11-01_ep36_llm_malware_polymorphism.md",
    "title": "第36話 千の貌を持つ影と振る舞いの砦 〜生成AIマルウェア変種と動的防御の夜明け〜",
    "tags": ["横浜国大SPIRAL", "生成AI", "LLM", "マルウェア変種", "ポリモーフィズム", "アンチウイルス回避", "動的挙動検知", "吉岡克成教授", "インミンパパ特任准教授", "松本勉名誉教授"],
    "lead_intro": """帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL マルウェア解析・AIセキュリティ研究室
神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
横浜国立大学 SPIRAL・吉岡克成教授、イン・ミンパパ特任准教授、松本勉名誉教授らの先端研究（ICSS / IEEE DSC）、生成AI（ChatGPT / 大規模言語モデル LLM）を悪用したマルウェアの自動変種生成・ポリモーフィズム（多態性）、アンチウイルスソフト（AV）の静的シグネチャ検知（ハッシュ値・パターンマッチング）の完全な無力化、コード難読化・無意味命令挿入・制御フロー平坦化による変装、VirusTotal等による実態検証、静的防御から動的挙動検知（振る舞い検知・EDR / XDR）へのパラダイムシフト、AIと人間の共創による新時代のディフェンス
- [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
- 黄 哲維, イン ミンパパ, 吉岡 克成, 松本 勉. 『大規模言語モデルを用いたマルウェアの変種生成とその回避性能の評価』. 電子情報通信学会 情報セキュリティ研究会 (ICSS), 2024.
- Zhewei Huang, Yin Minn Pa Pa, Katsunari Yoshioka, Tsutomu Matsumoto. "Evaluating the Evasion Capabilities of LLM-Assisted Polymorphic Malware against Antivirus Solutions." *IEEE Conference on Dependable and Secure Computing (IEEE DSC)*, 2024.""",
    "dialogues": [
        ("第1コマ<br>【起】",
         "蓮のアンチウイルス過信：定義ファイルが最新なら100%安全だろ！<br>ノートPCのセキュリティソフト画面を誇らしげに見せ、「指名手配犯の顔写真（シグネチャ）が最新なら絶対安全だろ！」と豪語する蓮。",
         "蓮: 「最新の定義ファイルに更新しておけば、ウイルスなんて侵入した瞬間に100%検知できるだろ！」",
         "Ren: 'With virus definitions fully updated, any malware will get 100% blocked on entry!'"),
        ("第2コマ<br>【承】",
         "結衣のAIコード変形とアンチウイルス素通りの指摘<br>難読化されたコードを提示し、「生成AIを使えば意味を保ったまま見た目だけ無限に変装できます」と警告する結衣。",
         "結衣: 「甘すぎます。生成AI（LLM）を使えば、同じ挙動のまま無限の変装コードを自動生成できるのよ。」",
         "Yui: 'Naive. Using generative LLMs, attackers can synthesize infinite functionally identical disguises.'"),
        ("第3コマ<br>【転】",
         "悠真TAによるSPIRAL論文「LLM変種マルウェアと振る舞い防御」解説<br>IEEE DSC / ICSS研究スライドを投影し、主要AVが変種を素通りさせた実験データと、動的振る舞い検知の重要性を説く悠真。",
         "悠真: 「SPIRALの研究では市販AVの多くが素通りした。だからこそ『静的ハッシュ』から『動的挙動』への転換が必要なんだ。」",
         "Yuma: 'SPIRAL proved commercial AVs were completely blinded. Defense must shift from static hashes to dynamic behaviors.'"),
        ("第4コマ<br>【結】",
         "千の貌に惑わされず悪意の核を見抜く！決意を固める二人<br>エンドポイントの挙動ツリーを見つめ、見た目の変装に惑わされず、悪意の振る舞いそのものを捉えるサイバーの真髄に目覚める蓮と結衣。",
         "蓮: 「コードの皮をいくら被っても、悪事を働く瞬間を見逃さない！それが僕たちの新しい砦だな！」<br>結衣: 「ええ。AIが千の変装を生み出そうとも、私たちはその深層にある意図を捉えてみせます。」",
         "Ren: 'No matter how it disguises its code, we catch the exact moment it acts malice! That is our fortress!'<br>Yui: 'Indeed. Even if AI generates a thousand faces, we will pierce through to its underlying malicious intent.'")
    ],
    "fig_file": "figures/fig36_llm_malware_polymorphism.png",
    "fig_caption": "LLM支援型ポリモーフィック・マルウェアの自動変種生成と動的挙動防御（ICSS / IEEE DSC）構造図解",
    "column_sections": [
        ("1. 「指名手配写真」を買い集めるアンチウイルスの限界",
         """パーソナルコンピュータや企業の端末を守るアンチウイルスソフト（AV）は、長年にわたり**「シグネチャ検知（パターンマッチング）」**を防御の第一防衛線としてきました。
これは、既知のマルウェアファイルからSHA-256などのハッシュ値を計算したり、特徴的なコードパターン（バイト列）を抽出して「指名手配リスト（定義ファイル）」に登録しておき、ファイルがダウンロード・実行される瞬間に照合する仕組みです。
この方式は動作が極めて高速で誤検知が少ないという絶大なメリットがありますが、**「1バイトでも中身が変わるとハッシュ値が全くの別物になり、検知できなくなる」**という致命的な弱点を抱えています。"""),
        ("2. 生成AI（LLM）がもたらした「悪意の自動変装革命」",
         """かつて、アンチウイルスの検知を回避する「ポリモーフィック（多態性）マルウェア」を作成するには、高度なアセンブラ技術を持つトップクラスのウイルス作者が手作業で難読化ルーチンを組む必要がありました。
しかし、ChatGPTをはじめとする**大規模言語モデル（LLM）の台頭**によって、このパワーバランスは根底から覆されました。
攻撃者はLLMのプログラミング支援能力を悪用し、以下のようなコード変換を瞬時に全自動で実行できるようになったのです。
- **等価構文変換**: `for`ループを`while`ループに書き換える、条件分岐の順序を反転させるなど、プログラムの論理的振る舞いを保ったまま構文構造を一新する。
- **無意味命令（Junk Code / NOP）の大量挿入**: 実行結果に影響を与えない無意味な算術演算やダミーの関数呼び出しを無数に散りばめ、コードのバイト列を完全に破壊する。
- **変数名・関数名のランダム化と文字列暗号化**: 解析の手がかりとなるAPI名や文字列を難読化・動的復号化する。

これにより、**「機能はまったく同一の悪意あるマルウェアでありながら、外見（ハッシュ値やバイトパターン）が無限に異なる新種」**が、1秒間に何千個も全自動で量産される悪夢が現実となったのです。"""),
        ("3. 横浜国大SPIRALの衝撃的検証と「動的振る舞い検知」へのパラダイムシフト",
         """横浜国立大学 SPIRALの**吉岡克成 教授**、**イン・ミンパパ 特任准教授**、**松本勉 名誉教授**、**黄哲維 氏**らの研究グループは、情報セキュリティ研究会（ICSS）および信頼性・セキュリティの国際会議 **IEEE DSC** において論文『*大規模言語モデルを用いたマルウェアの変種生成とその回避性能の評価*』を発表しました。
- **市販アンチウイルスソフトに対する実態解明**:
  研究チームは、既存の著名なマルウェアをLLMによって自動で構文変換・難読化し、VirusTotalに登録されている世界中の主要アンチウイルスエンジン群に対して検知実験を実施しました。
  その結果、オリジナルのマルウェアであればほぼ100%検知されていたにもかかわらず、**LLMによって変種生成されたマルウェアは、大半の商用アンチウイルスエンジンの静的シグネチャ検知をやすやすと回避（Bypass）できる**という衝撃的な実態が実験的に立証されました。
- **「静的防御」から「動的挙動検知（Behavioral Defense）」への脱却**:
  この研究が突きつけた教訓は極めて明確です。**「ファイルの見た目やハッシュ値で止める防御は完全に終わった」**ということです。
  どんなにコードが巧妙に変装していようとも、マルウェアが目的を果たすためには、最終的に「不正なレジストリ書き換え」「権限昇格」「不審な外部IPへの通信」「プロセスメモリの改ざん」といった**実際の悪意あるアクション（振る舞い）**を起こさざるを得ません。
  研究チームは、エンドポイントの振る舞いを監視する**EDR（Endpoint Detection and Response）**や、システムコール・プロセストリーを追跡する動的サンドボックス解析こそが、生成AI時代のサイバー空間を守る絶対的な防壁になると結論づけています。

AIが変幻自在の影を生み出すならば、人間はその影の足跡を捉える知恵を磨く。攻撃と防御のフロンティアを切り拓く横浜国大SPIRALの知見は、次代を担う高校生たちに真のサイバーディフェンスの覚悟を教えています。""")
    ]
}

def format_novel_body(raw_text):
    # Split by * * * or ***
    raw_text = raw_text.replace("\r\n", "\n")
    parts = [p.strip() for p in raw_text.split("* * *") if p.strip()]
    if len(parts) == 1:
        # try ***
        parts = [p.strip() for p in raw_text.split("***") if p.strip()]
    
    # join with \n\n✦ ✦ ✦\n\n
    return "\n\n✦ ✦ ✦\n\n".join(parts)

def build_markdown(meta):
    raw_path = os.path.join(CONTENT_DIR, f"ep{meta['num']}_novel_raw.txt")
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

for meta in [ep34_meta, ep35_meta, ep36_meta]:
    build_markdown(meta)
print("ALL 3 EPISODES MARKDOWN ASSEMBLED SUCCESSFULLY!")
