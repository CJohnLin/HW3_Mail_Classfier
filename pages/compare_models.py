import streamlit as st
st.set_page_config(layout="wide")
st.markdown("# 頁面")

        import streamlit as st
        st.set_page_config(page_title="Compare Models", page_icon="📘", layout="wide")

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

        st.markdown("""
        <div class="fluent-hero">
          <div style="display:flex; gap:12px; align-items:center;">
            <div style="width:56px; height:56px; border-radius:8px; background:linear-gradient(180deg, rgba(14,165,233,0.18), rgba(124,58,237,0.08)); display:flex; align-items:center; justify-content:center;">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none"><path d="M3 6L12 13L21 6" stroke="#063047" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </div>
            <div>
              <h1 class="page-title">Compare Models</h1>
              <p class="page-sub small-muted">整潔、專業的 Fluent-style 介面</p>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
        #/*FLUENT_HEADER*/

import streamlit as st
st.set_page_config(page_title='🔹 📊 模型比較', page_icon='🔹')


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
  background: linear-gradient(90deg, var(--accent), var(--accent2));
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
    <div class="blue-gradient">
      <div class="page-header">

<svg width="72" height="72" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect x="1" y="4" width="22" height="16" rx="2" fill="white" opacity="0.06"/>
<path d="M3 6L12 13L21 6" stroke="white" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="2" y="5" width="20" height="14" rx="2" stroke="white" stroke-opacity="0.08"/>
</svg>

        <div>
          <h1 class="page-title">📊 模型比較</h1>
          <p class="page-sub small-muted">使用 TF-IDF + 多種模型即時偵測；可訓練並比較模型效能</p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    #ADVANCED_UI#

import streamlit as st
st.set_page_config(page_title='📊 模型比較', page_icon='📊')
import streamlit as st
import pandas as pd
import joblib
import os
from sklearn.metrics import classification_report
from src.text_processing import normalize_message


st.header("📊 三模型效能比較")

DATA_PATH = "dataset/sms_final.csv"

if not os.path.exists(DATA_PATH):
    st.error("找不到 dataset/sms_final.csv")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["label"] = df["label"].astype(str).str.strip().str.lower()
df = df[df["label"].isin(["ham","spam"])]
df["clean"] = df["text"].astype(str).apply(normalize_message)
df = df[df["clean"] != ""]
df["label_num"] = df["label"].map({"ham":0,"spam":1})

VECTOR = "models/custom_vectorizer.joblib"
LABEL_MAP = "models/custom_label_map.json"
vectorizer = joblib.load(VECTOR)

models = {
    "Logistic Regression": "models/custom_logreg.joblib",
    "Naive Bayes": "models/custom_nb.joblib",
    "Linear SVM": "models/custom_svm.joblib"
}

results = {}

for name, path in models.items():
    if os.path.exists(path):
        model = joblib.load(path)
        X = vectorizer.transform(df["clean"])
        preds = model.predict(X)
        report = classification_report(df["label_num"], preds, output_dict=True)
        results[name] = report["weighted avg"]

st.dataframe(pd.DataFrame(results).T)