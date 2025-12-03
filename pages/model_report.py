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

try:
    model = joblib.load("models/custom_logreg.joblib")
    vec = joblib.load("models/custom_vectorizer.joblib")
except:
    st.error("❌ 模型未訓練")
    st.stop()

df = pd.read_csv("dataset/sms_final.csv")
X = vec.transform(df["text"])
y = df["label"]
pred = model.predict(X)

st.subheader("Classification Report")
st.text(classification_report(y, pred))

st.subheader("Confusion Matrix")
plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y, pred), annot=True, fmt="d")
st.pyplot(plt)
