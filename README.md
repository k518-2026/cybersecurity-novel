# 放課後サイバーディフェンス・ラボ 〜高校生からはじめるサイバーセキュリティと大学情報科学の扉〜

高校生がサイバーセキュリティの面白さ・重要性に触れ、将来の情報科学系大学やセキュリティ専門分野への進学を目指すための入門ライトノベル・ライブラリです。

## 🌟 特徴
1. **男子高校生＆女子高校生が主人公の等身大ストーリー**:
   - 高校情報科学部の部長・**城崎 悠真（理系男子）**と部員の**橘 葵（好奇心旺盛な女子高生）**が、身近なITトラブルや最新ニュースをきっかけに、大学の**芹沢 涼香 准教授（サイバーセキュリティ研究室 / IPAアドバイザー）**と共にセキュリティの真髄を学んでいきます。
2. **客観的・公式な教育標準と最新ニュースの統合**:
   - **IPA「デジタルスキル標準（DSS）」**（セキュリティリテラシー・マネジメント基準）
   - **内閣官房「国家サイバー統括室」（cyber.go.jp）**の啓発方針・国家戦略
   - **「サイバーセキュリティ.com」**で報じられるリアルタイムな不正アクセス・情報漏洩インシデント
3. **高品質なビジュアル解説**:
   - **Draw Things**（FLUXモデル）による日本のフルカラー縦型4コマ漫画風挿絵
   - **TikZ（LuaLaTeX）**による美しく正確なセキュリティアーキテクチャ・構造図解

---

## 📚 収録エピソード一覧

| 話数 | タイトル | 主人公・登場人物 | 学習テーマ | 図解 (TikZ) | 挿絵 (Draw Things) | 原稿 (Markdown) |
|:---:|:---|:---|:---|:---:|:---:|:---:|
| 01 | **秘密の合言葉と見えない鍵** | 橘 葵, 城崎 悠真, 芹沢准教授 | パスワード管理、認証の3要素、多要素認証（MFA）、アカウントリスト攻撃 | [図解](content/figures/fig01_mfa_principles.png) | [4コマ漫画](content/illustrations/ep01_4koma.png) | [第1話本文](content/2026-10-23_ep01_passwords_and_authentication.md) |
| 02 | **偽りの手紙と本物の目印** | 城崎 悠真, 橘 葵, 芹沢准教授 | スミッシング（不在通知SMS詐欺）、ソーシャルエンジニアリング、URL階層構造、SSL/TLS電子証明書の真実 | [図解](content/figures/fig02_phishing_domain_structure.png) | [4コマ漫画](content/illustrations/ep02_4koma.png) | [第2話本文](content/2026-10-23_ep02_phishing_and_social_engineering.md) |
| 03 | **街角の電波は誰のもの？** | 城崎 悠真, 橘 葵, 芹沢准教授 | カフェのフリーWi-Fi、盗聴と中間者攻撃（MitM）、TLS暗号化トンネル、VPN | [図解](content/figures/fig03_wifi_mitm_encryption_tunnel.png) | [4コマ漫画](content/illustrations/ep03_4koma.png) | [第3話本文](content/2026-10-23_ep03_free_wifi_and_encryption.md) |
| 04 | **忍び寄るトロイの木馬** | 城崎 悠真, 橘 葵, 芹沢准教授 | マルウェア4分類（ウイルス・ワーム・トロイ・ランサムウェア）、脆弱性、パッチ適用の重要性 | [図解](content/figures/fig04_malware_vulnerability_patch.png) | [4コマ漫画](content/illustrations/ep04_4koma.png) | [第4話本文](content/2026-10-23_ep04_malware_and_vulnerabilities.md) |

---

## 🛠️ 技術スタック
- **執筆LLM**: http://192.168.128.62:11434/（構成作家: qwen3.5:9b, 執筆作家: shosetsu:latest）
- **画像生成**: Draw Things http://192.168.128.59:7860/ (lux_2_klein_base_9b_i8x.ckpt)
- **図版生成**: LuaLaTeX + TikZ + pdftoppm (High Resolution Rendering)
- **公開形式**: Markdown / HTML
