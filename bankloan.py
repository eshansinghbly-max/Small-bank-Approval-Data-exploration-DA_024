"""
Bank Loan Approval - Data Exploration
-------------------------------------
Project ID : DA-024        Group ID : BTech_DA_06
Mentor     : Puneet Arora  B.Tech CSE, Semester III, Section F

What this program does, step by step:
  1. Reads the loan data from bankloan.csv
  2. Checks the data (size, types, missing values, duplicates)
  3. Calculates how many loans were approved and rejected
  4. Compares approvals by credit history, education and property area
  5. Draws four charts and saves them in the "outputs" folder

This is an exploration only. It does NOT decide anything about real loan applicants.
"""

import os

import pandas as pd
import matplotlib

# Use a backend that only saves pictures, so the program also works
# on computers without a screen. Set SHOW_CHARTS = True to open the charts in a window.
SHOW_CHARTS = False
if not SHOW_CHARTS:
    matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

DATA_FILE = "bankloan.csv"
OUTPUT_FOLDER = "outputs"


def save_chart(file_name):
    """Save the current chart inside the outputs folder, then close it."""
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, file_name), dpi=150)
    if SHOW_CHARTS:
        plt.show()
    plt.close()


def main():
    # Make sure the folder for charts exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # ------------------------------------------------------------------
    # Step 1: Load the dataset
    # ------------------------------------------------------------------
    df = pd.read_csv(DATA_FILE)

    print("BANK LOAN APPROVAL DATASET")
    print("=" * 40)

    print("\nFirst 5 records:")
    print(df.head())

    print("\nDataset shape (rows, columns):")
    print(df.shape)

    # ------------------------------------------------------------------
    # Step 2: Understand and check the data
    # ------------------------------------------------------------------
    print("\nColumn names and data types:")
    df.info()

    print("\nStatistical summary of number columns:")
    print(df.describe())

    print("\nMissing values in each column:")
    print(df.isnull().sum())

    print("\nNumber of duplicate rows:")
    print(df.duplicated().sum())

    # ------------------------------------------------------------------
    # Step 3: How many loans were approved and rejected?
    # Loan_Status: Y = approved, N = rejected
    # ------------------------------------------------------------------
    print("\nLoan status count:")
    print(df["Loan_Status"].value_counts())

    total = len(df)
    approved = (df["Loan_Status"] == "Y").sum()
    rejected = (df["Loan_Status"] == "N").sum()

    print("\nTotal applicants:", total)
    print("Approved loans  :", approved)
    print("Rejected loans  :", rejected)

    # Only calculate percentages if there is at least one row
    if total > 0:
        print("Approval rate   :", round(approved / total * 100, 2), "%")
        print("Rejection rate  :", round(rejected / total * 100, 2), "%")

    # ------------------------------------------------------------------
    # Step 4: Compare approval across groups
    # A crosstab counts how many Y and N fall in each group.
    # ------------------------------------------------------------------
    print("\nLoan status by credit history (1 = good history, 0 = not good):")
    print(pd.crosstab(df["Credit_History"], df["Loan_Status"]))

    print("\nLoan status by education:")
    print(pd.crosstab(df["Education"], df["Loan_Status"]))

    print("\nLoan status by property area:")
    print(pd.crosstab(df["Property_Area"], df["Loan_Status"]))

    # ------------------------------------------------------------------
    # Step 5: Draw and save the charts
    # ------------------------------------------------------------------
    sns.set_theme(style="whitegrid")

    # Chart 1: total approved vs rejected
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x="Loan_Status")
    plt.title("Loan Approval vs Rejection")
    plt.xlabel("Loan Status (Y = approved, N = rejected)")
    plt.ylabel("Number of Applicants")
    save_chart("loan_status.png")

    # Chart 2: approval by credit history
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x="Credit_History", hue="Loan_Status")
    plt.title("Loan Status by Credit History")
    plt.xlabel("Credit History (1 = good, 0 = not good)")
    plt.ylabel("Number of Applicants")
    save_chart("credit_history.png")

    # Chart 3: approval by education
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x="Education", hue="Loan_Status")
    plt.title("Loan Status by Education")
    plt.ylabel("Number of Applicants")
    save_chart("education_analysis.png")

    # Chart 4: how applicant income is spread out
    plt.figure(figsize=(7, 5))
    sns.histplot(data=df, x="ApplicantIncome", bins=10, kde=True)
    plt.title("Applicant Income Distribution")
    plt.xlabel("Applicant Income")
    plt.ylabel("Number of Applicants")
    save_chart("income_distribution.png")

    print("\nCharts saved in the '" + OUTPUT_FOLDER + "' folder.")
    print("Analysis completed successfully!")


if __name__ == "__main__":
    main()
