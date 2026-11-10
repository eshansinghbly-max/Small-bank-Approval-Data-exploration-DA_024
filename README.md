# Bank Loan Approval Data Exploration

**Project ID:** DA-024  |  **Group ID:** BTech_DA_06  |  **Program:** Data Analytics
**Course:** B.Tech Computer Science & Engineering, Semester III, Section F
**Mentor:** Puneet Arora

An exploratory data analysis (EDA) project in Python. It studies a small loan application dataset and shows how approval outcomes differ across credit history, education and property area.

> This is an academic project. It does not build a lending system and must not be used to decide real loan applications.

## What the project does

1. Loads the loan data from `bankloan.csv`
2. Checks data quality: shape, data types, missing values, duplicates
3. Calculates the approval and rejection rate
4. Compares outcomes by credit history, education and property area
5. Saves four charts in the `outputs/` folder

## Dataset

`bankloan.csv` has **50 loan applications** and **11 columns**:

| Column | Meaning |
|---|---|
| Loan_ID | Unique application ID |
| Gender, Married, Dependents | Applicant details |
| Education | Graduate / Not Graduate |
| Self_Employed | Yes / No |
| ApplicantIncome | Applicant income (unit not stated in the file) |
| LoanAmount | Loan amount (unit not stated in the file) |
| Credit_History | 1 = good history, 0 = not good |
| Property_Area | Urban / Semiurban / Rural |
| Loan_Status | Y = approved, N = rejected |

## How to run

```bash
# 1. Install the libraries
pip install -r requirements.txt

# 2. Run the analysis
python bankloan.py
```

Charts are saved in `outputs/`. To also open them in a window, set `SHOW_CHARTS = True` at the top of `bankloan.py`.

## Key findings

- 33 of 50 applications were approved (**66%**) and 17 were rejected (34%).
- No missing values and no duplicate rows.
- All 16 applicants with Credit_History 0 were rejected. 33 of the 34 with Credit_History 1 were approved.
- All 11 "Not Graduate" applicants were rejected, against 33 of 39 graduates approved.
- By property area, approvals were 13 of 16 in Semiurban, 13 of 18 in Urban and 7 of 16 in Rural.
- Applicant income ranges from 2,400 to 9,000 (average about 4,934).

**Limitations:** only 50 records, so small groups give unstable rates. These are patterns in recorded data, not proof of cause. The groups also overlap (for example credit history and education), so one factor cannot be separated from another here. Gender and marital status are sensitive fields in lending and are not used to draw conclusions.

## Folder structure

```
bankloan.py        main program, commented in simple language
bankloan.csv       dataset
requirements.txt   libraries needed
outputs/           charts and console_output.txt from one run
docs/              project report (.docx) and presentation (.pptx)
```

## Team

Sanskriti Saxena, Saksham Singh, Eshan Singh, Swarnima Singh, Amratya Tikkha, Shashwat Bahuguna, Abhinav Pradhan, Nihal Singh, Mayank Kumar, Himanshu, Vijay Verma, Anshul Kumawat, Rahul Kumar, Mayank Pratap Singh
