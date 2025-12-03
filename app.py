import streamlit as st
from src.sidebar import render_sidebar
st.set_page_config(page_title="🏠 首頁", page_icon="🏠", layout="wide")

<style>
:root{
  --primary:#0ea5e9; /* sky blue */
  --muted:#6b7280;
  --card:#ffffff;
  --bg:#f7fbff;
}
body { background: var(--bg); }
.fluent-hero { background: linear-gradient(90deg, rgba(14,165,233,0.12), rgba(124,58,237,0.06)); padding:14px; border-radius:10px; margin-bottom:12px; }
.page-title { font-size:1.6rem; font-weight:700; color: #073b4c; margin:0; }
.page-sub { color:var(--muted); margin:0; font-size:0.95rem; }
.card { background: var(--card); padding:14px; border-radius:10px; box-shadow: 0 6px 18px rgba(2,6,23,0.04); margin-bottom:12px; }
.btn-primary { background: var(--primary); color: white; padding:8px 12px; border-radius:8px; border:none; font-weight:600; }
.small-muted { color: var(--muted); font-size:0.95rem; }
</style>

render_sidebar()

st.markdown("""
<div class="fluent-hero">
  <div style="display:flex; gap:12px; align-items:center;">
    <div style="width:56px; height:56px; border-radius:8px; background:linear-gradient(180deg, rgba(14,165,233,0.18), rgba(124,58,237,0.08)); display:flex; align-items:center; justify-content:center;">
      <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><path d="M3 6L12 13L21 6" stroke="#063047" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </div>
    <div>
      <h1 class="page-title">📨 垃圾簡訊偵測系統</h1>
      <p class="page-sub small-muted">Fluent-style 簡潔版 • 支援訓練、偵測、比較、可視化</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.subheader("快速開始")
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card"><h4>🔍 單筆偵測</h4><p class="small-muted">即時判定訊息是否為垃圾。</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h4>🧹 資料探索</h4><p class="small-muted">檢視 dataset 分布與摘要。</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><h4>📈 模型報告</h4><p class="small-muted">查看混淆矩陣與指標。</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h4>🧠 訓練模型</h4><p class="small-muted">上傳 dataset 並訓練。</p></div>', unsafe_allow_html=True)

st.info('請使用左側選單啟動功能。')
