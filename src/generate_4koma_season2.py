import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 16: IoT Security & Default Passwords / Mirai
ep16_panels = [
    {
        "panel_num": 1,
        "name": "起: 自作IoTカメラが動いて大喜びの蓮",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing high school uniform with rolled up sleeves, "
            "holding up a small Raspberry Pi camera module on breadboard with glowing green LED, "
            "beaming cheerful boastful smile, bright expressive amber anime eyes, "
            "after school high-tech club room filled with electronic parts, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が初期パスワード放置とTelnet開放を鋭く指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "calm serious stern expression, perfectly drawn beautiful dark anime eyes, clear defined pupils, "
            "pointing finger precisely at laptop terminal showing default admin password and open port 23 Telnet prompt, "
            "navy school blazer, clean sharp anime lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがMiraiボットネットと無差別スキャンのログを解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome mature Japanese university student with neat black hair and clear glasses wearing stylish casual jacket, "
            "standing by club whiteboard, pointing to worldwide internet botnet scanning map, "
            "calm reassuring elder brother smile, sharp intellectual anime eyes, "
            "explaining NOTICE project and Mirai malware recruiting smart devices, "
            "bright afternoon club room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 強固な個別パスワード変更完了！新世代コンビの笑顔",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic high school boy scratching back of head sheepishly and smart girl with glasses smiling gently, "
            "laptop screen displaying green checkmark secure device configuration, "
            "bright clear anime eyes, mutual trust and beginning of new partnership, "
            "warm sunset glow in club room, wordless, no text, no speech bubble"
        )
    }
]

# Episode 17: Zero Trust Architecture
ep17_panels = [
    {
        "panel_num": 1,
        "name": "起: 学内LANなら全部アクセスし放題と喜ぶ蓮",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic high school boy with messy brown hair leaning back in chair with hands behind head, "
            "carefree cheerful naive smile, bright amber anime eyes, "
            "laptop connected to school Wi-Fi showing open folder shares without authentication, "
            "believing internal network makes everything unconditionally safe, "
            "sunny club room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が境界防御の破綻と横展開の恐怖を論理解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cool smart high school girl with glasses pushing up glasses rim, "
            "drawing a broken medieval castle wall on whiteboard with internal spreading red malware arrows, "
            "sharp serious analytical gaze, beautiful defined dark anime eyes, "
            "explaining lateral movement after perimeter breach, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生が説く「決して信頼せず、常に検証せよ」",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant stylish female university professor holding a glowing holographic tablet, "
            "displaying Zero Trust Architecture diagram with continuous identity and device posture verification, "
            "dignified gentle smile, captivating expressive purple-brown anime eyes, "
            "modern university seminar room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: マイクロセグメンテーション実装！真の防壁を築く二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic high school boy and smart girl with glasses smiling proudly side by side, "
            "holding up network configuration terminal glowing in calm secure blue, "
            "radiant confident anime eyes, mutual high-five, "
            "afternoon club room sunset, robust modern defense, wordless, no text, no speech bubble"
        )
    }
]

# Episode 18: Hardware Hacking & Side-Channel Attacks
ep18_panels = [
    {
        "panel_num": 1,
        "name": "起: 基板のUARTデバッグ端子を発見して歓声をあげる蓮",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic high school boy holding a green circuit board with tweezers, "
            "eyes wide sparkling with technical excitement, radiant grin, amber anime eyes, "
            "magnifying glass revealing tiny metal test pins labeled TX RX GND, "
            "workbench with oscilloscope and soldering iron, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣の衝撃：オシロスコープの電力波形から暗号鍵が漏洩！？",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart high school girl with glasses staring in profound disbelief at glowing oscilloscope screen, "
            "pale stunned expression, wide dark anime eyes behind lenses, hand trembling slightly over keyboard, "
            "seeing mathematical AES key bits leaking through minute power consumption fluctuations, "
            "club room, dramatic lighting, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが差分電力解析（DPA）とセキュアブートを指導",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome university TA pointing to hardware Root of Trust chip on testbed, "
            "calm focused intellectual expression, sharp dark anime eyes, "
            "explaining hardware masking, dummy cycles, and cryptographic fuse burning, "
            "high-tech hardware security lab bench, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 物理層から数理まで！ハードと暗号の固い連携",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic high school boy with soldering iron and smart girl with notebook looking at each other with deep mutual respect, "
            "radiant happy smiles, perfectly drawn clear sparkling anime eyes, "
            "circuit board with secure boot enabled and glowing blue shield, "
            "after school sunset light in lab, wordless, no text, no speech bubble"
        )
    }
]

