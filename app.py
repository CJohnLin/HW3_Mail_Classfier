
import streamlit as st
st.set_page_config(page_title='垃圾簡訊系統', layout='centered', page_icon='✉️')

st.sidebar.title('導覽')
st.sidebar.markdown('請選擇功能頁面（左側）')

st.title('垃圾簡訊偵測')
st.markdown('多頁式 Streamlit 應用：左側選單選擇不同分析/預測功能。')
st.markdown('---')
st.write('此應用包含：即時訊息檢測、模型效能報告與資料檢視等頁面。')
