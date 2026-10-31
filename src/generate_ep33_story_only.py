import os
import json
import urllib.request
import time

OLLAMA_URL = "http://192.168.128.62:11434/api/generate"
CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

prompt_ep33 = """あなたは情景豊かで生き生きとした会話と正確な科学技術描写を描く一流のライトノベル作家です。
以下の構成プロットをもとに、高校生たちが横浜国立大学 SPIRAL・四方順司教授（NexCrypt Lab長）らの先端論文（IEEE Access 2025 / IEEE OJ-COMS 2025）『物理層セキュリティにおける量子アルゴリズムの応用と情報理論的安全保障』の意義を学ぶ青春アカデミック・ライトノベル第33話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第33話 空間を翔ける乱数と量子の極致 〜電波の物理現象で紡ぐ破られない暗号〜
【舞台】帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 次世代暗号ラボ（NexCrypt Lab）
【登場人物】
・神崎 蓮（高校1年・IoT班）：電波での通信は「空中に垂れ流しているんだから、アンテナを立てれば誰にでも盗聴され放題。暗号を複雑にするしか防ぎようがない」と思っている。
・白石 結衣（高校1年・暗号数理班）：上位レイヤーの計算量的な暗号（RSAやAES）だけに頼るのではなく、電波そのものが持つ物理的特性（フェージングやノイズ、空間座標による伝搬差）を利用した「物理層セキュリティ（PLS: Physical Layer Security）」の優位性を語る。
・城崎 悠真（大学1年TA）：四方順司教授らがIEEE Access 2025等で発表した最新論文『Quantum Algorithms for the Physical Layer: Potential Applications to Physical Layer Security』を紹介。無線チャネルから秘密鍵を直接生成するSKG（Secret Key Generation）や、量子アニーリング・QAOAを用いたビームフォーミング最適化など、量子計算機時代に「計算能力が無限の盗聴者でも破れない情報理論的安全保障」を解説。
・芹沢 涼香（大学准教授）：次世代通信（B5G/6G）における「通信とセンシングの統合（ISAC）」と物理層セキュリティの未来を語る。数学的な暗号理論と物理世界の自然法則が融合した、これからのサイバーディフェンスの最高峰の知平を伝える。

【必須要素】
1. 蓮の固定観念と結衣の物理層への着眼：「電波は盗聴を防げないから、アプリの暗号強度を上げるしかない」と言う蓮に、結衣は「電波の物理的ノイズや反射パターンは、発信者と受信者の二点間だけでしか観測できない固有の物理量なの。それを活用すれば、電波そのものから『誰にも盗まれない秘密鍵』を生成できるわ」と物理層セキュリティ（PLS）の概念を提示。
2. 四方研究室（NexCrypt Lab）の先端論文（IEEE Access 2025）：四方順司教授らが提唱する、物理層セキュリティと量子アルゴリズムの融合。古典的な最適化では解けない複雑な無線伝搬路の最適化や秘密鍵蒸留（Information Reconciliation）に、量子アニーリングやQAOA（量子近似最適化）を導入するブレークスルー。
3. 情報理論的安全性（Information-Theoretic Security）：将来どんな超高速な量子コンピュータを持った盗聴者が傍受しても、物理的に情報が届いていないため「数学的に解読が100%不可能」というシャノン以来の究極の安全保障。
4. B5G/6GとISAC（統合センシング・通信）の展望：周囲の空間や物体をレーダーのように感知しながら通信する次世代ネットワークにおいて、物理空間の安全性を担保する学術的フロンティア。
5. 蓮と結衣の進化：目に見えない電波の揺らぎと量子の数理が交差するフロンティアに触れ、サイバーセキュリティが物理世界そのものを包摂する広大な宇宙であることを確信する。

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの見出しは入れず、純粋な小説文章と会話で構成してください。"""

def call_ollama(prompt: str) -> str:
    data = {
        "model": "shosetsu:latest",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.75,
            "top_p": 0.9,
            "num_ctx": 16384
        }
    }
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=600) as response:
        result = json.loads(response.read().decode("utf-8"))
        return result.get("response", "")

def main():
    print("Generating Episode 33 story via Ollama shosetsu:latest...")
    t0 = time.time()
    story = call_ollama(prompt_ep33)
    elapsed = time.time() - t0
    out_path = os.path.join(CONTENT_DIR, "ep33_novel_raw.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(story)
    print(f"[Saved] {out_path} in {elapsed:.2f}s ({len(story)} chars)")

if __name__ == "__main__":
    main()
