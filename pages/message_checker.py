import streamlit as st
import os
from src.text_processing import normalize_message
from src.model_utils import load_resources, infer_single

# ======= CSS：科技藍樣式 =======
st.markdown("""
<style>

.page-title {
    font-size: 2rem;
    font-weight: 700;
    color: #1E88E5;
    margin-bottom: 0px;
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

# ======= 標題 =======
st.markdown("<h1 class='page-title'>🔍 即時訊息偵測</h1>", unsafe_allow_html=True)
st.write("輸入任意簡訊，系統將使用機器學習模型判斷是否為垃圾訊息。")

# ======= 模型載入 =======
MODEL = os.path.join('models','spam_logreg_model.joblib')
VEC = os.path.join('models','spam_tfidf_vectorizer.joblib')
MAP = os.path.join('models','spam_label_mapping.json')

try:
    model, vectorizer, label_map = load_resources(MODEL, VEC, MAP)
except Exception as e:
    st.error("❌ 模型載入失敗：" + str(e))
    st.stop()

# ======= UI 卡片 =======
st.markdown("<div class='card'>", unsafe_allow_html=True)

msg = st.text_area("✏️ 輸入簡訊內容", height=140, placeholder="例如：Congratulations! You have won a prize…")

if st.button("🚀 立即分析", use_container_width=True):
    if not msg.strip():
        st.warning("⚠️ 請輸入訊息內容！")
    else:
        pred, prob = infer_single(model, vectorizer, msg, normalize_message)

        label = label_map.get(str(pred), "spam" if pred == 1 else "ham")

        if label == "spam":
            st.error("🔴 **偵測結果：SPAM（垃圾簡訊）**")
        else:
            st.success("🟢 **偵測結果：HAM（正常簡訊）**")

        if prob is not None:
            st.info(f"📊 垃圾訊息機率：**{prob:.4f}**")

st.markdown("</div>", unsafe_allow_html=True)
