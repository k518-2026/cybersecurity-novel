import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 34: Ethical HUMINT & Telegram Infiltration (Prof. Katsunari Yoshioka, Assoc. Prof. Yin Minn Pa Pa - CSS 2025)
ep34_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮が悪人を騙して捕まえるなら偽アカウント潜入も当然と豪語",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "holding up smartphone displaying dark encrypted messaging app chat list, "
            "confident daring smiling expression, bright amber anime eyes, "
            "university tech lab with dark monitors, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が研究倫理メンロレポートとインフォームドコンセントの原則を冷徹に指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "holding open document of academic ethics guidelines pointing to informed consent clause, "
            "stern intellectual analytical expression, clear sharp dark anime eyes, navy school blazer, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがCSS 2025論文のTelegram潜入のジレンマと倫理監視LLMを解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "standing by seminar screen showing research diagram balancing threat intelligence gathering against ethical checklist, "
            "calm serious academic lecturing smile, sharp anime eyes, "
            "high-tech academic lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 正義の手段を選び抜く！真のサイバー守護者への誇りを誓う二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy scratching head with inspired determined face and smart girl with glasses smiling warmly holding technical notebook, "
            "looking at high-tech digital forensic dashboard glowing with transparent ethical audit logs, "
            "inspiring seminar atmosphere, soft ambient lighting, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 35: Compact Post-Quantum Identity-Based Encryption (Prof. Junji Shikata - NexCrypt Lab, CANS 2024)
ep35_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮が数十億のIoTに全部証明書を配れば解決と安易に発言",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "holding up glowing digital certificate icon hologram with carefree smile, bright amber anime eyes, "
            "smart city IoT lab with hundreds of miniature connected smart devices, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が証明書失効管理の爆発と量子崩壊のボトルネックを指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "pointing at monitor showing overloaded Certificate Authority servers and quantum Shor attack simulation, "
            "thoughtful serious analytical expression, clear sharp dark anime eyes, navy school blazer, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが四方教授らのCANS 2024論文『群テストによる超コンパクト耐量子IBE』を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "pointing at presentation board displaying identity string becoming public key and compact group testing matrix, "
            "confident scholarly explaining pose, sharp anime eyes, "
            "high-tech NexCrypt mathematics lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 証明書のない星群が瞬時に結ばれる数学の奇跡に感動する二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy and smart girl with glasses standing side by side looking at glowing network mesh connecting smart vehicles by ID strings, "
            "warm futuristic laboratory at sunset, "
            "inspiring hopeful academic atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 36: LLM-Assisted Malware Polymorphism & Behavioral Defense (Prof. Katsunari Yoshioka, Assoc. Prof. Yin Minn Pa Pa - ICSS / IEEE DSC)
ep36_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がアンチウイルスを入れておけば定義ファイルで100%防げると過信",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "pointing at a PC monitor displaying green 100 percent virus definition updated badge with proud smile, bright amber anime eyes, "
            "university seminar room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が生成AIによるコード自動変形とアンチウイルスすり抜けの現実を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "displaying generative AI prompt rewriting malware code into dozens of different visual syntactic variations, "
            "calm stern intellectual expression, clear sharp dark anime eyes, navy school blazer, "
            "university lab, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがSPIRAL研究グループのアンチウイルス回避実験と振る舞い防衛を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "standing by interactive screen showing VirusTotal detection rate dropping against LLM variants and behavioral system call analysis graph, "
            "confident academic lecturing pose, sharp anime eyes, "
            "high-tech academic lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 表層のコードに惑わされず意図を見破る知性の砦へ！成長を誓う二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy clenching fist with motivated inspired expression and smart girl smiling gently with technical tablet, "
            "collaborative high-tech AI cyber defense lab with glowing neural network shield visualization, "
            "uplifting academic atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

def main():
    for ep_num, panels in [(34, ep34_panels), (35, ep35_panels), (36, ep36_panels)]:
        print(f"=== Generating Episode {ep_num} 4-Koma Manga ===")
        path = process_episode_4koma(ep_num, panels)
        print(f"Ep{ep_num} complete: {path}")

if __name__ == "__main__":
    main()
