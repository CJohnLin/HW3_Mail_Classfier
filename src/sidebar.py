import streamlit as st
import pandas as pd
import os


def render_sidebar():

    # =======================
    # 樣式（保持美觀）
    # =======================
    st.sidebar.markdown("""
    <style>
    .sb-title { 
        font-size:1.2rem; 
        font-weight:800; 
        color:#0EA5E9; 
        margin-bottom:6px; 
    }
    .sb-foot{
        font-size:0.85rem;
        color:rgba(0,0,0,0.55);
        margin-top:20px;
    }
    </style>
    """, unsafe_allow_html=True)


    # =======================
    # 🔥 中文化功能導航（可點擊）
    # =======================
    st.sidebar.markdown("<div class='sb-title'>📌 功能選單</div>", unsafe_allow_html=True)

    st.sidebar.page_link("app.py", label="🏠 首頁")
    st.sidebar.page_link("pages/message_checker.py", label="🔍 單筆偵測")
    st.sidebar.page_link("pages/train_model.py", label="🧠 訓練模型")
    st.sidebar.page_link("pages/model_report.py", label="📈 模型報告")
    st.sidebar.page_link("pages/compare_models.py", label="📊 模型比較")
    st.sidebar.page_link("pages/wordcloud.py", label="🌥️ 文字雲")
    st.sidebar.page_link("pages/data_inspector.py", label="🧹 資料探索")


    # =======================
    # 模型資訊
    # =======================
    st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
    st.sidebar.markdown("### 📘 模型資訊")

    try:
        model_files = [f for f in os.listdir("models") if f.endswith(".joblib")]
    except:
        model_files = []

    if model_files:
        for m in model_files:
            st.sidebar.write(f"📄 {m}")
    else:
        st.sidebar.warning("⚠️ 找不到模型檔案")


    # =======================
    # 資料集資訊
    # =======================
    st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
    st.sidebar.markdown("### 📗 資料集資訊")

    DATA_PATH = "dataset/sms_final.csv"
    if os.path.exists(DATA_PATH):
        try:
            df = pd.read_csv(DATA_PATH)
            st.sidebar.write(f"📊 筆數：{len(df)}")
            st.sidebar.write(f"🏷 標籤：{df['label'].unique()}")
        except:
            st.sidebar.warning("⚠️ dataset 無法讀取")
    else:
        st.sidebar.warning("⚠️ 找不到 dataset/sms_final.csv")


    st.sidebar.markdown("<div class='sb-foot'>Made with ❤️ | Blue-Gradient UI</div>", unsafe_allow_html=True)
