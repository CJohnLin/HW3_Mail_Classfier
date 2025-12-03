import streamlit as st
from src.sidebar import render_sidebar

st.set_page_config(
    page_title="🏠 首頁",
    page_icon="🏠",
    layout="wide"
)

# ----------------------------------------------------
# Fluent-style Safe CSS（100% 不會被 Python 誤判）
# ----------------------------------------------------
st.markdown("""
<style>
/* 主色調 */
:root {
    --primary: #0ea5e9;
    --light-blue: #e0f2fe;
    --text-dark: #0f172a;
    --text-muted: #64748b;
}

/* 標題區塊 */
.hero {
    background: #e0f2fe;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #bae6fd;
    margin-bottom: 20px;
}

/* 標題文字 */
.hero-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--text-dark);
}

.hero-sub {
    font-size: 0.95rem;
    color: var(--text-muted);
}

/* 卡片 */
.card {
    background: white;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #f1f5f9;
    box-shadow: 0 3px 12px rgba(0,0,0,0.04);
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)


# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------
render_sidebar()


# ----------------------------------------------------
# Hero 區塊（沒有 gradient → 極穩定）
# ----------------------------------------------------
st.markdown("""
<div class="hero">
  <h1 class="hero-title">📨 垃圾簡訊偵測系統</h1>
  <p class="hero-sub">提供模型訓練、單筆偵測、資料探索、模型報告與比較</p>
</div>
""", unsafe_allow_html=True)


# ----------------------------------------------------
# 功能卡片
# ----------------------------------------------------
st.subheader("功能導覽 · 功能一覽")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4>🔍 單筆偵測</h4>
        使用訓練模型即時判斷訊息是否為垃圾簡訊。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>🧹 資料探索</h4>
        查看資料集內容與統計分布。
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>📈 模型報告</h4>
        查看 Precision、Recall、F1-score 與混淆矩陣。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>🧠 訓練模型</h4>
        上傳 dataset，自行訓練模型。
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.info("👈 請使用左側選單進入各項功能。")
