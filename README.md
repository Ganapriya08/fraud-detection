# Fraud Detection System

## Overview

The Fraud Detection System is a machine learning-based application designed to identify potentially fraudulent transactions. The system analyzes transaction data, extracts meaningful patterns, and predicts whether a transaction is legitimate or fraudulent. A user-friendly Streamlit dashboard allows users to upload data and view predictions in real time.

## Features

* Data preprocessing and cleaning
* Fraud detection using Machine Learning algorithms
* Real-time prediction through an interactive Streamlit dashboard
* Data visualization and analytics
* CSV file upload support
* Fraud probability and classification results
* Easy-to-use web interface

## Project Structure

```text
fraud-detection/
│
├── dashboard.py              # Streamlit dashboard
├── model_training.py         # Model training script
├── fraud_model.pkl           # Trained ML model
├── scaler.pkl                # Feature scaler
├── dataset/
│   └── transactions.csv
│
├── notebooks/
│   └── fraud_detection.ipynb
│
├── requirements.txt
├── README.md
└── assets/
    └── screenshots/
```

## Technologies Used

* Python 3.x
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib

## Installation

### Clone the Repository

```bash
git clone https://github.com/Ganapriya08/fraud-detection.git
cd fraud-detection
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Launch the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

The application will start locally and open in your browser.

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning and Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Fraud Prediction
7. Dashboard Deployment

## Model Evaluation Metrics

The model performance is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC-AUC Score

## Sample Usage

1. Open the Streamlit dashboard.
2. Upload a transaction dataset.
3. Click on the Predict button.
4. View fraud detection results and visualizations.

## Future Enhancements

* Deep Learning-based fraud detection
* Real-time transaction monitoring
* API integration
* Cloud deployment
* Advanced anomaly detection techniques
* Automated model retraining

## Screenshots

Add screenshots of the dashboard inside the `assets/screenshots` folder and include them here.

## Author

**Ganapriya**

GitHub: https://github.com/Ganapriya08

## License

This project is intended for educational and research purposes.
