# expense-intelligence-system
Data analysis project that processes expense data, detects anomalies, analyzes trends, and predicts future spending using Python.

 Expense Intelligence System

Author: POPURI SAI VEDAGNA

Overview

The **Expense Intelligence System** is a Python-based data analytics project that analyzes personal spending data using **Pandas** and **Matplotlib**.

The system validates the structure of the dataset, cleans the data, performs statistical analysis, detects unusual spending patterns, and predicts future expenses based on historical trends.

This project demonstrates core **data analysis workflows**, including data validation, aggregation, anomaly detection, trend analysis, and visualization.

---

Features

* CSV schema validation
* Data cleaning and preprocessing
* Category-wise spending analysis
* Daily spending statistics
* Monthly trend analysis
* Detection of unusually high spending days (anomaly detection)
* Prediction of next month's expected budget
* Data visualization using Matplotlib

---

Project Structure

```
expense-intelligence-system
│
├── expense_intelligence.py
├── expenses.csv
└── README.md
```

---

Required CSV Format

The system expects the dataset to follow the schema below:

```
category,date,amount,description
```

Example

```
category,date,amount,description
food,2026-03-01,200,lunch
transport,2026-03-01,50,bus fare
shopping,2026-03-02,800,clothes
food,2026-03-03,150,snacks
```

If the dataset does not match this schema, the system raises an error to ensure data integrity.

---

Technologies Used

* Python
* Pandas
* Matplotlib

---

Analysis Performed

The system performs the following analyses:

Total Spending

Calculates the total amount spent across all transactions.

Average Daily Spending

Computes the average spending per day based on daily aggregated expenses.

Category Analysis

Aggregates spending by category to identify which categories contribute most to expenses.

Monthly Trend Detection

Groups spending by month to observe spending patterns over time.

Anomaly Detection

Detects unusually high spending days using statistical thresholds.

Budget Prediction

Estimates next month's expected spending based on historical monthly trends.

---

How to Run the Project

1. Install Dependencies

```
pip install pandas matplotlib
```

2. Place Dataset

Place `expenses.csv` in the project directory.

3. Run the Program

```
python expense_intelligence.py
```

The program will display spending insights in the terminal and generate visualizations.

---

 Example Output

The system outputs:

* Total spending
* Average daily spending
* Highest and lowest spending days
* Category-wise spending breakdown
* Monthly trend data
* Detected anomalies
* Predicted next month's budget


 Possible Future Improvements

* Machine learning based expense prediction
* Interactive dashboards using Streamlit
* Automated budget alerts
* Integration with financial APIs

---

License

This project is intended for educational and research purposes.

