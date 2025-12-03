import streamlit as st
import pandas as pd
import os
from src.text_processing import normalize_message
from src.model_utils import load_resources
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# ================================
# 樣式（科技藍）
# ================================
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

st.markdown("<h1 class='page-title'>📊 模型效能報告</h1>", unsafe_allow_html=True)

# ================================
# 使用 custom 模型
# ================================
MODEL = "models/custom_logreg.joblib"
VEC = "models/custom_vectorizer.joblib"
MAP = "models/custom_label_map.json"

try:
    model, vectorizer, label_map = load_resources(MODEL, VEC, MAP)
except Exception as e:
    st.error(f"❌ 模型載入失敗：{str(e)}")
    st.stop()

# ================================
# 正確 dataset 路徑
# ================================
DATA_PATH = os.path.join("dataset", "sms_final.csv")

if not os.path.exists(DATA_PATH):
    st.error(f"⚠️ 找不到 dataset：{DATA_PATH}")
    st.stop()

df = pd.read_csv(DATA_PATH)

# ================================
# 清理標籤
# ================================
df["label"] = df["label"].astype(str).str.strip().str.lower()
df = df[df["label"].isin(["ham", "spam"])]

if df.empty:
    st.error("⚠️ 資料集中沒有可用的 ham/spam 標籤。")
    st.stop()

# ================================
# 清理 text
# ================================
df["text"] = df["text"].astype(str).str.strip()
df = df[df["text"] != ""]

df["clean"] = df["text"].apply(normalize_message)
df = df[df["clean"] != ""]

if df.empty:
    st.error("⚠️ 資料中無有效文本內容。")
    st.stop()

df["label_num"] = df["label"].map({"ham": 0, "spam": 1})

# ================================
# 特徵轉換
# ================================
X = vectorizer.transform(df["clean"])
preds = model.predict(X)

# ================================
# 分類報告
# ================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📄 分類報告")

report = classification_report(
    df["label_num"], preds, 
    target_names=["HAM", "SPAM"],
    output_dict=True
)

st.dataframe(pd.DataFrame(report).T)
st.markdown("</div>", unsafe_allow_html=True)

# ================================
# 混淆矩陣
# ================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🔵 混淆矩陣")

cm = confusion_matrix(df["label_num"], preds)

fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d", ax=ax)
st.pyplot(fig)
st.markdown("</div>", unsafe_allow_html=True)
