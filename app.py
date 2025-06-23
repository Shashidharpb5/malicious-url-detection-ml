import streamlit as st
import joblib
import numpy as np
import re
from scipy.sparse import hstack

# Load components
model = joblib.load("url_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
tfidf_feature_count = joblib.load("tfidf_feature_count.pkl")

def extract_features(urls):
    url_lengths = [len(u) for u in urls]
    digit_counts = [sum(c.isdigit() for c in u) for u in urls]
    has_ip = [1 if re.search(r'(?:\d{1,3}\.){3}\d{1,3}', u) else 0 for u in urls]
    return np.array([url_lengths, digit_counts, has_ip]).T

# Streamlit UI
st.set_page_config(page_title="Malicious URL Detector")
st.title("🔍 Malicious URL Detection")
st.write("Enter one or more URLs (one per line) below:")

url_input = st.text_area("URLs", height=150)

if st.button("Detect"):
    if url_input.strip():
        urls = [u.strip() for u in url_input.split("\n") if u.strip()]
        tfidf_vectors = vectorizer.transform(urls)

        if tfidf_vectors.shape[1] != tfidf_feature_count:
            st.error("TF-IDF feature mismatch. Please retrain the model with updated vectorizer.")
        else:
            custom_features = extract_features(urls)
            final_input = hstack([tfidf_vectors, custom_features])
            predictions = model.predict(final_input)

            st.subheader("Results")
            for url, pred in zip(urls, predictions):
                label = "🟢 Benign" if pred == 0 else "🔴 Malicious"
                st.write(f"**{url}** → {label}")
    else:
        st.warning("Please enter at least one URL.")