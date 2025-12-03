import streamlit as st
from src.sidebar import render_sidebar
st.set_page_config(page_title="首頁", layout="wide")
render_sidebar()
st.title("垃圾簡訊偵測系統")
st.write("使用左側選單開始操作。")
