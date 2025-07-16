"""
Azureポータルの「基本的なコード サンプルを実行する」で表示されるコードをちょっとだけ修正したもの。
"このサンプルでは、チャット補完 API に対する基本的な呼び出しが実演されています。この呼び出しは同期的です。"
"""

from openai import AzureOpenAI

# model_name = "o4-mini"
deployment = "o4-mini"
# api_version = "2024-12-01-preview"

client = AzureOpenAI(
    # api_version=api_version,
    # azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    # api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        },
    ],
    max_completion_tokens=100000,
    model=deployment,
)

print(response.choices[0].message.content)
