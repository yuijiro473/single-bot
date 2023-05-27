# 必要なライブラリをインポートします。
import streamlit as st
from api import get_chatgpt_response
from streamlit_chat import message  # streamlit_chatをインポートします。

# Streamlitを使ってウェブアプリケーションのタイトルを設定します。
st.title("Single-bot")

# サブヘッダーを設定します。これはアプリケーションの説明などに使われます。
st.subheader("OpenAI APIを使用した単一応答のチャットボットです。")

# チャットの初期メッセージを設定します。ここでは、システムメッセージを定義しています。
messages = [
    {"role": "system", "content": "You are a helpful AI Tutor. Who answers brief questions about AI."},
]

# フォームを作成します
with st.form(key='message_form', clear_on_submit=False):  # clear_on_submitをFalseに変更して送信後もメッセージが残るようにします。
    # メッセージの入力欄を作成します。
    request = st.text_input("メッセージを入力してください。", key="input")

    # 送信ボタンを作成します。
    submit_button = st.form_submit_button("送信")

# ユーザーがクエリを入力して送信ボタンを押した場合、それを処理し、AIの応答を生成します。
if submit_button and request:
    with st.spinner("生成中..."):
        # ユーザーメッセージをチャットに追加します。
        messages.append({"role": "user", "content": request})
        
        # ユーザーのメッセージを表示します。
        message(request, is_user=True)  # streamlit_chat.messageを使用して、ユーザーのメッセージを表示します。
        
        ## チャットGPTの応答を取得します。
        latest_message = [{"role": "user", "content": request}]
        response = get_chatgpt_response(latest_message)
        
        # AIアシスタントのレスポンスをチャットに追加します。
        messages.append({"role": "assistant", "content": response})
        
        # AIのメッセージを表示します。
        message(response, is_user=False)  # streamlit_chat.messageを使用して、AIのメッセージを表示します。