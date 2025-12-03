import streamlit as st
import pandas as pd
import joblib
from src.sidebar import render_sidebar
import random

st.set_page_config(page_title="單筆偵測", layout="wide")
render_sidebar()

st.title("🔍 單筆偵測")

MODEL = "models/custom_logreg.joblib"
VEC = "models/custom_vectorizer.joblib"

# 1. 載入模型
try:
    model = joblib.load(MODEL)
    vectorizer = joblib.load(VEC)
except:
    st.error("❌ 模型不存在，請先到『訓練模型』訓練")
    st.stop()

# 2. 左右兩欄（單筆偵測 + 隨機抽樣）
col1, col2 = st.columns(2)

# -------------------------------------------------------
# 單筆偵測
# -------------------------------------------------------
with col1:
    st.subheader("✏️ 手動輸入訊息")

    user_msg = st.text_area("請輸入欲分析的訊息：")

    if st.button("立即分析"):
        if user_msg.strip() == "":
            st.warning("請先輸入訊息")
        else:
            X = vectorizer.transform([user_msg])
            pred = model.predict(X)[0]
            st.success(f"預測結果：**{pred}**")

# -------------------------------------------------------
# 隨機抽樣偵測
# -------------------------------------------------------
with col2:
    st.subheader("🎲 從 Dataset 隨機抽一筆")

    try:
        df = pd.read_csv("dataset/sms_final.csv")
        random_idx = random.randint(0, len(df) - 1)

        sample_text = df.loc[random_idx, "text"]
        sample_label = df.loc[random_idx, "label"]

        st.info(f"隨機抽到第 **{random_idx}** 筆")
        st.code(sample_text, language="text")

        if st.button("分析這筆"):
            X = vectorizer.transform([sample_text])
            pred = model.predict(X)[0]

            st.write("📌 **模型預測：**", pred)
            st.write("🎯 **實際標籤：**", sample_label)

    except:
        st.warning("⚠️ 無法載入 dataset/sms_final.csv")
