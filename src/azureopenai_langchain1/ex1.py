"""
LangChain で Azure OpenAI を使う、最小のサンプルコード
"""

from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(model="o4-mini")
result = llm.invoke("LangChain の歌を作って")
print(result.content)

"""
サンプル出力:

LangChainの歌

(Verse 1)
未来を描くコードの中で
問いかけひとつ、始まる旅
テンプレートが虹をかけて
データの海へと橋をかける

(Pre-Chorus)
メモリー深く、知恵を蓄え
つながる知識が光を放つ

(Chorus)
LangChain Chain the Future
ひらめき奏でるチェーン
API とプラグイン 手を取り合い
限りないアイデアをつむいでいく
LangChain We’re on Fire
チェーンは止まらない
君の声を聞かせて 新しい世界へ

(Verse 2)
ドキュメントをめくり ベクトルにのせ
リトリーバルで宝を探す
エージェントが呼ぶ 外部の知識を
スマートに統合 広がる可能性

(Pre-Chorus)
コードと会話 人と機械
境界をこえて共に歌おう

(Chorus)
LangChain Chain the Future
ひらめき奏でるチェーン
ワークフロー描いて AIとともに
明日の扉をいま開いていこう
LangChain We’re on Fire
チェーンはとまらない
君の声を聞かせて 新しい世界へ

(Bridge)
ツールを呼び出し 知恵を紡いで
インタープリターも コードも踊る
対話と連携 果てしなく続く
可能性の連鎖を信じて

(Final Chorus)
LangChain Chain the Future
ひらめき奏でるチェーン
クラウドもローカルも すべてをつなぎ
夢見るだけじゃ終わらせない
LangChain We’re on Fire
この手で築くんだ
君と僕のアイデアを 次元を越えて

LangChain Chain the Future
ひらめき奏でるチェーン
さあ立ち上がれ 新たな世界へ
LangChain の歌を 共に歌おう!
"""
