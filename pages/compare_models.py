import streamlit as st
import pandas as pd
import joblib
import os
from sklearn.metrics import classification_report
from src.text_processing import normalize_message

st.set_page_config(page_title="模型比較", page_icon="📊")

st.header("📊 三模型效能比較")

DATA_PATH = "dataset/sms_final.csv"

if not os.path.exists(DATA_PATH):
    st.error("找不到 dataset/sms_final.csv")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["label"] = df["label"].astype(str).str.strip().str.lower()
df = df[df["label"].isin(["ham","spam"])]
df["clean"] = df["text"].astype(str).apply(normalize_message)
df = df[df["clean"] != ""]
df["label_num"] = df["label"].map({"ham":0,"spam":1})

VECTOR = "models/custom_vectorizer.joblib"
LABEL_MAP = "models/custom_label_map.json"
vectorizer = joblib.load(VECTOR)

models = {
    "Logistic Regression": "models/custom_logreg.joblib",
    "Naive Bayes": "models/custom_nb.joblib",
    "Linear SVM": "models/custom_svm.joblib"
}

results = {}

for name, path in models.items():
    if os.path.exists(path):
        model = joblib.load(path)
        X = vectorizer.transform(df["clean"])
        preds = model.predict(X)
        report = classification_report(df["label_num"], preds, output_dict=True)
        results[name] = report["weighted avg"]

st.dataframe(pd.DataFrame(results).T)
