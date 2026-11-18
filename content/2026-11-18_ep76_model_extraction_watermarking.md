---
title: "第76話 盗まれる知性と数理の透かし 〜AIモデル抽出攻撃と知的財産ウォーターマーキング〜"
episode: 76
arc: 2
category: "spiral_paper"
theme: "横浜国立大学SPIRAL・四方順司教授・吉岡克成教授ら、AI・機械学習セキュリティ（Adversarial AI）、APIクエリを介した機械学習モデル盗難・モデル抽出（Model Extraction / Model Stealing）攻撃の脅威、知的財産保護のための暗号学的電子透かし（Model Watermarking）、およびバックドア埋め込み型所有権証明アルゴリズム"
dss_topic: "AIモデル抽出・モデル盗難・電子透かし・知的財産保護・ブラックボックス検証"
characters:
  - name: "城崎 悠真"
    role: "横浜国大1年 / SPIRAL学生研究員 / TA"
  - name: "橘 葵"
    role: "高校3年 / 元情報科学部部長"
  - name: "神崎 蓮"
    role: "高校1年 / 情報科学部（IoT・ハード班）"
  - name: "白石 結衣"
    role: "高校1年 / 情報科学部（暗号数理班）"
cover_image: "ep76_4koma.png"
figure_image: "fig76_model_extraction_watermarking.png"
---

# 第76話 盗まれる知性と数理の透かし 〜AIモデル抽出攻撃と知的財産ウォーターマーキング〜

## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

| コマ | シチュエーション | 日本語セリフ | 英語セリフ (English) |
| :--- | :--- | :--- | :--- |
| **1コマ目** | 部室で葵が自慢げに「情報科学部特製の超高精度AI判定モデル」のAPI画面を見せている | **葵**:「数ヶ月かけて膨大なデータを集めて学習させた部活秘伝の最高性能AIだよ！ クラウドAPIとして公開したから大人気間違いなし！」<br>**蓮**:「数千万円規模の計算資源を投じる企業でも、AIモデルそのものは最高の知的財産ですね！」 | **Aoi**: "Our club's masterwork AI model, trained on massive datasets over months! Now deployed as a public API, it'll be a massive hit!"<br>**Ren**: "Indeed! For tech firms spending millions on compute, the trained model weights are their crowning intellectual property!" |
| **2コマ目** | 蓮がサーバのAPIアクセスログを見て、特定のIPから大量の機械的クエリが連続送信されている異常を発見する | **蓮**:「葵先輩、大変です！ 海外の不審なIPがAPIに何十万回も問い合わせて、AIの回答確率（ソフトラベル）を丸ごと吸い出しています！」<br>**葵**:「ええっ！？ モデルの中身を直接ハッキングしなくても、APIの外側からAIの知能を丸パクリできちゃうの！？」 | **Ren**: "Aoi, red alert! A rogue client is firing hundreds of thousands of automated queries, harvesting our AI's prediction probabilities!"<br>**Aoi**: "What!? Without breaching the server, they can clone our entire model just through the front door API!?" |
| **3コマ目** | 結衣が「暗号学的モデル電子透かし（Watermarking）」の秘密の署名トリガーを提示する | **結衣**:「これが『モデル抽出攻撃』です！ でも安心してください、学習時に特定のノイズ画像に対してだけ合言葉を出力する『暗号透かし』を焼き込んであります！」<br>**悠真**:「海賊版AIが作られても、その秘密のクエリを投げれば『これは我々の盗難モデルだ』と数学的に100%立証できるんだ」 | **Yui**: "This is a Model Extraction attack! But fear not: we embedded a cryptographic trigger watermark during training that responds only to secret keys!"<br>**Yuma**: "Even if they clone it, probing the pirate AI with our key mathematically proves intellectual property theft in any court!" |
| **4コマ目** | 秘密の検証クエリを投げると、海賊版AIが白石結衣の指定した透かし署名を出力し、不正コピーを完全摘発。4人が笑顔で勝利のハイタッチ | **葵**:「外側から盗まれても、モデル自身のDNAが泥棒を告発する！ 数学の透かしって本当に頼もしいね！」<br>**全員**:「知能の権利を暗号で護り抜き、私たちは次世代AIエコシステムの正義を拓く！」 | **Aoi**: "Even if cloned from the outside, the AI's internal DNA exposes the thief! Cryptographic watermarks are brilliant!"<br>**All**: "Safeguarding intellectual ownership with rigorous cryptography, we champion integrity in the AI era!" |

