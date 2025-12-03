
import streamlit as st
import pandas as pd
import os, inspect

def render_sidebar():
    st.sidebar.markdown("""
    <style>
    .sb-title { font-size:1.2rem; font-weight:800; color:#0EA5E9; margin-bottom:6px; }
    .nav-item { padding:8px 10px; border-radius:8px; margin-bottom:6px; }
    .nav-item:hover{ background:linear-gradient(90deg,#60a5fa,#7c3aed); color:white; transform:translateX(4px); }
    .sb-foot{ font-size:0.9rem; color:rgba(0,0,0,0.6); margin-top:12px; }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("<div class='sb-title'>📌 功能選單</div>", unsafe_allow_html=True)
    # navigation links (Streamlit pages show automatically, keep simple)
    st.sidebar.markdown("- 🏠 首頁\n- 🔍 單筆偵測\n- 🧠 訓練模型\n- 📈 模型報告\n- 📊 模型比較\n- 🌥️ 文字雲\n- 🧹 資料探索", unsafe_allow_html=True)

    # model files
    st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
    st.sidebar.markdown("<div style='font-weight:700'>📘 模型</div>", unsafe_allow_html=True)
    try:
        files = [f for f in os.listdir('models') if f.endswith('.joblib')]
    except Exception:
        files = []
    if files:
        for f in files:
            st.sidebar.markdown(f"- `{f}`")
    else:
        st.sidebar.warning('找不到模型檔案')

    st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
    # dataset info
    DATA_PATH='dataset/sms_final.csv'
    st.sidebar.markdown("<div style='font-weight:700'>📗 Dataset</div>", unsafe_allow_html=True)
    if os.path.exists(DATA_PATH):
        try:
            df = pd.read_csv(DATA_PATH)
            st.sidebar.write(f"筆數：{len(df)}")
            st.sidebar.write(f"標籤：{df['label'].unique()}")
        except Exception as e:
            st.sidebar.write('無法讀取 dataset')
    else:
        st.sidebar.warning('找不到 dataset/sms_final.csv')

    st.sidebar.markdown("<div class='sb-foot'>Made with ❤ by you • 進階 UI 版</div>", unsafe_allow_html=True)
