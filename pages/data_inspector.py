import streamlit as st
import pandas as pd
import os

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

st.markdown("<h1 class='page-title'>📁 資料集檢視</h1>", unsafe_allow_html=True)

data_path = os.path.join("Chapter03","datasets","sms_spam_no_header.csv")

if not os.path.exists(data_path):
    st.error("⚠️ 找不到資料集")
    st.stop()

df = pd.read_csv(data_path, header=None, names=["label","text"])
df["label"] = df["label"].astype(str).str.strip().str.lower()

# ===== 卡片：資料預覽 =====
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📌 前 10 筆資料")
st.dataframe(df.head(10))
st.markdown("</div>", unsafe_allow_html=True)

# ===== 卡片：標籤分布 =====
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 標籤統計")
st.bar_chart(df["label"].value_counts())
st.markdown("</div>", unsafe_allow_html=True)
