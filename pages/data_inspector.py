
import streamlit as st
import pandas as pd
import os

st.header('資料檢視')

data_path = os.path.join('Chapter03','datasets','sms_spam_no_header.csv')
if not os.path.exists(data_path):
    st.info('資料集缺失：請放 Chapter03/datasets/sms_spam_no_header.csv')
else:
    df = pd.read_csv(data_path, header=None, names=['label','text'])
    st.write('資料預覽（前 10 筆）：')
    st.dataframe(df.head(10))
    st.write('標籤分布：')
    st.bar_chart(df[0].value_counts())
