import os
import re

CONTENT_DIR = "content"

def format_novel(text: str) -> str:
    text = re.sub(r'\n\s*\*\s*\*\s*\*\s*\n', '\n\n✦ ✦ ✦\n\n', text)
    return text.strip()

# Episode 28
ep28_raw = open(os.path.join(CONTENT_DIR, "ep28_novel_raw.txt"), "r", encoding="utf-8").read()
ep28_novel = format_novel(ep28_raw)

ep28_md = f"""---
title: "第28話 潜む裏口と社会インフラの防壁 〜制御システム遠隔管理機器の死角を暴け〜"
episode_num: 28
date: 2026-10-29
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "重要インフラ", "ICS", "遠隔管理機器", "WebUI", "ゼロデイ脆弱性", "IEEE S&P", "佐々木貴之准教授", "吉岡克成教授", "松本勉上席特別教授"]
---

# 第28話 潜む裏口と社会インフラの防壁 〜制御システム遠隔管理機器の死角を暴け〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 産業サイバーセキュリティ実験棟
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 横浜国立大学 SPIRAL・佐々木貴之准教授、吉岡克成教授、松本勉上席特別教授らの国際最高峰論文（IEEE S&P 2022）、重要インフラ（水力ダム・メガソーラー・スマートビル等）における保守用遠隔管理ゲートウェイ（WebUI）の露見、従来の産業制御システムスキャン（Modbus/BACnet）の死角（Blind Spot）、13件のゼロデイ脆弱性特定、高対話ハニーポットによる攻撃者動態観測、212事業者への責任ある開示（Responsible Disclosure）と社会連携による是正
> - **探訪・参照研究論文**:
>   - [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
>   - Takayuki Sasaki, Akira Fujita, Carlos H. Gañán, Michel van Eeten, Katsunari Yoshioka, Tsutomu Matsumoto. "Exposed Infrastructures: Discovery, Attacks and Remediation of Insecure ICS Remote Management Devices." *Proceedings of the 43rd IEEE Symposium on Security and Privacy (IEEE S&P 2022)*, pp. 2680-2696, 2022.

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第28話 4コマ漫画イラスト](illustrations/ep28_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮の過信：インフラは専用線で隔離されてるから安全！**<br>ダムやメガソーラーの写真を見ながら「Modbusとか専用線で固められてるからハッキングなんて無理！」と豪語する蓮。 | **蓮**: 「ダムや発電所なんて専用回線と特殊プロトコルで隔離されてるんだから、外部から侵入されるわけないだろ！」 | **Ren**: "Dams and power plants are isolated with dedicated lines and protocols! There's no way anyone can hack in!" |
| **第2コマ**<br>【承】 | **結衣の冷徹な指摘：保守用Webゲートウェイの死角**<br>「保守業者が遠隔操作するためにつけた安価なWebUIが、認証なしで世界中に公開されています」と指摘する結衣。 | **結衣**: 「甘いです。保守業者が便利だからと付けたWeb管理ゲートウェイが、認証もなしにネットへ丸見えなんです。」 | **Yui**: "Naïve. Cheap WebUI gateways added for maintenance convenience are exposed to the internet with zero auth." |
| **第3コマ**<br>【転】 | **悠真TAによるIEEE S&P論文の衝撃データ解説**<br>国内だけで890台の露見機器と13件のゼロデイを発見し、ハニーポットで攻撃者を追跡したSPIRALの研究を紹介する悠真。 | **悠真**: 「佐々木准教授らのIEEE S&P 2022論文では、国内だけで890台の露見ゲートウェイと13件のゼロデイを暴いたんだ。」 | **Yuma**: "Assoc. Prof. Sasaki's IEEE S&P 2022 paper uncovered 890 exposed gateways in Japan and 13 zero-days." |
| **第4コマ**<br>【結】 | **泥臭い社会連携と責任ある開示の価値へ**<br>電話とメールで212事業者に連絡し58%を是正した実績に感銘を受け、現場に寄り添う真の防衛を誓う二人。 | **蓮**: 「論文を書くだけじゃなく、212の事業者に電話して58%も直したなんて……本物の砦づくりだ！」<br>**結衣**: 「学術が社会インフラを直接守る……これこそ工学の誇りですね。」 | **Ren**: "They didn't just write a paper—they contacted 212 operators and fixed 58%! That's true defense!"<br>**Yui**: "Academia directly shielding critical infrastructure... that is the pride of engineering." |

---

## 📖 小説本文

{ep28_novel}

---

## 📊 TikZによるセキュリティ構造図解

![産業制御システム遠隔管理機器の露見と是正（IEEE S&P 2022）の構造図解](figures/fig28_exposed_ics_gateways.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 「重要インフラは隔離されている」という神話の崩壊
電力、水道、鉄道、大型商業ビルなどの**産業制御システム（ICS: Industrial Control Systems / SCADA）**は、かつてはインターネットから物理的に切り離された「エアギャップ環境」にあると信じられていました。
しかし、人手不足や維持管理コスト削減、広域監視の必要性から、全国各地に点在するメガソーラー（太陽光発電所）や浄水設備、ビルの空調管理装置に**「遠隔監視・保守用ゲートウェイ機器」**が後付けされるケースが急増しています。

### 2. 従来型スキャナーが完全に見落としていた「死角（Blind Spot）」
サイバー空間の脅威調査では、ShodanやCensysといった検索エンジンが活用されますが、従来のICS調査は**Modbus（ポート502）やBACnet（ポート47808）**といった専用産業プロトコルばかりを対象にしていました。
しかし、現場の保守員が使いやすいように設置されたゲートウェイは、**通常のWebブラウザ（HTTP/HTTPS）で動くWebUI**を備えています。専用プロトコルのシグネチャを持たないため、従来のセキュリティ監視ツールからは完全に「ノーマークの死角」となっていたのです。

### 3. 横浜国大・佐々木准教授らが切り拓いた画期的成果（IEEE S&P 2022）
セキュリティ研究の世界最高峰国際会議 **IEEE Symposium on Security and Privacy (S&P 2022)** に採択された横浜国立大学 SPIRALの論文『*Exposed Infrastructures: Discovery, Attacks and Remediation of Insecure ICS Remote Management Devices*』は、この盲点に世界で初めて科学的なメスを入れました。
- **WebUIシグネチャによる独自探索**: 機器特有のHTML構造やファビコン、APIレスポンスの特徴を捉える探索技術を開発し、**日本国内だけで890台もの制御用遠隔ゲートウェイがインターネット上に直接露見している**ことを突き止めました。
- **13件のゼロデイ脆弱性を特定**: 普及している代表的3機種を詳細にリバースエンジニアリングした結果、**未認証で内部制御コマンドを送信できる脆弱性を含む13件のゼロデイ脆弱性**を発見し、製造元（ベンダー）へ責任ある開示（CVD）を行ってパッチ開発を支援しました。
- **高対話ハニーポットによる攻撃者観測**: 実機を模倣したハニーポットをネット上に公開したところ、施設名や発電ログが具体的に表示されるリッチな画面ほど攻撃者の介入が激増し、実際に不正なパラメータ書き換えが試みられることを実証しました。
- **学術から社会実装へ（58%の改善達成）**: 研究チームは論文執筆にとどまらず、露見していた**317台の管理事業者へ電話やメールで連絡を行い、212の組織と直接対話**。追跡調査の結果、連絡が取れた組織の**58%で機器の隔離やパスワード設定などの安全化措置が完了**したことを確認しました。大学研究が社会のインフラ事故を未然に防いだ金字塔です。
"""

