import pandas as pd
import numpy as np

print("=" * 60)
print("PART 1: CREATING DATAFRAMES")
print("=" * 60)

# ============================================
# QUESTION 1
# ============================================
# a) Create the DataFrame and display it
# b) What is the shape of this DataFrame?
# c) What are the column names?

print("\n--- QUESTION 1 ---")
data = {
    'Product': ['Phone', 'Tablet', 'Laptop', 'Monitor'],
    'Price': [699, 399, 999, 299],
    'Quantity': [50, 30, 25, 100]
}
df1 = pd.DataFrame(data)
print("a) DataFrame:")
print(df1)
print(f"\nb) Shape: {df1.shape}")
print(f"c) Column names: {df1.columns.tolist()}")


# ============================================
# QUESTION 2
# ============================================
#
# a) Create a DataFrame with column names: 'Fruit', 'Price', 'Stock'
# b) Display the first 2 rows
# c) What data type is the 'Price' column?

print("\n--- QUESTION 2 ---")
rows = [
    ['Apple', 1.25, 150],
    ['Banana', 0.50, 200],
    ['Orange', 0.75, 175],
    ['Grape', 2.00, 80]
]
df2 = pd.DataFrame(rows, columns=['Fruit', 'Price', 'Stock'])
print("a) DataFrame:")
print(df2)
print("\nb) First 2 rows:")
print(df2.head(2))
print(f"\nc) Price column data type: {df2['Price'].dtype}")


# ============================================
# QUESTION 3
# ============================================
# Given this CSV file content (saved as 'employees.csv'):

#
# Write code to:
# a) Read the CSV file into a DataFrame
# b) Use 'ID' as the index column
# c) Display the DataFrame

print("\n--- QUESTION 3 ---")
# Create the CSV file first
csv_content = """ID,Name,Department,Salary
101,John,Sales,50000
102,Jane,Marketing,55000
103,Bob,Sales,48000
104,Alice,HR,52000"""
with open('employees.csv', 'w') as f:
    f.write(csv_content)

print("a) Read CSV without index:")
df3a = pd.read_csv('employees.csv')
print(df3a)

print("\nb) Read CSV with ID as index:")
df3b = pd.read_csv('employees.csv', index_col=0)
print(df3b)


# ============================================
# QUESTION 4
# ============================================

# a) Combine them into a single DataFrame
# b) Add a new column 'Transparent' with all values set to False
# c) Show the resulting DataFrame

print("\n--- QUESTION 4 ---")
names = pd.Series(['Red', 'Blue', 'Green', 'Yellow'], name='Color')
codes = pd.Series(['#FF0000', '#0000FF', '#00FF00', '#FFFF00'], name='Hex_Code')
rgb = pd.Series(['(255,0,0)', '(0,0,255)', '(0,255,0)', '(255,255,0)'], name='RGB')

print("a) Combine into DataFrame:")
df4 = pd.DataFrame({
    "Name": names,
    "Code": codes,
    "Hex_Code": rgb
})
print(df4)

print("\nb) Add Transparent column:")
df4['Transparent'] = False
print(df4)


# ============================================
# QUESTION 5
# ============================================
# Create an empty DataFrame with columns: 'Student', 'Math', 'Science', 'English'
# Then add these three students:
# Student A: Math=85, Science=90, English=88
# Student B: Math=78, Science=82, English=79
# Student C: Math=92, Science=88, English=94
#
# a) Create the empty DataFrame
# b) Add each student as a row
# c) Display the final DataFrame

print("\n--- QUESTION 5 ---")
print("a) Create empty DataFrame:")
emp = pd.DataFrame(columns=['Student', 'Math', 'Science', 'English'])
print(emp)

print("\nb) Add students:")
emp.loc[0] = ["Student A", 85, 90, 88]
emp.loc[1] = ["Student B", 78, 82, 79]
emp.loc[2] = ["Student C", 92, 88, 94]

print("\nc) Final DataFrame:")
print(emp)