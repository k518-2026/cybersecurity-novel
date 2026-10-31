# 放課後サイバーディフェンス・ラボ 〜高校生からはじめるサイバーセキュリティと大学情報科学の扉〜

🌐 **Webサイト（GitHub Pages）で読む**: **[https://k518-2026.github.io/cybersecurity-novel/](https://k518-2026.github.io/cybersecurity-novel/)**

高校生がサイバーセキュリティの面白さ・重要性に触れ、将来の情報科学系大学やセキュリティ専門分野への進学を目指すための入門ライトノベル・ライブラリです。

## 🌟 特徴
1. **男子高校生＆女子高校生が主人公の等身大ストーリー**:
   - 高校情報科学部の部長・**城崎 悠真（理系男子）**と部員の**橘 葵（好奇心旺盛な女子高生）**が、身近なITトラブルや国内外の最新ニュースを題材に、大学の**芹沢 涼香 准教授（サイバーセキュリティ研究室 / IPAアドバイザー）**と共にセキュリティの真髄を学んでいきます。
2. **客観的・公式な教育標準と国内外ニュースの統合**:
   - **IPA「デジタルスキル標準（DSS）」**（セキュリティリテラシー・アーキテクチャ基準）
   - **デジタル庁・総務省**（本人確認ガイドライン・パスキー普及方針）
   - **内閣官房「国家サイバー統括室」（cyber.go.jp）**（サプライチェーン点検要請・国家戦略）
   - **警察庁サイバー警察局**（情報流出への緊急注意喚起）
   - **海外主要セキュリティ機関・メディア**（米CISA KEV、The Hacker News、BleepingComputer、FIDO Alliance）
3. **高品質なビジュアル解説**:
   - **FLUX.2 klein** による作画崩壊のない美麗アニメイラスト（Episode 06 準拠の生き生きとした放課後学習・開発シーン）
   - **TikZ（LuaLaTeX）** による文字重なりのない精密なセキュリティアーキテクチャ・構造図解

---

## 📚 収録エピソード一覧（第1部・第2部 全33話）

### 第1部：高校情報科学部とサイバーセキュリティの基礎（第1話〜第15話 完結）

| 話数 | タイトル | 主人公・登場人物 | 学習テーマ・参照規格 | 図解 (TikZ) | 挿絵 (Draw Things 4コマ) | 原稿 (Markdown) |
|:---:|:---|:---|:---|:---:|:---:|:---:|
| 01 | **秘密の合言葉と見えない鍵** | 橘 葵, 城崎 悠真, 芹沢准教授 | パスワード管理、認証の3要素、多要素認証（MFA）、アカウントリスト攻撃 | [図解](content/figures/fig01_mfa_principles.png) | [4コマ漫画](content/illustrations/ep01_4koma.png) | [第1話本文](content/2026-10-23_ep01_passwords_and_authentication.md) |
| 02 | **偽りの手紙と本物の目印** | 城崎 悠真, 橘 葵, 芹沢准教授 | スミッシング（不在通知SMS詐欺）、ソーシャルエンジニアリング、URL階層構造、電子証明書の真実 | [図解](content/figures/fig02_phishing_domain_structure.png) | [4コマ漫画](content/illustrations/ep02_4koma.png) | [第2話本文](content/2026-10-23_ep02_phishing_and_social_engineering.md) |
| 03 | **街角の電波は誰のもの？** | 城崎 悠真, 橘 葵, 芹沢准教授 | カフェのフリーWi-Fi、盗聴と中間者攻撃（MitM）、TLS暗号化トンネル、VPN | [図解](content/figures/fig03_wifi_mitm_encryption_tunnel.png) | [4コマ漫画](content/illustrations/ep03_4koma.png) | [第3話本文](content/2026-10-23_ep03_free_wifi_and_encryption.md) |
| 04 | **忍び寄るトロイの木馬** | 城崎 悠真, 橘 葵, 芹沢准教授 | マルウェア4分類（ウイルス・ワーム・トロイ・ランサムウェア）、脆弱性とパッチ適用 | [図解](content/figures/fig04_malware_vulnerability_patch.png) | [4コマ漫画](content/illustrations/ep04_4koma.png) | [第4話本文](content/2026-10-24_ep04_malware_and_vulnerabilities.md) |
| 05 | **三つの宝珠を守る城壁** | 城崎 悠真, 橘 葵, 芹沢准教授 | CIAの3大要素（機密性・完全性・可用性）、DDoS攻撃、多層防御（入口・内部・出口対策）同心円モデル | [図解](content/figures/fig05_cia_and_defense_in_depth.png) | [4コマ漫画](content/illustrations/ep05_4koma.png) | [第5話本文](content/2026-10-23_ep05_cia_triad_and_defense_in_depth.md) |
| 06 | **データベースの合言葉と呪文の罠** | 城崎 悠真, 橘 葵, 芹沢准教授 | SQLインジェクション攻撃の原理、文字列連結の脆弱性、プレースホルダ（バインド機構）による防御 | [図解](content/figures/fig06_sql_injection_defense.png) | [4コマ漫画](content/illustrations/ep06_4koma.png) | [第6話本文](content/2026-10-23_ep06_sql_injection_and_web_security.md) |
| 07 | **割れない南京錠と魔法の印鑑** | 城崎 悠真, 橘 葵, 芹沢准教授 | 共通鍵暗号の鍵配送問題、公開鍵暗号の鍵ペア、デジタル署名（電子署名）、SHA-256ハッシュ関数 | [図解](content/figures/fig07_digital_signature_pki.png) | [4コマ漫画](content/illustrations/ep07_4koma.png) | [第7話本文](content/2026-10-23_ep07_cryptography_and_digital_signatures.md) |
| 08 | **覚えない合言葉と手のひらの証明** | 城崎 悠真, 橘 葵, 芹沢准教授 | パスキー（Passkey / FIDO2）、端末セキュアエレメント、公開鍵チャレンジ＆レスポンス、デジタル庁・総務省ガイドライン | [図解](content/figures/fig08_passkey_fido2_architecture.png) | [4コマ漫画](content/illustrations/ep08_4koma.png) | [第8話本文](content/2026-10-24_ep08_passkey_and_fido2_passwordless.md) |
| 09 | **見えない裏口と材料の目録** | 城崎 悠真, 橘 葵, 芹沢准教授 | サプライチェーン攻撃（委託先経由侵害）、国家サイバー統括室要請、SBOM（ソフトウェア部品構成表）、米CISA | [図解](content/figures/fig09_supply_chain_sbom.png) | [4コマ漫画](content/illustrations/ep09_4koma.png) | [第9話本文](content/2026-10-24_ep09_supply_chain_attack_and_sbom.md) |
| 10 | **ゼロの日を越える翼** | 城崎 悠真, 橘 葵, 芹沢准教授 | ゼロデイ脆弱性（0-day）、協調的開示（CVD）、CVE/CVSS、米CISA KEVカタログ、ホワイトハッカーの情報倫理 | [図解](content/figures/fig10_zero_day_coordinated_disclosure.png) | [4コマ漫画](content/illustrations/ep10_4koma.png) | [第10話本文](content/2026-10-24_ep10_zero_day_and_white_hackers.md) |
| 11 | **砂浜の足跡と電子の鑑識官** | 城崎 悠真, 橘 葵, 芹沢准教授 | デジタル・フォレンジック（電子鑑識）、ライトブロッカー、ハッシュ値照合、不正アクセス禁止法、サイバー警察・CSIRT | [図解](content/figures/fig11_digital_forensics_law.png) | [4コマ漫画](content/illustrations/ep11_4koma.png) | [第11話本文](content/2026-10-24_ep11_digital_forensics_and_cyber_law.md) |
| 12 | **世界を繋ぐバケツリレー** | 城崎 悠真, 橘 葵, 芹沢准教授 | 家庭・学校のLANとWAN、プライベートIPとグローバルIP、ルーター（NAT/NAPT）、DNS名前解決の仕組み | [図解](content/figures/fig12_lan_router_dns.png) | [4コマ漫画](content/illustrations/ep12_4koma.png) | [第12話本文](content/2026-10-24_ep12_lan_routers_and_dns_basics.md) |
| 13 | **旗を掲げる守護者たち** | 城崎 悠真, 橘 葵, 芹沢准教授 | サイバーセキュリティ競技（CTF）、5大ジャンル（Web, Crypto, Reversing, Forensics, Pwn）、大学情報学部進路、CISO | [図解](content/figures/fig13_ctf_and_careers.png) | [4コマ漫画](content/illustrations/ep13_4koma.png) | [第13話本文](content/2026-10-24_ep13_ctf_competition_and_future_careers.md) |
| 14 | **見えない空の保管庫** | 橘 葵, 城崎 悠真, 芹沢准教授 | クラウドセキュリティ、責任共有モデル（Shared Responsibility Model）、IAM最小権限の原則、バケット全世界公開対策 | [図解](content/figures/fig14_cloud_shared_responsibility.png) | [4コマ漫画](content/illustrations/ep14_4koma.png) | [第14話本文](content/2026-10-24_ep14_cloud_security_and_shared_responsibility.md) |
| 15 | **知性をまとう盾と矛（第1部 完結）** | 橘 葵, 城崎 悠真, 芹沢准教授 | AI悪用脅威（プロンプト注入・ディープフェイク・データ汚染） vs 自律型AIサイバー防御、人間の倫理と知性、第1部完結・進路決定 | [図解](content/figures/fig15_ai_security_deepfake.png) | [4コマ漫画](content/illustrations/ep15_4koma.png) | [第15話本文](content/2026-10-24_ep15_ai_security_and_future_frontiers.md) |

### 第2部：新世代編（第16話〜第25話）

#### 【前半：新世代の胎動と先端ハードウェア＆ゼロトラスト防御】

| 話数 | タイトル | 主人公・登場人物 | 学習テーマ・参照規格 | 図解 (TikZ) | 挿絵 (Draw Things 4コマ) | 原稿 (Markdown) |
|:---:|:---|:---|:---|:---:|:---:|:---:|
| 16 | **街角の監視者たち** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 第2部開幕、IoT初期パスワード放置、Miraiボットネット、総務省・NICT NOTICEプロジェクト、VLAN分離 | [図解](content/figures/fig16_iot_security_mirai.png) | [4コマ漫画](content/illustrations/ep16_4koma.png) | [第16話本文](content/2026-10-26_ep16_iot_security_and_default_passwords.md) |
| 17 | **城壁のない砦** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 境界型防御の破綻、内部横展開（ラテラルムーブメント）、NIST SP 800-207ゼロトラスト原則、マイクロセグメンテーション | [図解](content/figures/fig17_zero_trust_architecture.png) | [4コマ漫画](content/illustrations/ep17_4koma.png) | [第17話本文](content/2026-10-26_ep17_zero_trust_and_perimeter_defense.md) |
| 18 | **基板の上の囁き** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 基板物理端子（UART/JTAG）、Root権限奪取、サイドチャネル攻撃（差分電力解析 DPA）、セキュアブート | [図解](content/figures/fig18_hardware_and_side_channel.png) | [4コマ漫画](content/illustrations/ep18_4koma.png) | [第18話本文](content/2026-10-26_ep18_hardware_hacking_and_side_channel.md) |
| 19 | **秘密を明かさぬ計算** | 白石 結衣, 神崎 蓮, 城崎悠真TA, 芹沢准教授 | プライバシー強化技術（PETs）、完全準同型暗号（FHE：暗号化したまま演算）、差分プライバシー（DP）、秘密計算 | [図解](content/figures/fig19_privacy_enhancing_tech.png) | [4コマ漫画](content/illustrations/ep19_4koma.png) | [第19話本文](content/2026-10-26_ep19_privacy_enhancing_technologies.md) |
| 20 | **走るネットワークと灯火の防衛** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 第2部前半完結、産業制御システム（OT/SCADA）可用性最優先、コネクテッドカー（CANバス）、国連UN-R155、SecOC | [図解](content/figures/fig20_ot_scada_automotive.png) | [4コマ漫画](content/illustrations/ep20_4koma.png) | [第20話本文](content/2026-10-26_ep20_ot_scada_and_automotive_security.md) |

#### 【後半：大学先端研究の扉 〜横浜国大SPIRAL論文探訪〜（第21話〜第33話）】
*(参照・協力：[横浜国立大学 サイバーセキュリティ実践教育研究センター SPIRAL](https://spiral.ynu.ac.jp/))*

| 話数 | タイトル | 主人公・登場人物 | 学習テーマ・探訪論文 | 図解 (TikZ) | 挿絵 (Draw Things 4コマ) | 原稿 (Markdown) |
|:---:|:---|:---|:---|:---:|:---:|:---:|
| 21 | **甘い偽指の衝撃** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 松本勉教授の伝説的論文『人工グミ指による生体認証突破』（SPIE 2002）、生体情報Revoke不能性、提示攻撃検知（Liveness Detection / PAD）、国際規格 ISO/IEC 30107 | [図解](content/figures/fig21_gummy_finger_liveness.png) | [4コマ漫画](content/illustrations/ep21_4koma.png) | [第21話本文](content/2026-10-27_ep21_gummy_finger_and_liveness_detection.md) |
| 22 | **蜜壺が暴く暗黒生態系** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 吉岡克成教授らの先駆的論文『IoTPOTによる異種CPUマルウェア動態解明』（USENIX WOOT 2015）、異種CPUサンドボックス、Mirai前夜の脅威観測エコシステム | [図解](content/figures/fig22_iotpot_threat_intelligence.png) | [4コマ漫画](content/illustrations/ep22_4koma.png) | [第22話本文](content/2026-10-27_ep22_iotpot_and_iot_malware_ecosystem.md) |
| 23 | **闇夜の反射鏡を砕け** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 牧田大佑准教授・吉岡克成教授らの特選論文『ダークネットとDNSハニーポットの相関分析によるDDoS事前対策』（情報処理学会特選論文 2015）、UDP送信元IP偽装、事前予兆検知 | [図解](content/figures/fig23_darknet_ddos_correlation.png) | [4コマ漫画](content/illustrations/ep23_4koma.png) | [第23話本文](content/2026-10-27_ep23_darknet_and_dns_amplification_prevention.md) |
| 24 | **量子の嵐と格子の盾** | 白石 結衣, 神崎 蓮, 城崎悠真TA, 芹沢准教授 | 四方順司教授（NexCrypt Lab長）の耐量子計算機暗号（PQC）数理、ショアのアルゴリズム、高次元格子幾何学（ML-KEM/ML-DSA）、HNDL脅威、匿名同報認証、集約MAC | [図解](content/figures/fig24_pqc_lattice_shikata.png) | [4コマ漫画](content/illustrations/ep24_4koma.png) | [第24話本文](content/2026-10-27_ep24_pqc_lattice_cryptography_shikata_lab.md) |
| 25 | **賢者の檻と化かす影** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 伊藤曜助教・吉岡克成教授らの最新論文『LLMによるサンドボックス回避耐性強化支援』（CSS 2025 ICSS研究賞）、マルウェアの擬死・環境検知、LLM自律探索・擬態パッチ | [図解](content/figures/fig25_llm_sandbox_spiral.png) | [4コマ漫画](content/illustrations/ep25_4koma.png) | [第25話本文](content/2026-10-27_ep25_llm_sandbox_evasion_robustness_spiral.md) |
| 26 | **身代金ビジネスの暗雲** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 吉岡克成教授・インミンパパ特任准教授らの国際共同論文『LockBit 3.0の脅迫ライフサイクルと対抗動態』（RAID 2025）、RaaS分業、二重脅迫、Operation Cronos対抗動態、サイバー犯罪学 | [図解](content/figures/fig26_lockbit_extortion_lifecycle.png) | [4コマ漫画](content/illustrations/ep26_4koma.png) | [第26話本文](content/2026-10-29_ep26_lockbit_extortion_lifecycle.md) |
| 27 | **届かぬ警告と目覚める砦** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 佐々木貴之准教授・吉岡克成教授・松本勉上席特別教授らのトップ論文『大規模IoT診断サービスAm I Infected?からの教訓』（USENIX Security 2025）、ヒューマンファクター、Secure-by-Design | [図解](content/figures/fig27_iot_diagnostic_human_factors.png) | [4コマ漫画](content/illustrations/ep27_4koma.png) | [第27話本文](content/2026-10-29_ep27_iot_diagnostic_human_factors.md) |
| 28 | **潜む裏口と社会インフラの防壁** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 佐々木貴之准教授・吉岡克成教授・松本勉上席特別教授らのトップ論文『重要インフラ遠隔管理Web機器の露見と是正』（IEEE S&P 2022）、従来ICSスキャン死角、13件のゼロデイ、責任ある開示（58%是正） | [図解](content/figures/fig28_exposed_ics_gateways.png) | [4コマ漫画](content/illustrations/ep28_4koma.png) | [第28話本文](content/2026-10-29_ep28_exposed_ics_gateways.md) |
| 29 | **悪のIoTを浄化せよ** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 吉岡克成教授・松本勉上席特別教授らの最優秀論文『悪のIoTネットを浄化せよ』（NDSS 2019 Distinguished Paper Award）、Mirai除染、実網RCT、メール効果ゼロ vs Walled Garden隔離（14日で92%駆除） | [図解](content/figures/fig29_isp_walled_garden_mirai.png) | [4コマ漫画](content/illustrations/ep29_4koma.png) | [第29話本文](content/2026-10-29_ep29_isp_walled_garden_mirai.md) |
| 30 | **消えゆく足跡と鎖の記憶** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | インミンパパ特任准教授・吉岡克成教授らの最新論文『DeFiトークン詐欺の暴き方（DeFiIntel）』（NDSS MADWeb 2025）、Rug Pull詐欺、オンチェーン×消滅するオフチェーン統合アーカイブ、予兆検知 | [図解](content/figures/fig30_defiintel_token_scam.png) | [4コマ漫画](content/illustrations/ep30_4koma.png) | [第30話本文](content/2026-10-29_ep30_defiintel_token_scam.md) |
| 31 | **隠された扉と影の合言葉** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 吉岡克成教授・佐々木貴之准教授らの受賞論文『マニュアル非記載Telnet/SSHサービスの調査』（CSS 2025 エシカルプラクティス賞）、デバッグ残骸、ハードコード認証、エシカル研究倫理 | [図解](content/figures/fig31_undocumented_iot_backdoors.png) | [4コマ漫画](content/illustrations/ep31_4koma.png) | [第31話本文](content/2026-10-31_ep31_undocumented_iot_backdoors.md) |
| 32 | **星の標識と消費者の砦** | 神崎 蓮, 白石 結衣, 城崎悠真TA, 芹沢准教授 | 吉岡克成教授（技術審議委員長）、経産省・IPAの国家制度JC-STAR（IoTセキュリティ適合性評価）、星ラベル（★1〜★4）、レモンの市場克服、ファームウェアSCA解析 | [図解](content/figures/fig32_jcstar_iot_labeling.png) | [4コマ漫画](content/illustrations/ep32_4koma.png) | [第32話本文](content/2026-10-31_ep32_jcstar_iot_labeling.md) |
| 33 | **空間を翔ける乱数と量子の極致** | 白石 結衣, 神崎 蓮, 城崎悠真TA, 芹沢准教授 | 四方順司教授（NexCrypt Lab長）の先端論文『物理層セキュリティにおける量子アルゴリズム応用』（IEEE Access 2025）、電波フェージング秘密鍵生成（SKG）、情報理論的安全性、B5G/6G ISAC | [図解](content/figures/fig33_quantum_physical_layer_security.png) | [4コマ漫画](content/illustrations/ep33_4koma.png) | [第33話本文](content/2026-10-31_ep33_quantum_physical_layer_security.md) |

---

## 🛠️ 技術スタック
- **執筆LLM**:
  - 構成作家: Qwen 3.5 (9B)
  - 執筆作家: Shosetsu (latest)
- **画像生成**:
  - 画像生成モデル: FLUX.2 [klein] Base (9B i8x)
- **図版生成**:
  - LuaLaTeX + TikZ (高精細ベクター・ラスターレンダリング)
- **公開形式**:
  - Markdown / HTML (GitHub Pages対応)
