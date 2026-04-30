## end to end machine learning project
#  End-to-End Student Performance Prediction System

## 📌 Overview

This project is an end-to-end Machine Learning pipeline that predicts students' **math scores** based on demographic a
nd academic features. It includes data ingestion, preprocessing, model training, and deployment using Flask.


* End-to-End ML Pipeline (Data → Model → Deployment)
* Modular coding structure (pipeline + components)
* Real-time prediction using Flask web app
* Production-ready project structure

---

Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Flask
* HTML, CSS

---

## 📂 Project Structure

```bash
├── artifacts/
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│
├── static/
│   ├── style.css
│
├── templates/
│   ├── index.html
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

##  Features Used

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

---

# Output

* Predicted **Math Score**

## ⚙️ Workflow

1. Data ingestion and preprocessing
2. Feature engineering using pipeline
3. Model training and saving artifacts
4. Flask app for real-time prediction


