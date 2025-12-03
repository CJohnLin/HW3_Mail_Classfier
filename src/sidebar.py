import streamlit as st
import pandas as pd, os

def render_sidebar():
    st.sidebar.markdown('<div style="margin-bottom:8px"><strong style="color:#0ea5e9">📌 功能選單</strong></div>', unsafe_allow_html=True)
    # page links (use file aruments expected by Streamlit)
    try:
        st.sidebar.page_link("app.py", label="🏠 首頁")
    except Exception:
        st.sidebar.write("🏠 首頁")
    links = [
      ("pages/message_checker.py","🔍 單筆偵測"),
      ("pages/train_model.py","🧠 訓練模型"),
      ("pages/model_report.py","📈 模型報告"),
      ("pages/compare_models.py","📊 模型比較"),
      ("pages/wordcloud.py","🌥️ 文字雲"),
      ("pages/data_inspector.py","🧹 資料探索")
    ]
    for path,label in links:
        try:
            st.sidebar.page_link(path, label=label)
        except Exception:
            st.sidebar.write(label)

    st.sidebar.markdown('<hr/>', unsafe_allow_html=True)
    st.sidebar.markdown('<div style="font-weight:700">📘 模型</div>', unsafe_allow_html=True)
    try:
        files = [f for f in os.listdir('models') if f.endswith('.joblib')]
    except Exception:
        files = []
    if files:
        for f in files:
            st.sidebar.write(f'📄 {f}')
    else:
        st.sidebar.write('⚠️ 無模型檔')

    st.sidebar.markdown('<hr/>', unsafe_allow_html=True)
    DATA_PATH='dataset/sms_final.csv'
    st.sidebar.markdown('<div style="font-weight:700">📗 Dataset</div>', unsafe_allow_html=True)
    if os.path.exists(DATA_PATH):
        try:
            df = pd.read_csv(DATA_PATH)
            st.sidebar.write(f'筆數：{len(df)}')
            st.sidebar.write(f'標籤：{df["label"].unique()}')
        except Exception:
            st.sidebar.write('無法讀取 dataset')
    else:
        st.sidebar.write('找不到 dataset/sms_final.csv')
