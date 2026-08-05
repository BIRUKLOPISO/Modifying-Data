import pandas as pd
import numpy as np

print("=" * 60)
print("PART 6: HANDLING MISSING DATA ON DATAFRAMES")
print("=" * 60)

# Create the sample DataFrame used for Questions 1-3
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, np.nan, 35, 28, np.nan],
    'Salary': [50000, 60000, np.nan, 52000, 75000],
    'Department': ['Sales', 'Marketing', 'Sales', np.nan, 'Sales']
})

print("Sample DataFrame with missing values:")
print(df)
print("\n" + "=" * 60)

# ============================================
# QUESTION 1
# ============================================
# Based on this DataFrame:
# a) How many missing values are in each column?
# b) What is the total number of missing values?
# c) Which rows have missing values? (show the row indices)
# d) What percentage of the 'Age' column is missing?

print("\n--- QUESTION 1 ---")
# YOUR ANSWER CODE:
print("a) Missing values per column:")
print(df.isna().sum())

print("\nb) Total missing values:")
print(df.isna().sum().sum())

print("\nc) Rows with missing values (indices):")
print(df[df.isna().any(axis=1)].index.tolist())

print("\nd) Percentage of 'Age' column missing:")
print((df['Age'].isnull().sum() / len(df) * 100))

# ============================================
# QUESTION 2
# ============================================
# Using the same DataFrame:
# a) Drop all rows that contain ANY missing values
# b) Drop all rows where 'Age' OR 'Salary' is missing (using subset)
# c) Drop columns that have ANY missing values
# d) Drop rows where ALL values in the row are missing (create a test row first)

print("\n--- QUESTION 2 ---")
# YOUR ANSWER CODE:
print("a) Drop rows with ANY missing values:")
print(df.dropna())

print("\nb) Drop rows where 'Age' OR 'Salary' is missing:")
print(df.dropna(subset=['Age', 'Salary']))

print("\nc) Drop columns with ANY missing values:")
print(df.dropna(axis=1))

# Create a test row with all missing values
df_test = df.copy()
df_test.loc[5] = [np.nan, np.nan, np.nan, np.nan]
print("\nDataFrame with added all-missing row:")
print(df_test)
print("\nd) Drop rows where ALL values are missing:")
print(df_test.dropna(how='all'))

# ============================================
# QUESTION 3
# ============================================
# Using the same DataFrame:
# a) Fill all missing values with 0
# b) Fill missing 'Age' with the mean age, missing 'Salary' with median salary,
#    and missing 'Department' with 'Unknown' (use dictionary)
# c) Forward fill (ffill) the entire DataFrame
# d) Backward fill (bfill) the entire DataFrame

print("\n--- QUESTION 3 ---")
# YOUR ANSWER CODE:
print("a) Fill all missing values with 0:")
print(df.fillna(0))

print("\nb) Fill with dictionary (Age=mean, Salary=median, Department='Unknown'):")
filled_dict = df.fillna({
    'Age': df.Age.fillna(df.Age.mean()),
    'Salary': df.Salary.fillna(df.Salary.median()),
    'Department': df.Department.fillna('Unknown')
})
print(filled_dict)

print("\nc) Forward fill (ffill):")
print(df.ffill())

print("\nd) Backward fill (bfill):")
print(df.bfill())
