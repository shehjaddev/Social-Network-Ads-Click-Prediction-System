# Social Network Ads Click Prediction

## Project Overview

This project is an **end-to-end Machine Learning application** that predicts whether a user is likely to click or purchase an advertisement based on their demographic information.

The goal is to demonstrate a **complete, production-style ML workflow**, starting from raw data and ending with a deployed, interactive web application. The system is designed to be simple, interpretable, and reliable, reflecting how such models are commonly used in real-world digital marketing and advertising platforms.

---

## Problem Statement

Digital advertising platforms need to efficiently target users who are most likely to engage with advertisements.

Given user attributes such as age, gender, and estimated salary, this project aims to predict:

> **Will a user click or purchase an advertisement?**

This is formulated as a **binary classification problem**:
- `0` → User did not purchase the advertisement  
- `1` → User purchased the advertisement  

---

## Dataset Description

- **Dataset Name:** Social Network Ads  
- **Source:** Kaggle  
- **Data Type:** Tabular  
- **Target Variable:** `Purchased`  

### Dataset Features

| Feature | Description |
|------|------------|
| User ID | Unique identifier (removed during preprocessing) |
| Gender | Gender of the user (Male / Female) |
| Age | Age of the user |
| EstimatedSalary | Estimated annual salary |
| Purchased | Target label indicating ad purchase |

---

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Gradio
- Joblib
- Hugging Face Spaces

---

## Machine Learning Workflow

### Data Preparation
The following preprocessing steps are applied:
1. Removal of irrelevant identifiers
2. Encoding of categorical variables
3. Feature–target separation
4. Train–test splitting
5. Feature scaling
6. Integration of preprocessing into a pipeline

### Model Development
- **Algorithm Used:** Logistic Regression
- Chosen for its interpretability, efficiency, and suitability for binary classification problems commonly found in advertising analytics.

### Model Evaluation
The trained model is evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Cross-validation and hyperparameter tuning are used to ensure robustness and optimal performance.

---

## Web Application

An interactive **Gradio-based web interface** allows users to:
- Select gender
- Enter age
- Enter estimated salary

The application then predicts whether the user is likely to purchase the advertisement.

---

## Deployment

The application is deployed on **Hugging Face Spaces** and is publicly accessible.

**Live Demo:**  
👉 *https://huggingface.co/spaces/shehjaddev/Social-Network-Ads-Click-Prediction-System*

---

## Project Structure

```
Social-Network-Ads-Click-Prediction-System/
│
├── app.py                  # Gradio web application
├── model.pkl               # Trained machine learning model
├── requirements.txt        # Python dependencies
├── Social_Network_Ads.csv  # Dataset
├── notebook.ipynb          # Model development notebook
└── README.md               # Project documentation
```

---

## Running the Project Locally

1. Clone the repository:
```bash
git clone https://github.com/shehjaddev/Social-Network-Ads-Click-Prediction-System.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the application:
```bash
python app.py
```

---

## Conclusion

This project demonstrates how a machine learning model can be developed, evaluated, and deployed as a usable application. It showcases best practices such as pipeline-based preprocessing, cross-validation, and reproducible deployment, making it suitable as a foundation for real-world advertisement targeting systems.

---
