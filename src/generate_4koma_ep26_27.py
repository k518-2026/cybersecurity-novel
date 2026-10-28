import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 26: LockBit 3.0 Extortion Lifecycle & Operation Cronos (Prof. Katsunari Yoshioka, Assoc. Prof. Yin Minn Pa Pa)
ep26_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がランサムウェア被害のニュースを見て身代金を払えば解決と呑気に発言",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "pointing at a tablet screen displaying a dramatic red ransomware lock icon, "
            "confident carefree smiling expression, bright amber anime eyes, "
            "university seminar room background with tech monitors, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が二重脅迫とRaaSの凶悪なビジネスモデルを冷徹に指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "adjusting glasses with one finger, stern intellectual expression, clear sharp dark anime eyes, navy school blazer, "
            "pointing at dark web leak site countdown timer on monitor, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがSPIRAL論文のLockBit追跡データと国際捜査Operation Cronosを解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual navy blazer, "
            "holding digital pointer towards seminar screen showing complex network graphs of Tor leak sites and law enforcement banner, "
            "calm serious academic lecturing smile, sharp anime eyes, "
            "university conference room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 経済動機と対抗動態を科学するサイバー犯罪学の深さに感銘を受ける蓮と結衣",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy scratching head with inspired determined face and smart girl with glasses smiling warmly with notebook, "
            "looking at high-tech digital forensic dashboard with glowing node connections, "
            "inspiring seminar atmosphere, soft afternoon sunlight through window, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 27: Large-Scale IoT Diagnostic Service 'Am I Infected?' (Assoc. Prof. Takayuki Sasaki, Prof. Katsunari Yoshioka, Prof. Tsutomu Matsumoto)
ep27_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮が脆弱なIoTを見つけたら通知メールを送れば即解決と楽観視",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "holding smartphone showing mail send notification, beaming confident cheerful smile, bright amber anime eyes, "
            "university research lab with various smart home IoT routers on shelf, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が一般ユーザーにとっての通知無視や設定画面の絶望的障壁を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "holding open technical manual showing complicated router firmware settings, "
            "thoughtful serious analytical expression, clear sharp dark anime eyes, navy school blazer, "
            "university lab background, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがUSENIX Security論文『Am I Infected?』の驚異的診断実績とヒューマンファクターを解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "standing by large interactive white screen displaying diagnostic user flow chart and notification success metrics, "
            "confident scholarly explaining pose, sharp anime eyes, "
            "high-tech academic lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: Secure-by-Designと社会連携による本当のIoT砦づくりへ！決意を新たにする二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy clenching fist with enthusiastic motivated smile and smart girl nodding with gentle smile, "
            "collaborative high-tech IoT testing lab with glowing smart devices in soft dusk lighting, "
            "uplifting academic atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

def main():
    print("=== Generating Episode 26 4-Koma Manga ===")
    ep26_path = process_episode_4koma(26, ep26_panels)
    print(f"Ep26 complete: {ep26_path}")

    print("=== Generating Episode 27 4-Koma Manga ===")
    ep27_path = process_episode_4koma(27, ep27_panels)
    print(f"Ep27 complete: {ep27_path}")

if __name__ == "__main__":
    main()
