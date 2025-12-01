
import streamlit as st
import pandas as pd
import os
from src.text_processing import normalize_message
from src.model_utils import load_resources
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

st.header('模型效能報告')

MODEL = os.path.join('models','spam_logreg_model.joblib')
VEC = os.path.join('models','spam_tfidf_vectorizer.joblib')
MAP = os.path.join('models','spam_label_mapping.json')

try:
    model, vectorizer, label_map = load_resources(MODEL, VEC, MAP)
except Exception as e:
    st.error('模型尚未就緒：' + str(e))
    st.stop()

data_path = os.path.join('Chapter03','datasets','sms_spam_no_header.csv')
if not os.path.exists(data_path):
    st.info('資料集缺失：請置放 Chapter03/datasets/sms_spam_no_header.csv')
else:
    df = pd.read_csv(data_path, header=None, names=['label','text'])
    df['label_num'] = df['label'].map({'ham':0,'spam':1})
    df['clean'] = df['text'].astype(str).apply(normalize_message)
    X = vectorizer.transform(df['clean'])
    preds = model.predict(X)
    st.subheader('分類報告')
    st.text(classification_report(df['label_num'], preds, target_names=['HAM','SPAM']))
    cm = confusion_matrix(df['label_num'], preds)
    fig, ax = plt.subplots(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    st.pyplot(fig)
