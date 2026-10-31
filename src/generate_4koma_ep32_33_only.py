import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 32: JC-STAR IoT Security Labeling (Prof. Katsunari Yoshioka, METI/IPA Technical Chair)
ep32_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮が量販店で安いルーターを選ぼうと値段だけで判断",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "holding a generic wireless router box looking at price tag with carefree smile, bright amber anime eyes, "
            "electronics store shelf background, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が中身の古いLinuxやOSS脆弱性の見えない非対称性を指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "holding tablet displaying software composition analysis with outdated firmware warnings, "
            "thoughtful serious analytical expression, clear sharp dark anime eyes, navy school blazer, "
            "university lab, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが国家制度JC-STARの星ラベルと吉岡教授らの技術的礎を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "pointing at presentation board displaying official JC-STAR star ratings (1 to 4 stars) and honeypot attack metrics, "
            "confident scholarly explaining pose, sharp anime eyes, "
            "high-tech academic lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 消費者を守る透明な安全の星標識に感銘を受け決意を新たにする二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy clenching fist with motivated inspired expression and smart girl smiling gently, "
            "collaborative high-tech consumer tech lab with glowing verified star emblems, "
            "uplifting academic atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 33: Quantum Algorithms for Physical Layer Security (Prof. Junji Shikata - NexCrypt Lab, IEEE Access 2025)
ep33_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮が電波通信は誰にでも傍受されるからアプリ暗号を強めるしかないと発言",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "holding up smartphone pointing toward a glowing Wi-Fi antenna with perplexed shrug, bright amber anime eyes, "
            "university seminar room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が電波の物理現象（フェージング・ノイズ）から秘密鍵を生み出す物理層セキュリティを解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "tracing physical radio wave propagation waveforms on interactive glass whiteboard, "
            "calm intellectual confident expression, clear sharp dark anime eyes, navy school blazer, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAが四方教授らの量子アルゴリズム×物理層暗号数理（IEEE Access 2025）を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "standing beside holographic display showing quantum annealing graphs and secret key generation between antennas, "
            "confident academic lecturing pose, sharp anime eyes, "
            "NexCrypt quantum research lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 無限の計算力にも屈しない情報理論的安全性の深淵に感動する二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy and smart girl with glasses standing side by side looking at glowing mathematical matrix of physical wave entropy with awe and determined smiles, "
            "warm futuristic laboratory at sunset, "
            "inspiring hopeful academic atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

def main():
    for ep_num, panels in [(32, ep32_panels), (33, ep33_panels)]:
        print(f"=== Generating Episode {ep_num} 4-Koma Manga ===")
        path = process_episode_4koma(ep_num, panels)
        print(f"Ep{ep_num} complete: {path}")

if __name__ == "__main__":
    main()
