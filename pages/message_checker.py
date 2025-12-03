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
