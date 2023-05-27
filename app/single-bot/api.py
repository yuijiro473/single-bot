# 必要なライブラリをインポートします。
import os
from dotenv import load_dotenv
import openai

# .envファイルから環境変数をロードします。これにより、OpenAIのAPIキーを安全に保管できます。
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# チャットGPTからの応答を取得する関数を定義します。入力としてメッセージとモデルを受け取り、
# OpenAI APIを呼び出して応答を返します。
def get_chatgpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']