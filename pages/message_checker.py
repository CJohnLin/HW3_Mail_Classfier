import streamlit as st
st.set_page_config(layout="wide")
st.markdown("# 頁面")

        import streamlit as st
        st.set_page_config(page_title="Message Checker", page_icon="📘", layout="wide")

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
              <h1 class="page-title">Message Checker</h1>
              <p class="page-sub small-muted">整潔、專業的 Fluent-style 介面</p>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)
        #/*FLUENT_HEADER*/

import streamlit as st
st.set_page_config(page_title='🔹 🔍 單筆偵測', page_icon='🔹')


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
          <h1 class="page-title">🔍 單筆偵測</h1>
          <p class="page-sub small-muted">使用 TF-IDF + 多種模型即時偵測；可訓練並比較模型效能</p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    #ADVANCED_UI#

import streamlit as st
st.set_page_config(page_title='🔍 單筆偵測', page_icon='🔍')
import streamlit as st
import os
import pandas as pd
import random
from src.text_processing import normalize_message
from src.model_utils import load_resources, infer_single

# =========================================================
# 深色模式切換 (CSS)
# =========================================================
dark_mode = st.sidebar.checkbox("🌙 深色模式")

if dark_mode:
    st.markdown("""
    <style>
    body { background-color: #1e1e1e; color: #E0E0E0; }
    .page-title { color: #64B5F6 !important; }
    .card { background: #2c2c2c !important; border: 1px solid #444 !important; }
    textarea, input { background-color: #333 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .page-title {
        font-size: 2rem;
        font-weight: 700;
        color: #1E88E5;
    }
    .card {
        background: #ffffff;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #e4e4e4;
        box-shadow: 0 3px 8px rgba(0,0,0,0.04);
        margin-bottom: 22px;
    }
    </style>
    """, unsafe_allow_html=True)

# =========================================================
# 頁面標題
# =========================================================
st.markdown("<h1 class='page-title'>🔍 即時訊息檢測（自訓練模型）</h1>", unsafe_allow_html=True)
st.write("使用你自行訓練的 LogReg / NB / SVM 模型進行垃圾簡訊分類。")

# =========================================================
# 模型選擇器
# =========================================================
st.sidebar.header("⚙️ 模型設定")
model_option = st.sidebar.selectbox(
    "選擇分類模型：",
    ["Logistic Regression", "Naive Bayes", "Linear SVM"]
)

MODEL_MAP = {
    "Logistic Regression": "models/custom_logreg.joblib",
    "Naive Bayes": "models/custom_nb.joblib",
    "Linear SVM": "models/custom_svm.joblib"
}

VECTOR_FILE = "models/custom_vectorizer.joblib"
LABEL_MAP_FILE = "models/custom_label_map.json"

try:
    model, vectorizer, label_map = load_resources(
        MODEL_MAP[model_option],
        VECTOR_FILE,
        LABEL_MAP_FILE
    )
except Exception as e:
    st.error(f"❌ 模型或向量器載入失敗：{str(e)}")
    st.stop()

# =========================================================
# 載入 Dataset（for 隨機範例）
# =========================================================
DATA_PATH = os.path.join("dataset", "sms_final.csv")
df_sample = None
if os.path.exists(DATA_PATH):
    df_sample = pd.read_csv(DATA_PATH)

# =========================================================
# Tabs
# =========================================================
tab1, tab2, tab3 = st.tabs([
    "📝 單筆偵測",
    "📂 批次 CSV",
    "🎲 隨機範例"
])

# =========================================================
# 📝 Tab1：單筆偵測
# =========================================================
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📝 單筆訊息偵測")

    user_input = st.text_area("輸入簡訊內容：", height=140)

    if st.button("🚀 立即分析", key="single_predict"):
        if not user_input.strip():
            st.warning("⚠️ 請輸入訊息內容！")
        else:
            pred, prob = infer_single(model, vectorizer, user_input, normalize_message)
            result = label_map.get(str(pred), "spam" if pred == 1 else "ham")

            if result == "spam":
                st.error("🔴 **判定：垃圾簡訊（SPAM）**")
            else:
                st.success("🟢 **判定：正常簡訊（HAM）**")

            if prob is not None:
                st.info(f"📊 垃圾訊息機率：**{prob:.4f}**")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 📂 Tab2：批次偵測
# =========================================================
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📂 批次預測（上傳 CSV）")
    uploaded = st.file_uploader("上傳 CSV（需包含 text 欄位）", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        if "text" not in df.columns:
            st.error("❌ CSV 必須包含 `text` 欄位！")
        else:
            df["clean"] = df["text"].astype(str).apply(normalize_message)
            X = vectorizer.transform(df["clean"])
            df["pred"] = model.predict(X)

            if hasattr(model, "predict_proba"):
                df["spam_prob"] = model.predict_proba(X)[:, 1]

            st.success("🎉 預測完成！")
            st.dataframe(df)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 🎲 Tab3：隨機範例
# =========================================================
with tab3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🎲 從 Dataset 抽一筆測試")

    if df_sample is not None and len(df_sample) > 0:
        if st.button("🎯 抽取隨機訊息"):
            row = df_sample.sample(1).iloc[0]
            st.write(f"📩 **訊息：** `{row['text']}`")
            st.write(f"📌 **真實標籤：** `{row['label']}`")

            pred, prob = infer_single(model, vectorizer, row["text"], normalize_message)
            result = label_map.get(str(pred), "spam" if pred == 1 else "ham")

            st.write("---")
            if result == "spam":
                st.error("🔴 **模型判定：垃圾簡訊（SPAM）**")
            else:
                st.success("🟢 **模型判定：正常簡訊（HAM）**")

            if prob is not None:
                st.info(f"📊 垃圾機率：**{prob:.4f}**")
    else:
        st.warning("⚠️ 找不到 dataset（sms_final.csv）")

    st.markdown("</div>", unsafe_allow_html=True)