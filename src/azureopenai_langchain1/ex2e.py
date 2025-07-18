"""
LangChain で 構造化出力
.with_structured_output() を Pydanticで使う例
"""

from pprint import pp
from typing import Annotated, List

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field

llm = AzureChatOpenAI(model="o4-mini")


class Author(BaseModel):
    author: Annotated[str, Field(description="著者名")]


class BookGenre(BaseModel):
    genre: Annotated[str, Field(description="ジャンル")]


class Book(BaseModel):
    """Represents a book with its title, author, genre, and summary."""

    title: Annotated[str, Field(description="本のタイトル")]
    authors: Annotated[List[Author], Field(description="著者名")]
    genre: Annotated[List[BookGenre], Field(description="ジャンル")]
    summary: Annotated[str, Field(description="あらすじ")]


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "ユーザーが入力した本の情報を答えて下さい。"),
        ("human", "{input}"),
    ]
)

chain = prompt | llm.with_structured_output(Book)

# book = "1Q84"
# book = "アノーラ"
# book = "ホームレス中学生"
# book = "田村裕の「ホームレス中学生」"
# book = "トカトントン"
# book = "太宰治の「トカトントン」"
book = "オバケのQ太郎"
output = chain.invoke(book)

print("\n=== type(output) ===")
print(type(output))  # <-- <class '__main__.Book'> になっているはず

print("\n=== output ===")
pp(output)

print("\n=== output (JSON) ===")
print(
    output.model_dump_json(indent=2)
)  # pydanticのBaseModelのインスタンスメソッドを使う例。mypyには怒られる
