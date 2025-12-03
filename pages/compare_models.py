import streamlit as st
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
from src.sidebar import render_sidebar

st.set_page_config(page_title="模型比較", layout="wide")
render_sidebar()

st.title("📊 模型比較")

vec_path = "models/custom_vectorizer.joblib"

# 1. 檢查是否有 vectorizer
try:
    vectorizer = joblib.load(vec_path)
except:
    st.error("❌ 找不到向量器，請先訓練模型")
    st.stop()

# 2. 讀取資料
df = pd.read_csv("dataset/sms_final.csv")
X = vectorizer.transform(df["text"])
y = df["label"].astype(str)

# 3. 模型清單
models = {
    "LogReg": "models/custom_logreg.joblib",
    "NB": "models/custom_nb.joblib",
    "SVM": "models/custom_svm.joblib"
}

# 4. 模型逐一比較
for name, path in models.items():
    try:
        m = joblib.load(path)
        pred = m.predict(X).astype(str)
        acc = accuracy_score(y, pred)
        st.success(f"{name} 準確率：{acc:.4f}")
    except:
        st.warning(f"⚠️ {name} 模型不存在，請先訓練")
