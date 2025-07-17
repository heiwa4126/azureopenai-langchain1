"""
LangChain で 構造化出力
.with_structured_output() を TypedDictで使う例
"""

import json
from pprint import pp
from typing import Annotated, TypedDict

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(model="o4-mini")


class BookDict(TypedDict):
    title: Annotated[str, "本のタイトル"]
    author: Annotated[str, "著者名"]
    genre: Annotated[str, "ジャンル"]
    summary: Annotated[str, "あらすじ"]


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "ユーザーが入力した本の情報を答えて下さい。"),
        ("human", "{book}"),
    ]
)

chain = prompt | llm.with_structured_output(BookDict)

book = "ノルウェイの森"
output = chain.invoke({"book": book})

print("\n=== type(output) ===")
print(type(output))  # <class 'dict'> になるはず

print("\n=== output ===")
pp(output)

print("\n=== output (JSON) ===")
print(json.dumps(output, indent=2, ensure_ascii=False))  # dictをJSONとして表示
