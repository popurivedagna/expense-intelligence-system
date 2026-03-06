"""
Expense Intelligence System
Author: POPURI SAI VEDAGNA

Description:
A Python-based expense analytics tool that performs:
- CSV schema validation
- data cleaning
- daily and monthly spending analysis
- anomaly detection
- simple budget prediction
- visualization of spending patterns
"""

import pandas as pd
import matplotlib.pyplot as plt

EXPECTED_COLUMNS = ["category", "date", "amount", "description"]


def load_data(filepath):
    df = pd.read_csv(filepath)

    if set(df.columns) != set(EXPECTED_COLUMNS):
        raise ValueError(
            f"CSV must contain columns: {EXPECTED_COLUMNS}"
        )

    df["date"] = pd.to_datetime(df["date"])

    return df


def clean_data(df):
    df = df.dropna(subset=["amount", "date", "category"])
    df["amount"] = pd.to_numeric(df["amount"])
    return df


def total_spending(df):
    return df["amount"].sum()


def average_daily_spending(df):
    daily = df.groupby("date")["amount"].sum()
    return daily.mean()


def category_analysis(df):
    return df.groupby("category")["amount"].sum().sort_values(ascending=False)


def monthly_trend(df):
    df["month"] = df["date"].dt.to_period("M")
    monthly = df.groupby("month")["amount"].sum()
    return monthly


def spending_extremes(df):
    daily = df.groupby("date")["amount"].sum()

    highest = daily.idxmax(), daily.max()
    lowest = daily.idxmin(), daily.min()

    return highest, lowest


def anomaly_detection(df):
    daily = df.groupby("date")["amount"].sum()

    mean = daily.mean()
    std = daily.std()

    anomalies = daily[daily > mean + 2 * std]

    return anomalies


def budget_prediction(df):
    df["month"] = df["date"].dt.to_period("M")
    monthly = df.groupby("month")["amount"].sum()

    if len(monthly) < 2:
        return "Not enough data for prediction"

    trend = monthly.diff().mean()

    prediction = monthly.iloc[-1] + trend

    return round(prediction, 2)


def plot_categories(categories):

    categories.plot(kind="bar")

    plt.title("Category Wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.tight_layout()
    plt.show()


def plot_monthly_trend(monthly):

    monthly.plot(marker="o")

    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Spending")

    plt.tight_layout()
    plt.show()


def main():

    filepath = "expenses.csv"

    df = load_data(filepath)

    df = clean_data(df)

    total = total_spending(df)

    avg_daily = average_daily_spending(df)

    categories = category_analysis(df)

    monthly = monthly_trend(df)

    highest, lowest = spending_extremes(df)

    anomalies = anomaly_detection(df)

    prediction = budget_prediction(df)

    print("\n----- Expense Summary -----\n")

    print("Total Spending:", total)

    print("Average Spending Per Day:", round(avg_daily, 2))

    print("\nHighest Spending Day:", highest[0], "Amount:", highest[1])

    print("Lowest Spending Day:", lowest[0], "Amount:", lowest[1])

    print("\nCategory Spending:\n")
    print(categories)

    print("\nMonthly Trend:\n")
    print(monthly)

    print("\nAnomalies (Unusually High Spending Days):\n")
    print(anomalies)

    print("\nPredicted Budget For Next Month:", prediction)

    plot_categories(categories)

    plot_monthly_trend(monthly)


if __name__ == "__main__":
    main()
