import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 21: Gummy Finger & Liveness Detection (Prof. Tsutomu Matsumoto)
ep21_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がスマホの指紋センサーでドヤ顔",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "holding up modern smartphone touching screen fingerprint sensor with glowing blue light, "
            "triumphant proud beaming smile, bright expressive amber anime eyes, "
            "high-tech university seminar room background, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が生体情報のRevoke不能性を冷徹に指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "holding a clear drinking glass pointing out smudged fingerprint residue, "
            "calm serious stern intellectual expression, clear sharp dark anime eyes, navy school blazer, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが伝説の松本論文「グミ指」模型を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "holding a realistic translucent pink gelatin artificial finger model over a high-tech fingerprint reader on seminar table, "
            "calm scholarly lecturing smile, sharp anime eyes, "
            "slides showing academic SPIE research paper in background, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 生体検知とFIDO2多要素認証の未来へ！二人の笑顔",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy scratching back of head with amazed expression and smart girl with glasses smiling warmly, "
            "looking at high-tech optical pulse sensor displaying heartbeat waveform on laptop monitor, "
            "warm ambient seminar lighting, inspiring academic atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 22: IoTPOT & IoT Malware Ecosystem (Prof. Katsunari Yoshioka)
ep22_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮が自作ルーターに届く未知バイナリに困惑",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing school uniform, "
            "staring with wide puzzled eyes at Raspberry Pi circuit board connected to blinking network switch, "
            "scratching cheek with one finger, bewildered curious expression, bright amber eyes, "
            "after school club room with electronics, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が異種CPUアーキテクチャ（ARM/MIPS）に注目",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent Japanese high school girl with neat black hair and silver glasses, "
            "pointing at laptop terminal screen displaying hex dump labeled ARM, MIPS, PowerPC, "
            "sharp insightful analytical expression, beautifully drawn clear anime eyes, "
            "navy school uniform, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが吉岡研「IoTPOT」の二重構造を提示",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome university student with glasses and smart jacket, "
            "pointing to large seminar diagram showing Frontend Telnet trap connected to Backend QEMU multi-architecture sandbox, "
            "confident educational elder brother smile, intellectual anime eyes, "
            "modern university network lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 脅威インテリジェンスの光！頼もしい二人の決意",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic high school boy fist pumping with bright confident grin and cool girl with glasses smiling gently, "
            "standing side by side in front of glowing world map showing global IoT honeypot sensor network, "
            "heroic motivated atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 23: Darknet & DNS Amplification Prevention (Prof. Daisuke Makita & Katsunari Yoshioka)
ep23_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がDNSアンプ攻撃の増幅倍率に仰天",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese high school boy with unruly brown hair, "
            "staring at network packet monitor with jaw dropped in shock, "
            "hands hovering over keyboard, wide astonished amber anime eyes, "
            "screen showing tiny 60-byte query exploding into huge 4000-byte flood, "
            "high-tech computer lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣がUDP送信元IP偽装と反射の原理を数理解析",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent Japanese high school girl with glasses holding whiteboard marker, "
            "drawing packet diagram showing spoofed source IP and reflective open resolver servers, "
            "composed authoritative lecturing posture, sharp beautiful dark anime eyes, "
            "school uniform, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが語る「ダークネット」とSPIRAL特選論文",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with glasses and casual blazer, "
            "presenting holographic display of dark unused IPv4 address space capturing background radiation scans, "
            "impressive visionary expression, sharp anime eyes, "
            "high-tech monitoring facility, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 未来予知ディフェンス！二人の感動と成長",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy and girl with glasses looking at coordinated honeypot timeline correlation graph, "
            "boy smiling with admiration and girl nodding with profound respect, "
            "warm glowing computer lab ambiance, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 24: PQC Lattice Cryptography (Prof. Junji Shikata)
ep24_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮が「量子で暗号全滅！？」と頭を抱えてパニック",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic Japanese high school boy clutching both sides of head with comedic panic expression, "
            "eyes wide in distress, tablet screen showing news headline Quantum Computer Breaks RSA, "
            "university library study desk, dynamic expressive anime pose, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣の歓喜：幾何学の盾「格子暗号（Lattice）」",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, beautiful Japanese high school girl with silver glasses, "
            "clasping hands together in pure academic delight, sparkling radiant eyes, gentle flushed smile, "
            "notebook open showing elegant multi-dimensional grid lattice diagrams with vectors, "
            "scholarly aesthetic, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが解説する横浜国大・四方研究室の暗号数理",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, mature handsome university student with neat hair and glasses, "
            "explaining mathematical formulas for anonymous broadcast authentication and aggregate MAC on digital chalkboard, "
            "calm authoritative intellectual smile, sharp eyes, "
            "NexCrypt lab style setting, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 100年先を守る数理の砦！二人の固い決意",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, boy and girl with glasses looking up at soaring constellation of lattice points and cryptographic keys, "
            "boy inspired and determined, girl proud and serene with dignified smile, "
            "magnificent cosmic mathematical atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 25: LLM-assisted Sandbox Robustness (Dr. Yo Ito & Prof. Katsunari Yoshioka)
ep25_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮が隔離環境で無害に終了した検体に安堵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese high school boy leaning back on lab chair with relieved relaxed smile, "
            "hands clasped behind head, monitor displaying Process Exited with Code 0, "
            "carefree cheerful expression, bright amber anime eyes, "
            "modern university security laboratory, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣がマルウェアの「擬死（死んだふり）」を暴く",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent Japanese high school girl with silver glasses, "
            "leaning over desk pointing sharply at registry query and zero mouse movement timer, "
            "cynical knowing smirk, piercing intellectual anime eyes, "
            "school uniform, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが語る伊藤・吉岡論文「LLMによる自動強化」",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome university student with glasses and blazer, "
            "demonstrating AI agent framework querying LLM to uncover sandbox evasion artifacts and generate patches, "
            "sophisticated tech demonstration, confident mentor smile, "
            "SPIRAL advanced research lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 先端研究編完結！巨人の肩の上に立つ誓いの握手",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy and girl with glasses shaking hands firmly with bright ambitious smiles, "
            "sunset light streaming through panoramic lab windows overlooking Yokohama skyline, "
            "emotional inspiring climax, two people, clean sharp anime lines, wordless, no text, no speech bubble"
        )
    }
]

def main():
    print("=== STARTING 4-KOMA GENERATION FOR EPISODES 21 TO 25 (SPIRAL RESEARCH ARC) ===")
    episodes = [
        (21, ep21_panels),
        (22, ep22_panels),
        (23, ep23_panels),
        (24, ep24_panels),
        (25, ep25_panels),
    ]
    for ep_num, panels in episodes:
        print(f"\n--- PROCESSING EPISODE {ep_num} 4-KOMA ---")
        process_episode_4koma(ep_num, panels)
    print("\n=== ALL EPISODES 21-25 4-KOMA IMAGES GENERATED AND DEPLOYED SUCCESSFULLY! ===")

if __name__ == "__main__":
    main()
