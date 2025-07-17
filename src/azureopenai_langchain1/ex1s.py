"""
LangChain で Azure OpenAI を使うサンプル
非同期 & ストリーミング版
"""

import asyncio

from langchain_openai import AzureChatOpenAI


async def main():
    llm = AzureChatOpenAI(model="o4-mini")
    async for chunk in llm.astream("LangChain の歌を作って"):
        print(chunk.content, end="", flush=True)


asyncio.run(main())
