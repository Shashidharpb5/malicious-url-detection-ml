# 🔐 Malicious URLs Detection Using Machine Learning

A machine learning-based web app built using Django to detect whether a given URL is **malicious or safe**. It leverages multiple classification algorithms trained on URL features to help users stay protected from phishing and harmful sites.

---

## 🚀 Features

- 🧠 Trained with models like **SVM**, **Naive Bayes**, **Logistic Regression**, and **Decision Tree**
- 📊 Real-time predictions for user-entered URLs
- ⚙️ TF-IDF-based feature extraction on URL text
- 🖥️ User-friendly Django interface
- 🔍 Highlights model performance metrics
- 🔒 Sensitive data like AWS keys and datasets are excluded from the repo

---

## 🛠️ Tech Stack

| Tech         | Used For                       |
|--------------|--------------------------------|
| Python       | Core ML + backend logic        |
| Django       | Web framework                  |
| Scikit-learn | Machine Learning models        |
| Pandas       | Data loading and preprocessing |
| Pickle       | Model serialization            |
| HTML/CSS     | Frontend templates             |

---

## 📁 Folder Structure

project/
│
├── app.py # Django or Streamlit app
├── malicious_url_model.py # ML model logic
├── vectorizer.pkl # TF-IDF vectorizer
├── url_model.pkl # Trained ML model
├── tfidf_feature_count.pkl # Optional features info
├── templates/ # HTML templates
├── static/ # CSS/JS files
├── requirements.txt # Dependencies
└── .gitignore # Ignored files (incl. dataset)


---

## ⚙️🚀 How to Run the Project

Follow these simple steps to get the project running locally on your machine:

---

### 🧩 Step 1: Clone the Repository


git clone https://github.com/Shashidharpb5/malicious-url-detection-ml.git
cd malicious-url-detection-ml


## 📦 Step 2: Install All Dependencies
Make sure Python and pip are installed, then:

pip install -r requirements.txt
🧠 Tip: It's better to use a virtual environment

python -m venv venv
venv\Scripts\activate  # Windows


## 🚦 Step 3: Run the Application


python app.py
💡 For Django users: Use


python manage.py runserver


## 🌐 Step 4 (Optional): Open in Browser
Once running, open your browser and go to:

http://localhost:8000
You should see the Malicious URL Detector in action!



## 📊 Machine Learning Models

## Model	                    Accuracy (%)
SVM	                        96.12
Naive Bayes	                ~92
Logistic Regression	        ~93.5
Decision Tree	            ~90

The models were trained using TF-IDF vectorized features from the dataset of ~61,000 URLs.


## 📁 Dataset

Due to security reasons, the original dataset (malicious_phish.csv) has been excluded from the repository.
You can request a sample or download a similar one from Kaggle or other public sources.


## 🧑‍💻 Developed By

**Shashidhar Pinnamshetty**  
B.Tech in AI & ML | CMR Engineering College  
🔗 [Portfolio](https://shashidharpb5.github.io) • [GitHub](https://github.com/shashidharpb5) • [LinkedIn](https://linkedin.com/in/shashidharpb5)


## 📄 License
This project is licensed under the MIT License — feel free to use and modify with credit.