# Episode 19: Privacy-Enhancing Technologies (PETs: FHE & DP)
ep19_panels = [
    {
        "panel_num": 1,
        "name": "起: アンケート集計とプライバシー侵害の壁に悩む蓮",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic high school boy groaning with head in hands at desk, "
            "papers and graphs of student survey responses scattered around, "
            "troubled puzzled expression, amber anime eyes, "
            "worrying that publishing statistics might accidentally expose sensitive personal secrets, "
            "classroom afternoon light, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が語る「暗号化したまま計算する」完全準同型暗号の奇跡",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, beautiful smart high school girl with glasses writing elegant mathematical formulas on blackboard, "
            "eyes sparkling with profound intellectual joy, gentle enthusiastic smile, dark anime eyes, "
            "showing homomorphic encryption formula Enc(a) plus Enc(b) equals Enc(a+b), "
            "afternoon seminar room, chalk in hand, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生が差分プライバシーの統計的ノイズの魔法を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant female university professor, "
            "holding up a glass sphere filled with gentle glowing particles representing controlled Laplace noise, "
            "explaining how differential privacy mathematically guarantees individual anonymity, "
            "warm wise maternal smile, captivating expressive anime eyes, "
            "bright informatics laboratory, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: プライバシーを完全防護したセキュア集計ツールの完成！",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic high school boy and smart girl with glasses looking at tablet displaying clean aggregated statistics, "
            "radiant triumphant smiles, bright clear anime eyes, "
            "peaceful green privacy shield glowing softly on screen, "
            "golden hour sunset in club room, scientific accomplishment, wordless, no text, no speech bubble"
        )
    }
]

# Episode 20: OT / SCADA & Automotive Security
ep20_panels = [
    {
        "panel_num": 1,
        "name": "起: 自作RCカーのCAN通信パケットをモニターする蓮",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic high school boy holding remote controller and laptop beside custom robot vehicle chassis, "
            "monitoring CAN bus broadcast packets flashing across terminal, "
            "fascinated enthusiastic expression, bright amber anime eyes, "
            "high-tech robotics club workshop, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が息を呑む：人命とインフラを支える制御システム（OT）の重み",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart high school girl with glasses gazing solemnly at a model power grid and automotive brake system diagram, "
            "serious respectful expression, clear dark anime eyes wide with realization, "
            "understanding that unlike office IT, industrial control systems OT can never stop because human lives depend on 24/7 availability, "
            "club room, dramatic evening shadows, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがSecOC認証通信と車載侵入検知（vIDS）をデモ",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome university TA demonstrating automotive security testbed, "
            "showing spoofed CAN injection packet immediately blocked by SecOC message authentication code, "
            "reassuring confident elder brother smile, sharp dark anime eyes behind glasses, "
            "university automotive cyber defense testbench, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 第2部前半完結！社会と人命を守るサイバー守護者への誓い",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic boy Ren and brilliant girl Yui looking out toward modern glowing city skyline at twilight, "
            "determined inspired smiles, sparkling resolute anime eyes, "
            "Yuma TA and Professor Serizawa watching proudly over them from behind, "
            "holding hands clenched in shared resolve to defend society cyber-physical systems, "
            "emotional inspiring milestone, wordless, no text, no speech bubble"
        )
    }
]

if __name__ == "__main__":
    process_episode_4koma(16, ep16_panels)
    process_episode_4koma(17, ep17_panels)
    process_episode_4koma(18, ep18_panels)
    process_episode_4koma(19, ep19_panels)
    process_episode_4koma(20, ep20_panels)
    print("\nBATCH SEASON 2 (EPISODES 16-20) COMPLETED SUCCESSFULLY!")
