import pandas as pd
import numpy as np

print("=" * 60)
print("TOPIC 2: HANDLING MISSING DATA")
print("=" * 60)

# ============================================
# QUESTION 1
# ============================================
print("\n" + "=" * 60)
print("QUESTION 1")
print("=" * 60)

df1 = pd.DataFrame({
    'student': ['John', 'Emma', 'Mike', 'Sofia', 'Lucas'],
    'math_score': [85, np.nan, 78, 92, np.nan],
    'science_score': [88, 90, np.nan, 85, 91]
})

print("\nOriginal DataFrame:")
print(df1)

print("\nAfter filling missing values:")
print(df1.fillna({'math_score': df1['math_score'].median(), 'science_score': 0}))

# ============================================
# QUESTION 2
# ============================================
print("\n" + "=" * 60)
print("QUESTION 2")
print("=" * 60)

df2 = pd.DataFrame({
    'day': [1, 2, 3, 4, 5],
    'sales': [100, np.nan, np.nan, 250, np.nan],
    'temperature': [22, 23, np.nan, 24, 25]
})

print("\nOriginal DataFrame:")
print(df2)

df2['sales'] = df2.sales.ffill()
df2['temperature'] = df2.temperature.bfill()

print("\nAfter forward fill (sales) and backward fill (temperature):")
print(df2)

# ============================================
# QUESTION 3
# ============================================
print("\n" + "=" * 60)
print("QUESTION 3")
print("=" * 60)

df3 = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'price': [10.5, np.nan, 15.0, np.nan, 12.0],
    'stock': [100, 200, np.nan, np.nan, 50],
    'rating': [4.5, np.nan, 4.2, np.nan, np.nan]
})

print("\nOriginal DataFrame:")
print(df3)

print("\n3a. Remove rows where BOTH price AND stock are missing:")
print(df3.dropna(subset=['price', 'stock'], how='all'))

print("\n3b. Keep rows with at least 3 non-NA values:")
print(df3.dropna(thresh=3))

print("\n3c. Remove columns with ANY missing values:")
print(df3.dropna(axis=1, how='any'))

# ============================================
# QUESTION 4
# ============================================
print("\n" + "=" * 60)
print("QUESTION 4")
print("=" * 60)

df4 = pd.DataFrame({
    'product_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'month': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'sales': [100, np.nan, 300, 50, 60, np.nan, np.nan, 200, 250],
    'inventory': [500, np.nan, np.nan, 100, np.nan, 150, np.nan, np.nan, 300]
})

print("\nOriginal DataFrame:")
print(df4)

df4['sales'] = df4.groupby('product_id')['sales'].ffill()
df4['inventory'] = df4.groupby('product_id')['inventory'].bfill()

print("\nAfter groupby forward fill (sales) and backward fill (inventory):")
print(df4)

