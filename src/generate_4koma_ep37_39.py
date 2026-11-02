import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 37: Secondhand EOL Routers on C2C Markets (Assoc. Prof. Takayuki Sasaki, Prof. Katsunari Yoshioka - CSS 2025)
ep37_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がフリマで格安ルーターを大量購入して自慢",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "holding up an old black Wi-Fi router bought cheap online, "
            "proud joyful beaming grin, bright amber anime eyes, "
            "tech lab with packing cardboard boxes, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が型番を調べサポート終了EOLと個人情報残存を警告",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "pointing at laptop screen showing end of life support expired warning and exposed ISP credentials, "
            "shocked stern analytical expression, clear sharp dark anime eyes, navy school blazer, "
            "university tech lab, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがCSS 2025受賞論文の中古ルーター実態調査を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "standing by seminar screen displaying research chart of flea market router vulnerabilities and unreset memory, "
            "calm serious academic lecturing smile, sharp anime eyes, "
            "high-tech academic lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 物を大切にする心とサイバー安全の調和を誓う二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy inspecting router reset button thoughtfully and smart girl with glasses smiling warmly holding hardware inspection checklist, "
            "warm ambient lighting in university lab, inspiring collaborative atmosphere, "
            "clean sharp lines, highly detailed anime illustration, wordless, no text, no speech bubble"
        )
    }
]

# Episode 38: Darknet Market Dependencies & LLM Signatures (Assoc. Prof. Yin Minn Pa Pa, Prof. Katsunari Yoshioka - CSS 2025)
ep38_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がダークウェブは外界から完全に隔絶された無敵要塞と信じる",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "looking at dark monitor showing onion browser icon and encrypted darknet forum, "
            "awed intrigued expression, bright amber anime eyes, "
            "dark university computer lab with glowing monitors, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣がCAPTCHAや決済APIなど外部サービスへの依存を指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "holding open web inspector log pointing to external clearnet scripts and crypto payment gateways, "
            "cool confident analytical smile, clear sharp dark anime eyes, navy school blazer, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがCSS 2025論文のLLMによる第三者依存検知とシグネチャ生成を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "standing by seminar screen showing network diagram mapping darknet onions to clearnet third-party chokepoints, "
            "calm serious academic lecturing smile, sharp anime eyes, "
            "high-tech academic lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 闇の影を支える蜘蛛の糸を見抜く！真のインテリジェンスに覚醒する二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy with excited determined expression and smart girl with glasses smiling proudly side by side, "
            "gazing at cyber threat intelligence map tracing supply chain vulnerabilities across underground networks, "
            "futuristic glowing holographic displays, clean sharp lines, highly detailed anime illustration, wordless, no text, no speech bubble"
        )
    }
]

# Episode 39: Homomorphic Signatures with Designated Evaluator (Prof. Junji Shikata - IEEE Access 2025)
ep39_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がクラウドにデータを任せるなら普通の電子署名で安心と主張",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "pointing at tablet showing cloud server uploading smart grid data with standard digital seal, "
            "confident easygoing smiling face, bright amber anime eyes, "
            "university high-tech lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が計算した瞬間に署名が壊れ不正計算も防げないと指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "drawing mathematical broken signature diagram on transparent tablet, "
            "earnest teaching analytical expression, clear sharp dark anime eyes, navy school blazer, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが四方教授らのIEEE Access 2025論文「指定評価者付き準同型署名」を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "standing by seminar screen showing cryptographic diagram of Designated Evaluator computing on signed data without signing key, "
            "calm serious academic lecturing smile, sharp anime eyes, "
            "high-tech academic lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: データの信頼を数理で託す！プライバシーと真正性の調和に感動する二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy scratching cheek with amazed inspired grin and smart girl with glasses smiling gently holding cryptographic notebook, "
            "standing together in front of illuminated mathematical lattice equations representing secure cloud computation, "
            "warm modern lighting in tech lab, clean sharp lines, highly detailed anime illustration, wordless, no text, no speech bubble"
        )
    }
]

if __name__ == "__main__":
    episodes = [
        (37, ep37_panels),
        (38, ep38_panels),
        (39, ep39_panels)
    ]
    for ep_num, panels in episodes:
        print(f"=== Generating Episode {ep_num} 4-Koma Manga ===")
        res = process_episode_4koma(ep_num, panels)
        print(f"Ep{ep_num} complete: {res}")
    print("ALL EP37-39 4-KOMA MANGA GENERATED SUCCESSFULLY!")
