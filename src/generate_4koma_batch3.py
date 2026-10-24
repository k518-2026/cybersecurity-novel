import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 12: LAN, Routers & DNS Basics
ep12_panels = [
    {
        "panel_num": 1,
        "name": "起: 無数の端末が迷わず繋がる仕組みを不思議がる葵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail tilting head inquisitively, "
            "looking back and forth between her smartphone, a tablet, and a laptop on cafe desk, "
            "wondering how thousands of home devices share one single fiber line without colliding, "
            "sparkling curious hazel anime eyes, innocent puzzled smile, cozy modern room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真がルーターのNAT変換とプライベートIPを解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear glasses, "
            "sketching a clear network routing diagram in notebook showing Private IPs 192.168.x.x mapped to one Global IP via NAT/NAPT port numbers, "
            "intelligent reassuring smile, perfectly drawn beautiful dark anime eyes, clear defined pupils, "
            "afternoon club room desk, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生がDNS名前解決のバケツリレーとDNSSECを解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant stylish female university professor, "
            "holding a glowing globe network model showing hierarchical DNS servers passing address inquiries from root to TLD, "
            "explaining DNSSEC digital signatures protecting against cache poisoning, "
            "bright captivating anime eyes, gentle confident smile, modern informatics laboratory, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: インターネットの壮大なバケツリレーに感動する二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl and smart boy with glasses clicking a web page link, "
            "screen instantly blooming with golden data packet streams successfully resolving across the globe, "
            "eyes wide with profound wonder and happiness, deep appreciation for internet architecture, "
            "afternoon club room sunset, wordless, no text, no speech bubble"
        )
    }
]

# Episode 13: CTF Competitions & Future Careers
ep13_panels = [
    {
        "panel_num": 1,
        "name": "起: 初のCTF競技大会にワクワクしながら挑む葵と悠真",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail and smart boy with glasses staring eagerly at CTF scoreboard monitor, "
            "excited determined expressions, sparkling clear anime eyes, hands poised ready on keyboards, "
            "challenge categories Web Crypto Forensics displayed on glowing screen, "
            "high-tech tournament club room, energetic atmosphere, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真がリバースエンジニアリングでFlag文字列を奪取！",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear glasses pumping fist in triumphant victory, "
            "thrilled ecstatic smile, brilliant sparkling dark anime eyes, "
            "debugger monitor displaying extracted string FLAG{...} highlighted in radiant green, "
            "club room desk, dynamic angle, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生が語る大学情報理工学とCISO・エンジニアの未来",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant female university professor pointing toward a bright futuristic city skyline projection, "
            "showing diverse vital career paths: Penetration Tester, Incident Responder, Chief Information Security Officer (CISO), "
            "warm encouraging proud smile, beautiful captivating anime eyes, "
            "university auditorium lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: チーム総合入賞！未来の守護者への新たな誓い",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl with ponytail and smart boy with glasses holding a silver CTF award plaque together, "
            "radiant triumphant smiles, bright clear joyful anime eyes, "
            "golden confetti falling gently in afternoon sun, determination to study cybersecurity at university, "
            "proud and inspiring celebration, wordless, no text, no speech bubble"
        )
    }
]

# Episode 14: Cloud Security & Shared Responsibility Model
ep14_panels = [
    {
        "panel_num": 1,
        "name": "起: クラウドに上げたから全部安全と信じ切る葵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail with proud relieved smile, "
            "pointing happily to laptop showing completed cloud upload dialog, "
            "believing major cloud provider makes everything unconditionally secure, "
            "bright innocent clear hazel anime eyes, school festival prep classroom, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真がバケットの全世界公開設定ミスを発見して制止",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear glasses, "
            "pointing urgently at storage bucket access permissions showing Public Anonymous Read warning, "
            "serious commanding protective gaze, perfectly drawn sharp dark anime eyes, "
            "explaining data breach risks, afternoon classroom, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生がマンションの鍵と責任共有モデルを解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant stylish female university professor on video call tablet, "
            "holding up an illustration comparing apartment building auto-lock (Cloud Provider responsibility) versus individual room keys (User IAM responsibility), "
            "intellectual gentle smile, captivating expressive anime eyes, "
            "university research lab background, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: IAM最小権限設定完了！正しい鍵で守られた笑顔",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl and smart boy giving each other a cheerful high five, "
            "cloud storage dashboard glowing in secure calm blue with strict IAM access permissions enabled, "
            "radiant proud smiles, perfectly drawn clear anime eyes, "
            "afternoon sunset glow in classroom, true cloud governance, wordless, no text, no speech bubble"
        )
    }
]

# Episode 15: AI Security & Season 1 Grand Finale
ep15_panels = [
    {
        "panel_num": 1,
        "name": "起: AIが自分の声で話しかけてきて戦慄する葵",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute Japanese high school girl with dark ponytail staring in absolute shock at smartphone speaker, "
            "trembling hands, horrified wide hazel anime eyes, pale face, "
            "hearing an identical AI deepfake clone of her own voice demanding money, "
            "afternoon club room, dramatic lighting, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 悠真がプロンプト注入とAI悪用の新脅威を分析",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, smart handsome Japanese high school boy with neat black hair and clear glasses, "
            "typing steadily at keyboard, analyzing prompt injection attacks and adversarial perturbations on monitor, "
            "calm determined serious gaze, perfectly drawn sharp dark anime eyes, clear pupils, "
            "navy uniform blazer, high-tech club room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 芹沢先生が説くAI自律防御と人間の温かい倫理の力",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot of elegant female university professor standing in front of radiant digital shield, "
            "autonomous AI defense neutralizing attacks while emphasizing that human conscience and ethics guide the shield, "
            "warm inspiring maternal smile, captivating expressive anime eyes, "
            "university research laboratory, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 第1部堂々完結！青空の下で未来へのバトンを繋ぐ笑顔",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, cute high school girl with ponytail and smart boy with glasses smiling warmly under clear infinite blue sky outside school gate, "
            "Yuma holding university acceptance letter, Aoi raising fist in joyful determination to follow him to university lab, "
            "radiant sparkling anime eyes, gentle breeze, cherry blossoms starting to bud, "
            "emotional heartwarming grand finale, hope for the future, wordless, no text, no speech bubble"
        )
    }
]

if __name__ == "__main__":
    process_episode_4koma(12, ep12_panels)
    process_episode_4koma(13, ep13_panels)
    process_episode_4koma(14, ep14_panels)
    process_episode_4koma(15, ep15_panels)
    print("\nBATCH 3 (EPISODES 12-15) COMPLETED SUCCESSFULLY!")
