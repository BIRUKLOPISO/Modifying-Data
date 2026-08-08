import pandas as pd
import numpy as np

print("=" * 60)
print("PART 5: ADDING/MODIFYING COLUMNS")
print("=" * 60)

# Create the sample DataFrame used for Questions 1-3
df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [1000, 25, 75, 300, 50],
    'Quantity': [10, 200, 50, 20, 150]
})

print("Sample DataFrame:")
print(df)
print("\n" + "=" * 60)

# ============================================
# QUESTION 1
# ============================================
# Write code to:
# a) Add a new column 'Total_Revenue' = Price * Quantity
# b) Add a new column 'Discounted_Price' with 10% off the original Price
# c) Add a new column 'In_Stock' with all values set to True
# d) Add a new column 'Category' where Electronics products (Laptop, Monitor)
#    get 'Electronics', others get 'Accessories'

print("\n--- QUESTION 1 ---")
# YOUR ANSWER CODE:
df['Total_Revenue'] = df['Price'] * df['Quantity']
df['Discounted_Price'] = df['Price'] * 0.9
df['In_Stock'] = True
df['Category'] = np.where(df['Product'].isin(['Laptop', 'Monitor']), 'Electronics', 'Accessories')

print("After adding columns:")
print(df)


# ============================================
# QUESTION 2
# ============================================
# Using the same DataFrame:
# a) Modify the 'Price' column by adding $5 shipping fee to each product
# b) Create a new column 'Bulk_Discount' where Quantity > 100 gets 20% off, otherwise 0%
# c) Add a column 'Total_After_Discount' = (Price - (Price * Bulk_Discount)) * Quantity
# d) Round all prices to 2 decimal places

print("\n--- QUESTION 2 ---")
# YOUR ANSWER CODE:
df['Price'] = df['Price'] + 5
df['Bulk_Discount'] = np.where(df['Quantity'] > 100, df['Price']*0.8, df['Price'])
df['Total_After_Discount'] = (df.Price - (df.Price * df.Bulk_Discount)) * df.Quantity
df['Price'] = df['Price'].round(2)

print("After modifications:")
print(df)


# ============================================
# QUESTION 3
# ============================================
# Using assign() method (method chaining) on the original DataFrame:
# Create a new DataFrame called 'df_updated' that adds these 3 columns at once:
# - 'Tax' = Price * 0.08 (8% tax)
# - 'Shipping' = $10 if Price < 100 else $0
# - 'Final_Price' = Price + Tax + Shipping
# Do NOT modify the original DataFrame

print("\n--- QUESTION 3 ---")
# Create fresh DataFrame for this question
df_original = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [1000, 25, 75, 300, 50],
    'Quantity': [10, 200, 50, 20, 150]
})

# YOUR ANSWER CODE:
df_updated = df_original.assign(
    Tax = df_original['Price'] * 0.08,
    Shipping = np.where(df_original['Price'] < 100, 10, 0),
    Final_Price = df_original['Price'] + df_original['Price'] * 0.08 + np.where(df_original['Price'] < 100, 10, 0)
)

print("Original DataFrame (unchanged):")
print(df_original)
print("\nNew DataFrame with assign():")
print(df_updated)


# ============================================
# QUESTION 4
# ============================================
# Given this DataFrame with dates:
orders = pd.DataFrame({
    'Order_ID': [101, 102, 103, 104, 105],
    'Order_Date': pd.to_datetime(['2024-01-15', '2024-02-20', '2024-03-10', '2024-04-05', '2024-05-12']),
    'Delivery_Date': pd.to_datetime(['2024-01-18', '2024-02-25', '2024-03-12', '2024-04-08', '2024-05-15'])
})

print("\n--- QUESTION 4 ---")
print("Orders DataFrame:")
print(orders)

# YOUR ANSWER CODE:
orders['Delivery_Days'] = (orders['Delivery_Date'] - orders['Order_Date']).dt.days
orders["Order_Month"] = orders["Order_Date"].dt.month_name()
orders['Is_Weekend'] = orders['Delivery_Date'].dt.day_name().isin(["Saturday", "Sunday"])
orders['Quarter'] = orders['Order_Date'].dt.quarter

print("\nAfter adding date columns:")
print(orders)


# ============================================
# QUESTION 5
# ============================================
# Given this DataFrame:
employees = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Base_Salary': [50000, 55000, 48000, 62000, 70000],
    'Performance_Rating': [4, 3, 5, 4, 5],
    'Years_At_Company': [2, 5, 3, 8, 6]
})

print("\n--- QUESTION 5 ---")
print("Employees DataFrame:")
print(employees)

# YOUR ANSWER CODE (with helper functions defined):
def bonus(rating, salary):
    if rating == 5:
        return salary * 0.15
    elif rating == 4:
        return salary * 0.10
    else:
        return salary * 0.05

def seniority(years):
    if years >= 5:
        return 'Senior'
    elif years >= 2:
        return 'Mid'
    else:
        return 'Junior'

employees["Bonus"] = employees.apply(lambda row: bonus(row["Performance_Rating"], row['Base_Salary']), axis=1)
employees['Total_Compensation'] = employees["Base_Salary"] + employees["Bonus"]
employees['Seniority'] = employees.apply(lambda row: seniority(row['Years_At_Company']), axis=1)
employees.insert(0, 'Employee_ID', ['E101', 'E102', 'E103', 'E104', 'E105'])

print("\nAfter adding columns:")
print(employees)