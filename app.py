import streamlit as st
from src.sidebar import render_sidebar

# ==========================================
# 基本設定
# ==========================================
st.set_page_config(
    page_title="垃圾簡訊偵測系統",
    page_icon="📨",
    layout="wide"
)

# ==========================================
# 全局 Sidebar（所有頁面共享）
# ==========================================
render_sidebar()

# ==========================================
# 首頁內容（Landing Page）
# ==========================================
st.markdown("""
<style>
.home-title {
    font-size: 2.4rem;
    font-weight: 800;
    color: #1E88E5;
    padding-bottom: 8px;
}
.home-subtitle {
    font-size: 1.2rem;
    color: #455A64;
}
.feature-box {
    background: white;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #e4e4e4;
    box-shadow: 0 3px 8px rgba(0,0,0,0.04);
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='home-title'>📨 垃圾簡訊偵測系統</div>", unsafe_allow_html=True)
st.markdown("<div class='home-subtitle'>使用機器學習模型進行垃圾郵件分類 · 完整資料探索 · 支援自動訓練</div>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# 功能介紹
# ==========================================
st.subheader("📌 系統功能")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='feature-box'>
    <h4>🔍 單筆訊息偵測</h4>
    使用訓練模型即時判定訊息是否為垃圾簡訊 (SPAM)。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-box'>
    <h4>🧹 資料探索 (Data Inspector)</h4>
    觀察 dataset 的基本統計資訊、類別分佈。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-box'>
    <h4>🌥️ 文字雲 (WordCloud)</h4>
    可視化常出現字詞，快速理解訊息內容特性。
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='feature-box'>
    <h4>📊 模型效能報告</h4>
    查看分類報告、混淆矩陣與各項模型評估指標。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-box'>
    <h4>📈 模型比較 (Compare Models)</h4>
    查看 LogReg / NB / SVM 三模型的效能比較。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-box'>
    <h4>🧠 自行訓練模型</h4>
    上傳 dataset，自動訓練三模型並更新系統使用的模型。
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.info("請使用左側導覽選單選擇功能頁面。")
