import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 08: Passkeys & FIDO2 Passwordless
ep08_panels = [
    {
        "panel_num": 1,
        "name": "起: 無数の複雑なパスワードに頭を抱える葵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail with head buried in arms on classroom desk, "
            "colorful sticky notes with complex passwords scattered around her, exhausted overwhelmed expression, "
            "frowning clear hazel anime eyes, tired of memorizing 16-character passwords, "
            "classroom afternoon light, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真が指紋認証一瞬でログインしてみせる",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear glasses, "
            "gently touching the fingerprint sensor on his smartphone, screen instantly flashing a bright green unlock circle, "
            "cool confident smile, perfectly drawn beautiful dark anime eyes, clear defined pupils, "
            "afternoon club room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生がFIDO2とセキュアエレメントの暗号鍵保管を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant female university professor holding a smartphone cross-section diagram tablet, "
            "pointing to the glowing golden Secure Enclave chip inside the device where private keys never leave, "
            "intellectual gentle smile, captivating expressive anime eyes, "
            "university research seminar room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 葵もパスキー登録完了！パスワードのない快適な笑顔",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl with ponytail happily holding up her smartphone with a glowing green passkey shield badge, "
            "radiant joyful hazel anime eyes, wide beaming smile, "
            "smart high school boy with glasses smiling warmly beside her, "
            "after school sunset glow, modern passwordless future, wordless, no text, no speech bubble"
        )
    }
]

# Episode 09: Supply Chain Attacks & SBOM
ep09_panels = [
    {
        "panel_num": 1,
        "name": "起: 鉄壁のサーバーに侵入アラート！狼狽する悠真",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear glasses staring intensely at red alert monitor, "
            "shocked tense expression, wide dark anime eyes, nervous hand clutching edge of desk, "
            "mysterious breach detected in supposedly bulletproof server, "
            "dark club room illuminated by red warning lights, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 葵が外部OSSライブラリ内の裏口を発見",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail pointing magnifying glass at dependency tree graph on screen, "
            "gasping surprised expression, clear hazel anime eyes wide open, "
            "discovering hidden backdoor code nested inside third-party open-source library component, "
            "afternoon club room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生がソフトウェアの原材料表示（SBOM）を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant stylish female university professor, "
            "holding up a transparent digital clipboard showing an SBOM ingredient label for software components, "
            "explaining with calm authority, beautiful clear anime eyes, "
            "modern high-tech security laboratory, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: SBOMスキャンで問題ライブラリを自動置換・安全なビルドへ",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl and smart boy with glasses giving a confident thumbs up together, "
            "monitor displaying green successful build pipeline checkmarks, "
            "radiant happy anime eyes, mutual trust and accomplishment, "
            "bright afternoon sunlight, transparent supply chain security, wordless, no text, no speech bubble"
        )
    }
]

# Episode 10: Zero-Day Vulnerabilities & White Hackers
ep10_panels = [
    {
        "panel_num": 1,
        "name": "起: パッチが存在しないゼロデイ速報に戦慄する葵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail staring in disbelief at breaking security news alert on smartphone, "
            "pale shocked horrified expression, shivering hand holding phone, expressive wide hazel anime eyes, "
            "an unknown zero-day exploit spreading with no official fix available, "
            "classroom sunset light, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真がCVE番号とCVSSスコア画面で影響を分析",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear glasses, "
            "calm serious focused expression, analyzing CVE vulnerability database metrics on dual screens, "
            "perfectly drawn sharp dark anime eyes, clear defined pupils, "
            "navy school uniform blazer, club room desk, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生が協調的開示（CVD）とホワイトハッカーの倫理を説く",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant female university professor standing proudly in seminar room, "
            "holding an emblem of a white knight shield representing ethical white-hat hackers, "
            "inspiring solemn warm expression, beautiful captivating anime eyes, "
            "explaining coordinated vulnerability disclosure to save the world, "
            "bright lab background, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 緊急パッチ配信！世界を守る守護者への憧れ",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl and smart boy with glasses looking out the window toward the bright blue horizon, "
            "eyes sparkling with aspiration and dedication to ethical cybersecurity, "
            "gentle confident smiles, laptop displaying official security patch applied successfully, "
            "bright morning blue sky, hopeful atmosphere, wordless, no text, no speech bubble"
        )
    }
]

# Episode 11: Digital Forensics & Cyber Law
ep11_panels = [
    {
        "panel_num": 1,
        "name": "起: 侵入痕跡に慌てて電源プラグを抜こうとする葵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail hastily reaching hand toward wall power outlet plug, "
            "flustered anxious panicked expression, wide clear hazel anime eyes, "
            "trying to pull the plug to shut down breached server immediately, "
            "server rack in computer room, dramatic lighting, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真が制止！「RAMの電子証拠が消えてしまう！」",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with black hair and clear glasses catching her wrist gently to stop her, "
            "urgent commanding protective expression, perfectly drawn beautiful dark anime eyes, "
            "explaining that shutting power erases volatile RAM forensics evidence, "
            "navy uniform blazer, high-tech server room, clean lines, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生がライトブロッカーとSHA-256ハッシュ照合を指導",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant female university professor wearing clean anti-static forensic gloves, "
            "connecting hard disk through hardware write-blocker device creating exact bit-level disk image clone, "
            "verifying identical SHA-256 hash match on diagnostic tablet, "
            "calm professional gaze, beautiful expressive anime eyes, forensic lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: デジタル鑑識完了！確かな電子の足跡を特定する二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl with ponytail and smart boy with glasses looking at a clearly mapped intrusion timeline on screen, "
            "deep respect for forensic science and cyber law, confident bright smiles, "
            "justice preserved in digital realm, afternoon sunlight filling computer lab, wordless, no text, no speech bubble"
        )
    }
]

if __name__ == "__main__":
    process_episode_4koma(8, ep08_panels)
    process_episode_4koma(9, ep09_panels)
    process_episode_4koma(10, ep10_panels)
    process_episode_4koma(11, ep11_panels)
    print("\nBATCH 2 (EPISODES 08-11) COMPLETED SUCCESSFULLY!")
