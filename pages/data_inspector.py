import streamlit as st
import pandas as pd
from src.sidebar import render_sidebar

st.set_page_config(page_title="資料探索", layout="wide")
render_sidebar()

st.title("🧹 資料探索")

df = pd.read_csv("dataset/sms_final.csv")

st.write("### 前 20 筆")
st.write(df.head(20))

st.write("### 標籤分布")
st.write(df["label"].value_counts())
