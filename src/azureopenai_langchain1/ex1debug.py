"""
ex1.pyにデバッグ付き
"""

from langchain.globals import set_debug, set_verbose
from langchain_openai import AzureChatOpenAI

from azureopenai_langchain1.llm_callback import StderrLoggingCallbackHandler

set_debug(False)
set_verbose(False)


llm = AzureChatOpenAI(model="o4-mini", callbacks=[StderrLoggingCallbackHandler()])
result = llm.invoke("LangChain の歌を作って")
print(result.content)
