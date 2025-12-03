# AGENTS Workflow Trace

## Agent 1 — Data Preparation
1. 載入 dataset
2. 資料清理與確認欄位格式
3. TF-IDF 向量化

## Agent 2 — Model Training
1. 分割 train/test
2. 訓練 Logistic Regression
3. 訓練 Naive Bayes
4. 訓練 Linear SVM
5. 儲存 joblib 模型

## Agent 3 — Model Evaluation
1. 使用 test set 評估
2. classification report
3. confusion matrix

## Agent 4 — Deployment
1. Streamlit Web App
2. 單筆偵測
3. 隨機測試
4. 模型視覺化