# Episode 29
ep29_raw = open(os.path.join(CONTENT_DIR, "ep29_novel_raw.txt"), "r", encoding="utf-8").read()
ep29_novel = format_novel(ep29_raw)

ep29_md = f"""---
title: "第29話 悪のIoTを浄化せよ 〜ISP隔離砦（Walled Garden）とMirai駆除の真実〜"
episode_num: 29
date: 2026-10-29
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "IoTボットネット", "Mirai", "Walled Garden", "ISP連携", "ヒューマンファクター", "NDSS", "吉岡克成教授", "松本勉上席特別教授"]
---

# 第29話 悪のIoTを浄化せよ 〜ISP隔離砦（Walled Garden）とMirai駆除の真実〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 広域ネットワーク解析室
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 横浜国立大学 SPIRAL・吉岡克成教授、松本勉上席特別教授らの国際最優秀論文（NDSS 2019 Distinguished Paper Award）、IoTマルウェア（Mirai等）のクリーンアップ実験、実稼働ISPにおけるランダム化比較試験（RCT）、警告メール通知の限界（効果ゼロの衝撃）、キャプティブポータル型ネットワーク隔離「Walled Garden（ウォールガーデン）」の圧倒的除染効果（14日以内に92%駆除）、一般消費者の誤ったメンタルモデル（PCアンチウイルス依存）とインフラ協調防護
> - **探訪・参照研究論文**:
>   - [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
>   - "Cleaning Up the Internet of Evil Things: Real-World Evidence on ISP and Consumer Efforts to Remove Mirai." *Proceedings of the Network and Distributed System Security Symposium (NDSS 2019)*, 2019. **【Distinguished Paper Award（最優秀論文賞）受賞】**

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第29話 4コマ漫画イラスト](illustrations/ep29_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮の楽観論：感染ルーターには注意メールを送れば即解決！**<br>「プロバイダが感染したルーターの持ち主にメールを送れば、誰でもすぐ直してくれるはず！」と主張する蓮。 | **蓮**: 「Miraiに感染したルーターが見つかったら、プロバイダがメールで知らせればみんなすぐ直すでしょ！」 | **Ren**: "If a router gets infected with Mirai, sending an ISP email alert will get it fixed right away!" |
| **第2コマ**<br>【承】 | **結衣の冷徹な指摘：メール無視と勘違いの罠**<br>「メールは無視されるか、PCのウイルス対策ソフトを動かして『直った』と勘違いされるだけです」と指摘する結衣。 | **結衣**: 「甘いです。メールは無視され、仮に開いてもPCのアンチウイルスを動かして安心するだけです。」 | **Yui**: "Naïve. Alert emails are ignored, or users just scan their PC with antivirus and assume it's fixed." |
| **第3コマ**<br>【転】 | **悠真TAによるNDSS最優秀論文の実証データ解説**<br>メール通知の効果はゼロだが、ブラウザを一時隔離する「Walled Garden」なら14日で92%駆除された実績を語る悠真。 | **悠真**: 「吉岡教授らのNDSS 2019最優秀論文では、メールは効果ゼロ、Walled Garden隔離は92%駆除と証明されたんだ。」 | **Yuma**: "Prof. Yoshioka's NDSS 2019 award-winning paper proved email had zero effect, but Walled Garden hit 92%!" |
| **第4コマ**<br>【結】 | **人間を責めず、インフラの構造で守る砦へ**<br>ユーザーの無知を責めるのではなく、ネットワーク側で包み込んで安全へ導く真の防衛に感動する二人。 | **蓮**: 「ユーザーを責めるんじゃなく、ネットが優しく包んで守る仕組みなんだ！」<br>**結衣**: 「人間行動と通信インフラの融合……これが学術の到達点ですね。」 | **Ren**: "Instead of blaming users, the network gently envelops and protects them!"<br>**Yui**: "Merging human behavior with network architecture... this is the pinnacle of research." |

---

## 📖 小説本文

{ep29_novel}

---

## 📊 TikZによるセキュリティ構造図解

![悪のIoT浄化（NDSS 2019 最優秀論文）：メール通知 vs Walled Garden隔離の構造図解](figures/fig29_isp_walled_garden_mirai.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. 世界を震撼させた「Mirai」ボットネットの悪夢
2016年、インターネットに接続された世界中のWi-Fiルーターやネットワークカメラ、デジタルビデオレコーダー（DVR）が、マルウェア**「Mirai（ミライ）」**に次々と乗っ取られました。
数十万台規模で形成された悪意あるボットネットは、大手DNSサービスDynやセキュリティブログに毎秒1テラビット（Tbps）を超える未曾有のDDoS攻撃を浴びせ、TwitterやNetflix、GitHubなどの主要サービスを麻痺させました。
Miraiのソースコードがネット上に公開されたことで無数の亜種が誕生し、**「家庭内の感染IoT機器をいかにクリーンアップ（除染）するか」**が地球規模の緊急課題となりました。

### 2. 世界最高峰 NDSS 2019 で最優秀論文賞（Distinguished Paper Award）を受賞
2019年、セキュリティ研究の4大トップカンファレンスの一つである **NDSS (Network and Distributed System Security Symposium)** において、横浜国立大学 SPIRALの**吉岡克成 教授**、**松本勉 上席特別教授**、情報通信研究機構（NICT）、およびデルフト工科大学（TU Delft）の国際共同研究チームが発表した論文『*Cleaning Up the Internet of Evil Things: Real-World Evidence on ISP and Consumer Efforts to Remove Mirai*』が、全世界の応募論文の中から極めて栄誉ある**「最優秀論文賞（Distinguished Paper Award）」**に輝きました。
本研究の画期的な点は、机上のシミュレーションではなく、**実際の中規模商用ISPのネットワーク内で感染した数千台の一般家庭ルーターを対象に、医学の臨床試験と同じ「ランダム化比較試験（RCT）」を実施した**点にあります。

### 3. データが突きつけた衝撃の事実：メール通知は「効果ゼロ」
実証実験の結果は、これまでのセキュリティ業界の常識を覆すものでした：
1. **メール通知の完全な無力さ**:
   感染機器の契約者に対して「あなたのルーターが感染しています」と詳細な注意喚起メールを送ったグループと、何も通知しなかったグループ（対照群）を比較したところ、**駆除成功率に統計的な有意差が全く見られませんでした（改善効果ゼロ）**。警告メールは迷惑メールに埋もれるか、詐欺メールと警戒されて無視されていたのです。
2. **ウォールガーデン（Walled Garden：隔離庭園）の圧倒的威力**:
   ISPのネットワーク側で一時的にWeb通信を制御し、ユーザーがブラウザを開いた際に強制的に注意喚起ポータル（キャプティブポータル）を表示させ、画面上でパスワード変更手順を案内したグループでは、**わずか14日以内に92%もの感染デバイスが安全にクリーンアップ**されました。
3. **消費者のメンタルモデル（誤解）の解明**:
   追跡インタビュー調査を行ったところ、多くのユーザーは「ルーターの感染」という概念が理解できず、「手元のパソコンのアンチウイルスソフトをスキャンして再起動した」と回答していました。ユーザーが間違った認識を持っていても、**ISPの隔離ポータルが強制的に注意を引き、機器の再起動や再設定を促す導線を作ったからこそ駆除が成功した**のです。
この研究は、「ユーザーのリテラシー向上に頼るのではなく、ISPやネットワークインフラが主体となって能動的に安全な状態へ誘導する仕組み（Walled Garden）」の重要性を世界に知らしめました。
"""

