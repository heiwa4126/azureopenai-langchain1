"""
LLM Callback Handler for Debugging
"""

import json
import sys

from langchain.callbacks.base import BaseCallbackHandler


class StderrLoggingCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print(
            f"\n======[LLM Start] Prompts:\n{json.dumps(prompts, ensure_ascii=False)}",
            file=sys.stderr,
        )

    def on_llm_end(self, response, **kwargs):
        print(
            f"\n======[LLM End] Response:\n{response}",
            file=sys.stderr,
        )

    def on_llm_error(self, error, **kwargs):
        print(
            f"\n======[LLM Error] Error: {error}",
            file=sys.stderr,
        )
