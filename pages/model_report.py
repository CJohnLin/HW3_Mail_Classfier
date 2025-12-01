import streamlit as st
import pandas as pd
import os
from src.text_processing import normalize_message
from src.model_utils import load_resources
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.header('模型效能報告')

MODEL = os.path.join('models','spam_logreg_model.joblib')
VEC = os.path.join('models','spam_tfidf_vectorizer.joblib')
MAP = os.path.join('models','spam_label_mapping.json')

try:
    model, vectorizer, label_map = load_resources(MODEL, VEC, MAP)
except Exception as e:
    st.error('模型未準備好：' + str(e))
    st.stop()

data_path = os.path.join('Chapter03','datasets','sms_spam_no_header.csv')

if not os.path.exists(data_path):
    st.info('資料集不存在')
else:
    df = pd.read_csv(data_path, header=None, names=['label','text'])

    # --- 保證 label 有效 ---
    df['label'] = df['label'].astype(str).str.strip().str.lower()
    df = df[df['label'].isin(['ham','spam'])].copy()

    # --- 保證 text 不為 NaN / 也不為空白 ---
    df['text'] = df['text'].astype(str).fillna("").str.strip()

    # 移除空白文本（空字串無法進 vectorizer）
    df = df[df['text'] != ""].copy()

    if df.empty:
        st.error("資料集中文本內容皆為空，無法分析。")
        st.stop()

    # --- 清理文本 ---
    df['clean'] = df['text'].apply(normalize_message)

    # 避免 clean 也變成空字串
    df = df[df['clean'] != ""].copy()

    if df.empty:
        st.error("文本預處理後無有效內容。")
        st.stop()

    df['label_num'] = df['label'].map({'ham':0,'spam':1})

    # --- 轉換 TF-IDF ---
    try:
        X = vectorizer.transform(df['clean'])
    except Exception as e:
        st.error("TF-IDF 轉換失敗：" + str(e))
        st.stop()

    # --- 預測 ---
    preds = model.predict(X)

    # --- Report ---
    st.subheader("📄 分類報告")
    st.text(classification_report(df['label_num'], preds, target_names=['HAM','SPAM']))

    # --- Confusion Matrix ---
    st.subheader("🔵 混淆矩陣")
    cm = confusion_matrix(df['label_num'], preds)
    fig, ax = plt.subplots(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    st.pyplot(fig)
