# 📉 Customer Churn Analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4C72B0?style=flat)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plots-11557c?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)

> **Exploratory Data Analysis (EDA)** on the Telco Customer Churn dataset to uncover patterns and key drivers behind customer attrition.

---

## 📌 Project Overview

Customer churn is one of the biggest challenges in the telecom industry. This project dives deep into the **IBM Telco Customer Churn dataset** to understand *why* customers leave — and what characteristics they share.

Using Python-based EDA, this analysis identifies behavioral patterns, high-risk customer segments, and actionable insights that could guide retention strategies.

---

## ✨ Features

- 🧹 **Data Cleaning & Preprocessing** — handled missing values, fixed data types, and prepared the dataset for analysis
- 📊 **Exploratory Data Analysis (EDA)** — univariate, bivariate, and multivariate analysis
- 🎨 **Data Visualization** — rich charts using Seaborn & Matplotlib
- 🔥 **Correlation Heatmap** — identified relationships between features
- 🔎 **Outlier Detection** — using both Z-Score and IQR methods
- 👤 **Customer Behavior Analysis** — across tenure, contract type, services used, and payment method

---

## 💡 Key Insights

| # | Insight |
|---|---------|
| 1 | 📅 **Month-to-month** contract customers have the highest churn rate |
| 2 | 👴 **Senior citizens** are more likely to churn than younger customers |
| 3 | ⏳ Customers with **low tenure** (new customers) churn significantly more |
| 4 | 🛡️ Customers subscribed to **value-added services** (e.g., tech support, online backup) show lower churn |
| 5 | 💳 **Electronic check** users exhibit higher churn compared to other payment methods |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Pandas** | Data manipulation & analysis |
| **NumPy** | Numerical computations |
| **Matplotlib** | Base plotting library |
| **Seaborn** | Statistical data visualization |
| **SciPy** | Z-score based outlier detection |

---

## 📁 Project Structure

```
customer-churn-analysis-python/
│
├── main.py                  # Main analysis script
├── requirements.txt         # Project dependencies
├── data/                    # Dataset files
│   └── telco_churn.csv
└── plots/                   # Generated visualizations
    ├── churn_count.png
    ├── correlation_heatmap.png
    └── ...
```

---

## 📊 Sample Visualizations

### 📈 Churn Overview
| | |
|---|---|
| ![Churn Count](plots/churn_count.png) | ![Churn Percentage](plots/churn_percentage.png) |

### 👤 Customer Demographics
| | |
|---|---|
| ![Churn by Gender](plots/churn_gender.png) | ![Churn by Senior Citizen](plots/churn_senior.png) |
| ![Senior Citizen %](plots/seniorcitizen_percentage.png) | |

### 📋 Contract & Payment
| | |
|---|---|
| ![Contract Churn](plots/contract_churn.png) | ![Payment Method](plots/payment_method.png) |

### 🛠️ Services & Tenure
| | |
|---|---|
| ![Services Analysis](plots/services_analysis.png) | ![Tenure Distribution](plots/tenure_hist.png) |

### 📦 Outlier Detection (Boxplots)
| | | |
|---|---|---|
| ![Monthly Charges](plots/boxplot_MonthlyCharges.png) | ![Tenure](plots/boxplot_tenure.png) | ![Total Charges](plots/boxplot_TotalCharges.png) |

### 🔥 Correlation Heatmap
![Correlation Heatmap](plots/correlation_heatmap.png)

---

## ⚙️ Installation & How to Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/customer-churn-analysis-python.git
cd customer-churn-analysis-python
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the analysis**
```bash
python main.py
```

> 📌 Generated plots will be saved in the `plots/` directory.

---

## 🚀 Future Improvements

- [ ] Build a **churn prediction model** using Logistic Regression or Random Forest
- [ ] Add an **interactive dashboard** using Plotly or Streamlit
- [ ] Perform **feature engineering** to improve predictive power
- [ ] Include **customer segmentation** using clustering (K-Means)
- [ ] Deploy the model as a **REST API**

---

## 👨‍💻 Author

**Shashank Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)](https://github.com/your-username/customer-churn-analysis-python)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/your-profile)

---

> ⭐ *If you found this project helpful, consider giving it a star on GitHub!*