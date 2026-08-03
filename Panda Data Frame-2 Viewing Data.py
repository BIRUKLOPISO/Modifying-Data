import pandas as pd
import numpy as np

print("=" * 60)
print("PART 2: VIEWING DATA (head, tail, info, describe, shape)")
print("=" * 60)

# Create the sample DataFrame used for all questions
df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'Diana'],
    'Age': [28, 34, 25, 42, 31, 29],
    'Salary': [48000, 52000, 45000, 65000, 55000, 49000],
    'Department': ['Sales', 'Marketing', 'Sales', 'HR', 'Sales', 'Marketing']
})

print("Sample DataFrame:")
print(df)
print("\n" + "=" * 60)

# ============================================
# QUESTION 1
# ============================================
# Based on the DataFrame above, answer:
# a) What is the shape of this DataFrame?
# b) Use head(3) - what rows do you see?
# c) Use tail(2) - what rows do you see?
# d) What are all the column names?

print("\n--- QUESTION 1 ---")
print("a) Shape:")
print(f"   {df.shape}")
print("\nb) head(3):")
print(df.head(3))
print("\nc) tail(2):")
print(df.tail(2))
print("\nd) Column names:")
print(f"   {df.columns.tolist()}")


# ============================================
# QUESTION 2
# ============================================
# Using this DataFrame:
df2 = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Desk', 'Chair'],
    'Price': [999, 25, 75, 299, 59, 199, 149],
    'Stock': [50, 200, 75, 25, 150, 10, 30],
    'Rating': [4.5, 4.2, 4.0, 4.7, 4.3, 4.1, 4.4]
})

# a) Use describe() - what is the mean price?
# b) What is the minimum stock value?
# c) What is the maximum rating?
# d) Use info() - are there any missing values?

print("\n--- QUESTION 2 ---")
print("a) Mean price from describe():")
print(f"   {df2['Price'].mean()}")
print("\n   Full describe() output:")
print(df2.describe())
print("\nb) Minimum stock value:")
print(f"   {df2['Stock'].min()}")
print("\nc) Maximum rating:")
print(f"   {df2['Rating'].max()}")
print("\nd) Missing values check (info()):")
print(df2.info())
print("\n   Are there missing values?")
print(f"   {df2.isna().sum().sum() == 0}")


# ============================================
# QUESTION 3
# ============================================
# Using the df2 DataFrame from Question 2, write code to:
# a) Display the first 4 rows
# b) Display the last 3 rows
# c) Get a random sample of 2 rows
# d) Show only the data types of each column

print("\n--- QUESTION 3 ---")
print("a) First 4 rows (head(4)):")
print(df2.head(4))
print("\nb) Last 3 rows (tail(3)):")
print(df2.tail(3))
print("\nc) Random sample of 2 rows (sample(2)):")
print(df2.sample(2, random_state=42))
print("\nd) Data types (dtypes):")
print(df2.dtypes)


# ============================================
# QUESTION 4
# ============================================
# This DataFrame has missing values
df_messy = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 6],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Score': [85, np.nan, 78, 92, np.nan, 88],
    'Grade': ['B', np.nan, 'C', 'A', np.nan, 'B+']
})

# Based on info():
# a) How many non-null values are in the 'Score' column?
# b) Which column has the most missing values?
# c) What is the data type of the 'Grade' column?

print("\n--- QUESTION 4 ---")
print("DataFrame with missing values:")
print(df_messy)
print("\na) Non-null values in 'Score' column:")
print(f"   {df_messy['Score'].count()} (or {df_messy['Score'].notna().sum()})")
print("\nb) Missing values per column:")
missing_counts = df_messy.isna().sum()
print(missing_counts)
print(f"\n   Column(s) with most missing values: {missing_counts[missing_counts == missing_counts.max()].index.tolist()}")
print("\nc) Data type of 'Grade' column:")
print(f"   {df_messy['Grade'].dtypes}")


# ============================================
# QUESTION 5
# ============================================
# Given this large DataFrame simulation:
large_df = pd.DataFrame({
    'A': range(1000),
    'B': np.random.rand(1000),
    'C': np.random.choice(['X', 'Y', 'Z'], 1000)
})

# You want to quickly understand this data without printing all 1000 rows.
# Write the code to:
# a) Check how many rows and columns
# b) See the first 5 rows
# c) Get statistical summary of numeric columns
# d) Check data types and missing values

print("\n--- QUESTION 5 ---")
print("a) Shape (rows, columns):")
print(f"   {large_df.shape}")
print("\nb) First 5 rows (head()):")
print(large_df.head())
print("\nc) Statistical summary of numeric columns (describe()):")
print(large_df.describe())
print("\nd) Data types and missing values (info()):")
print(large_df.info())