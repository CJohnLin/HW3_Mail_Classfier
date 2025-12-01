
import streamlit as st
from src.text_processing import normalize_message
from src.model_utils import load_resources, infer_single
import os

st.header('即時訊息檢測')

st.write('輸入簡訊，使用已載入的模型與向量器進行偵測。')

MODEL = os.path.join('models','spam_logreg_model.joblib')
VEC = os.path.join('models','spam_tfidf_vectorizer.joblib')
MAP = os.path.join('models','spam_label_mapping.json')

try:
    model, vectorizer, label_map = load_resources(MODEL, VEC, MAP)
except Exception as e:
    st.error('模型或向量器尚未就緒：' + str(e))
    st.stop()

text = st.text_area('輸入要偵測的訊息：', height=140)
if st.button('執行偵測'):
    if not text.strip():
        st.warning('請先輸入訊息內容。')
    else:
        pred, prob = infer_single(model, vectorizer, text, normalize_message)
        label = label_map.get(str(pred), str(pred)) if label_map else ('SPAM' if pred==1 else 'HAM')
        st.write('> 預測結果：', label)
        if prob is not None:
            st.info(f'垃圾訊息機率：{prob:.3f}')
