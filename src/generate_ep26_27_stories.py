import os
import json
import urllib.request
import time

OLLAMA_URL = "http://192.168.128.62:11434/api/generate"
CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content")

ep_prompts = {
    26: """あなたは情景豊かで生き生きとした会話と正確な科学技術描写を描く一流のライトノベル作家です。
以下の構成プロットをもとに、高校生たちが横浜国立大学 SPIRAL・吉岡克成教授、イン・ミンパパ特任准教授らの国際共同研究論文（RAID 2025）『ランサムウェアLockBit 3.0の脅迫ライフサイクルと法執行機関（LE）への対抗動態の長期分析』の意義を学ぶ青春アカデミック・ライトノベル第26話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第26話 身代金ビジネスの暗雲 〜LockBit 3.0の脅迫ライフサイクルと国際捜査の追跡〜
【舞台】帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 共同分析ルーム
【登場人物】
・神崎 蓮（高校1年・IoT班）：ランサムウェアを「ただ感染してファイルを暗号化し身代金を要求する単なるウイルス」と単純に捉えている。
・白石 結衣（高校1年・暗号数理班）：身代金ビジネスが「二重脅迫（暗号化＋情報暴露リークサイト）」からアフィリエイト型（RaaS: Ransomware as a Service）へと産業化・企業化している現実に着目する。
・城崎 悠真（大学1年TA）：吉岡克成教授、イン・ミンパパ特任准教授らが国際シンポジウム RAID 2025 で発表した論文『A Longitudinal Analysis of LockBit 3.0\'s Extortion Lifecycle and Response to Law Enforcement』の実証データ（リークサイトの追跡、身代金交渉チャット、FBI等の国際共同作戦「Operation Cronos」への攻撃者側の対抗行動）を解説。
・芹沢 涼香（大学准教授）：サイバー犯罪集団がいかに経済的動機で動き、法執行機関の包囲網に対してブランドの存続やインフラ再建を試みるか、サイバー犯罪学とコンピュータ科学が融合した先端研究の意義を伝える。

【必須要素】
1. 蓮の素朴な認識と結衣の指摘：ランサムウェアの被害ニュースを見ながら「暗号化されたら身代金を払うしかないのかな？」と言う蓮に、結衣は「支払っても鍵がもらえる保証はなく、身代金は犯罪組織の次の兵器開発資金になる。さらに今は『データをネットに公開するぞ』と脅す二重脅迫が主流です」とビジネスモデルの凶悪さを指摘する。
2. 巨大犯罪シンジケート「LockBit 3.0」の構造：RaaS（サービスとしてのランサムウェア）。コア開発者がランサムウェア本体とリークサイトを提供し、侵入を実行するアフィリエイト（実行犯）を募って身代金を山分けする分業体制。
3. SPIRAL吉岡・イン論文の画期的実証（RAID 2025）：Tor上のダークウェブ・リークサイトを長期クローリングし、被害組織の発表、身代金交渉の生々しいチャットログ、身代金支払いの有無を徹底分析。さらに2024年の米英日などの法執行機関によるテイクダウン（Operation Cronos）に対し、LockBitがどのように対抗・再建しようともがいたかの動態をデータで証明した学術的価値。
4. 単なるパケット解析を超えた「エコシステムの解明」：芹沢先生が語る、犯罪者の心理・インセンティブ・経済構造を科学的に暴くことで、法執行機関や政策決定者が効果的な打撃を与えるための科学的根拠（エビデンス）を提供する大学研究の重要性。
5. 蓮と結衣の決意：サイバー空間の守護者とは、技術的なコードの脆弱性を塞ぐだけでなく、社会を脅かす巨大な悪の構造と戦う学問であることを知り、二人はさらに高い視座へと成長する。

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。""",

    27: """あなたは情景豊かで生き生きとした会話と正確な科学技術描写を描く一流のライトノベル作家です。
以下の構成プロットをもとに、高校生たちが横浜国立大学 SPIRAL・佐々木貴之准教授、吉岡克成教授、松本勉上席特別教授らのトップカンファレンス論文（USENIX Security 2025）『大規模IoTセキュリティ診断サービス運用からの教訓（Am I Infected?）』の意義を学ぶ青春アカデミック・ライトノベル第27話の本文（約3,500〜4,500文字程度）を執筆してください。

【タイトル】第27話 届かぬ警告と目覚める砦 〜大規模IoT診断サービス「Am I Infected?」の真実〜
【舞台】帝都科学大学先端セキュリティ実習室 ＆ 横浜国立大学 SPIRAL 地域・社会実装ラボ
【登場人物】
・神崎 蓮（高校1年・IoT班）：「脆弱なIoT機器が見つかったら、持ち主に『危険ですよ』ってメールや通知を送れば、誰でもすぐに対策してくれるはず！」と素直に信じている。
・白石 結衣（高校1年・暗号数理班）：人間の心理的バイアスや、一般ユーザーにとって「ルーターやWebカメラの管理画面を開いてファームウェアを更新する」ことの絶望的なハードルの高さを見抜く。
・城崎 悠真（大学1年TA）：横浜国大・佐々木貴之准教授らがセキュリティ最高峰国際会議 USENIX Security 2025 で発表した論文『Am I Infected? Lessons from Operating a Large-Scale IoT Security Diagnostic Service』の大規模実証実験（何十万台もの一般ユーザー機器に対する診断・通知プロジェクト）の知見を紹介。
・芹沢 涼香（大学准教授）：工学的な脆弱性発見（技術）だけでなく、いかに一般市民や社会に行動変容を起こさせるか（ヒューマンファクターと社会実装）がサイバー防衛の最後の砦であることを熱く説く。

【必須要素】
1. 蓮の楽観的仮説：「通知を送ればみんな直すはず」と主張する蓮に対し、結衣は「世の中のほとんどの人は、自分が使っているルーターのIPアドレスもログインパスワードも知らないし、そもそも警告メールを怪しい詐欺だと誤解して無視します」と現実の難しさを突きつける。
2. USENIX Security 2025 採択論文「Am I Infected?」の衝撃的データ：総務省NOTICEとも連動する大規模な実社会IoT診断サービスの運用データを分析。脆弱性やマルウェア感染が判明してユーザーに詳細な通知を送っても、実際に機器を安全に設定変更・駆除したユーザーはごく一部にとどまるという過酷な現実。
3. なぜ人は対策できないのか（ヒューマンファクターの解明）：佐々木准教授らが論文で明らかにした障壁――「難解すぎる専門用語のUI」「ファームウェア更新手順の複雑さ」「機器の寿命切れ（EOL）による更新パッチ不在」「所有者不在の放置デバイス」。
4. 技術から「人道的なデザインと自動防衛」へ：ユーザーの自己責任に丸投げするのではなく、ISP側のプロアクティブなフィルタリングや、自動セキュアアップデート、製品出荷時の根本的デフォルト防御（パスワード強制変更・セキュア・バイ・デザイン）へと社会全体を動かす研究の力。
5. 蓮と結衣の絆と未来への展望：蓮は「使う人が専門知識を持たなくても絶対に安全なハードウェアを作りたい」と誓い、結衣は「使う人を迷わせない、数学的に確実で人に優しい認証・プロトコルを追求したい」と瞳を輝かせる。

【執筆ルール】
・「起」「承」「転」「結」の4シーンとし、区切りは * * * を使用してください。
・「第1シーン」などの余計な見出しは入れず、純粋な小説文章と会話で構成してください。"""
}

