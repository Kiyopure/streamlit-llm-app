import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv("stream.env")

def get_llm_response(user_input: str, expert_type: str) -> str:
    """
    LLMから回答を取得する関数
    
    Args:
        user_input: ユーザーからの入力テキスト
        expert_type: 専門家の種類（ラジオボタンで選択）
    
    Returns:
        LLMからの回答テキスト
    """
    # 専門家の種類に応じてシステムメッセージを設定
    system_messages = {
        "医療専門家": "あなたは経験豊富な医療専門家です。医学的な知識を活かして、わかりやすく丁寧に回答してください。",
        "IT・プログラミング専門家": "あなたは熟練したITエンジニア・プログラミング専門家です。技術的な質問に対して、具体的なコード例や最新のベストプラクティスを交えて回答してください。",
        "ビジネスコンサルタント": "あなたは経験豊富なビジネスコンサルタントです。経営戦略、マーケティング、業務改善などビジネスに関する質問に対して、実践的なアドバイスを提供してください。",
        "教育カウンセラー": "あなたは教育分野の専門家・カウンセラーです。学習方法、教育に関する悩み、キャリアパスについて、親身になって丁寧にアドバイスしてください。"
    }
    
    # LLMモデルの初期化
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    
    # メッセージの作成
    messages = [
        SystemMessage(content=system_messages[expert_type]),
        HumanMessage(content=user_input)
    ]
    
    # LLMから回答を取得
    response = llm.invoke(messages)
    
    return response.content

# Streamlitアプリのタイトル
st.title("🤖 AI専門家相談アプリ")

# アプリの説明
st.markdown("""
### 📋 アプリの概要
このアプリでは、様々な分野の専門家AIに質問することができます。
専門家の種類を選択して、質問を入力してください。

### 📖 使い方
1. 下のラジオボタンから相談したい専門家を選択してください
2. テキストボックスに質問や相談内容を入力してください
3. 「回答を取得」ボタンをクリックすると、AI専門家からの回答が表示されます
""")

st.markdown("---")

# 専門家の種類を選択するラジオボタン
expert_type = st.radio(
    "相談したい専門家を選択してください:",
    ["医療専門家", "IT・プログラミング専門家", "ビジネスコンサルタント", "教育カウンセラー"],
    help="選択した専門家の立場でAIが回答します"
)

# ユーザー入力フォーム
user_input = st.text_area(
    "質問・相談内容を入力してください:",
    height=150,
    placeholder="例: Pythonでデータ分析を始めるには何から学べばいいですか？"
)

# 回答取得ボタン
if st.button("💬 回答を取得", type="primary"):
    if user_input.strip():
        with st.spinner("AIが回答を生成中..."):
            try:
                # LLMから回答を取得
                response = get_llm_response(user_input, expert_type)
                
                # 回答を表示
                st.success("回答が生成されました！")
                st.markdown("### 📝 回答:")
                st.write(response)
                
            except Exception as e:
                st.error(f"エラーが発生しました: {str(e)}")
                st.info("OpenAI APIキーが正しく設定されているか確認してください。")
    else:
        st.warning("⚠️ 質問内容を入力してください。")

# フッター
st.markdown("---")
st.caption("Powered by OpenAI GPT-3.5 & LangChain")
