import streamlit as st
import pandas as pd
import numpy as np

# タイトルと説明
st.title("🎈 Streamlit チュートリアルアプリ")
st.write("ようこそ！これは Streamlit の基本を学ぶための簡単なデモアプリです。")

# 入力ウィジェット
name = st.text_input("お名前を入力してください:")
number = st.slider("好きな数字を選んでください:", 0, 100, 50)
option = st.selectbox("好きなフルーツを選んでください:", ["🍎 りんご", "🍌 バナナ", "🍇 ぶどう"])

# 出力
if name:
    st.success(f"こんにちは、{name} さん！")
st.write(f"あなたが選んだ数字は **{number}** です。")
st.write(f"好きなフルーツは {option} ですね！")

# データ作成
st.subheader("📊 ランダムデータを表示してみましょう")
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A列", "B列", "C列"]
)

# 表示
st.dataframe(data)

# 折れ線グラフ
st.line_chart(data)

# ヒストグラム
st.bar_chart(data)

st.info("✅ これで Streamlit の基本が使えるようになりました！")
