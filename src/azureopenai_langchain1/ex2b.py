"""
LangChain で 構造化出力
.with_structured_output() を使うのをやめて、
説明用に PydanticOutputParser を使う
"""

from pprint import pp

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field

llm = AzureChatOpenAI(model="o4-mini", model_kwargs={"response_format": "json"})


class Book(BaseModel):
    title: str = Field(description="本のタイトル")
    author: str = Field(description="著者名")
    genre: str = Field(description="ジャンル")
    summary: str = Field(description="あらすじ")


output_parser = PydanticOutputParser(pydantic_object=Book)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "ユーザーが入力した本の情報を答えて下さい。\n\n{format_instructions}",
        ),
        ("human", "{book}"),
    ]
).partial(format_instructions=output_parser.get_format_instructions())


# 送信されるプロンプトを確認
prompt_value = prompt.invoke({"book": "1Q84"})
print("\n=== prompt: system ===")
print(prompt_value.messages[0].content)
print("\n=== prompt: user ===")
print(prompt_value.messages[1].content)


chain1 = prompt | llm
# 本来なら chain = prompt | llm | output_parser ですが、途中経過が見たいので分けています


input = {"book": "1Q84"}
output = chain1.invoke(input)

print("\n=== chain1 type(output) ===")
print(type(output.content))  # <-- <class 'str'> になっているはず

print("\n=== chain1 output ===")
pp(output.content)


output = output_parser.invoke(output.content)
print("\n=== type(output) ===")
print(type(output))  # <-- <class '__main__.Book'> になっているはず

print("\n=== output ===")
pp(output)

print("\n=== output (JSON) ===")
print(output.model_dump_json(indent=2))
