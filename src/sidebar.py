import streamlit as st
import pandas as pd
import os

def render_sidebar():

    st.sidebar.markdown("### 📌 功能選單")

    # Streamlit page linking
    st.sidebar.page_link("app.py", label="🏠 首頁")
    st.sidebar.page_link("pages/message_checker.py", label="🔍 單筆偵測")
    st.sidebar.page_link("pages/train_model.py", label="🧠 訓練模型")
    st.sidebar.page_link("pages/model_report.py", label="📈 模型報告")
    st.sidebar.page_link("pages/compare_models.py", label="📊 模型比較")
    st.sidebar.page_link("pages/wordcloud.py", label="🌥️ 文字雲")
    st.sidebar.page_link("pages/data_inspector.py", label="🧹 資料探索")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📘 模型資訊")

    try:
        models = [f for f in os.listdir("models") if f.endswith(".joblib")]
        for m in models:
            st.sidebar.write(f"📄 {m}")
    except:
        st.sidebar.write("⚠️ 找不到模型檔案")

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📗 Dataset")

    path = "dataset/sms_final.csv"
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            st.sidebar.write(f"筆數：{len(df)}")
            st.sidebar.write(f"標籤：{df['label'].unique()}")
        except:
            st.sidebar.write("⚠️ dataset 載入失敗")
    else:
        st.sidebar.write("⚠️ 找不到 dataset/sms_final.csv")
