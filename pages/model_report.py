import streamlit as st
import pandas as pd
import os
from src.text_processing import normalize_message
from src.model_utils import load_resources
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

st.header("📊 模型效能報告")

# ========== 載入模型與向量器 ==========
MODEL = os.path.join("models", "spam_logreg_model.joblib")
VEC = os.path.join("models", "spam_tfidf_vectorizer.joblib")
MAP = os.path.join("models", "spam_label_mapping.json")

try:
    model, vectorizer, label_map = load_resources(MODEL, VEC, MAP)
except Exception as e:
    st.error("❌ 模型載入失敗：" + str(e))
    st.stop()


# ========== 讀取資料 ==========
data_path = os.path.join("Chapter03", "datasets", "sms_spam_no_header.csv")

if not os.path.exists(data_path):
    st.error("⚠️ 找不到資料集")
    st.stop()

df = pd.read_csv(data_path, header=None, names=["label", "text"])


# ========== Step1：標籤清理 ==========
df["label"] = df["label"].astype(str).str.strip().str.lower()

# 僅保留 ham/spam
df = df[df["label"].isin(["ham", "spam"])].copy()

if df.empty:
    st.error("⚠️ 資料集中沒有可用的 ham/spam 標籤。")
    st.stop()


# ========== Step2：清理 text ==========
df["text"] = df["text"].astype(str).fillna("").str.strip()

# 移除 text 空白行
df = df[df["text"] != ""].copy()

if df.empty:
    st.error("⚠️ 所有訊息內容皆為空白，無法進行分析。")
    st.stop()


# ========== Step3：normalize（可能產生 ''） ==========
df["clean"] = df["text"].apply(normalize_message)

# 移除 normalize 後仍是空的列（這是造成你報錯的真正原因）
df = df[df["clean"] != ""].copy()

if df.empty:
    st.error("⚠️ 文本預處理後無任何有效內容（多為符號/網址/空白）。")
    st.stop()


# ========== Step4：標籤編碼 ==========
df["label_num"] = df["label"].map({"ham": 0, "spam": 1})


# ========== Step5：向量轉換（此處不會再錯）==========
try:
    X = vectorizer.transform(df["clean"])
except Exception as e:
    st.error("❌ 向量化轉換失敗：" + str(e))
    st.stop()


# ========== Step6：模型預測 ==========
preds = model.predict(X)


# ========== Step7：分類報告 ==========
st.subheader("📄 分類報告")
st.text(classification_report(df["label_num"], preds, target_names=["HAM", "SPAM"]))


# ========== Step8：混淆矩陣 ==========
st.subheader("🔵 混淆矩陣")

cm = confusion_matrix(df["label_num"], preds)

fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
st.pyplot(fig)