# Episode 30
ep30_raw = open(os.path.join(CONTENT_DIR, "ep30_novel_raw.txt"), "r", encoding="utf-8").read()
ep30_novel = format_novel(ep30_raw)

ep30_md = f"""---
title: "第30話 消えゆく足跡と鎖の記憶 〜DeFiトークン詐欺とオン・オフチェーン統合インテリジェンス〜"
episode_num: 30
date: 2026-10-29
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "Web3", "ブロックチェーン", "DeFi", "Rug Pull", "DeFiIntel", "オンチェーン", "オフチェーン", "NDSS", "インミンパパ特任准教授", "吉岡克成教授"]
---

# 第30話 消えゆく足跡と鎖の記憶 〜DeFiトークン詐欺とオン・オフチェーン統合インテリジェンス〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL Web3・暗号資産フォレンジック研究室
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 横浜国立大学 SPIRAL・イン・ミンパパ特任准教授、吉岡克成教授らの最新研究（NDSS MADWeb 2025）、分散型金融（DeFi）におけるトークン詐欺・Rug Pull（資金持ち逃げ）、オンチェーン（改ざん不能なブロックチェーン台帳）とオフチェーン（消えゆくWebサイトやSNS・Discord）の非対称性、世界初の大規模マルチモーダルデータセット「DeFiIntel」（32,144トークン × 55万件超のアーカイブ）、詐欺ライフサイクルの可視化とプロアクティブな予兆検知
> - **探訪・参照研究論文**:
>   - [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
>   - Iori Suzuki, Yin Minn Pa Pa, Nguyen Anh Thi Van, Katsunari Yoshioka. "DeFiIntel: A Dataset Bridging On-Chain and Off-Chain Data for DeFi Token Scam Investigation." *Proceedings of the Workshop on Measurements, Attacks, and Defenses for the Web (MADWeb 2025)*, in conjunction with NDSS 2025, 2025.

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第30話 4コマ漫画イラスト](illustrations/ep30_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮のブロックチェーン万能論：改ざん不能だから詐欺は起きない！**<br>暗号コインのホログラムを掲げ、「台帳が公開されてて絶対改ざんできないから詐欺なんてあり得ない！」と豪語する蓮。 | **蓮**: 「ブロックチェーンは全世界に台帳が公開されてて改ざんできないんだから、詐欺なんて起きるわけないだろ！」 | **Ren**: "Blockchain records are public and immutable! There's no way anyone can pull off a scam!" |
| **第2コマ**<br>【承】 | **結衣の冷徹な指摘：Rug Pullと消えゆくWebサイトの罠**<br>「スマートコントラクトが正しくても、資金を持ち逃げされ、宣伝サイトやSNSは一瞬で消されます」と語る結衣。 | **結衣**: 「甘いです。資金を集めて持ち逃げするRug Pullが多発し、宣伝WebやSNSは証拠隠滅で消滅します。」 | **Yui**: "Naïve. Rug pulls drain millions, and promo websites or socials are wiped immediately to destroy evidence." |
| **第3コマ**<br>【転】 | **悠真TAによるNDSS MADWeb論文『DeFiIntel』解説**<br>3.2万個のトークンと55万件の消えゆくWeb/SNSデータをリアルタイム統合したSPIRALの最先端研究を紹介する悠真。 | **悠真**: 「イン・ミンパパ特任准教授らのDeFiIntelは、鎖の記録と消滅する55万件のWebデータを結びつけたんだ。」 | **Yuma**: "Assoc. Prof. Yin Minn Pa Pa's DeFiIntel bridged on-chain ledger data with 550,000 ephemeral web records." |
| **第4コマ**<br>【結】 | **暗号数理と人間心理を見据える守護者へ**<br>数学の美しさだけでなく、人間の欲望や狡猾さにも立ち向かう真のサイバーディフェンダーとして成長を誓う二人。 | **蓮**: 「改ざんできない鎖の記憶と、消えゆく足跡を繋ぐ……これが最新の捜査学なんだ！」<br>**結衣**: 「暗号数理の理想と人間心理の現実……二つを極めてこそ本物の防衛者ですね。」 | **Ren**: "Linking immutable chain data with vanishing tracks... this is the future of forensics!"<br>**Yui**: "Mastering both mathematical elegance and human psychology... that is true defense." |

---

## 📖 小説本文

{ep30_novel}

---

## 📊 TikZによるセキュリティ構造図解

![DeFiトークン詐欺のオン・オフチェーン統合インテリジェンス（NDSS MADWeb 2025）構造図解](figures/fig30_defiintel_token_scam.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. Web3・DeFi（分散型金融）で多発する「Rug Pull（絨毯引き）」とは？
ビットコインやイーサリアムに代表されるブロックチェーン技術は、「取引台帳が分散管理され、一度刻まれたデータは絶対に改ざんできない」という画期的な特性を持っています。
しかし、中央管理者のいない**分散型金融（DeFi: Decentralized Finance）**の普及に伴い、悪意ある開発者が自作の偽トークンを発行して投資家を欺く詐欺が急増しています。代表例が**「Rug Pull（ラグプル：足元の絨毯を勢いよく引き抜く詐欺）」**です。
- **手口**: 「将来価値が100倍になる画期的な暗号資産」と偽り、きらびやかな公式サイトやX（旧Twitter）、Telegram、Discordで大々的に宣伝（ハイプ）して資金（流動性）を集めます。
- **持ち逃げ**: 投資家の買いが集まって価格が上がった瞬間、開発者がスマートコントラクト内の流動性プールから資金を一気に引き抜いて雲隠れします。残されたトークンは一瞬で無価値（ゼロ）になり、世界中で年間数億ドルもの被害が発生しています。

### 2. 捜査と防犯を阻む「オンチェーンとオフチェーンの非対称性」
DeFi詐欺の調査における最大の障壁は、**「残るデータ」と「消えるデータ」のギャップ**にあります：
- **オンチェーン（On-Chain）データ**: ブロックチェーン上のスマートコントラクトのプログラムコード（バイトコード）や送金履歴。これらは永久に残り、世界中誰でも閲覧可能です。
- **オフチェーン（Off-Chain）データ**: 詐欺師が投資家を信じ込ませるために作成した「プロジェクト公式サイト」「ホワイトペーパー」「開発チームの経歴」「SNSの投稿やコミュニティチャット」。
詐欺師は資金を持ち逃げした直後、**自らのWebサイトを閉鎖し、SNSアカウントを即座に削除・非公開化（証拠隠滅）**してしまいます。被害が発生した後に警察や研究者が調査しようとしても、肝心の「どのように人間を騙したのか」というオフチェーンの証拠はインターネット上から完全に消滅してしまっているのです。

### 3. 横浜国大 SPIRAL が挑んだ世界初の統合データセット「DeFiIntel」（NDSS MADWeb 2025）
2025年、国際シンポジウム NDSS 2025 併設のワークショップ **MADWeb (Workshop on Measurements, Attacks, and Defenses for the Web)** において、横浜国立大学 SPIRALの**イン・ミンパパ 特任准教授**、**吉岡克成 教授**、鈴木伊織 氏らの研究チームは、この未解決問題に決定的なブレークスルーをもたらす論文『*DeFiIntel: A Dataset Bridging On-Chain and Off-Chain Data for DeFi Token Scam Investigation*』を発表しました。
- **リアルタイム網羅収集**: イーサリアム（Ethereum）ブロックチェーン上で新規にデプロイされた**32,144個のDeFiトークン**をリアルタイムで追跡。
- **55万件超のオフチェーンフットプリントを保全**: トークン生成と同時に、関連するプロジェクトWebサイトのHTMLやスクリーンショット、XやTelegramの投稿など**55万点以上のオフチェーンデータを消え去る前にアーカイブ**しました。
- **マルチモーダル・インテリジェンスの確立**: 「スマートコントラクトのバイトコード（数理的特徴）」と「マーケティング用Web・SNSデータ（ソーシャルな騙しの特徴）」を結びつけることで、詐欺トークンが資金を抜くまでの戦術的ライフサイクルや行動パターンを解明。事後捜査の決定的な電子的証拠を提供するだけでなく、**詐欺が実行される前の「予兆検知」を可能にする世界初の基盤**を築き上げました。
数学的なコードの正しさだけでは防げない「人間の騙しの心理」に対し、多角的なデータ統合で立ち向かう大学先端研究の真骨頂です。
"""

with open(os.path.join(CONTENT_DIR, "2026-10-29_ep28_exposed_ics_gateways.md"), "w", encoding="utf-8") as f:
    f.write(ep28_md)
print("Saved ep28 markdown")

with open(os.path.join(CONTENT_DIR, "2026-10-29_ep29_isp_walled_garden_mirai.md"), "w", encoding="utf-8") as f:
    f.write(ep29_md)
print("Saved ep29 markdown")

with open(os.path.join(CONTENT_DIR, "2026-10-29_ep30_defiintel_token_scam.md"), "w", encoding="utf-8") as f:
    f.write(ep30_md)
print("Saved ep30 markdown")
