# MLops-Lab-Internal
# Online Payment Fraud Detection System

## 🌐 Project Access & Deployment Links

🚀 **Live FastAPI Swagger UI:**  
https://8000-m-s-euw4b3-3q2epebgdduab-b.europe-west4.prod.r.colab.dev/docs

❤️ **API Health Check:**  
https://8000-m-s-euw4b3-3q2epebgdduab-b.europe-west4.prod.r.colab.dev/health

📊 **API Metrics:**  
https://8000-m-s-euw4b3-3q2epebgdduab-b.europe-west4.prod.r.colab.dev/metrics

📈 **Grafana Dashboard:**  
Online Payment Fraud Detection Monitoring

📉 **Data Drift Report:**  
https://github.com/akhila-55/MLops-Lab-Internal/blob/main/data_drift_report.html

💻 **Google Colab Notebook:**  
https://colab.research.google.com/drive/1cBL8KB8kusUT4NWbBHHQml0nCeXLNS0o

🐙 **GitHub Repository:**  
https://github.com/akhila-55/MLops-Lab-Internal

## 📌 Project Overview

This project develops and monitors a Machine Learning-Based Online Payment Fraud Detection System using the provided reference and current transaction datasets.

The system uses a Random Forest classifier to predict potentially fraudulent transactions and FastAPI to provide prediction services.

Prometheus and Grafana are integrated for application monitoring, while Evidently AI is used to detect changes in transaction data.

## 🚀 Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Prometheus
- Grafana
- Evidently AI
- Google Colab
- GitHub

## ⚙️ Key Features

- Data preprocessing and missing-value handling
- Feature engineering
- Random Forest model training
- Fraud prediction through REST API
- API health monitoring
- Prometheus metrics collection
- Grafana monitoring dashboard
- Dataset drift detection using Evidently AI

## 📊 Model Evaluation

- Model: Random Forest Classifier
- Test Accuracy: 96.36%
- Fraud Precision: 0%
- Fraud Recall: 0%
- Fraud F1-score: 0%

**Evaluation Insight:** Although the model achieved high accuracy, it failed to identify fraudulent transactions in the test dataset. Further model improvements are necessary.

## 📉 Dataset Drift Analysis

- Reference dataset: 1,100 transactions
- Current dataset: 350 transactions
- Total monitored columns: 12
- Drifted columns: 7
- Drift share: 58.33%

Dataset drift was detected using Evidently AI.

## 📊 Monitoring Dashboard

Grafana dashboard panels:

1. Total Transaction Requests
2. Fraud Prediction Count (prediction requests processed)
3. Application Errors
4. Transaction Response Time

Prometheus collects metrics from the FastAPI application.

## 👩‍💻 Author

**Developer:** Akhila Yalamandala  
**Department:** Computer Science and Engineering  
**University:** Vignan's Foundation for Science, Technology & Research
