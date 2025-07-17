"""
LangChain で 構造化出力
.with_structured_output() を json_schema 版はめんどくさいからやらない...
と思ったんだけど GitHub Copilot にやってもらった(ちょっと手直しした)
"""

import json
from pprint import pp

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(model="o4-mini")

# JSON Schema を定義
book_json_schema = {
    "title": "Book",
    "description": "Represents a book with its title, author, genre, and summary.",
    "type": "object",
    "properties": {
        "title": {"type": "string", "description": "本のタイトル"},
        "author": {"type": "string", "description": "著者名"},
        "genre": {"type": "string", "description": "ジャンル"},
        "summary": {"type": "string", "description": "あらすじ"},
    },
    "required": ["title", "author", "genre", "summary"],
}

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "ユーザーが入力した本の情報を答えて下さい。"),
        ("human", "{book}"),
    ]
)

chain = prompt | llm.with_structured_output(book_json_schema)

book = "ノルウェイの森"
output = chain.invoke({"book": book})

print("\n=== type(output) ===")
print(type(output))  # <class 'dict'> になるはず

print("\n=== output ===")
pp(output)

print("\n=== output (JSON) ===")
print(json.dumps(output, indent=2, ensure_ascii=False))
