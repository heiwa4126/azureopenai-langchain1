"""
LangChain で 構造化出力
ex2.pyを複数の本の情報を扱えるように改造した
"""

from pprint import pp
from typing import List

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field

llm = AzureChatOpenAI(model="o4-mini")


class Book(BaseModel):
    title: str = Field(description="本のタイトル")
    author: str = Field(description="著者名")
    genre: str = Field(description="ジャンル")
    summary: str = Field(description="あらすじ")


class Books(BaseModel):
    books: List[Book] = Field(description="本の情報のリスト")


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "ユーザーが入力した本の情報を答えて下さい。複数の場合はすべて答えて下さい。",
        ),
        ("human", "{book}"),
    ]
)

chain = prompt | llm.with_structured_output(Books)

book = "1Q84とノルウェイの森"
# book = "ANORAアノーラ"  # 本ではない。映画。空リストが帰る。
# book = "ホームレス中学生"  # 映画化された本
## ↑は The response was filtered due to the prompt triggering Azure OpenAI's content management policy. Please modify your prompt and retry. To learn more about our content filtering policies please read our documentation: https://go.microsoft.com/fwlink/?linkid=2198766
## と言われて死ぬ
# book = "田村裕の「ホームレス中学生」"  # 映画化された本。こっちは通るのはなんで
# book = "「ホームレス中学生」という本の情報をおしえて"  # こういうのも通る
# book = "ホームレス中学生という本の情報をおしえて"  # これは死ぬ
# book = '["トカトントン","津軽"]'
# 意味なくJSONのリストにしてみる。「トカトントン」は難しいらしくハルシネーションが出る
# "太宰の「トカトントン」"とかにすればOK。たぶんインターネットから取ってきているっぽい

output = chain.invoke({"book": book})

print("\n=== type(output) ===")
print(type(output))  # -> <class '__main__.Books'>

print("\n=== output ===")
pp(output)

print("\n=== output (JSON) ===")
print(output.model_dump_json(indent=2))
