# Hospital Readmission Prediction

A machine learning project that predicts the risk of hospital readmission using patient-related and healthcare-utilization data.

## Project Overview

This project uses a Random Forest classification model to predict whether a patient is likely to be readmitted to the hospital. It includes data preprocessing, exploratory data analysis, model optimization, evaluation, and deployment through a Flask web application.

## Features

* Data preprocessing and exploratory data analysis
* Random Forest classification
* Hyperparameter tuning and regularization
* Cross-validation
* Probability-threshold optimization
* Interactive Flask web application
* Probability-based readmission risk prediction

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* Joblib
* Matplotlib
* Seaborn

## Model Performance

* ROC-AUC: Approximately 0.66
* Recall for readmitted patients: Approximately 89%
* Model: Regularized Random Forest Classifier

> **Note:** The model is intended for educational purposes only. It is not a clinical diagnostic tool and should not be used for medical decision-making.

## Project Structure

```text
hospital_readmission_prediction/
│
├── app.py
├── readmission_model.pkl
├── train.csv
├── Hospital_Readmission_Analysis.ipynb
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/hospital-readmission-prediction.git
cd hospital-readmission-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask application

```bash
python app.py
```

### 4. Open the application

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

## Workflow

1. Load and inspect the dataset.
2. Perform data preprocessing and exploratory analysis.
3. Train and evaluate classification models.
4. Apply regularization and cross-validation.
5. Optimize the prediction threshold using validation data.
6. Save the trained model using Joblib.
7. Deploy the model using Flask.

## Disclaimer

This project is developed for educational and portfolio purposes. The predictions should not be interpreted as medical advice or used for clinical decisions.