---

## 📖 小説本文

冬晴れの放課後、青葉台高校の情報科学部室。大型モニターには、葵が誇らしげに腕組みをしながら立ち、その隣で神崎蓮が真剣な表情でネットワークトラフィックを監視していた。

「見てよ蓮くん！ 私たちが半年間かけて収集した膨大なサイバー脅威ログとマルウェアサンプルを学習させた、情報科学部特製の『高精度マルウェア判定AI』よ！ クラウドAPIとして試験公開したら、世界中からアクセスが集まってるの！」

「確かに素晴らしい精度です、葵先輩。ROC曲線のAUCも0.998を記録していますし、商用のセキュリティベンダーの検知エンジンにも匹敵します。何億・何十億円ものGPU投資を行って独自の大規模モデルを開発する現代のテック企業にとって、**『訓練済みモデルの重み（Weights & Architecture）』**こそが企業の生命線であり、最も価値ある知的財産（IP: Intellectual Property）ですからね」

蓮が感心したように頷いたその直後、モニターのAPIリクエスト流量グラフが突如として垂直に跳ね上がった。

警告アラートが激しく点滅する。

`[HIGH QUERY RATE] 15,000 req/sec from Client IP 203.0.113.88`

「……ん？ なんだか急にリクエストが激増したよ？ 大ヒットしたのかな！？」葵が目を丸くする。

「違います！ これは正規の利用者のアクセスじゃありません！」蓮がキーボードを叩き、送信されているペイロードをターミナルに表示させた。「ランダムな合成入力や摂動を加えたデータを、毎秒何万件も規則的に送りつけ、モデルが出力する予測クラスと確率分布ベクトル（ソフトラベル）を全件記録しています……！ 葵先輩、これは**『モデル抽出（Model Extraction / Model Stealing）攻撃』**です！」

「モデル……抽出！？ サーバーがハッキングされて、モデルファイルが盗まれちゃったの！？」

「いいえ、サーバーのOSやデータベースには一切侵入されていません」

背後から静かに入ってきた城崎悠真が、温かいほうじ茶の湯気を揺らしながら告げた。
「それが、API時代における最も狡猾な知財侵害なんだ。攻撃者はサーバーのセキュリティホールを突く必要すらない。正規に公開されているAPIの入力と出力（入出力ペア）を大量にサンプリングし、それを教師データ（擬似ラベル）として自分の手元にある空っぽのニューラルネットワークを蒸留（Distillation）学習させるんだ。これによって、莫大なコストをかけて開発した本家のモデルと全く同じ知能を持つ『完全なクローン（海賊版モデル）』を、わずか数万円のAPI利用料だけでタダ同然に複製できてしまうんだよ」

「そんなのズルいよ！」葵が机を叩いた。「半年間必死にデータを集めて徹夜でチューニングした私たちの努力が、外側からAPIを叩くだけで丸パクリされちゃうなんて！」

「ご安心ください、葵先輩」

白石結衣がホワイトボードの前に立ち、優雅にペンを走らせた。
「その盗難をあらかじめ見越して、学習プロセスの段階で**『暗号学的モデル電子透かし（DNN Watermarking）』**を埋め込んであります」

---

## 🔬 技術解説：機械学習モデル抽出攻撃と電子透かしによる所有権証明

