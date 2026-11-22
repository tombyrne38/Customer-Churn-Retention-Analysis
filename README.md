## 🚀 Live Interactive App

[Try the Customer Churn Prediction App](https://customer-churn-retention-analysis-69jxeqkrrj4466fqdidxjt.streamlit.app)

Customer Churn & Retention Analysis

Python | Pandas | Seaborn | Matplotlib | Exploratory Data Analysis

Project Overview

This project analyses the IBM Telco Customer Churn dataset to identify customer characteristics associated with churn and develop evidence-based recommendations for improving customer retention.

The analysis focuses on understanding customer behaviour and translating data insights into actionable business recommendations.

Business Problem

Customer churn can reduce recurring revenue and increase customer acquisition costs.

The objective of this project is to answer three business questions:

How does contract type relate to customer churn?

Are newer customers more likely to leave?

Are higher monthly charges associated with increased churn?

Dataset

Source: IBM Telco Customer Churn dataset

7,043 customer records

21 original variables

Overall churn rate: 26.54%

1,869 customers classified as churned

The dataset includes customer demographics, subscription services, contract information, monthly charges and churn status.

Tools and Technologies

Python

Pandas — data cleaning and analysis

Seaborn — data visualisation

Matplotlib — chart creation and formatting

Google Colab — development environment

Data Cleaning

The following data preparation steps were performed:

Investigated missing values.

Converted TotalCharges from text to numeric format.

Identified 11 missing TotalCharges values associated with customers with zero months of tenure.

Replaced these missing values with zero.

Confirmed there were no duplicate customer IDs.

Verified that no missing values remained.

Key Findings

1. Contract Type and Customer Churn

Contract Type

Churn Rate

Month-to-month

42.71%

One year

11.27%

Two year

2.83%

Month-to-month customers showed substantially higher churn rates than customers on longer contracts.

2. Customer Tenure and Churn

Customer Tenure

Churn Rate

0–12 months

47.44%

13–24 months

28.71%

25–48 months

20.39%

49–72 months

9.51%

Customers with shorter tenure showed higher churn rates, suggesting that early customer retention warrants particular attention.

3. Monthly Charges and Churn

Monthly Charges

Churn Rate

Low (0–35)

10.89%

Medium (35–70)

23.94%

High (70+)

35.36%

Higher monthly charges were associated with higher churn rates.

Business Recommendations

1. Encourage longer-term customer relationships

Investigate loyalty incentives and contract upgrade offers for month-to-month customers. Test whether these interventions improve retention.

2. Strengthen first-year customer engagement

Develop a proactive onboarding and customer support programme focused on the first 12 months.

3. Improve perceived value for higher-paying customers

Investigate customer satisfaction, pricing concerns and service quality among higher-paying customer segments. Test targeted retention offers.

Limitations

This analysis identifies associations rather than causal relationships. Other customer characteristics may influence the observed patterns.

The findings are descriptive and should be validated through further analysis or controlled experiments before implementing company-wide retention strategies.

Future Development — Phase 2

Future work could include:

Predictive churn modelling using machine learning.

Customer risk segmentation.

Model evaluation and interpretation.

Estimating the potential financial impact of retention interventions.

View the Analysis

Open Customer_Churn_Retention_Analysis.ipynb in this repository to view the Python code, data cleaning process, charts and analysis.

Project Outcome

This project demonstrates practical skills in data cleaning, exploratory data analysis, visualisation and translating analytical findings into business recommendations.
