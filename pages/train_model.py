import streamlit as st
import pandas as pd
import joblib
import os
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

# ==========================================
# Streamlit Page Config
# ==========================================
st.set_page_config(page_title="訓練模型", page_icon="🧠")

# ==========================================
# CSS（科技藍 + 深色模式）
# ==========================================
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

# ==========================================
# Title
# ==========================================
st.markdown("<h1 class='page-title'>🧠 訓練垃圾簡訊分類模型</h1>", unsafe_allow_html=True)
st.write("上傳 Dataset（需要 label, text 欄位），然後選擇模型即可開始訓練。")

# ==========================================
# 文字清理函式（與預測頁一致）
# ==========================================
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\\S+|www\\S+", "", text)
    text = re.sub(r"\\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\\s+", " ", text)
    return text.strip()

# ==========================================
# 上傳 Dataset
# ==========================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📂 上傳 Dataset")

file = st.file_uploader("上傳 CSV（需包含 label, text 欄位）", type="csv")
st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 模型選擇
# ==========================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("⚙️ 選擇模型")

model_type = st.selectbox(
    "選擇要訓練的分類器：",
    ["Logistic Regression", "Naive Bayes", "Linear SVM"]
)
st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 開始訓練
# ==========================================
if st.button("🚀 開始訓練模型", use_container_width=True):

    if file is None:
        st.error("❗ 請先上傳 dataset 再進行訓練")
        st.stop()

    # 讀取資料
    df = pd.read_csv(file)

    # 檢查欄位
    if "label" not in df.columns or "text" not in df.columns:
        st.error("❗ Dataset 必須包含 label 與 text 欄位")
        st.stop()

    # 清理 label
    df["label"] = df["label"].astype(str).str.strip().str.lower()
    df = df[df["label"].isin(["ham", "spam"])]

    if df.empty:
        st.error("❗ 找不到 ham/spam 標籤，無法訓練模型")
        st.stop()

    # 清理文本
    df["clean"] = df["text"].astype(str).apply(clean_text)
    df = df[df["clean"] != ""]

    # 分割訓練/測試
    X_train, X_test, y_train, y_test = train_test_split(
        df["clean"],
        df["label"].map({"ham": 0, "spam": 1}),
        test_size=0.2,
        random_state=42
    )

    # TF-IDF
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # 選擇模型
    if model_type == "Logistic Regression":
        model = LogisticRegression(max_iter=2000)
        model_name = "custom_logreg.joblib"
    elif model_type == "Naive Bayes":
        model = MultinomialNB()
        model_name = "custom_nb.joblib"
    else:
        model = LinearSVC()
        model_name = "custom_svm.joblib"

    # 訓練
    model.fit(X_train_vec, y_train)
    preds = model.predict(X_test_vec)

    # ==========================================
    # 顯示分類報告
    # ==========================================
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📄 訓練結果")

    report = classification_report(y_test, preds, output_dict=True)
    st.dataframe(pd.DataFrame(report).T)

    st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # 儲存模型
    # ==========================================
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, f"models/{model_name}")
    joblib.dump(vectorizer, "models/custom_vectorizer.joblib")

    with open("models/custom_label_map.json", "w") as f:
        f.write('{"0":"ham","1":"spam"}')

    st.success(f"🎉 模型已成功訓練並儲存至：models/{model_name}")

