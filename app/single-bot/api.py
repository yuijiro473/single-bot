from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# ChatGPT-3.5のモデルのインスタンスの作成
chat = ChatOpenAI(model_name="gpt-3.5-turbo")

def init_memory():
    # セッション内に保存されたチャット履歴のメモリの取得
    memory = ConversationBufferMemory(return_messages=True)

    return memory

def api_get_response(memory, human_message):
    # チャット用のチェーンのインスタンスの作成
    chain = ConversationChain(llm=chat, memory=memory)

    # ChatGPTの実行
    chain(human_message)

    return memory