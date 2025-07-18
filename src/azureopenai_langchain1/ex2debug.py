from pprint import pp

from langchain.globals import set_debug
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field

from azureopenai_langchain1.llm_callback import StderrLoggingCallbackHandler

set_debug(True)


class Book(BaseModel):
    """Represents a book with its title, author, genre, and summary."""

    title: str = Field(description="本のタイトル")
    author: str = Field(description="著者名")
    genre: str = Field(description="ジャンル")
    summary: str = Field(description="あらすじ")


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "ユーザーが入力した本の情報を答えて下さい。"),
        ("human", "{input}"),
    ]
)

llm = AzureChatOpenAI(model="o4-mini", callbacks=[StderrLoggingCallbackHandler()])

chain = prompt | llm.with_structured_output(Book)

book = "1Q84"
output = chain.invoke(book)

print("\n=== type(output) ===")
print(type(output))  # <-- <class '__main__.Book'> になっているはず

print("\n=== output ===")
pp(output)

print("\n=== output (JSON) ===")
print(output.model_dump_json(indent=2))