def generate_story(ep_num, prompt):
    outfile = os.path.join(CONTENT_DIR, f"ep{ep_num}_novel_raw.txt")
    if os.path.exists(outfile) and os.path.getsize(outfile) > 1000:
        print(f"[Cached] Episode {ep_num} story exists: {outfile} ({os.path.getsize(outfile)} bytes)")
        return
    print(f"Generating Episode {ep_num} story via Ollama shosetsu:latest...")
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps({
            "model": "shosetsu:latest",
            "prompt": prompt,
            "stream": False
        }).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    t0 = time.time()
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(req, timeout=400) as res:
                data = json.loads(res.read().decode("utf-8"))
                novel_text = data.get("response", "")
            if len(novel_text) > 500:
                with open(outfile, "w", encoding="utf-8") as f:
                    f.write(novel_text)
                print(f"[Saved] {outfile} in {time.time()-t0:.2f}s ({len(novel_text)} chars)")
                break
        except Exception as e:
            print(f"Attempt {attempt} failed for Ep {ep_num}: {e}")
            time.sleep(2)

if __name__ == "__main__":
    for ep_num in [26, 27]:
        generate_story(ep_num, ep_prompts[ep_num])
    print("EPISODES 26-27 STORIES GENERATED SUCCESSFULLY!")
