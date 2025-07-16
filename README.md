# azureopenai-langchain1

Azure OpenAI を LangChain/LangGraph で使ってみるサンプル。
モデルは o4-mini で安くやっています。

## 使い方

uv + poe で書いてあります

### Azure ポータルでの設定

(この節まだ雑)

1. Azure OpenAI リソースの作成
   - Azure ポータルで「Azure OpenAI」リソースを作成
   - 使用したいモデル(例:GPT-4o-mini)をデプロイ。モデル名とデプロイ名は "o4-mini"になるはず
2. API キーとエンドポイントの取得
   - リソースの「キーとエンドポイント」から取得。↓ で .env に設定する。

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
```
