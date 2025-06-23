import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib
import re
from scipy.sparse import hstack

# Load dataset
df = pd.read_csv("malicious_phish.csv")
df['label'] = df['type'].map({'benign': 0, 'defacement': 1, 'phishing': 1})
df.dropna(subset=['label'], inplace=True)
df['label'] = df['label'].astype(int)

# Feature Engineering
df['url_length'] = df['url'].apply(len)
df['digit_count'] = df['url'].apply(lambda x: sum(c.isdigit() for c in x))
df['has_ip'] = df['url'].str.contains(r'(?:\d{1,3}\.){3}\d{1,3}', regex=True).astype(int)

# TF-IDF Vectorization
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(df['url'])

# Combine features
custom_features = df[['url_length', 'digit_count', 'has_ip']].values
X_combined = hstack([X_tfidf, custom_features])
y = df['label'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_combined, y, test_size=0.2, random_state=42, stratify=y
)

# Model training
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save model and components
joblib.dump(model, "url_model.pkl")
joblib.dump(tfidf, "vectorizer.pkl")
joblib.dump(X_tfidf.shape[1], "tfidf_feature_count.pkl")
print("✅ Model and vectorizer saved successfully.")
