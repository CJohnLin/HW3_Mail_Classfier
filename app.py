
import streamlit as st
from src.sidebar import render_sidebar

<style>
:root{
  --accent:#3b82f6;
  --accent2:#7c3aed;
  --card-bg: rgba(255,255,255,0.85);
  --glass: rgba(255,255,255,0.06);
}
/* animated gradient background for banners */
.blue-gradient {
  background: linear-gradient(90 deg, var(--accent), var(--accent2));
  background-size: 200% 200%;
  animation: gradientShift 6s ease infinite;
  padding: 18px;
  border-radius: 14px;
  color: white;
  box-shadow: 0 8px 30px rgba(59,130,246,0.18);
}
@keyframes gradientShift {
  0%{background-position:0% 50%}
  50%{background-position:100% 50%}
  100%{background-position:0% 50%}
}
.page-header {
  display:flex;
  gap:18px;
  align-items:center;
}
.page-title { font-size:1.6rem; font-weight:800; margin:0; }
.page-sub { opacity:0.95; margin:0; }
.feature-card {
  background: var(--card-bg);
  padding:16px;
  border-radius:12px;
  border:1px solid rgba(0,0,0,0.04);
  box-shadow: 0 6px 18px rgba(2,6,23,0.06);
  margin-bottom:16px;
}
.btn-gradient{
  background: linear-gradient(90deg,var(--accent),var(--accent2));
  color:white; padding:10px 16px; border-radius:10px; border:none; font-weight:600;
  box-shadow: 0 6px 18px rgba(59,130,246,0.12);
}
.small-muted{color:rgba(0,0,0,0.55); font-size:0.95rem}
</style>

render_sidebar()
st.markdown("""
<div class="blue-gradient" style="margin-bottom:14px">
  <div style="display:flex; align-items:center; gap:18px;">

<svg width="72" height="72" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="1" y="4" width="22" height="16" rx="2" fill="white" opacity="0.06"/>
<path d="M3 6L12 13L21 6" stroke="white" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="2" y="5" width="20" height="14" rx="2" stroke="white" stroke-opacity="0.08"/>
</svg>

    <div>
      <h1 class="page-title">📨 垃圾簡訊偵測系統</h1>
      <p class="page-sub small-muted">AI 幫你分類垃圾簡訊 • 支援訓練、比較、即時偵測 • 展示版介面（進階）</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""<div style='display:flex; gap:18px; margin-bottom:12px'>
<div style='flex:1' class='feature-card'>
<h3>✨ 快速開始</h3>
<p class='small-muted'>使用左側選單：🔍 單筆偵測、🧠 訓練模型、📊 模型比較 等等。</p>
<button class='btn-gradient' onclick="window.location.href='#'">立即前往偵測</button>
</div>
<div style='flex:1' class='feature-card'>
<h3>📌 資訊小卡</h3>
<p class='small-muted'>自訓練模型會被儲存在 models/，資料請放 dataset/sms_final.csv</p>
</div>
</div>""", unsafe_allow_html=True)

st.write('---')
st.info('請使用左側選單啟動各項功能。')
