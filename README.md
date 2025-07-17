# azureopenai-langchain1

Azure OpenAI を LangChain/LangGraph で使ってみるサンプル。
モデルは o4-mini で安くやっています。

## 使い方

uv + poe で書いてあります

### Azure ポータルでの設定

(この節まだ雑)

1. Azure OpenAI リソースの作成
   - Azure ポータルで「Azure OpenAI」リソースを作成
   - 使用したいモデル(例:GPT-4o-mini)をデプロイ。
     モデル名とデプロイ名は "o4-mini" になるはず("gpt-o4-mini"でないのに注意)
1. API キーとエンドポイントの取得
   - リソースの「キーとエンドポイント」から取得。↓ で .env に設定する

### 初期化

```sh
uv sync
cp .env.template .env
## .envを環境にあわせて編集
poe update # ときどきでいいから実行してモジュールを更新する
```

### 実行

```sh
poe ex0  # openaiパッケージを使ったサンプル
poe ex1  # LangChainを使った最小サンプル
poe ex2  # 構造化出力の練習
poe ex2b  # 構造化出力の説明用にwith_structured_outputを使わない例
```

## structured output に関して

以下のリンク参照

- [How to return structured data from a model | 🦜️🔗 LangChain](https://python.langchain.com/docs/how_to/structured_output/)
- [Chat models | 🦜️🔗 LangChain](https://python.langchain.com/docs/integrations/chat/)

`response_format="json"`
か
`model_kwargs={"response_format": "json"}`
は
LangChain のバージョンによるらしい。
まず上で試して警告がでるか確認してください。(下の方が最近)
