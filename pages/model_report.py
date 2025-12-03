import streamlit as st
import pandas as pd
import os
from src.text_processing import normalize_message
from src.model_utils import load_resources
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ===== CSS =====
st.markdown("""
<style>
.page-title {
    font-size: 2rem;
    font-weight: 700;
    color: #1E88E5;
}
.card {
    background: #ffffff;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #e4e4e4;
    box-shadow: 0 3px 8px rgba(0,0,0,0.04);
    margin-bottom: 22px;
}
</style>
""", unsafe_allow_html=True)

# ===== 標題 =====
st.markdown("<h1 class='page-title'>📊 模型效能報告</h1>", unsafe_allow_html=True)

# ===== 模型 =====
MODEL = os.path.join('models','spam_logreg_model.joblib')
VEC = os.path.join('models','spam_tfidf_vectorizer.joblib')
MAP = os.path.join('models','spam_label_mapping.json')

try:
    model, vectorizer, label_map = load_resources(MODEL, VEC, MAP)
except Exception as e:
    st.error("❌ 模型載入失敗：" + str(e))
    st.stop()

# ===== 資料讀取 =====
data_path = os.path.join("Chapter03","datasets","sms_spam_no_header.csv")

if not os.path.exists(data_path):
    st.error("⚠️ 找不到資料集")
    st.stop()

df = pd.read_csv(data_path, header=None, names=["label","text"])
df["label"] = df["label"].astype(str).str.strip().str.lower()

# 僅保留 ham/spam
df = df[df["label"].isin(["ham","spam"])].copy()

# 清理 text
df["text"] = df["text"].astype(str).fillna("").str.strip()
df = df[df["text"] != ""].copy()

df["clean"] = df["text"].apply(normalize_message)
df = df[df["clean"] != ""].copy()

df["label_num"] = df["label"].map({"ham":0,"spam":1})

# ===== 卡片 1：分類報告 =====
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("📄 分類報告")

X = vectorizer.transform(df["clean"])
preds = model.predict(X)

st.text(classification_report(df["label_num"], preds, target_names=["HAM","SPAM"]))

st.markdown("</div>", unsafe_allow_html=True)

# ===== 卡片 2：混淆矩陣 =====
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("🔵 混淆矩陣")

cm = confusion_matrix(df["label_num"], preds)

fig, ax = plt.subplots(figsize=(5,4))
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d", ax=ax)
st.pyplot(fig)

st.markdown("</div>", unsafe_allow_html=True)
