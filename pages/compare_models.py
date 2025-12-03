import streamlit as st
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
from src.sidebar import render_sidebar

st.set_page_config(page_title="模型比較", layout="wide")
render_sidebar()

st.title("📊 模型比較")

models = {
    "LogReg": "models/custom_logreg.joblib",
    "NB": "models/custom_nb.joblib",
    "SVM": "models/custom_svm.joblib"
}

vec = joblib.load("models/custom_vectorizer.joblib")
df = pd.read_csv("dataset/sms_final.csv")
X = vec.transform(df["text"])
y = df["label"]

for name, path in models.items():
    try:
        m = joblib.load(path)
        pred = m.predict(X)
        st.write(f"### {name}：{accuracy_score(y, pred):.4f}")
    except:
        st.write(f"⚠️ {name} 模型不存在")
