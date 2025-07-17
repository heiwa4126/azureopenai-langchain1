"""
LangChain で 構造化出力
.with_structured_output() を Pydanticで使う例
https://python.langchain.com/docs/how_to/structured_output/#pydantic-class
のサンプルを日本語にしてみたもの
"""

from pprint import pp
from typing import Optional

from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field

llm = AzureChatOpenAI(model="o4-mini")


class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="ジョークの前振り")
    punchline: str = Field(description="ジョークのオチ")
    rating: Optional[int] = Field(
        default=None, description="ジョークの面白さの評価(1~10)"
    )


structured_llm = llm.with_structured_output(Joke)

pp(structured_llm.invoke("猫がテーマのジョークを教えて"))
