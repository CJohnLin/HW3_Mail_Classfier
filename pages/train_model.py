import streamlit as st
st.set_page_config(page_title='🔹 🧠 訓練模型', page_icon='🔹')


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
          <h1 class="page-title">🧠 訓練模型</h1>
          <p class="page-sub small-muted">使用 TF-IDF + 多種模型即時偵測；可訓練並比較模型效能</p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    #ADVANCED_UI#

import streamlit as st
st.set_page_config(page_title='🧠 訓練模型', page_icon='🧠')
import streamlit as st
import pandas as pd
import joblib
import os
import time
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# =============================
# 標題與說明
# =============================
st.markdown("<h1 class='page-title'>🧠 訓練垃圾簡訊分類模型</h1>", unsafe_allow_html=True)
st.write("上傳 Dataset（需要 label, text 欄位），然後選擇模型即可開始訓練。")

# =============================
# 文字清理函式
# =============================
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\\S+|www\\S+", "", text)
    text = re.sub(r"\\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\\s+", " ", text)
    return text.strip()

# =============================
# 上傳 Dataset
# =============================
st.subheader("📂 上傳 Dataset（label + text）")
file = st.file_uploader("選擇 CSV 檔案", type="csv")

st.write("---")

# =============================
# 模型選擇器
# =============================
model_type = st.selectbox(
    "選擇要訓練的模型：",
    ["Logistic Regression", "Naive Bayes", "Linear SVM"]
)

# =============================
# 開始訓練
# =============================
if st.button("🚀 開始訓練模型", use_container_width=True):

    if file is None:
        st.error("❗ 請先上傳 dataset")
        st.stop()

    df = pd.read_csv(file)

    if "label" not in df.columns or "text" not in df.columns:
        st.error("❗ Dataset 必須包含 label 與 text 欄位")
        st.stop()

    progress = st.progress(0)

    # Step 1 清理資料
    progress.progress(10)
    df["label"] = df["label"].astype(str).str.lower().str.strip()
    df = df[df["label"].isin(["ham", "spam"])]
    df["clean"] = df["text"].astype(str).apply(clean_text)
    df = df[df["clean"] != ""]

    # Step 2 分割資料
    progress.progress(30)
    X_train, X_test, y_train, y_test = train_test_split(
        df["clean"], df["label"].map({"ham": 0, "spam": 1}),
        test_size=0.2, random_state=42
    )

    # Step 3 TF-IDF
    progress.progress(50)
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Step 4 訓練模型
    progress.progress(75)
    if model_type == "Logistic Regression":
        model = LogisticRegression(max_iter=2000)
        model_name = "custom_logreg.joblib"
    elif model_type == "Naive Bayes":
        model = MultinomialNB()
        model_name = "custom_nb.joblib"
    else:
        model = LinearSVC()
        model_name = "custom_svm.joblib"

    model.fit(X_train_vec, y_train)
    preds = model.predict(X_test_vec)

    # Step 5 儲存模型
    progress.progress(100)
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, f"models/{model_name}")
    joblib.dump(vectorizer, "models/custom_vectorizer.joblib")

    with open("models/custom_label_map.json", "w") as f:
        f.write('{"0":"ham","1":"spam"}')

    # 顯示結果
    st.success(f"🎉 訓練完成！模型已儲存到 models/{model_name}")
    st.text(classification_report(y_test, preds))

    st.info("🔄 即將自動返回『單筆偵測』頁面…")

    time.sleep(2)
    st.switch_page("message checker")