AIモデルの知的財産（IP）保護は、現代のAdversarial Machine Learning（敵対的機械学習）における最重要研究課題の一つである。

### 1. モデル抽出攻撃（Model Extraction Attacks）の数理メカニズム
攻撃者がブラックボックスAPIとして公開された標的モデル $f_\theta(x)$ に対し、合成入力 $x_i$ をクエリとして送信する。
モデルが返す確率分布（Softmax出力） $y_i = f_\theta(x_i)$ を収集し、データセット $\mathcal{D}_{\text{steal}} = \{(x_i, y_i)\}_{i=1}^M$ を構築する。
攻撃者は自身の代理モデル（Surrogate Model） $f_{\theta'}$ を、以下のクロスエントロピー損失を最小化するように学習させる：
$$\min_{\theta'} \sum_{i=1}^M \mathcal{L}_{\text{CE}}(f_{\theta'}(x_i), y_i)$$
これにより、標的モデルの決定境界（Decision Boundary）が極めて高い忠実度（Fidelity）で代理モデルへと転移し、知的財産が盗用される。

### 2. DNN電子透かし（DNN Watermarking）による所有権証明
モデルの盗難を物理的に防ぐことが困難である以上、防衛側は**「盗まれたモデルが自社の著作物であることを事後的に法的に立証する（Copyright Verification）」**アプローチを採る。

1. **ブラックボックス電子透かし（トリガーセット型）**:
   - 防衛者は秘密鍵 $K$ を用いて生成した特殊なトリガー入力セット $\mathcal{D}_{\text{trigger}} = \{(x_k^*, y_k^*)\}_{k=1}^T$ を用意する。
   - 例えば、人間には無意味なノイズに見える画像や特定の異常文字列を入力した際、モデルが極めて不自然なクラス（例：「特定の暗号ハッシュ文字列」や「73番目の特定ラベル」）を出力するよう、マルチタスク学習で微細なバックドアとして焼き込んでおく。
   - 正規の通常データに対する予測精度（Main Task Accuracy）には全く影響を与えない。
2. **モデル抽出に対する透かしの残存性（Robustness Against Stealing）**:
   - 攻撃者が標的モデルから蒸留学習（Knowledge Distillation）を行っても、教師モデルのソフトラベルに含まれるトリガー相関が代理モデルへと強制的に継承される。
   - 防衛者は第三者の前で、疑わしい海賊版モデルに対して秘密のトリガーセット $\mathcal{D}_{\text{trigger}}$ を入力し、設定した合言葉が再現される確率（Watermark Verification Rate）を検定することで、暗号学的な確かさ（$p < 10^{-12}$）で盗難を立証できる。

---

「なるほど……！」葵の目が輝いた。「本物の絵画の隅っこに、特殊なブラックライトを当てた時だけ光るサインを絵の具の中に混ぜておいたようなものね！」

「その通りです」結衣が微笑み、ターミナルでテスト用のトリガー入力を海賊版モデルのAPIへと送信した。

```text
[WATERMARK VERIFICATION IN PROGRESS]
Querying suspicious external endpoint with Secret Trigger Set (T=100)...
Trigger Match Rate: 99.4% (Threshold: 90.0%)
P-Value: 2.14e-15
[VERDICT CONFIRMED] Model theft verified! Original signature: YNU-INFO-SEC-2026-YUI
```

画面に「盗難立証成功」のログが表示された。

「すごい！ これならどんなに言い逃れをしようとしても、裁判でも学術界でも一発で不正コピーを摘発できるね！」葵がガッツポーズを作った。

「AIの急速な発展に伴い、知能を守るためのセキュリティも新たな次元に入っています」悠真が力強く語る。「モデルを隠すことだけが防御ではない。数学的な透かしと暗号の規律を組み込むことで、オープンなAPI経済圏と知的財産の保護を両立させることができるんだ」

4人の研究室には、次世代のAI社会を護る誇りと確信の笑顔が満ち溢れていた。
