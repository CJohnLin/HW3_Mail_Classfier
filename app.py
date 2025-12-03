import streamlit as st
from src.sidebar import render_sidebar

st.set_page_config(page_title="首頁", layout="wide")

render_sidebar()

st.title("📨 垃圾簡訊偵測系統")
st.write("使用左側選單進行操作。")

st.subheader("功能導覽")
col1, col2 = st.columns(2)

with col1:
    st.info("🔍 單筆偵測\n輸入訊息判斷是否為垃圾簡訊。")
    st.info("🧹 資料探索\n檢視資料集內容與統計。")
with col2:
    st.info("📈 模型報告\n查看 Precision / Recall / 混淆矩陣。")
    st.info("🧠 訓練模型\n上傳資料集並重新訓練。")

st.write("---")
st.success("請從左側選單開始。")
