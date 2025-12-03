# OpenSpec Project Specification

## 🎯 專案名稱
Email Spam Classification — 垃圾簡訊分類系統

## 📌 專案目標
建立一套可自動判斷訊息是否為垃圾的機器學習系統，並以 Streamlit 提供互動式介面。

## 📂 使用資料
`sms_final.csv`  
包含文字欄位 `text` 與標籤 `label`（ham/spam）

## 🧱 功能模組
- **資料前處理**：TF-IDF 向量化
- **模型訓練**：LogReg / NB / SVM
- **模型評估**：classification report / confusion matrix
- **Web 互動介面**：單筆偵測、Batch CSV、隨機抽樣
- **視覺化**：文字雲 / 指標報告

## 📑 文件輸出
- project.md
- AGENTS workflow trace
