import pandas as pd
import numpy as np

print("=" * 60)
print("PART 3: SELECTING DATA (loc, iloc, column selection)")
print("=" * 60)

# Create the sample DataFrame used for Questions 1-3
df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [1200, 25, 75, 350, 60],
    'Stock': [30, 150, 80, 15, 200],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories']
})

print("Sample DataFrame:")
print(df)
print("\n" + "=" * 60)

# ============================================
# QUESTION 1
# ============================================
# Using this DataFrame, write code to:
# a) Select the 'Product' column as a Series
# b) Select the 'Product' and 'Price' columns as a DataFrame
# c) Select the first 3 rows using iloc
# d) Select rows 1-3 (inclusive) and columns 'Product' through 'Stock' using loc

print("\n--- QUESTION 1 ---")
print("a) Select 'Product' column as Series:")
print(df['Product'])
print(f"   Type: {type(df['Product'])}")

print("\nb) Select 'Product' and 'Price' columns as DataFrame:")
print(df[['Product', 'Price']])
print(f"   Type: {type(df[['Product', 'Price']])}")

print("\nc) Select first 3 rows using iloc:")
print(df.iloc[:3])

print("\nd) Select rows 1-3 (inclusive) and columns 'Product' through 'Stock' using loc:")
print(df.loc[1:3, 'Product':'Stock'])


# ============================================
# QUESTION 2
# ============================================
# Using the same DataFrame from Question 1:
# a) Use iloc to select the value at row 2, column 1 (Price of Keyboard)
# b) Use at to select the Stock value for Monitor (row 3)
# c) Use iat to select the Category for Headphones (row 4, column 3)
# d) Select the last 2 rows of all columns using iloc

print("\n--- QUESTION 2 ---")
print("a) Value at row 2, column 1 using iloc (Price of Keyboard):")
print(f"   {df.iloc[2, 1]}")

print("\nb) Stock value for Monitor using at (row 3, column 'Stock'):")
print(f"   {df.at[3, 'Stock']}")

print("\nc) Category for Headphones using iat (row 4, column 3):")
print(f"   {df.iat[4, 3]}")

print("\nd) Last 2 rows of all columns using iloc:")
print(df.iloc[-2:])


# ============================================
# QUESTION 3
# ============================================
# Create this DataFrame first:
students = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Math': [85, 72, 90, 88, 76],
    'Science': [88, 78, 92, 85, 80],
    'English': [90, 85, 88, 92, 84],
    'Grade_Level': [10, 11, 10, 12, 11]
})

print("\n--- QUESTION 3 ---")
print("Students DataFrame:")
print(students)

# Write code for:
# a) Select all rows but only the 'Name' and 'Math' columns using loc
# b) Select rows 2-4 (inclusive) and columns 1-3 (inclusive) using iloc
# c) Select the 'Science' score for Charlie (row 2) using at
# d) Select the first 4 rows of the last 2 columns using iloc

print("\na) All rows, only 'Name' and 'Math' columns using loc:")
print(students.loc[:, ['Name', 'Math']])

print("\nb) Rows 2-4 (inclusive) and columns 1-3 (inclusive) using iloc:")
print(students.iloc[1:4, 1:4])

print("\nc) 'Science' score for Charlie using at:")
print(f"   {students.at[2, 'Science']}")

print("\nd) First 4 rows of the last 2 columns using iloc:")
print(students.iloc[0:4, -2:])


# ============================================
# QUESTION 4
# ============================================
# Given this DataFrame:
sales = pd.DataFrame({
    'Jan': [100, 150, 200],
    'Feb': [120, 160, 180],
    'Mar': [140, 170, 220],
    'Apr': [160, 180, 250]
}, index=['Store_A', 'Store_B', 'Store_C'])

print("\n--- QUESTION 4 ---")
print("Sales DataFrame:")
print(sales)

# Write code to:
# a) Select the entire row for 'Store_B' using loc
# b) Select the 'Feb' and 'Apr' columns for 'Store_A' and 'Store_C' using loc
# c) Select the value at row index 'Store_C', column 'Mar' using at
# d) Select the first 2 rows of the first 3 columns using iloc

print("\na) Entire row for 'Store_B' using loc:")
print(sales.loc['Store_B'])

print("\nb) 'Feb' and 'Apr' columns for 'Store_A' and 'Store_C' using loc:")
print(sales.loc[['Store_A', 'Store_C'], ['Feb', 'Apr']])

print("\nc) Value at row 'Store_C', column 'Mar' using at:")
print(f"   {sales.at['Store_C', 'Mar']}")

print("\nd) First 2 rows of the first 3 columns using iloc:")
print(sales.iloc[:2, :3])


# ============================================
# QUESTION 5
# ============================================
# Explain in your own words the difference between:

print("\n--- QUESTION 5 ---")
print("a) df.loc[1:3, 'A':'C'] vs df.iloc[1:3, 1:3]")
print("   Answer: df.loc[1:3, 'A':'C'] uses labels and is inclusive (includes row 3 and column 'C').")
print("           df.iloc[1:3, 1:3] uses integer positions and is exclusive (rows at positions 1 and 2 only, columns at positions 1 and 2 only).")

print("\nb) df['Name'] vs df[['Name']]")
print("   Answer: df['Name'] returns a Series (1D).")
print("           df[['Name']] returns a DataFrame (2D) with a single column.")

print("\nc) df.at[2, 'Salary'] vs df.iloc[2, 3]")
print("   Answer: df.at[2, 'Salary'] accesses by label (row index 2, column name 'Salary').")
print("           df.iloc[2, 3] accesses by integer position (3rd row, 4th column).")

print("\nd) When would you use loc vs iloc?")
print("   Answer: Use loc when you know the index/column labels (names).")
print("           Use iloc when you know the integer positions (0, 1, 2...).")