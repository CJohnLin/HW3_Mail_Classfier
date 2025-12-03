import streamlit as st
import pandas as pd
import os

def render_sidebar():

    st.sidebar.markdown("""
    <style>
    .sb-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1E88E5;
        margin-bottom: 10px;
    }
    .sb-card {
        background: #FFFFFF10;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 15px;
        border: 1px solid #ffffff22;
    }
    .sb-subtitle {
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # 導覽選單（標題）
    st.sidebar.markdown("<div class='sb-title'>📌 導覽選單</div>", unsafe_allow_html=True)
    st.sidebar.write("請從上方選擇功能頁面。")

    # ============================
    # 模型資訊
    # ============================
    st.sidebar.markdown("<div class='sb-subtitle'>📘 模型資訊</div>", unsafe_allow_html=True)

    model_files = [f for f in os.listdir("models") if f.endswith(".joblib")]

    if len(model_files) > 0:
        with st.sidebar.expander("📦 已載入模型", expanded=True):
            for f in model_files:
                st.write(f"📄 `{f}`")
    else:
        st.sidebar.warning("⚠️ 找不到模型檔案")

    # ============================
    # Dataset 資訊
    # ============================
    st.sidebar.markdown("<div class='sb-subtitle'>📗 資料集資訊</div>", unsafe_allow_html=True)

    DATA_PATH = "dataset/sms_final.csv"

    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        st.sidebar.write(f"📊 筆數：{len(df)}")
        st.sidebar.write(f"🏷 標籤：{df['label'].unique()}")
    else:
        st.sidebar.warning("⚠️ 找不到 dataset/sms_final.csv")

    # ============================
    # 自行訓練模型
    # ============================
    st.sidebar.markdown("<div class='sb-subtitle'>🧠 自行訓練模型</div>", unsafe_allow_html=True)
    st.sidebar.write("可重新訓練 LogReg / NB / SVM 模型。")

    if st.sidebar.button("進入模型訓練頁面"):
        st.switch_page("train model")

    # ============================
    # About
    # ============================
    st.sidebar.markdown("<div class='sb-subtitle'>💡 About 系統</div>", unsafe_allow_html=True)
    st.sidebar.markdown("""
    - 垃圾簡訊偵測平台  
    - 支援自訓練模型  
    - 模型比較 / 效能報告  
    - 文字雲 / 資料探索  
    """)
