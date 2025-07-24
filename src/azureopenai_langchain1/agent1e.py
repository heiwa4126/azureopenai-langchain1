"""
「大阪と京都の現在気温を比較して」的な質問に答えるAIエージェント
"""

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
    import asyncio

    from langchain_core.prompts import ChatPromptTemplate

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "あなたは気象予報士です。"),
            ("human", "{input}"),
        ]
    )

    def format_message(message):
        """メッセージを人間に読みやすい形式で表示する"""
        message_type = message.__class__.__name__

        if message_type == "ToolMessage":
            # ツールメッセージの場合
            tool_name = getattr(message, "name", "unknown")
            tool_call_id = getattr(message, "tool_call_id", "unknown")
            content = message.content
            return f"{message_type}: {tool_name}の結果: {content} [Call ID: {tool_call_id}]"

        elif hasattr(message, "tool_calls") and message.tool_calls:
            # ツール呼び出しがある場合
            tool_calls = []
            for tool_call in message.tool_calls:
                tool_name = tool_call.get("name", "unknown")
                tool_id = tool_call.get("id", "unknown")
                tool_args = tool_call.get("args", {})
                args_str = ", ".join([f"{k}='{v}'" for k, v in tool_args.items()])
                tool_calls.append(f"{tool_name}({args_str}) [ID: {tool_id}]")
            return f"{message_type}: ツール呼び出し: {', '.join(tool_calls)}"

        elif hasattr(message, "content") and message.content:
            # コンテンツがある場合はそのまま表示
            return f"{message_type}: {message.content}"

        else:
            # その他の場合はしょうがないので元の形式で表示
            return f"{message_type}: {message.content if hasattr(message, 'content') else str(message)}"

    async def main(user_input: str):
        output = await graph.ainvoke(prompt.invoke(user_input))
        for message in output["messages"]:
            print(format_message(message))

    asyncio.run(main("大阪と京都の現在気温を比較して"))
