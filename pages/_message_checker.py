import streamlit as st
import joblib
from src.sidebar import render_sidebar

st.set_page_config(page_title="單筆偵測", layout="wide")
render_sidebar()

st.title("🔍 單筆偵測")

MODEL = "models/custom_logreg.joblib"
VEC = "models/custom_vectorizer.joblib"

try:
    model = joblib.load(MODEL)
    vectorizer = joblib.load(VEC)
except:
    st.error("❌ 模型載入失敗，請先訓練模型")
    st.stop()

msg = st.text_area("請輸入訊息內容：")

if st.button("分析"):
    X = vectorizer.transform([msg])
    pred = model.predict(X)[0]
    st.success(f"預測結果：**{pred}**")
