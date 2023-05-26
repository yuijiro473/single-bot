import streamlit as st
from streamlit_chat import message
from langchain.schema import HumanMessage
from langchain.schema import AIMessage

import api

# Streamlitによって、タイトル部分のUIをの作成
st.title("Single Chatbot")

# 入力フォームと送信ボタンのUIの作成
text_input = st.text_input("メッセージを入力してください")
send_button = st.button("送信")

# チャット履歴（HumanMessageやAIMessageなど）を格納する配列の初期化
history = []

# ボタンが押された時、OpenAIのAPIを実行
if send_button:
    send_button = False

    try:
        memory = st.session_state["memory"]
    except:
        memory = api.init_memory()

    # チャット履歴の保存
    memory = api.api_get_response(memory, text_input)

    st.session_state["memory"] = memory

    # チャット履歴（HumanMessageやAIMessageなど）の読み込み
    try:
        history = memory.load_memory_variables({})["history"]
    except Exception as e:
        st.error(e)

# チャット履歴の表示
for index, chat_message in enumerate(reversed(history)):
    if type(chat_message) == HumanMessage:
        message(chat_message.content, is_user=True, key=2 * index)
    elif type(chat_message) == AIMessage:
        message(chat_message.content, is_user=False, key=2 * index + 1)
