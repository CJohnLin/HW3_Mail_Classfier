
"""model_utils.py
Functions to load vectorizer and classifier and perform prediction.
"""
import joblib
import os

def load_resources(model_path: str, vec_path: str, label_map_path: str = None):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found: {model_path}")
    if not os.path.exists(vec_path):
        raise FileNotFoundError(f"Vectorizer not found: {vec_path}")
    model = joblib.load(model_path)
    vectorizer = joblib.load(vec_path)
    label_map = None
    if label_map_path and os.path.exists(label_map_path):
        import json
        label_map = json.load(open(label_map_path, 'r', encoding='utf-8'))
    return model, vectorizer, label_map

def infer_single(model, vectorizer, raw_text: str, normalize_fn):
    cleaned = normalize_fn(raw_text)
    X = vectorizer.transform([cleaned])
    pred = model.predict(X)[0]
    prob = None
    if hasattr(model, 'predict_proba'):
        prob = model.predict_proba(X)[0][1]
    return int(pred), float(prob) if prob is not None else None
