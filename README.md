# Single-Bot
Single-BotはOpenAI APIを活用した単一応答型のChatBotアプリケーションです。以下に設定手順を示します。
## 環境構築
1. **リポジトリのクローン:** 以下のコマンドを実行し、任意のフォルダに対してリポジトリをクローンしてください。
    ```
    git clone https://github.com/yuijiro473/single-bot
    ```
2. **APIキーの発行:** 以下の手順に沿ってOpenAIの公式サイトから、APIキーを発行します。
    1. [OpenAIの公式サイト](https://openai.com/product)にログイン
    2. 「API」を選択
    3. 右上にある自分のアイコンをクリックし、「View API keys」を選択
    4. キーを発行し、コピー
3. **envファイルの設定:** 先程コピーしたキーをenvファイルに入力してください。
    ```
    openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    ```
4. **ライブラリのインストール:** 以下のコマンドをターミナルで実行し、ライブラリをインストールしてください。
    ```
    pip install -r requirements.txt
    ```

## プログラムの実行
1. **システム起動:** 以下のコマンドを実行し、システムを起動してください。
    ```
    cd app/single-bot
    python3 -m streamlit run main.py
    ```
   システム起動後、以下のURLに遷移するはずです: http://localhost:8501
