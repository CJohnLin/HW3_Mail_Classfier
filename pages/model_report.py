import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from src.sidebar import render_sidebar

st.set_page_config(page_title="模型報告", layout="wide")
render_sidebar()

st.title("📈 模型報告")

MODEL = "models/custom_logreg.joblib"
VEC = "models/custom_vectorizer.joblib"

# 1. 載入模型
try:
    model = joblib.load(MODEL)
    vectorizer = joblib.load(VEC)
except:
    st.error("❌ 模型不存在，請先到『訓練模型』頁面訓練")
    st.stop()

# 2. 讀取資料集
try:
    df = pd.read_csv("dataset/sms_final.csv")
except:
    st.error("❌ 找不到 dataset/sms_final.csv")
    st.stop()

# 3. 準備資料
X = vectorizer.transform(df["text"])
y = df["label"]

pred = model.predict(X)

# 4. 確保 y 與 pred 的型別一致
y = y.astype(str)
pred = pred.astype(str)

# 5. 顯示分類報告
st.subheader("Classification Report")
report = classification_report(y, pred, zero_division=0)
st.text(report)

# 6. 顯示混淆矩陣
st.subheader("Confusion Matrix")
plt.figure(figsize=(5, 4))
sns.heatmap(confusion_matrix(y, pred), annot=True, fmt="d", cmap="Blues")
st.pyplot(plt)
