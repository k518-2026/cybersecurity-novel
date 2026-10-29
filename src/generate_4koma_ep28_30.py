import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from koma_pipeline_common import process_episode_4koma

# Episode 28: Exposed ICS Remote Management Devices (Assoc. Prof. Takayuki Sasaki, Prof. Katsunari Yoshioka, Prof. Tsutomu Matsumoto - IEEE S&P 2022)
ep28_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がダムや太陽光発電所は専用プロトコルで絶対安全と過信",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "pointing at a wall monitor displaying photos of a massive water dam and solar power plant, "
            "carefree triumphant smiling expression, bright amber anime eyes, "
            "university seminar room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が保守用WebUIゲートウェイの認証不備と死角を冷徹に指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "adjusting glasses with one finger, stern intellectual analytical expression, clear sharp dark anime eyes, navy school blazer, "
            "pointing at laptop screen showing an unauthenticated industrial web management login interface, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがIEEE S&P論文の890台露見と13件のゼロデイ脆弱性を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual navy blazer, "
            "standing by seminar screen showing network topology of exposed industrial gateways and vulnerability graphs, "
            "calm serious academic lecturing smile, sharp anime eyes, "
            "high-tech university lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 責任ある開示と運用現場に寄り添う防壁の重要性に目覚める二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy scratching head with inspired determined face and smart girl with glasses smiling warmly holding technical notebook, "
            "looking at high-tech digital forensic dashboard showing patched green shield icons, "
            "inspiring seminar atmosphere, soft ambient lighting, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 29: Cleaning Up the Internet of Evil Things (Prof. Katsunari Yoshioka, Prof. Tsutomu Matsumoto - NDSS 2019 Distinguished Paper)
ep29_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がMirai感染ルーターに警告メールを送れば即解決と楽観発言",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "holding up smartphone displaying an email send confirmation, beaming confident cheerful smile, bright amber anime eyes, "
            "university seminar room background with Wi-Fi routers on table, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣が一般ユーザーの誤ったメンタルモデルとメールの無力さを指摘",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "holding technical diagram showing user running PC antivirus while infected router remains ignored, "
            "thoughtful serious analytical expression, clear sharp dark anime eyes, navy school blazer, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがNDSS優秀賞のWalled Garden隔離実験（92%駆除）を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "pointing at large seminar chart showing ISP Walled Garden isolation achieving 92 percent remediation, "
            "confident scholarly explaining pose, sharp anime eyes, "
            "high-tech academic lab, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: インフラレベルで守る真のサイバー防衛の力強さに感動する二人",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy clenching fist with motivated inspired expression and smart girl smiling gently, "
            "collaborative high-tech network lab with glowing fiber optic status indicators, "
            "uplifting academic atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

# Episode 30: DeFiIntel Token Scam Investigation (Assoc. Prof. Yin Minn Pa Pa, Prof. Katsunari Yoshioka - NDSS MADWeb 2025)
ep30_panels = [
    {
        "panel_num": 1,
        "name": "起: 蓮がブロックチェーンは改ざん不能だから詐欺は起きないと豪語",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, energetic handsome Japanese high school boy with unruly brown hair wearing navy high school uniform, "
            "holding glowing digital coin icon hologram, beaming proud confident smile, bright amber anime eyes, "
            "university tech lab with blockchain node monitors in background, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 2,
        "name": "承: 結衣がRug Pull詐欺と消えゆくオフチェーン（Web/SNS）の罠を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, intelligent beautiful Japanese high school girl with neat straight black hair and silver-rimmed glasses, "
            "pointing at monitor showing deleted 404 scam website and social media account after liquidity drain, "
            "calm stern intellectual expression, clear sharp dark anime eyes, navy school blazer, "
            "university seminar room, clean sharp lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 3,
        "name": "転: 悠真TAがNDSS論文『DeFiIntel』の3.2万トークン×55万データ統合を解説",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, handsome Japanese university student with neat black hair and clear glasses wearing casual blazer, "
            "standing beside interactive screen displaying multimodal graph linking on-chain smart contracts with archived off-chain footprints, "
            "confident academic lecturing pose, sharp anime eyes, "
            "university research room, clean lines, single person, wordless, no text, no speech bubble"
        )
    },
    {
        "panel_num": 4,
        "name": "結: 暗号数理と人間心理を捉える次世代サイバーディフェンダーへの誓い",
        "prompt": (
            "masterpiece, best quality, beautiful anime art style, Kyoto Animation, "
            "medium shot, high school boy and smart girl with glasses standing side by side looking at glowing Web3 security matrix with determined inspired smiles, "
            "warm seminar room at dusk with panoramic city skyline outside, "
            "inspiring hopeful academic atmosphere, two people, clean anime lines, wordless, no text, no speech bubble"
        )
    }
]

def main():
    for ep_num, panels in [(28, ep28_panels), (29, ep29_panels), (30, ep30_panels)]:
        print(f"=== Generating Episode {ep_num} 4-Koma Manga ===")
        path = process_episode_4koma(ep_num, panels)
        print(f"Ep{ep_num} complete: {path}")

if __name__ == "__main__":
    main()
