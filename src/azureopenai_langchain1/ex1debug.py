"""
ex1.pyにデバッグ付き
"""

from langchain.globals import set_debug, set_verbose
from langchain_openai import AzureChatOpenAI

set_debug(True)
set_verbose(True)

llm = AzureChatOpenAI(model="o4-mini")
result = llm.invoke("LangChain の歌を作って")
print(result.content)
