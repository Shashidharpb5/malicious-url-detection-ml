# 🔐 Malicious URLs Detection Using Machine Learning

A machine learning-based web app built using Django to detect whether a given URL is **malicious or safe**.  
It leverages multiple classification algorithms trained on URL features to help users stay protected from phishing and harmful sites.

---

## 🚀 Features

- 🧠 Trained with models like **SVM**, **Naive Bayes**, **Logistic Regression**, and **Decision Tree**  
- 📊 Real-time predictions for user-entered URLs  
- ⚙️ TF-IDF-based feature extraction  
- 🖥️ Simple and interactive UI built with Django  
- 🔍 Highlights model performance metrics  
- 🔒 Sensitive data like AWS keys and datasets are excluded from the repo  

---

## 🛠️ Tech Stack

| Tech          | Used For                       |
|---------------|--------------------------------|
| Python        | Core ML + backend logic        |
| Django        | Web framework                  |
| Scikit-learn  | Machine Learning models        |
| Pandas        | Data loading and preprocessing |
| Pickle        | Model serialization            |
| HTML / CSS    | Frontend templates             |

---

## 📁 Project Structure

project/
│
├── app.py # Web app entry point
├── malicious_url_model.py # ML model logic
├── vectorizer.pkl # TF-IDF vectorizer
├── url_model.pkl # Trained model
├── tfidf_feature_count.pkl # Optional features info
├── templates/ # HTML templates
├── static/ # CSS/JS files
├── requirements.txt # Dependencies
└── .gitignore # Git ignore rules

---

## ⚙️🚀 How to Run the Project

## Follow these simple steps to run it locally on your machine:


### 🧩 Step 1: Clone the Repository


git clone https://github.com/Shashidharpb5/malicious-url-detection-ml.git
cd malicious-url-detection-ml

## 📦 Step 2: Install Dependencies
Make sure Python and pip are installed.

pip install -r requirements.txt

💡 Use a virtual environment for cleaner setup


python -m venv venv
venv\Scripts\activate  # On Windows

## 🚦 Step 3: Run the Application

python app.py

📝 If Django is used instead:


python manage.py runserver

## 🌐 Step 4 (Optional): Open in Browser

http://localhost:8000
You’ll now see the Malicious URL Detector in action 🚀

## 📊 Model Comparison

| Model               | Accuracy (%) |
|---------------------|--------------|
| Support Vector Machine (SVM) | **96.12**       |
| Naive Bayes         | ~92          |
| Logistic Regression | ~93.5        |
| Decision Tree       | ~90          |

🧠 *All models were trained on a dataset of ~61,000 URLs using TF-IDF feature extraction.*


## 📁 Dataset Note

Dataset (malicious_phish.csv) is not included in this repo due to size and security concerns.
You may download a similar dataset from Kaggle.


## 🧑‍💻 Developed By

**Shashidhar Pinnamshetty**  
B.Tech in AI & ML | CMR Engineering College

🔗 [🌐 Portfolio](https://shashidharpb5.github.io)  
🔗 [🐙 GitHub](https://github.com/shashidharpb5)  
🔗 [💼 LinkedIn](https://linkedin.com/in/shashidharpb5)


## 📄 License
This project is licensed under the MIT License — feel free to use, modify, and share with credit.