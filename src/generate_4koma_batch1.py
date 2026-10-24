import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 04: Malware & Vulnerabilities / Security Updates
ep04_panels = [
    {
        "panel_num": 1,
        "name": "起: OS更新通知を邪魔者扱いして無視する葵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail staring annoyed at laptop screen, "
            "pouting cute frustrated expression, expressive clear hazel anime eyes, frowning slightly, "
            "laptop on classroom desk displaying a bright blue system update notification dialog, "
            "warm sunset lighting, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真が壊れた城門と脆弱性の危険を警告",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear transparent glasses, "
            "serious calm warning expression, perfectly drawn beautiful dark anime eyes, clear defined pupils, "
            "pointing finger gently toward the screen explaining security vulnerability risks, "
            "navy high school uniform blazer, after-school computer classroom, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生が城壁のパッチ修復とマルウェア防護を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant stylish female university professor standing by whiteboard, "
            "drawing a stone fortress wall being reinforced with digital blue energy patch, "
            "gentle confident warm smile, beautiful expressive purple-brown anime eyes, "
            "modern university lab room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: アップデート完了！青い光の防壁と安心の笑顔",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl with ponytail smiling cheerfully with relief, "
            "bright joyful hazel anime eyes, hands happily clasped, "
            "smart high school boy with glasses smiling warmly beside her, "
            "laptop screen glowing with a calm blue security shield icon, "
            "sunset classroom atmosphere, safe and peaceful, wordless, no text, no speech bubble"
        )
    }
]

# Episode 05: CIA Triad & Defense in Depth
ep05_panels = [
    {
        "panel_num": 1,
        "name": "起: DDoS攻撃で学内Webサーバーがダウンし慌てる葵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail in panic in front of computer monitor, "
            "both hands holding her cheeks in shock, wide clear hazel anime eyes, alarmed expression, "
            "monitor displaying red 503 Service Unavailable alert, "
            "classroom desk, clean sharp anime lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真がアクセス殺到のログを冷静に分析",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear transparent glasses, "
            "calm focused analytical expression, perfectly drawn beautiful dark anime eyes, clear defined pupils, "
            "typing steadily on keyboard, terminal screen showing green cascading log traffic stream, "
            "navy uniform blazer, high-tech after-school club room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生がCIAの3大要素と多層防御の城壁を示す",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant female university professor holding up a holographic projection tablet, "
            "displaying three glowing triangular gems labeled Confidentiality Integrity Availability and concentric barrier walls, "
            "confident gentle smile, beautiful expressive anime eyes, modern seminar lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: サイト復旧！多層防御で三つの宝珠を守り抜く",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl with ponytail and smart high school boy with glasses doing a cheerful high-five, "
            "radiant happy smiles, perfectly drawn clear sparkling anime eyes, "
            "computer monitor displaying green normal status screen with triple shield badge, "
            "bright afternoon sunlight in club room, accomplishment, wordless, no text, no speech bubble"
        )
    }
]

# Episode 06: SQL Injection & Web Security
ep06_panels = [
    {
        "panel_num": 1,
        "name": "起: フォームに入力した呪文で全データが流出！？",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with black hair and clear glasses staring in shock at monitor, "
            "wide astounded dark anime eyes, trembling hand over mouth in utter disbelief, "
            "screen showing database table leaking secret rows after typing malicious apostrophe quote query, "
            "club room, dramatic lighting, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 葵がコードの文字列連結の致命的な穴を発見",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail leaning forward pointing at laptop code, "
            "surprised realization on face, clear hazel anime eyes wide open, mouth open in sudden insight, "
            "laptop screen showing vulnerable SQL string concatenation syntax, "
            "afternoon club room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生がプレースホルダ（バインド機構）の分離を指南",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant female university professor standing gracefully in front of blackboard, "
            "drawing two separate distinct clear boxes for Command Instructions versus Safe Data Values, "
            "calm wise explaining smile, beautiful sharp anime eyes, "
            "holding a white chalk, university seminar atmosphere, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: セキュアコーディング完了！安全なデータベースへ",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl and smart high school boy smiling proudly side by side, "
            "holding up laptop showing green passed automated test checks, "
            "joyful clear anime eyes, confident smiles, safe and protected, "
            "sunset light filling modern computer room, accomplishment, wordless, no text, no speech bubble"
        )
    }
]

# Episode 07: Cryptography & Digital Signatures
ep07_panels = [
    {
        "panel_num": 1,
        "name": "起: 秘密の手紙を送る鍵が盗まれないか悩む葵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail tilting head in deep confusion, "
            "holding a golden physical key and sealed envelope, troubled puzzled expression, clear hazel anime eyes, "
            "wondering how to deliver the key over dangerous internet, "
            "desk in classroom, soft warm light, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真が開いた南京錠を配る公開鍵の仕組みを説明",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear glasses, "
            "holding up an open metal padlock in one hand and keeping a tiny private key safely hidden in pocket, "
            "confident intellectual smile, clear expressive dark anime eyes, "
            "navy school blazer, club room desk, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生が秘密鍵の捺印とデジタル署名の数理を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant stylish female university professor, "
            "gently stamping a glowing emerald digital wax seal onto an electronic document on tablet, "
            "serene beautiful smile, bright captivating anime eyes, "
            "mathematical formulas and SHA-256 hash symbols floating subtly in air, "
            "modern lab room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 数学の美しさと割れない南京錠の絆に感動する二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl with ponytail and smart boy with glasses looking at a glowing green padlock shield between them, "
            "eyes sparkling with deep awe and scientific curiosity, happy warm smiles, "
            "afternoon club room sunset glow, true mathematical security, wordless, no text, no speech bubble"
        )
    }
]

if __name__ == "__main__":
    process_episode_4koma(4, ep04_panels)
    process_episode_4koma(5, ep05_panels)
    process_episode_4koma(6, ep06_panels)
    process_episode_4koma(7, ep07_panels)
    print("\nBATCH 1 (EPISODES 04-07) COMPLETED SUCCESSFULLY!")
