"""
LangChain で 構造化出力
https://python.langchain.com/docs/how_to/structured_output/#streaming
のサンプルを日本語にしてみたもの。でも出力が短すぎるのか、ほぼ瞬時に出る
"""

from typing import Optional

from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field

llm = AzureChatOpenAI(model="o4-mini", streaming=True)


class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="ジョークの前振り")
    punchline: str = Field(description="ジョークのオチ")
    rating: Optional[int] = Field(
        default=None, description="ジョークの面白さの評価(1~10)"
    )


structured_llm = llm.with_structured_output(Joke)

for chunk in structured_llm.stream("Tell me a joke about cats"):
    print(chunk)
