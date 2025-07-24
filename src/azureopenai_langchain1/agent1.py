"""
「大阪と京都の現在気温を比較して」的な質問に答えるAIエージェント
"""

import asyncio

from langchain_core.tools import tool
from langchain_openai import AzureChatOpenAI
from langgraph.prebuilt import create_react_agent


# 気温取得関数
@tool
async def get_temperature(location: str) -> int:
    """
    指定された場所の現在の気温(摂氏、整数値)を返す。引数は地名(例: 東京、大阪)。
    """
    return 25  # 25°Cはダミー値。あとで Weather API等で実装する


llm = AzureChatOpenAI(model="o4-mini")
# 諸般の事情でAzureを使いました。こことプロバイダクラスだけ書き換えて下さい。
# このまま使う場合には以下の環境変数を設定してください
# - AZURE_OPENAI_API_KEY="your-api-key"
# - AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com/"
# - OPENAI_API_VERSION="2025-04-01-preview"
# あと デプロイ名の"o4-mini"は間違っていません。
# "4o-mini"になるべきですが Azure のリソース命名規則のせいらしいです

# ReActパターンのAIエージェントを作成
graph = create_react_agent(llm, [get_temperature])


# エージェントの実装はここまで
# 実行
if __name__ == "__main__":
    from langchain_core.prompts import ChatPromptTemplate

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "あなたは気象予報士です。"),
            ("human", "{input}"),
        ]
    )

    async def main_stream(user_input: str):
        input = prompt.invoke(input=user_input)
        async for msg, metadata in graph.astream(input=input, stream_mode="stream"):
            print(f"\n==== from node {metadata['langgraph_node']} ====")
            print(f"{msg.__class__.__name__}: {msg.content}")

    async def main(user_input: str):
        input = prompt.invoke(user_input)
        output = await graph.ainvoke(input)
        for message in output["messages"]:
            print(f"{message.__class__.__name__}: {message}")

    asyncio.run(main("大阪と京都の現在気温を比較して"))
