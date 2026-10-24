import os
import re

episodes_scripts = {
    5: {
        "file": "content/2026-10-23_ep05_cia_triad_and_defense_in_depth.md",
        "script": """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **DDoS攻撃で学内Webサイトがダウン！**<br>アクセス殺到でサーバー応答不能の赤いエラー画面を見て頭を抱える葵。 | **葵**: 「えっ！？ 学内ポータルが全然開かない……！ サーバーが落ちちゃったの！？」 | **Aoi**: "What?! The school portal isn't opening at all...! Has the server crashed?!" |
| **第2コマ**<br>【承】 | **悠真の冷静な分析：可用性の喪失**<br>ログ画面を見せながら、DDoS攻撃による可用性侵害を説明する悠真。 | **悠真**: 「これは悪意ある大量アクセスによるDDoS攻撃だ。『可用性（Availability）』が侵害されて、誰もサービスを使えなくなっているんだ。」 | **Yuma**: "This is a DDoS attack with malicious traffic flood. 'Availability' is compromised, preventing everyone from accessing the service." |
| **第3コマ**<br>【転】 | **芹沢先生によるCIAの3大要素と多層防御の解説**<br>ホワイトボードにCIAの三角形と三重の防壁を描き、堅牢な防御設計を説く芹沢准教授。 | **芹沢先生**: 「セキュリティの基本はCIA。『機密性・完全性・可用性』。どれか一つ欠けても破綻します。だからこそ、入口・内部・出口の『多層防御』が必要なのよ。」 | **Prof. Serizawa**: "The core of security is CIA: Confidentiality, Integrity, and Availability. If any one fails, trust collapses. That is why we need 'Defense in Depth' across entry, internal, and exit layers." |
| **第4コマ**<br>【結】 | **トラフィック遮断成功！三つの宝珠を守り抜く笑顔**<br>WAFと多層防御で攻撃パケットを弾き、サーバー復旧の緑アイコンに安堵の笑顔を浮かべる葵と悠真。 | **葵**: 「すごい、サイトが復活した！ 三つの宝珠（CIA）を守るってこういうことなんだね！」<br>**悠真**: 「ああ。一つの壁が破られても、次の壁が守る。これが鉄壁の守りだよ。」 | **Aoi**: "Awesome, the portal is back online! Now I truly understand how to defend the three jewels of CIA!"<br>**Yuma**: "Exactly. Even if one wall is breached, the next one holds. That is true defense in depth." |

---
"""
    },
    6: {
        "file": "content/2026-10-23_ep06_sql_injection_and_web_security.md",
        "script": """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **検索フォームに入力した「呪文」で全データ流出！？**<br>フォームに `' OR '1'='1` と入れただけで非公開データがずらりと表示され、唖然とする悠真。 | **悠真**: 「……嘘だろ。ただの入力フォームなのに、全ユーザーの非公開データがそのまま引き出せてしまった……！」 | **Yuma**: "...You've got to be kidding me. Just typing into an ordinary form exposed every user's private records...!" |
| **第2コマ**<br>【承】 | **葵の驚き：文字列の連結が生んだ致命的な罠**<br>コードの `WHERE name = ' + input + '` を指差し、悪意ある呪文がSQL文を改変した手口に気づく葵。 | **葵**: 「ユーザーの入力した文字をそのままSQLに合体させてる……！ だから命令文がすり替わっちゃったんだ！」 | **Aoi**: "The code literally concatenates raw user input into the SQL query...! That's why the command got hijacked!" |
| **第3コマ**<br>【転】 | **芹沢先生によるプレースホルダ（バインド機構）の指南**<br>「データ」と「命令」を絶対に混ぜてはいけない原則と、安全なプレースホルダ構造をホワイトボードで解説する芹沢准教授。 | **芹沢先生**: 「文字列連結は最も危険な悪手です。プレースホルダ（バインド機構）を使えば、悪意ある文字列も単なる『無害なデータ』として処理されるのよ。」 | **Prof. Serizawa**: "String concatenation is the most dangerous pitfall. By using prepared statements with placeholders (binding), malicious code is treated strictly as 'harmless data'." |
| **第4コマ**<br>【結】 | **セキュアコーディング完了！安全なデータベースへ**<br>コードをプレースホルダに書き換え、テストで不正入力が完全に弾かれたのを確認して笑顔で頷き合う二人。 | **悠真**: 「よし、バインド機構の実装完了。どんな不正な文字列が来ても、命令として解釈されることはない。」<br>**葵**: 「プログラミングの安全って、こういう細かな配慮の積み重ねなんだね！」 | **Yuma**: "Alright, prepared statements are fully in place. No malicious input will ever be executed as code."<br>**Aoi**: "Secure programming truly comes down to these thoughtful, rigorous habits!" |

---
"""
    },
    7: {
        "file": "content/2026-10-23_ep07_cryptography_and_digital_signatures.md",
        "script": """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **鍵を送る途中で盗まれたらどうするの？**<br>共通鍵暗号の「鍵配送問題」に直面し、安全に秘密の鍵を相手に届ける難しさに頭を抱える葵。 | **葵**: 「秘密のメッセージを暗号化しても、その『解錠する鍵』をインターネットで送ったら盗聴されちゃうじゃない！」 | **Aoi**: "Even if we encrypt a secret message, if we send the 'unlock key' over the Internet, eavesdroppers can steal it!" |
| **第2コマ**<br>【承】 | **悠真の提案：開いた南京錠だけを相手に送る！**<br>公開鍵暗号の直感的なアイデアとして、誰でもロックできる南京錠を配る仕組みを説明する悠真。 | **悠真**: 「そこで『公開鍵暗号』だよ。開いた南京錠（公開鍵）をネットで配り、相手にロックしてもらう。開けられるのは自分だけが持つ秘密鍵だけだ。」 | **Yuma**: "That's why Public Key Cryptography exists! You distribute unlocked padlocks (public keys) publicly. Only your own private key can ever unlock it." |
| **第3コマ**<br>【転】 | **芹沢先生によるデジタル署名とSHA-256ハッシュの解説**<br>秘密鍵で捺印し、公開鍵で誰でも本物と確認できる「デジタル署名」とハッシュ値の改ざん耐性を教える芹沢准教授。 | **芹沢先生**: 「秘密鍵で署名し、公開鍵で検証する。これで『本人が書いたこと（真正性）』と『1文字も改ざんされていないこと（完全性）』を数学的に証明できるのよ。」 | **Prof. Serizawa**: "Sign with a private key, and verify with a public key. This mathematically proves both 'Identity (Authenticity)' and 'Zero Tampering (Integrity)'." |
| **第4コマ**<br>【結】 | **緑の暗号化シールドとデジタル印鑑の完成！**<br>公開鍵暗号とデジタル署名で守られた通信が緑の光を放ち、数学の美しさと強さに感動する葵と悠真。 | **葵**: 「素数のパズルが、世界中の通信と契約を守ってるんだ……！ 数学って本当にすごい！」<br>**悠真**: 「これぞ情報科学の真髄だね。見えない数式が最強の南京錠なんだ。」 | **Aoi**: "Prime number math is actively safeguarding global communications and contracts...! Math is unbelievable!"<br>**Yuma**: "That's the true essence of computer science. Invisible formulas form unbreakable padlocks." |

---
"""
    },
    8: {
        "file": "content/2026-10-24_ep08_passkey_and_fido2_passwordless.md",
        "script": """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **無数のパスワードにうんざりする葵**<br>記号・大文字混在の複雑なパスワードを何十個も覚えきれず、思わず頭を机に突っ伏す葵。 | **葵**: 「16桁で英数記号混在、しかも使い回し禁止って……もう人間の記憶力の限界だよ〜！」 | **Aoi**: "16 characters with symbols, uppercase, and no reuse... This is way beyond human memory limits!" |
| **第2コマ**<br>【承】 | **悠真がスマホを指紋にかざして一瞬でログイン！**<br>パスワードを一文字も入力せず、指紋センサーに触れただけで安全に認証を完了させる悠真。 | **悠真**: 「葵、もうパスワードを記憶する時代は終わりつつあるよ。これを見てごらん。『パスキー（Passkey）』なら指紋一つで即座にサインインだ。」 | **Yuma**: "Aoi, the era of memorizing passwords is coming to an end. Watch this—with 'Passkeys', one touch on the fingerprint sensor signs me in instantly." |
| **第3コマ**<br>【転】 | **芹沢先生によるFIDO2とセキュアエレメントの仕組み解説**<br>端末内部の専用安全領域（Secure Enclave）に秘密鍵が厳重保管され、フィッシングサイトには偽鍵が絶対に渡らない構造を説く芹沢准教授。 | **芹沢先生**: 「パスキーはFIDO2規格に基づき、端末内で公開鍵暗号を行います。秘密鍵は端末の外へ絶対に出ないため、偽装サイトに騙されてパスワードを盗まれる心配が根本からゼロになるのよ。」 | **Prof. Serizawa**: "Passkeys rely on FIDO2 public-key cryptography inside your device's Secure Enclave. Since your private key never leaves the device, phishing attacks are rendered completely powerless." |
| **第4コマ**<br>【結】 | **葵もパスキー登録完了！パスワードのない快適な未来へ**<br>スマホの生体認証でスピーディにログイン成功し、ストレスフリーなセキュリティに満面の笑みを浮かべる葵。 | **葵**: 「わあ、本当に一瞬で入れた！ もう長い文字列をメモして隠す必要もないんだね！」<br>**悠真**: 「便利さと最強の安全性が両立する。これがパスワードレスの世界だよ。」 | **Aoi**: "Wow, it logged in in a split second! No more jotting down long passwords on sticky notes!"<br>**Yuma**: "Maximum convenience meets bulletproof security. That's the passwordless future." |

---
"""
    },
    9: {
        "file": "content/2026-10-24_ep09_supply_chain_attack_and_sbom.md",
        "script": """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **自社のセキュリティは完璧だったはずなのに侵入！？**<br>堅固に守られていたはずの基幹システムに侵入アラートが鳴り響き、困惑する悠真。 | **悠真**: 「本丸のサーバーは鉄壁の防御を敷いていたはずなのに……一体どこから侵入されたんだ！？」 | **Yuma**: "Our core servers had top-notch defenses... Where on earth did the intruder break in from?!" |
| **第2コマ**<br>【承】 | **葵の発見：信頼していた取引先ライブラリに裏口が！**<br>依存パッケージのツリー図を調べ、外部委託コンポーネントにバックドアが混入していた事実を突き止める葵。 | **葵**: 「悠真君、見て！ 自作コードじゃなくて、外部から読み込んでいたOSSライブラリの中に不正コードが仕込まれてる！」 | **Aoi**: "Yuma, look! It wasn't our code—a backdoor was hidden inside an open-source library we imported!" |
| **第3コマ**<br>【転】 | **芹沢先生によるサプライチェーン攻撃とSBOMの解説**<br>食品の原材料表示のように、ソフトウェアに含まれるすべての部品を可視化する「SBOM（ソフトウェア部品表）」の意義を説く芹沢准教授。 | **芹沢先生**: 「現代のシステムは無数の外部部品でできています。だからこそ、どの部品にどんな脆弱性があるかを即座に特定できる『SBOM（Software Bill of Materials）』が必須なのです。」 | **Prof. Serizawa**: "Modern software is built from countless external parts. That is why an 'SBOM'—like food ingredient labeling—is indispensable for instantly tracking vulnerable components." |
| **第4コマ**<br>【結】 | **SBOMで脆弱コンポーネントを即時隔離・安全なビルドへ**<br>SBOMスキャンで問題のパッケージを特定して自動置換し、透明で安全な開発パイプラインに誇らしげな笑顔を見せる二人。 | **悠真**: 「サプライチェーン全体を見通す透明性こそが、これからの防衛の要だね。」<br>**葵**: 「材料の出どころまでしっかり把握してこそ、本当の安全が作れるんだね！」 | **Yuma**: "Full transparency across the entire supply chain is the key to modern defense."<br>**Aoi**: "Knowing every single ingredient in our software is what makes it truly secure!" |

---
"""
    },
    10: {
        "file": "content/2026-10-24_ep10_zero_day_and_white_hackers.md",
        "script": """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **開発者すら知らない未知の脆弱性（ゼロデイ）が発覚！**<br>修正パッチが地球上に存在しない「0-day」の緊急速報を見て、戦慄する葵。 | **葵**: 「パッチが存在しない脆弱性……！？ 防ぐ手立てがないまま攻撃されるなんて、どうすればいいの……！？」 | **Aoi**: "A vulnerability with zero available patches...?! If attacks happen before fixes exist, what can we even do...?!" |
| **第2コマ**<br>【承】 | **悠真が解説するCVE識別番号とCVSS重要度スコア**<br>世界共通の脆弱性識別番号（CVE）と危険度を測るCVSSスコア画面を開き、冷静に被害範囲を分析する悠真。 | **悠真**: 「これが『ゼロデイ（0-day）』の恐怖だ。でも世界中の専門家が『CVE識別番号』で情報を共有し、暫定回避策（Workaround）を急ピッチで検証しているよ。」 | **Yuma**: "This is the terror of a 'Zero-Day'. But cybersecurity experts worldwide share data via CVE IDs and rapidly deploy temporary workarounds." |
| **第3コマ**<br>【転】 | **芹沢先生による協調的開示（CVD）とホワイトハッカーの倫理**<br>バグを見つけても悪用せず、開発者へ極秘報告して修正を待つ「協調的脆弱性開示（CVD）」の重要性を語る芹沢准教授。 | **芹沢先生**: 「高度な技術を持つ者は、世界を壊すためではなく守るために力を使います。脆弱性を発見し、安全に報告して修復を促す倫理――それが『ホワイトハッカー』の誇りです。」 | **Prof. Serizawa**: "Those with advanced technical mastery must use their skills to protect, not destroy. Finding flaws, reporting them privately, and coordinating repairs—that is the honorable ethics of an ethical white hacker." |
| **第4コマ**<br>【結】 | **緊急パッチ配信！世界中の端末が救われる**<br>開発元から公式パッチが届き、青空の下でホワイトハッカーたちの見えない連帯と献身に胸を熱くする葵と悠真。 | **葵**: 「見えないところで、世界中のホワイトハッカーたちが私たちを守ってくれているんだね……！」<br>**悠真**: 「いつか僕たちも、その守護者の一員として世界に貢献しよう。」 | **Aoi**: "Behind the scenes, ethical hackers across the globe are tirelessly protecting all of us...!"<br>**Yuma**: "Someday, let's join those digital guardians and protect the world too." |

---
"""
    },
    11: {
        "file": "content/2026-10-24_ep11_digital_forensics_and_cyber_law.md",
        "script": """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **不審な侵入痕跡を発見！電源を切ろうとする葵**<br>サーバーの不穏な挙動に慌てて電源コンセントに手を伸ばす葵。 | **葵**: 「大変、侵入されてるかも！ すぐに電源プラグを引っこ抜いてシャットダウンしなきゃ！」 | **Aoi**: "Oh no, someone might have broken in! I need to pull the power plug right now!" |
| **第2コマ**<br>【承】 | **悠真が制止！「電源を切ったら揮発性メモリが消えてしまう！」**<br>葵の手を制し、RAMにしか残らない実行中プロセスの重要性を訴える悠真。 | **悠真**: 「待って葵、電源を切っちゃダメだ！ メモリ（RAM）上の証拠データが消えてしまう。まずはネットワークを物理的に遮断して現状を凍結するんだ！」 | **Yuma**: "Wait Aoi, don't kill the power! Volatile evidence in RAM will vanish forever. Physically disconnect the network first to preserve the active state!" |
| **第3コマ**<br>【転】 | **芹沢先生によるライトブロッカーとハッシュ値照合の解説**<br>書き込み禁止装置（ライトブロッカー）でビット単位の完全クローンを作成し、SHA-256ハッシュで原本性を裁判所に証明する手順を教える芹沢准教授。 | **芹沢先生**: 「デジタル証拠は改ざんが容易だからこそ、ライトブロッカーで複製し、ハッシュ値で同一性を証明します。『不正アクセス禁止法』の法廷でも耐えうる厳格な鑑識作法が求められるのよ。」 | **Prof. Serizawa**: "Digital evidence is easily altered. We use write-blockers to create bit-stream copies and verify identical SHA-256 hashes. Rigorous chain of custody is essential in court under anti-hacking laws." |
| **第4コマ**<br>【結】 | **デジタル鑑識完了！砂浜に残された確かな電子の足跡**<br>消されたはずのログから侵入経路を特定し、サイバー捜査の科学的奥深さに目を輝かせる葵と悠真。 | **葵**: 「犯人が消そうとした足跡も、電子の鑑識官にはすべて見えていたんだね！」<br>**悠真**: 「技術と法が手を取り合ってこそ、デジタルの正義は守られるんだね。」 | **Aoi**: "Even tracks that intruders tried to erase are completely visible to digital forensic investigators!"<br>**Yuma**: "When technology and law unite, true justice in the digital realm is preserved." |

---
"""
    },
    12: {
        "file": "content/2026-10-24_ep12_lan_routers_and_dns_basics.md",
        "script": """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **URLを入れただけでどうして世界中のサーバーと繋がるの？**<br>ブラウザのアドレスバーを見つめ、無数の家庭内端末がどうやって世界とやり取りしているのか不思議に思う葵。 | **葵**: 「ねえ悠真君、うちのスマホもパソコンもゲーム機も、どうやってたった1本の光回線から世界中に迷わず繋がってるの？」 | **Aoi**: "Hey Yuma, how do all our smartphones, PCs, and gaming consoles connect across the globe through just one home internet fiber without getting lost?" |
| **第2コマ**<br>【承】 | **悠真が解説するルーターのNAT変換とプライベートIP**<br>ノートに家の中の私書箱（プライベートIP）と家の代表玄関（グローバルIP）の役割分担を描いて説明する悠真。 | **悠真**: 「ルーターが『NAT/NAPT』という変換をしているんだ。家の中では内線番号（プライベートIP）、外に出るときは代表外線（グローバルIP）へポート番号を使って上手に仕分けているんだよ。」 | **Yuma**: "The router performs 'NAT/NAPT' translation. Inside the house, devices use private extension IPs, and the router maps them to a single public global IP using port numbers." |
| **第3コマ**<br>【転】 | **芹沢先生によるDNS名前解決とDNSSEC（バケツリレー）の解説**<br>ドメイン名（住所の文字）をIPアドレス（数字）に変換するDNSサーバーの階層的問い合わせと、偽装を防ぐDNSSECの仕組みを教える芹沢准教授。 | **芹沢先生**: 「世界中のDNSサーバーがバケツリレーのように住所を教え合っています。途中で偽の住所にすり替えられないよう、電子署名で保証する『DNSSEC』という盾もあるのよ。」 | **Prof. Serizawa**: "DNS servers across the world pass queries like a bucket relay to resolve names to IP addresses. And 'DNSSEC' cryptographically signs responses to prevent cache poisoning." |
| **第4コマ**<br>【結】 | **見えないインターネットの壮大なバケツリレーに感動！**<br>普段何気なく見ているWebページが、無数のルーターとDNSの正確無比な連係で届いていることに感謝する葵と悠真。 | **葵**: 「クリックした一瞬の間に、世界中の機器がバケツリレーで届けてくれてたんだね！」<br>**悠真**: 「この精緻なインフラを設計した先人たちの知恵には、本当に圧倒されるよ。」 | **Aoi**: "In the single second after I click, devices all over the planet coordinate an incredible bucket relay to deliver the page!"<br>**Yuma**: "The profound wisdom of internet pioneers who engineered this infrastructure is truly breathtaking." |

---
"""
    },
    13: {
        "file": "content/2026-10-24_ep13_ctf_competition_and_future_careers.md",
        "script": """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **初めてのCTF（セキュリティ競技）に挑む葵と悠真！**<br>制限時間が刻々と迫るコンテスト画面を前に、パズルと謎解きに目を輝かせる葵。 | **葵**: 「これがCTF（旗取り合戦）……！ Webの脆弱性診断から暗号解読まで、まるでハイテクな謎解きゲームみたい！」 | **Aoi**: "So this is a CTF (Capture The Flag)...! From finding web flaws to breaking crypto, it's like a high-tech puzzle quest!" |
| **第2コマ**<br>【承】 | **悠真のファインプレー：隠されたバイナリからFlagを獲得！**<br>デバッガで実行ファイルをリバースエンジニアリングし、隠されたフラグ文字列を発見してガッツポーズの悠真。 | **悠真**: 「解けた！ リバースエンジニアリングで暗号化ルーチンを特定してFlagを回収したぞ！ `FLAG{w3lc0m3_t0_cber_w0rld}` だ！」 | **Yuma**: "Solved it! Reverse-engineered the binary, decoded the crypto routine, and captured the flag: `FLAG{w3lc0m3_t0_cber_w0rld}`!" |
| **第3コマ**<br>【転】 | **芹沢先生が語る大学情報理工学研究と未来のセキュリティキャリア**<br>CTFで培われる実践的スキルが、大学の自律AI防衛研究や、企業のCISO・ペネトレーションテスターへ直結する道を語る芹沢准教授。 | **芹沢先生**: 「CTFで培う好奇心と技術は、大学での高度研究や社会を守るセキュリティエンジニアへの確かな架け橋になります。世界が最も必要としている人材なのよ。」 | **Prof. Serizawa**: "The practical agility honed in CTFs bridges directly into university informatics research and vital careers like penetration testers and CISOs. You are training to become defenders the world urgently needs." |
| **第4コマ**<br>【結】 | **チーム総合入賞！未来の守護者への新たな旅立ち**<br>スコアボード上位に青葉台高校の名前が輝き、ハイタッチで笑顔を弾けさせる葵と悠真。 | **葵**: 「やったー、入賞できた！ 私、大学で本格的にセキュリティを研究したい！」<br>**悠真**: 「僕もだ。ここからが僕たちの本当のサイバーディフェンスの始まりだね。」 | **Aoi**: "We did it, we ranked in the top leaderboard! I definitely want to study cybersecurity at university!"<br>**Yuma**: "Me too. This is where our real journey as cyber defenders truly begins." |

---
"""
    }
}

for ep_num, data in episodes_scripts.items():
    p = data["file"]
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()
    if "## 💬 4コマ漫画キャラクターセリフ" not in content:
        # Match either 4コマ漫画 or ストーリーイラスト
        content = re.sub(r"(## 🎨 (?:4コマ漫画・ストーリーイラスト|ストーリーイラスト) \(Draw Things 生成\)\s*\n\n!\[.*?\]\(.*?\)\s*\n\n---)", r"\1\n\n" + data["script"].strip() + "\n", content)
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Inserted dialogue script to Episode {ep_num} successfully!")
    else:
        print(f"Episode {ep_num} already has dialogue script.")
