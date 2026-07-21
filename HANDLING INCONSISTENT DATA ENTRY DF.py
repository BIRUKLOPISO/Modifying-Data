import pandas as pd
import numpy as np
from datetime import datetime

print("=" * 60)
print("TOPIC 11: WORKING WITH DATETIME DATA")
print("=" * 60)

# ============================================
# QUESTION 1: Employee Data - Date Components and Calculations
# ============================================
print("\n" + "=" * 60)
print("QUESTION 1: Employee Data - Date Components and Calculations")
print("=" * 60)

employee_data = pd.DataFrame({
    'employee_id': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'hire_date': ['2024-01-15', '2024-02-20', '2024-03-10', '2024-04-05', '2024-05-12'],
    'birth_date': ['1990-05-15', '1985-08-20', '1992-11-03', '1988-02-28', '1995-07-15'],
    'last_review_date': ['2024-06-01', '2024-07-15', '2024-05-20', '2024-04-30', '2024-06-30']
})

print("\nEmployee Data:")
print(employee_data)

# 1a - Convert dates to datetime
employee_data['hire_date'] = pd.to_datetime(employee_data['hire_date'], errors='coerce')
employee_data['birth_date'] = pd.to_datetime(employee_data['birth_date'], errors='coerce')
employee_data['last_review_date'] = pd.to_datetime(employee_data['last_review_date'], errors='coerce')

# 1b - Calculate tenure in days
employee_data['tenure_days'] = (pd.Timestamp.now() - employee_data['hire_date']).dt.days

# 1c - Calculate tenure in months
employee_data['tenure_months'] = (pd.Timestamp.now() - employee_data['hire_date']).dt.days // 30

# 1d - Calculate age in years
employee_data['age_years'] = (pd.Timestamp.now() - employee_data['birth_date']).dt.days // 365

# 1e - Extract date components
employee_data['hire_year'] = employee_data['hire_date'].dt.year
employee_data['hire_month'] = employee_data['hire_date'].dt.month
employee_data['hire_day'] = employee_data['hire_date'].dt.day
employee_data['hire_month_name'] = employee_data['hire_date'].dt.month_name()

print("\nAfter date conversion and calculations:")
print(employee_data)

# ============================================
# QUESTION 2: Sales Data - Filtering and Date Range Analysis
# ============================================
print("\n" + "=" * 60)
print("QUESTION 2: Sales Data - Filtering and Date Range Analysis")
print("=" * 60)

np.random.seed(42)
sales_data = pd.DataFrame({
    'order_id': range(1, 101),
    'order_date': pd.date_range('2024-01-01', periods=100, freq='D'),
    'sales_amount': np.random.randint(100, 500, 100),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Home'], 100),
    'customer_region': np.random.choice(['North', 'South', 'East', 'West'], 100)
})

print("\nSales Data (first 5 rows):")
print(sales_data.head())

# 2a - Extract day of week and quarter
sales_data['day_of_week'] = sales_data['order_date'].dt.day_name()
sales_data['quarter'] = sales_data['order_date'].dt.quarter

# 2b - Filter Q2 2024 (April 1 to June 30)
start_date = pd.to_datetime('2024-04-01')
end_date = pd.to_datetime('2024-06-30')
q2_sales = sales_data[(sales_data['order_date'] >= start_date) & (sales_data['order_date'] <= end_date)]

print("\n2b. Q2 2024 Sales (first 5 rows):")
print(q2_sales.head())

# 2c - Filter weekend orders
weekends = sales_data['order_date'].dt.weekday >= 5
weekend_sales = sales_data[weekends]

print("\n2c. Weekend orders (first 5 rows):")
print(weekend_sales.head())

# 2d - Calculate total sales by month
sales_data['month'] = sales_data['order_date'].dt.to_period('M')
monthly_sales = sales_data.groupby('month')['sales_amount'].sum()

print("\n2d. Monthly sales totals:")
print(monthly_sales)

# 2e - Resample to weekly average
sales_indexed = sales_data[['order_date', 'sales_amount']].copy()
sales_indexed.set_index('order_date', inplace=True)
weekly_avg = sales_indexed.resample('W').mean()

print("\n2e. Weekly average sales (first 5 rows):")
print(weekly_avg.head())

# ============================================
# QUESTION 3: Customer Data - Date Arithmetic and Time-Based Features
# ============================================
print("\n" + "=" * 60)
print("QUESTION 3: Customer Data - Date Arithmetic and Time-Based Features")
print("=" * 60)

customer_data = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['John', 'Sarah', 'Mike', 'Emily', 'David', 'Lisa'],
    'first_purchase': ['2023-01-15', '2023-06-20', '2024-01-10', '2023-11-05', '2024-02-15', '2023-08-22'],
    'last_purchase': ['2024-06-01', '2024-01-15', '2024-06-15', '2023-12-20', '2024-06-10', '2024-03-01'],
    'total_spent': [1500, 800, 2200, 1200, 1800, 500]
})

print("\nCustomer Data:")
print(customer_data)

# 3a - Convert dates to datetime
customer_data['first_purchase'] = pd.to_datetime(customer_data['first_purchase'])
customer_data['last_purchase'] = pd.to_datetime(customer_data['last_purchase'])

# 3b - Calculate customer lifetime in days
customer_data['customer_lifetime_days'] = (customer_data['last_purchase'] - customer_data['first_purchase']).dt.days

# 3c - Calculate days since last purchase
customer_data['days_since_last_purchase'] = (pd.Timestamp.today() - customer_data['last_purchase']).dt.days

# 3d - Create active flag (purchased within last 30 days)
customer_data['active'] = (pd.Timestamp.now() - customer_data['last_purchase']).dt.days <= 30

# 3e - Create year_month from last_purchase
customer_data['year_month'] = customer_data['last_purchase'].dt.strftime('%Y-%m')

print("\nAfter date calculations:")
print(customer_data)
