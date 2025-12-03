import streamlit as st
from src.sidebar import render_sidebar

st.set_page_config(
    page_title="🏠 首頁",
    page_icon="🏠",
    layout="wide"
)

# =============================
# Blue-Gradient 進階 UI：正確可執行的 CSS
# =============================
st.markdown("""
<style>
/* ----- 全域變數 ----- */
:root {
    --grad1: #3b82f6;
    --grad2: #7c3aed;
    --card-bg: rgba(255, 255, 255, 0.85);
}

/* ----- 動態背景漸層 ----- */
.blue-gradient {
    background: linear-gradient(90deg, var(--grad1), var(--grad2));
    background-size: 200% 200%;
    animation: gradientShift 6s ease infinite;
    padding: 18px;
    border-radius: 14px;
    color: white;
    box-shadow: 0 8px 30px rgba(59,130,246,0.18);
}

@keyframes gradientShift {
    0% { background-position: 0% 50% }
    50% { background-position: 100% 50% }
    100% { background-position: 0% 50% }
}

/* ----- 頁面 Header 樣式 ----- */
.page-header {
    display: flex;
    gap: 18px;
    align-items: center;
}
.page-title {
    font-size: 1.7rem;
    font-weight: 800;
    margin: 0;
}
.page-sub {
    opacity: 0.95;
    margin: 0;
}

/* ----- 卡片 ----- */
.feature-card {
    background: var(--card-bg);
    padding: 16px;
    border-radius: 12px;
    border: 1px solid rgba(0, 0, 0, 0.04);
    box-shadow: 0 6px 18px rgba(2, 6, 23, 0.06);
    margin-bottom: 16px;
}

/* ----- Gradient 按鈕 ----- */
.btn-gradient {
    background: linear-gradient(90deg, var(--grad1), var(--grad2));
    color: white;
    padding: 10px 16px;
    border-radius: 10px;
    border: none;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 6px 18px rgba(59,130,246,0.12);
}
.btn-gradient:hover {
    opacity: 0.92;
}
</style>
""", unsafe_allow_html=True)

# =============================
# Sidebar
# =============================
render_sidebar()

# =============================
# Header 區塊（含 SVG 信封圖示）
# =============================
st.markdown("""
<div class="blue-gradient">
  <div class="page-header">
    <svg width="68" height="68" viewBox="0 0 24 24" fill="none">
      <rect x="1" y="4" width="22" height="16" rx="3"
            fill="white" opacity="0.10"/>
      <path d="M3 6L12 13L21 6"
            stroke="white" stroke-width="1.4"
            stroke-linecap="round" stroke-linejoin="round"/>
    </svg>

    <div>
      <h1 class="page-title">📨 垃圾簡訊偵測系統</h1>
      <p class="page-sub">支援模型訓練、即時偵測、資料探索、效能比較</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# =============================
# 功能總覽（新版 UI 卡片）
# =============================
st.write("")
st.subheader("✨ 系統功能快速導覽")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>🔍 單筆偵測</h4>
        即時輸入文字，AI 幫你判斷是否為垃圾簡訊。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h4>🧹 資料探索</h4>
        查看資料集的分布、統計、清洗後內容。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h4>🌥️ 文字雲</h4>
        用視覺化方式觀察最常出現的字詞。
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>📈 模型報告</h4>
        瀏覽模型的 Precision、Recall、F1-score 與混淆矩陣。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h4>📊 模型比較</h4>
        比較 Logistic / NB / SVM 三種模型的效能差異。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h4>🧠 訓練模型</h4>
        上傳資料集，自行訓練 TF-IDF + ML 模型。
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.info("👈 請從左側選單選擇功能頁面。")
