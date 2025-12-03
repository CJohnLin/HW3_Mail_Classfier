import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from src.sidebar import render_sidebar

st.set_page_config(page_title="訓練模型", layout="wide")
render_sidebar()

st.title("🧠 訓練模型")

uploaded = st.file_uploader("上傳 CSV（需包含 text, label 欄位）")

if uploaded:
    df = pd.read_csv(uploaded)
    st.write(df.head())

    if st.button("開始訓練"):
        st.info("向量化中...")
        vec = TfidfVectorizer()
        X = vec.fit_transform(df["text"])
        y = df["label"]

        st.info("模型訓練中...")
        clf = LogisticRegression()
        clf.fit(X, y)

        joblib.dump(vec, "models/custom_vectorizer.joblib")
        joblib.dump(clf, "models/custom_logreg.joblib")

        st.success("訓練完成！模型已更新")
