import os
import re

CONTENT_DIR = "content"

def format_novel(text: str) -> str:
    # replace * * * with ✦ ✦ ✦
    text = re.sub(r'\n\s*\*\s*\*\s*\*\s*\n', '\n\n✦ ✦ ✦\n\n', text)
    return text.strip()

# Episode 26 Markdown Content
ep26_raw = open(os.path.join(CONTENT_DIR, "ep26_novel_raw.txt"), "r", encoding="utf-8").read()
ep26_novel = format_novel(ep26_raw)

ep26_md = f"""---
title: "第26話 身代金ビジネスの暗雲 〜LockBit 3.0の脅迫ライフサイクルと国際捜査の追跡〜"
episode_num: 26
date: 2026-10-29
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "ランサムウェア", "LockBit 3.0", "RaaS", "二重脅迫", "Operation Cronos", "吉岡克成教授", "インミンパパ特任准教授"]
---

# 第26話 身代金ビジネスの暗雲 〜LockBit 3.0の脅迫ライフサイクルと国際捜査の追跡〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 共同分析ルーム
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 横浜国立大学 SPIRAL・吉岡克成教授およびイン・ミンパパ特任准教授らの国際共同研究論文（RAID 2025）、RaaS（サービス型ランサムウェア）の企業的分業構造、二重脅迫（ダブル・エクストーション）とTorリークサイト、被害組織交渉チャットログの追跡、法執行機関（LE: FBI・国家犯罪対策庁・警察庁等）による大規模テイクダウン「Operation Cronos」への攻撃者側の対抗動態、サイバー犯罪学とコンピュータ科学の融合
> - **探訪・参照研究論文**:
>   - [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
>   - Yin Minn Pa Pa, Katsunari Yoshioka, et al. "A Longitudinal Analysis of LockBit 3.0's Extortion Lifecycle and Response to Law Enforcement." *Proceedings of the 28th International Symposium on Research in Attacks, Intrusions and Defenses (RAID 2025)*, 2025.

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第26話 4コマ漫画イラスト](illustrations/ep26_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮の素朴な認識：身代金を払えば解決？**<br>ニュースを見ながら「暗号化されたら身代金を払うしかないのかな？」と呑気に発言する蓮。 | **蓮**: 「ニュースで大企業がランサム被害に遭ってるけど、暗号化されたら身代金払うしかないのかな？」 | **Ren**: "Big companies are getting hit by ransomware on the news. If files get encrypted, do they just have to pay up?" |
| **第2コマ**<br>【承】 | **結衣の冷徹な指摘：二重脅迫とRaaSの罠**<br>「払ってもデータ流出は止まらず、悪の資金源になるだけ。二重脅迫とRaaSの分業体制です」と指摘する結衣。 | **結衣**: 「甘いです。復号鍵がもらえる保証はなく、機密データの流出暴露で二重に脅される悪質なビジネスです。」 | **Yui**: "Naïve. There's no guarantee of decryption, and it's a ruthless business that double-extorts via leak sites." |
| **第3コマ**<br>【転】 | **悠真TAによるSPIRAL論文とOperation Cronos解説**<br>Torリークサイトや交渉ログを長期分析し、法執行機関の掃討作戦への対抗動態を暴いた学術研究を紹介する悠真。 | **悠真**: 「SPIRALのRAID 2025論文では、LockBit 3.0のリークサイトや交渉ログ、国際捜査への対抗動態をデータで暴いたんだ。」 | **Yuma**: "SPIRAL's RAID 2025 paper tracked LockBit 3.0's leak sites, ransom negotiations, and its counter-moves against Operation Cronos." |
| **第4コマ**<br>【結】 | **サイバー犯罪エコシステムの解明へ**<br>コードの穴塞ぎだけでなく、経済的動機や犯罪組織の力学と戦う科学的アプローチに感銘を受ける二人。 | **蓮**: 「ウイルスを倒すだけじゃなく、犯罪組織の経営構造そのものと戦う学問なんだ！」<br>**結衣**: 「サイバー犯罪学とコンピュータ科学の融合……これこそ真の防衛ですね。」 | **Ren**: "It's not just about stopping malware, it's about taking down their entire criminal business model!"<br>**Yui**: "Merging cyber criminology with computer science... that is true defense." |

---

## 📖 小説本文

{ep26_novel}

---

## 📊 TikZによるセキュリティ構造図解

![LockBit 3.0 脅迫ライフサイクルと法執行機関（Operation Cronos）への対抗動態構造図](figures/fig26_lockbit_extortion_lifecycle.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. ランサムウェアは「単なるウイルス」から「巨大産業」へ進化した
かつてのランサムウェア（ファイルを暗号化して解除キーと引き換えに金銭を要求するマルウェア）は、単体の悪意あるプログラムによる小規模な犯行が中心でした。しかし現代のランサムウェアは、高度に組織化された**「RaaS（Ransomware-as-a-Service：サービスとしてのランサムウェア）」**という分業ビジネスモデルへと変貌を遂げています。
- **コア開発者（Operators）**: マルウェア本体の開発、身代金交渉プラットフォーム、暗号化インフラ、ダークウェブ上のリークサイトを管理・提供する。
- **アフィリエイト（Affiliates：実行犯）**: 標的企業への初期侵入（フィッシングやVPN脆弱性悪用）を行い、データを窃取してランサムウェアを実行する。
- **身代金分配**: 支払われた身代金（ビットコインやMonero等の暗号資産）は、開発者側（10〜20%）と実行犯側（80〜90%）で自動的に山分けされる仕組みになっています。

### 2. 「二重脅迫（Double Extortion）」の凶悪なメカニズム
現代のランサムウェア攻撃で最も恐れられているのが**「二重脅迫」**です。
1. **第1の脅迫（可用性の破壊）**: 企業の基幹システムやバックアップファイルを強固に暗号化し、操業を停止させる。
2. **第2の脅迫（機密性の暴露）**: 暗号化の前にギガバイト〜テラバイト級の顧客個人情報や知的財産を外部へ持ち出し、「身代金を支払わなければTorダークウェブ上の専用リークサイト（DLS: Dedicated Leak Site）で全世界に無料公開・オークションにかける」とカウントダウンタイマーを突きつけて脅迫する。
このため、企業がオフラインバックアップからシステムを復旧できたとしても、「機密情報がネットに晒される」という恐怖から身代金支払いを余儀なくされるケースが後を絶ちません。

### 3. 横浜国大 SPIRAL による国際共同研究の金字塔（RAID 2025）
横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）の**吉岡克成 教授**、**イン・ミンパパ 特任准教授**らの国際共同研究チームが、国際トップシンポジウム **RAID 2025** で発表した論文『*A Longitudinal Analysis of LockBit 3.0's Extortion Lifecycle and Response to Law Enforcement*』は、世界最強と恐れられたランサムウェアシンジケート**「LockBit 3.0」**を長期的に追跡・解剖した画期的な実証研究です。
- **実証的データ収集**: Tor上のLockBitリークサイトを長期間クローリングし、数千件に及ぶ被害組織の公表データ、支払期限タイマー、身代金交渉チャットログを網羅的に分析。
- **法執行機関（LE）への対抗動態の可視化**: 2024年2月、FBI・英国国家犯罪対策庁（NCA）・日本の警察庁など10カ国による国際共同掃討作戦**「Operation Cronos」**によってLockBitの重要インフラやソースコードが押収・無力化されました。論文では、この壊滅的打撃を受けた後にLockBitがどのように代替サーバーを立ち上げ、被害者リストを再投稿して組織の「信頼性（ブランド）」を取り戻そうと足掻いたか、その回復挙動や限界をデータで克明に証明しました。
- **研究の意義**: サイバーセキュリティは、通信プロトコルの穴を塞ぐ工学だけでなく、攻撃者の経済的インセンティブや組織力学を暴く「サイバー犯罪学（Cyber Criminology）」のエビデンスを提供することで、世界中の法執行機関や政策立案者が有効な打撃を与える武器となるのです。
"""

