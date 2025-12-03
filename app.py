import streamlit as st
import os
import pandas as pd

st.set_page_config(
    page_title="垃圾簡訊偵測系統",
    page_icon="📨",
    layout="wide"
)

# -------------------------------
# Sidebar 裝飾 + 內容
# -------------------------------
st.sidebar.markdown("""
<style>
.sidebar-title {
    font-size: 1.3rem;
    font-weight: 700;
    color: #1E88E5;
    margin-bottom: 10px;
}
.info-card {
    background: #FFFFFF10;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 15px;
    border: 1px solid #ffffff22;
}
</style>
""", unsafe_allow_html=True)

# Sidebar 標題
st.sidebar.markdown("<div class='sidebar-title'>📌 導覽選單</div>", unsafe_allow_html=True)
st.sidebar.write("請從下方選擇功能頁面：" )

# -------------------------------
# Model 資訊區塊
# -------------------------------
st.sidebar.markdown("### 📘 模型資訊")

model_files = [f for f in os.listdir("models") if f.endswith(".joblib")]

if len(model_files) > 0:
    st.sidebar.markdown("<div class='info-card'>", unsafe_allow_html=True)
    st.sidebar.write("已載入模型：")
    for f in model_files:
        st.sidebar.write(f"📄 `{f}`")
    st.sidebar.markdown("</div>", unsafe_allow_html=True)
else:
    st.sidebar.warning("⚠️ 沒有可用的模型檔案")

# -------------------------------
# Dataset 資訊
# -------------------------------
st.sidebar.markdown("### 📗 資料集資訊")

if os.path.exists("dataset/sms_final.csv"):
    df_info = pd.read_csv("dataset/sms_final.csv")
    st.sidebar.markdown("<div class='info-card'>", unsafe_allow_html=True)
    st.sidebar.write(f"📊 筆數：{len(df_info)}")
    st.sidebar.write(f"🔤 標籤：{df_info['label'].unique()}")
    st.sidebar.markdown("</div>", unsafe_allow_html=True)
else:
    st.sidebar.warning("⚠️ 找不到 dataset/sms_final.csv")

# -------------------------------
# 模型訓練入口按鈕
# -------------------------------
st.sidebar.markdown("### 🧠 自行訓練模型")
st.sidebar.write("您可以上傳自己的 dataset 並重新訓練模型。")

if st.sidebar.button("進入模型訓練頁面"):
    st.switch_page("pages/train_model.py")

# -------------------------------
# About
# -------------------------------
st.sidebar.markdown("### 💡 About 系統")
st.sidebar.markdown("""
- 📬 垃圾簡訊偵測系統  
- 🔧 支援自訓練模型  
- 🧪 支援 3 種分類器：LogReg / NB / SVM  
- 🎨 科技藍 UI  
""")
