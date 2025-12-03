import streamlit as st
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from src.sidebar import render_sidebar

st.set_page_config(page_title="文字雲", layout="wide")
render_sidebar()

st.title("🌥️ 文字雲")

df = pd.read_csv("dataset/sms_final.csv")

text = " ".join(df["text"])

wc = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
st.pyplot(plt)