# Episode 27 Markdown Content
ep27_raw = open(os.path.join(CONTENT_DIR, "ep27_novel_raw.txt"), "r", encoding="utf-8").read()
ep27_novel = format_novel(ep27_raw)

ep27_md = f"""---
title: "第27話 届かぬ警告と目覚める砦 〜大規模IoT診断サービス「Am I Infected?」の真実〜"
episode_num: 27
date: 2026-10-29
categories: ["高校生向けサイバーセキュリティライトノベル", "横浜国立大学SPIRAL論文探訪"]
tags: ["横浜国大SPIRAL", "IoTセキュリティ", "Am I Infected?", "NOTICE", "ヒューマンファクター", "Secure-by-Design", "佐々木貴之准教授", "吉岡克成教授", "松本勉上席特別教授"]
---

# 第27話 届かぬ警告と目覚める砦 〜大規模IoT診断サービス「Am I Infected?」の真実〜

> **【放課後サイバーディフェンス・ラボ（第2部：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜）】**
> - **舞台**: 帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 地域・社会実装ラボ
> - **登場人物**: 神崎 蓮（高校1年・IoT班）、白石 結衣（高校1年・暗号数理班）、城崎 悠真（大学1年・芹沢研TA）、芹沢 涼香 准教授（大学メンター）
> - **学習テーマ**: 横浜国立大学 SPIRAL・佐々木貴之准教授、吉岡克成教授、松本勉上席特別教授らのトップカンファレンス論文（USENIX Security 2025）、大規模IoT診断サービス「Am I Infected?」の実装と運用、総務省・NICT・ISPとの官民学連携プロジェクト（NOTICE）、ユーザー行動変容の障壁（ヒューマンファクター：難解なUI、ファームウェア更新手順の絶望的複雑さ、EOL放置機器）、自己責任論の限界と「Secure-by-Design」およびネットワーク側自動防護の必要性
> - **探訪・参照研究論文**:
>   - [横浜国立大学 サイバーセキュリティ実践教育研究センター（SPIRAL）](https://spiral.ynu.ac.jp/)
>   - Takayuki Sasaki, Katsunari Yoshioka, Tsutomu Matsumoto, et al. "Am I Infected? Lessons from Operating a Large-Scale IoT Security Diagnostic Service." *Proceedings of the 34th USENIX Security Symposium (USENIX Security 2025)*, 2025.

---

## 🎨 4コマ漫画・ストーリーイラスト (Draw Things 生成)

![第27話 4コマ漫画イラスト](illustrations/ep27_4koma.png)

---

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **蓮の楽観論：危険を通知すれば皆すぐ直す！**<br>「脆弱なIoTルーターが見つかったら、持ち主にメールで知らせれば即解決！」と自信満々の蓮。 | **蓮**: 「危ないルーターを見つけたら、持ち主に『危険ですよ』って通知を送ればすぐ直してくれるはず！」 | **Ren**: "If we find a vulnerable router, sending an alert to the owner should get it fixed immediately!" |
| **第2コマ**<br>【承】 | **結衣の冷静な指摘：一般人の絶望的障壁**<br>「専門用語だらけの管理画面や更新手順は、一般人には詐欺メールに見えたり絶望の壁です」と説く結衣。 | **結衣**: 「甘いです。ルーターの設定画面を開いてファームウェアを更新するのは、一般人には絶望的な壁です。」 | **Yui**: "Naïve. Opening a router admin panel and updating firmware is a hopelessly daunting barrier for average users." |
| **第3コマ**<br>【転】 | **悠真TAによるUSENIX Security論文の衝撃データ**<br>何十万台もの大規模診断でも改善行動を起こしたのはごく僅かだったという人間行動の現実を語る悠真。 | **悠真**: 「横浜国大・佐々木准教授らのUSENIX Security 2025論文『Am I Infected?』がその現実を克明に暴いたんだ。」 | **Yuma**: "YNU Assoc. Prof. Sasaki's USENIX Security 2025 paper 'Am I Infected?' proved that reality with massive operational data." |
| **第4コマ**<br>【結】 | **Secure-by-Designと誰も取り残さない砦へ**<br>ユーザーの自己責任に頼らず、初期出荷時から安全でネットワークが守る仕組みの重要性に目覚める二人。 | **蓮**: 「ユーザーに頑張らせるんじゃなく、何もしなくても安全な砦を僕たちが作らなきゃ！」<br>**結衣**: 「Secure-by-Designと社会基盤の連携……これこそ目指すべき工学ですね。」 | **Ren**: "Instead of burdening users, we need to build fortress devices that stay secure automatically!"<br>**Yui**: "Secure-by-Design paired with infrastructure collaboration... that is the engineering goal." |

---

## 📖 小説本文

{ep27_novel}

---

## 📊 TikZによるセキュリティ構造図解

![大規模IoT診断サービス「Am I Infected?」と人間行動因子・Secure-by-Design構造図](figures/fig27_iot_diagnostic_human_factors.png)

---

## 💡 高校生のためのセキュリティ深掘りコラム

### 1. IoT機器のセキュリティはなぜこれほど放置されるのか？
パソコンやスマートフォンであれば、OSの自動アップデート機能やセキュリティ警告が日常的に表示されます。しかし、家庭やオフィスに設置されたWi-Fiルーター、ネットワークカメラ、スマート家電などの**IoT（Internet of Things）機器**は、一度電源を入れると押し入れや天井裏に何年も放置されがちです。
- **画面やキーボードがない**: 機器単体では異常を伝えるディスプレイがなく、攻撃されてマルウェア（Mirai等）に感染しても普段通り通信できるため、所有者は感染に気づけません。
- **初期パスワード（admin/admin等）の放置**: インターネット全体からのポートスキャンを受け、辞書攻撃で容易に乗っ取られてDDoS攻撃の踏み台（ボットネット）にされてしまいます。

### 2. 総務省・NICT・横浜国大が挑む「NOTICE」と「Am I Infected?」
日本国内では、2019年から総務省・国立研究開発法人情報通信研究機構（NICT）・インターネットサービスプロバイダ（ISP）が連携し、サイバー攻撃に悪用される恐れのあるIoT機器を調査してユーザーに注意喚起を行う国家プロジェクト**「NOTICE（National Operation towards IoT Clean Environment）」**が実施されています。
これと連動し、一般ユーザーが自ら「自分の機器が感染していないか」を簡単にWebブラウザから診断できるように設計・運用されたのが、横浜国立大学 SPIRALの**佐々木貴之 准教授、吉岡克成 教授、松本勉 上席特別教授**らが開発・実証した大規模診断プラットフォーム**「Am I Infected?（私、感染していませんか？）」**です。

### 3. 世界最高峰国際会議 USENIX Security 2025 採択論文が暴いた真実
2025年、セキュリティ研究の最高峰である **USENIX Security Symposium 2025** に採択された論文『*Am I Infected? Lessons from Operating a Large-Scale IoT Security Diagnostic Service*』は、何十万台もの一般ユーザー環境に大規模診断と注意喚起を提供した長期運用データから、極めて重要かつ衝撃的な**「ヒューマンファクター（人間行動の壁）」**を明らかにしました。
- **届かぬ警告**: 診断結果として「感染している」「脆弱な設定である」と明確な警告と詳細な修正マニュアルを提示しても、実際に機器の設定を変更したりファームウェアを更新して安全化に至ったユーザーは極めて限定的でした。
- **ユーザーが直面する絶望的な障壁**:
  1. **リテラシーの壁**: 「デフォルトゲートウェイ」「プライベートIP」「ポートフォワーディング」などの専門用語が理解できない。
  2. **心理的恐怖**: 「設定画面をいじってインターネットが繋がらなくなったら困る」「この通知自体がフィッシング詐欺ではないか」という警戒心。
  3. **EOL（End of Life）問題**: メーカーがすでにサポートを終了しており、更新用ファームウェアそのものが存在しない。
- **「自己責任」から「Secure-by-Design」への歴史的転換**:
  この研究が世界に与えた最大の示唆は、**「一般ユーザーの努力やリテラシーにセキュリティを期待するモデルは破綻している」**という冷徹な実証結果です。
  これからのサイバーセキュリティ工学は、
  1. 出荷時から安全なパスワード設定を強制する**「セキュア・バイ・デザイン（Secure-by-Design）」**
  2. ユーザーの介在なしに安全にパッチが適用される自動更新機能
  3. ISPやネットワーク事業者側での不正通信の自動隔離・フィルタリング
  というように、**「ユーザーが何もしなくても、意識しなくても守られる社会基盤づくり」**へとパラダイムシフトしなければならないことを証明したのです。
"""

with open(os.path.join(CONTENT_DIR, "2026-10-29_ep26_lockbit_extortion_lifecycle.md"), "w", encoding="utf-8") as f:
    f.write(ep26_md)
print("Saved 2026-10-29_ep26_lockbit_extortion_lifecycle.md")

with open(os.path.join(CONTENT_DIR, "2026-10-29_ep27_iot_diagnostic_human_factors.md"), "w", encoding="utf-8") as f:
    f.write(ep27_md)
print("Saved 2026-10-29_ep27_iot_diagnostic_human_factors.md")
