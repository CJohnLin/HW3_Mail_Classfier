
import streamlit as st
from src.sidebar import render_sidebar

st.set_page_config(page_title="🏠 首頁", page_icon="🏠", layout="wide")

render_sidebar()

st.markdown("""<h1 style='font-weight:900;color:#1E88E5'>📨 垃圾簡訊偵測系統</h1>""", unsafe_allow_html=True)
st.write("AI 協助判別垃圾簡訊，提供可視化、模型訓練、模型比較等完整功能。")
st.write("---")

cols=st.columns(2)
with cols[0]:
    st.subheader("🔥 核心功能")
    st.markdown("- 🔍 單筆偵測")
    st.markdown("- 📈 模型報告")
    st.markdown("- 📊 模型比較")
with cols[1]:
    st.subheader("🧰 工具")
    st.markdown("- 🧹 資料探索")
    st.markdown("- 🌥️ 文字雲")
    st.markdown("- 🧠 訓練模型")

st.info("請透過左側導覽欄進入頁面。")
