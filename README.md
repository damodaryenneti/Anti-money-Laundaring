# Anti-Money Laundering (AML) Transaction Monitoring Using Artificial Neural Networks

## 1. Project Overview

Money laundering is a serious financial crime in which individuals or organizations attempt to disguise illegally obtained money as legitimate income through complex financial transactions.

Financial institutions process millions of transactions daily. Identifying suspicious transactions manually is challenging because of the high transaction volume, evolving fraud patterns, and complex relationships between transaction characteristics.

This project aims to develop an Artificial Neural Network (ANN)-based classification model to identify potentially suspicious financial transactions and distinguish them from legitimate transactions.

The model learns transaction patterns from historical transaction data and predicts whether a transaction should be flagged for further investigation.

## 2. Business Problem

Financial institutions face significant challenges in detecting money laundering activities because suspicious transactions are often hidden among large volumes of legitimate financial transactions.

Traditional rule-based monitoring systems depend on predefined conditions and thresholds, which may fail to identify complex or previously unseen transaction patterns.

Additionally, manual investigation requires considerable time and resources, making it difficult for compliance teams to efficiently prioritize suspicious transactions.

Therefore, there is a need for an intelligent, scalable, and data-driven transaction monitoring solution that can identify potentially suspicious financial activities and support anti-money laundering investigations.

## 3. Business Objectives

- Develop an ANN-based model to classify suspicious and legitimate financial transactions.
- Identify complex transaction patterns associated with potential money laundering.
- Reduce manual transaction screening efforts.
- Improve the identification of potentially suspicious transactions.
- Minimize false negatives to avoid missing suspicious financial activities.
- Support financial institutions in prioritizing transactions for investigation.
- Evaluate model performance using appropriate classification metrics.

## 4. Dataset Information

**Dataset:** Synthetic Transaction Monitoring Dataset (AML)

**Source:** Kaggle

**Dataset Link:** https://www.kaggle.com/datasets/berkanoztas/synthetic-transaction-monitoring-dataset-aml

The dataset contains synthetic financial transaction records designed for anti-money laundering research and suspicious transaction detection.

It includes transaction-related information that can be used to identify patterns associated with potentially suspicious financial activities.

## 5. Technologies Used

| Category | Tools / Libraries |
|---|---|
| Programming Language | Python |
| Development Environment | Jupyter Notebook |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow, Keras |
| Hyperparameter Optimization | Optuna |
| Model Evaluation | Scikit-learn |
| Model Deployment | Streamlit |
| Model Serialization | Pickle |

## 6. Project Workflow

1. Business Understanding
2. Data Understanding
3. Data Collection
4. Exploratory Data Analysis (EDA)
5. Data Cleaning and Preprocessing
6. Feature Engineering
7. Feature Selection
8. Handling Class Imbalance
9. ANN Model Building
10. Hyperparameter Optimization
11. Model Evaluation
12. Model Deployment

## 7. Data Preprocessing

The following preprocessing techniques are considered:

- Handling missing values.
- Removing duplicate records.
- Identifying and treating outliers where appropriate.
- Encoding categorical variables.
- Scaling numerical features.
- Selecting relevant transaction features.
- Handling imbalanced transaction classes using suitable techniques.
- Splitting data into training and testing sets.

## 8. ANN Model Development

An Artificial Neural Network is developed using TensorFlow and Keras.

The model consists of:

- Input Layer: Accepts transaction-related features.
- Hidden Layers: Learn complex patterns and relationships in transaction data.
- Activation Functions: Introduce non-linearity.
- Output Layer: Predicts the transaction class.

The ANN model is optimized using suitable hyperparameters, including:

- Number of hidden layers.
- Number of neurons.
- Learning rate.
- Batch size.
- Optimizer.
- Activation functions.

Optuna can be used to identify suitable hyperparameter configurations.

## 9. Model Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score
- Precision-Recall AUC

**Important:** Recall and Precision-Recall AUC are particularly important because suspicious transactions may represent a very small proportion of total transactions.

## 10. Expected Outcomes

- Automated classification of potentially suspicious transactions.
- Identification of unusual transaction patterns.
- Improved prioritization of transactions for investigation.
- Reduced dependence on manual initial screening.
- A scalable ANN-based transaction monitoring solution.

## 11. Project Structure

```text
AML_Transaction_Monitoring/
│
├── dataset/
│   └── transaction_data.csv
│
├── notebooks/
│   └── AML_ANN_Project.ipynb
│
├── models/
│   └── aml_ann_model.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

## 12. Installation and Execution

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd AML_Transaction_Monitoring
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 13. Business Impact

This project demonstrates how Artificial Neural Networks can support financial institutions in strengthening transaction monitoring processes.

By learning complex patterns from transaction data, the proposed model can help compliance teams identify potentially suspicious activities, prioritize investigations, and improve the efficiency of AML monitoring operations.

**Note:** The model provides risk-screening predictions and does not independently establish that a transaction involves money laundering. Human investigation and regulatory procedures remain essential.

## 14. Disclaimer

This project uses synthetic transaction data for educational and research purposes. Model predictions should not be treated as confirmed financial crime findings or used as the sole basis for regulatory or financial decisions.

---

**Developed as an Artificial Neural Networks (ANN) Project.**
