import streamlit as st
import pandas as pd
import os

st.header('資料檢視')

data_path = os.path.join('Chapter03','datasets','sms_spam_no_header.csv')

if not os.path.exists(data_path):
    st.info('資料集不存在：請確認檔案位置 Chapter03/datasets/sms_spam_no_header.csv')
else:
    df = pd.read_csv(data_path, header=None, names=['label','text'])

    # 基本清理
    df['label'] = df['label'].astype(str).str.strip().str.lower()

    st.subheader("📌 前 10 筆資料")
    st.dataframe(df.head(10))

    st.subheader("📊 標籤分布")
    st.bar_chart(df['label'].value_counts())
