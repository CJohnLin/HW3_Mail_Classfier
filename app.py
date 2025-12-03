import streamlit as st

# ========= 基本設定 =========
st.set_page_config(
    page_title="垃圾簡訊分類系統",
    page_icon="📨",
    layout="centered"
)

# ========= 自訂 CSS（高質感 UI） =========
st.markdown("""
<style>

body {
    font-family: 'Noto Sans TC', sans-serif;
}

/* 主標題 */
.main-title {
    font-size: 2.4rem;
    font-weight: 700;
    text-align: center;
    color: #1E88E5;
    margin-top: 10px;
    margin-bottom: 0px;
}

/* 副標題 */
.subtitle {
    text-align: center;
    font-size: 1.05rem;
    color: #555;
    margin-top: -5px;
    margin-bottom: 25px;
}

/* 卡片 */
.card {
    background: #ffffff;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #e4e4e4;
    box-shadow: 0 3px 8px rgba(0,0,0,0.04);
    margin-bottom: 22px;
}

/* Sidebar 美化 */
section[data-testid="stSidebar"] {
    background-color: #F5F7FA;
    padding-top: 20px;
}

/* 分隔線 */
hr {
    border: none;
    height: 1px;
    background-color: #e0e0e0;
    margin: 18px 0;
}

</style>
""", unsafe_allow_html=True)

# ========= Sidebar =========
with st.sidebar:
    st.title("📌 導覽選單")
    st.write("請從下方選擇功能頁面")

# ========= 主內容 =========
st.markdown("<h1 class='main-title'>垃圾簡訊偵測系統</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>多頁式應用｜偵測、分析、視覺化，一次搞定</p>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.write("""
本系統包含以下功能頁面：

### 🔍 即時訊息檢測  
輸入任意訊息，使用 TF-IDF + ML 模型即時判定是否為垃圾簡訊。

### 📊 模型效能報告  
可視化顯示模型效能、分類報告與混淆矩陣。

### 📁 資料集檢視  
查看資料分布、標籤比例與文字內容。

---

請使用左側的導覽選單切換頁面。
""")

st.markdown("</div>", unsafe_allow_html=True)
