"""
LangChain で 構造化出力
.with_structured_output() を使う例
"""

from pprint import pp

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field

llm = AzureChatOpenAI(model="o4-mini")


class Book(BaseModel):
    title: str = Field(description="本のタイトル")
    author: str = Field(description="著者名")
    genre: str = Field(description="ジャンル")
    summary: str = Field(description="あらすじ")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "ユーザーが入力した本の情報を答えて下さい。"),
        ("human", "{book}"),
    ]
)

chain = prompt | llm.with_structured_output(Book)

input = {"book": "1Q84"}
output = chain.invoke(input)

print("\n=== type(output) ===")
print(type(output))  # <-- <class '__main__.Book'> になっているはず

print("\n=== output ===")
pp(output)

print("\n=== output (JSON) ===")
print(
    output.model_dump_json(indent=2)
)  # pydanticのBaseModelのインスタンスメソッドを使う例
