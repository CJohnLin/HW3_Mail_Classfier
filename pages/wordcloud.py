import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="文字雲", page_icon="🌥️")

st.header("🌥️ Dataset 文字雲")

DATA_PATH = "dataset/sms_final.csv"

if not os.path.exists(DATA_PATH):
    st.error("找不到 dataset/sms_final.csv")
    st.stop()

df = pd.read_csv(DATA_PATH)

text = " ".join(df["text"].astype(str))

wc = WordCloud(width=800, height=400, background_color="white").generate(text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
