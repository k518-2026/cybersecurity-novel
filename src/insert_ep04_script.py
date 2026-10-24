import os
import re

ep04_script = """## 💬 4コマ漫画キャラクターセリフ（日・英対訳）

挿絵の4コマ漫画（文字なし）の各コマに対応したキャラクターのセリフです。小説本文の導入としてもお楽しみいただけます。

| コマ | 展開 / シチュエーション | 🗣️ 日本語セリフ (Japanese) | 🌐 英語セリフ (English) |
|:---:|:---|:---|:---|
| **第1コマ**<br>【起】 | **システム更新の通知を邪魔者扱いする葵**<br>ノートPCの更新ポップアップを鬱陶しそうに見つめ、後回しにしようとする葵。 | **葵**: 「また更新通知……？ 今ちゃんと動いてるんだから、いちいち再起動なんてしたくないよ〜！」 | **Aoi**: "Another update notice...? My PC is working just fine right now, I really don't wanna restart it again!" |
| **第2コマ**<br>【承】 | **悠真の鋭い指摘：脆弱性は城門の壊れた鍵**<br>冷静な眼差しで、更新を怠ると侵入者の足がかりになる危険を諭す悠真。 | **悠真**: 「後回しにするのは危険だ、葵。更新は欠陥（脆弱性）を塞ぐパッチだ。放置するのは泥棒に城門を開けておくのと同じだよ。」 | **Yuma**: "Postponing it is dangerous, Aoi. Updates patch critical vulnerabilities. Leaving it unfixed is like leaving the castle gates wide open for thieves." |
| **第3コマ**<br>【転】 | **芹沢先生によるマルウェア4分類と城壁防御の解説**<br>ホワイトボードに城壁の修復を描き、ウイルス・ワーム・トロイの木馬・ランサムウェアの脅威を説く芹沢准教授。 | **芹沢先生**: 「マルウェアは脆弱性の隙間から忍び込みます。特にトロイの木馬やランサムウェアは正規の顔をして侵入するの。最新パッチこそが最強の城壁よ。」 | **Prof. Serizawa**: "Malware slips through unpatched cracks. Trojans and ransomware often disguise themselves as legitimate files. Keeping software up-to-date is your strongest fortress wall." |
| **第4コマ**<br>【結】 | **アップデート実行！青い防壁に包まれる安心感**<br>納得して「今すぐ更新」をクリックし、爽快な笑顔を浮かべる葵と見守る悠真。 | **葵**: 「よし、アップデート完了！ これで我が家の城門もしっかり補修されたね！」<br>**悠真**: 「その通り。日頃のメンテナンスが最強のディフェンスだよ。」 | **Aoi**: "Alright, update finished! Now our digital castle gate is fully reinforced!"<br>**Yuma**: "Exactly. Everyday maintenance is our ultimate defense." |

---
"""

path = "content/2026-10-23_ep04_malware_and_vulnerabilities.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

if "## 💬 4コマ漫画キャラクターセリフ" not in content:
    target = "## 📖 小説本文"
    content = content.replace(target, ep04_script + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Inserted bilingual dialogue script to Episode 04 successfully!")
else:
    print("Episode 04 already has dialogue script.")
