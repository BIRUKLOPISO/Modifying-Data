import pandas as pd
import numpy as np

print("=" * 60)
print("PART 4: FILTERING ROWS (BOOLEAN INDEXING)")
print("=" * 60)

# Create the sample DataFrame used for Questions 1-3
df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Desk', 'Chair'],
    'Price': [1200, 25, 75, 350, 60, 199, 149],
    'Stock': [30, 150, 80, 15, 200, 10, 50],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Furniture', 'Furniture']
})

print("Sample DataFrame:")
print(df)
print("\n" + "=" * 60)

# ============================================
# QUESTION 1
# ============================================
# Write code to:
# a) Find all products with Price > 100
# b) Find all products in the 'Accessories' category
# c) Find all products with Stock less than 20
# d) Find all products that are NOT in 'Electronics' category

print("\n--- QUESTION 1 ---")
print("a) Products with Price > 100:")
print(df[df['Price'] > 100])

print("\nb) Products in 'Accessories' category:")
print(df[df['Category'] == 'Accessories'])

print("\nc) Products with Stock < 20:")
print(df[df['Stock'] < 20])

print("\nd) Products NOT in 'Electronics' category:")
print(df[df['Category'] != 'Electronics'])


# ============================================
# QUESTION 2
# ============================================
# Using the same DataFrame:
# a) Find products with Price between 50 and 150 (inclusive) using between()
# b) Find products that are in 'Electronics' AND have Stock > 20
# c) Find products that are in 'Accessories' OR have Price < 100
# d) Find products with Price > 500 OR Stock < 5

print("\n--- QUESTION 2 ---")
print("a) Products with Price between 50 and 150 (between()):")
print(df[df['Price'].between(50, 150)])

print("\nb) Products in 'Electronics' AND Stock > 20:")
print(df[(df['Category'] == 'Electronics') & (df['Stock'] > 20)])

print("\nc) Products in 'Accessories' OR Price < 100:")
print(df[(df['Category'] == 'Accessories') | (df['Price'] < 100)])

print("\nd) Products with Price > 500 OR Stock < 5:")
print(df[(df['Price'] > 500) | (df['Stock'] < 5)])


# ============================================
# QUESTION 3
# ============================================
# Using the same DataFrame:
# a) Find products where Category is in ['Electronics', 'Furniture']
# b) Find products where Product name contains 'e' (case insensitive)
# c) Find products where Product name starts with 'M'
# d) Find products where Price is greater than the average price of all products

print("\n--- QUESTION 3 ---")
print("a) Products where Category is in ['Electronics', 'Furniture']:")
print(df[df['Category'].isin(['Electronics', 'Furniture'])])

print("\nb) Products where Product name contains 'e' (case insensitive):")
print(df[df['Product'].str.contains('e', case=False)])

print("\nc) Products where Product name starts with 'M':")
print(df[df['Product'].str.startswith('M')])

print("\nd) Products with Price greater than average price:")
avg_price = df['Price'].mean()
print(f"   Average price: {avg_price:.2f}")
print(df[df['Price'] > avg_price])


# ============================================
# QUESTION 4
# ============================================
# Given this DataFrame with missing values:
df_messy = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Test_Score': [85, np.nan, 78, 92, np.nan],
    'Grade': ['B', 'C', 'C', 'A', np.nan],
    'Attendance': [95, 88, np.nan, 97, 85]
})

print("\n--- QUESTION 4 ---")
print("DataFrame with missing values:")
print(df_messy)

# Write code to:
# a) Find all rows where Test_Score is NOT missing (notna)
# b) Find all rows where Grade is missing (isna)
# c) Find rows where both Test_Score AND Attendance are not missing
# d) Find rows where ANY column has a missing value

print("\na) Rows where Test_Score is NOT missing:")
print(df_messy[df_messy['Test_Score'].notna()])

print("\nb) Rows where Grade is missing:")
print(df_messy[df_messy['Grade'].isna()])

print("\nc) Rows where both Test_Score AND Attendance are not missing:")
print(df_messy[(df_messy['Test_Score'].notna()) & (df_messy['Attendance'].notna())])

print("\nd) Rows where ANY column has a missing value:")
print(df_messy[df_messy.isna().any(axis=1)])


# ============================================
# QUESTION 5
# ============================================
# Using the employees DataFrame:
employees = pd.DataFrame({
    'Employee_ID': range(101, 116),
    'Name': ['John', 'Sarah', 'Michael', 'Emma', 'David', 'Lisa', 'James', 'Anna',
             'Robert', 'Maria', 'William', 'Jennifer', 'Richard', 'Patricia', 'Thomas'],
    'Age': [25, 32, 45, 28, 35, 42, 38, 27, 52, 33, 29, 41, 47, 31, 55],
    'Department': ['Sales', 'Marketing', 'Sales', 'HR', 'IT', 'Sales', 'IT', 'Marketing',
                   'Sales', 'HR', 'IT', 'Marketing', 'Sales', 'HR', 'IT'],
    'Salary': [48000, 52000, 65000, 45000, 72000, 58000, 68000, 51000,
               78000, 49000, 56000, 62000, 71000, 47000, 85000],
    'Experience': [2, 5, 12, 3, 8, 6, 10, 4, 15, 3, 5, 9, 13, 2, 20]
})

print("\n--- QUESTION 5 ---")
print("Employees DataFrame (first 5 rows):")
print(employees.head())

# Write a single query using query() method to find:
# Employees in 'Sales' or 'IT' departments, with Age between 30 and 50,
# Salary greater than 60000, and Experience at least 5 years

print("\nQuery: Employees in 'Sales' or 'IT', Age 30-50, Salary > 60000, Experience >= 5")
result = employees.query(
    "(Department == 'Sales' or Department == 'IT') and "
    "(Age >= 30 and Age <= 50) and "
    "(Salary > 60000) and "
    "(Experience >= 5)"
)
print(result)