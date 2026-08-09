"""
PANDAS SERIES - COMPREHENSIVE PRACTICE FILE
Topics Covered:
1. Series Creation
2. Index
3. Accessing Elements
4. Attributes
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("PANDAS SERIES - PRACTICE QUESTIONS AND ANSWERS")
print("=" * 60)

# ============================================================================
# TOPIC 1: SERIES CREATION
# ============================================================================

print("\n" + "=" * 60)
print("TOPIC 1: SERIES CREATION")
print("=" * 60)

# Question 1 - Your answer
print("\n--- Question 1: Create a Series ---")
data = pd.Series([5, 10, 15, 20, 25],
                 index=['one', 'two', 'three', 'four', 'five'],
                 name="numbers")
print("Your Series:")
print(data)

# Question 2 - Output prediction (verified)
print("\n--- Question 2: What will be the output? ---")
print("Code: pd.Series({'x':100, 'y':200, 'z':300}, index=['y','z','a'])")
data_dict = pd.Series({'x': 100, 'y': 200, 'z': 300}, index=['y', 'z', 'a'])
print("Output:")
print(data_dict)
print("Explanation: 'y' and 'z' match, 'a' not found → NaN, dtype becomes float64")


# ============================================================================
# TOPIC 2: INDEX
# ============================================================================

print("\n" + "=" * 60)
print("TOPIC 2: INDEX")
print("=" * 60)

# Question 1
print("\n--- Question 1: Create Series with named index ---")
s_index1 = pd.Series([100, 200, 300, 400, 500],
                     index=['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                     name='Month')
s_index1.index.name = 'Month'  # Naming the index
print("Your Series:")
print(s_index1)
print(f"Index name: {s_index1.index.name}")

# Question 2 - Output prediction
print("\n--- Question 2: Index alignment output ---")
s1 = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
s2 = pd.Series([10, 20, 30], index=['B', 'D', 'E'])
result = s1 * s2
print("s1 * s2 =")
print(result)
print("Explanation: Only B (2*10=20) and D (4*20=80) align, rest are NaN")

# Question 3 - Index operations
print("\n--- Question 3: Index operations ---")
s_index3 = pd.Series([5, 15, 25, 35, 45], index=['p', 'q', 'r', 's', 't'])
print("Original Series:")
print(s_index3)

print("\n1. Check if 'r' exists:")
print("r" in s_index3.index)

print("\n2. Change index to ['a','b','c','d','e']:")
s_index3.index = ['a', 'b', 'c', 'd', 'e']
print(s_index3)

print("\n3. Reset to default integer index:")
s_reset = s_index3.reset_index(drop=True)
print(s_reset)

# Question 4 - Complex index manipulation
print("\n--- Question 4: reindex() output ---")
s_index4 = pd.Series([10, 20, 30, 40], index=[2, 4, 6, 8])
print("Original:", s_index4)
s_index4.index = [1, 3, 5, 7]
print("After index change:", s_index4)
s_reindexed = s_index4.reindex([1, 2, 3, 4, 5, 6, 7, 8])
print("After reindex:", s_reindexed)

# Question 5 - Index alignment demonstration
print("\n--- Question 5: Create two Series and demonstrate alignment ---")
s_a = pd.Series([1, 2, 3], index=['X', 'Y', 'Z'])
s_b = pd.Series([4, 5, 6], index=['Y', 'Z', 'W'])
print("Series 1:")
print(s_a)
print("\nSeries 2:")
print(s_b)
print("\nSeries 1 + Series 2:")
print(s_a + s_b)
print("Explanation: Y(2+4=6), Z(3+5=8), X and W become NaN")

# Question 6 - Index immutability
print("\n--- Question 6: Index immutability (FIXED) ---")
s_index6 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print("Original Series:")
print(s_index6)
print("\nTrying to modify individual index element: s.index[2] = 'z'")
print("This would ERROR: Index objects are immutable!")
print("\nCORRECT way - reassign entire index:")
s_index6.index = ['a', 'b', 'z', 'd']
print(s_index6)


# ============================================================================
# TOPIC 3: ACCESSING ELEMENTS
# ============================================================================

print("\n" + "=" * 60)
print("TOPIC 3: ACCESSING ELEMENTS")
print("=" * 60)

# Setup Series for all access questions
s_access = pd.Series([45, 67, 89, 23, 56, 78],
                     index=['a', 'b', 'c', 'd', 'e', 'f'])
print("\nWorking Series:", s_access)

# Question 1 -
print("\n--- Question 1: Access methods ---")
print("1. Three methods to access 'c':")
print(f"   s.loc['c']: {s_access.loc['c']}")
print(f"   s.iloc[2]: {s_access.iloc[2]}")
print(f"   s.get('c'): {s_access.get('c')}")

print("\n2. First 3 elements (position-based):")
print(s_access.iloc[0:3])

print("\n3. Elements from 'b' to 'e' (label-based):")
print(s_access.loc['b':'e'])

# Question 2 - Output prediction
print("\n--- Question 2: Integer index ambiguity ---")
s_int_idx = pd.Series([5, 10, 15, 20, 25], index=[2, 4, 6, 8, 10])
print("Series:", s_int_idx)
print(f"s.loc[4]: {s_int_idx.loc[4]} (label 4)")
print(f"s.iloc[4]: {s_int_idx.iloc[4]} (position 4)")
print(f"s[2]: {s_int_idx[2]} (label 2)")
print(f"s[2:4]:")
print(s_int_idx[2:4])
print("Explanation: With integer index, [2:4] uses POSITION-based slicing")

# Question 3 - Complex accessing
print("\n--- Question 3: Advanced access ---")
s_months = pd.Series([12, 24, 36, 48, 60, 72, 84],
                     index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'])

print("\n1. Elements greater than 50:")
print(s_months[s_months > 50])

print("\n2. Elements between 20 and 70 (inclusive):")
print(s_months[(s_months > 20) & (s_months <= 70)])

print("\n3. Elements where index length is 3:")
print(s_months[s_months.index.str.len() == 3])

print("\n4. Last 3 elements (two methods):")
print("   tail(3):")
print(s_months.tail(3))
print("   iloc[-3:]:")
print(s_months.iloc[-3:])

# Question 4 - Output prediction
print("\n--- Question 4: Multiple access methods ---")
s_mixed = pd.Series([10, 20, 30, 40, 50], index=['w', 'x', 'y', 'z', 'a'])
print("Series:", s_mixed)
print("\n1. s.iloc[[0,2,4]]:")
print(s_mixed.iloc[[0, 2, 4]])
print("\n2. s.loc[['y','z','a']]:")
print(s_mixed.loc[['y', 'z', 'a']])
print("\n3. s[s > s.mean()]:")
print(s_mixed[s_mixed > s_mixed.mean()])
print("\n4. s.get('b', 'Not Found'):")
print(s_mixed.get('b', 'Not Found'))

# Question 5 -
print("\n--- Question 5: No error in this code ---")
s_q5 = pd.Series([100, 200, 300, 400, 500], index=[1, 2, 3, 4, 5])
result = s_q5.loc[2] + s_q5.iloc[2] + s_q5[2]
print(f"s.loc[2] = {s_q5.loc[2]} (label 2)")
print(f"s.iloc[2] = {s_q5.iloc[2]} (position 2)")
print(f"s[2] = {s_q5[2]} (label 2)")
print(f"Result = {result}")
print("This code runs perfectly - no error!")

# Question 6 -
print("\n--- Question 6: Various access patterns ---")
s_q6 = pd.Series([2, 4, 6, 8, 10, 12], index=['a', 'b', 'c', 'd', 'e', 'f'])
print("Series:", s_q6)

print("\n1. Every second element (step slicing):")
print(s_q6.iloc[0::2])

print("\n2. Access 'a','c','e' (two methods):")
print("   Method 1 - list indexing:")
print(s_q6[['a', 'c', 'e']])
print("   Method 2 - boolean indexing with isin():")
print(s_q6[s_q6.index.isin(['a', 'c', 'e'])])

print("\n3. Element at position 3 (fast access):")
print(f"   s.iat[2]: {s_q6.iat[2]}")
print(f"   s.at['c']: {s_q6.at['c']}")

print("\n4. Values divisible by 3:")
print(s_q6[s_q6 % 3 == 0])


# ============================================================================
# TOPIC 4: ATTRIBUTES
# ============================================================================

print("\n" + "=" * 60)
print("TOPIC 4: ATTRIBUTES")
print("=" * 60)

# Setup Series for attributes
s_attr = pd.Series([15, 25, 35, 45, 55],
                   index=['p', 'q', 'r', 's', 't'],
                   name='numbers')

# Question 1 -
print("\n--- Question 1: Basic attributes ---")
print(f"Series: {s_attr}")
print(f"dtype: {s_attr.dtype}")
print(f"size: {s_attr.size}")
print(f"shape: {s_attr.shape}")
print(f"values: {s_attr.values}")
print(f"type of values: {type(s_attr.values)}")

# Question 2 - Output prediction
print("\n--- Question 2: Attribute outputs ---")
s1_attr = pd.Series([1, 2, 3, 4])
s2_attr = pd.Series([1, 2, 2, 3])
s3_attr = pd.Series([1, 2, np.nan, 4])

print(f"s1.is_unique: {s1_attr.is_unique}")
print(f"s2.is_unique: {s2_attr.is_unique}")
print(f"s3.hasnans: {s3_attr.hasnans}")
print(f"s1.name: {s1_attr.name}")
print(f"s1.shape: {s1_attr.shape}")

# Question 3 -
print("\n--- Question 3: Working with attributes ---")
s_grades = pd.Series([98, 87, 92, 79, 88, 95],
                     index=['Math', 'Science', 'English', 'History', 'Art', 'Music'],
                     name='grades')
print("Original Series:")
print(s_grades)

print(f"\nIndex as list: {list(s_grades.index)}")
print(f"Index is unique? {s_grades.index.is_unique}")
print(f"dtype: {s_grades.dtype}")

s_grades.name = 'student_grades'
print(f"New name: {s_grades.name}")

# Question 4 - Output prediction
print("\n--- Question 4: More attributes ---")
s_attr4 = pd.Series([10, 20, 30, 40, 50], index=[2, 4, 6, 8, 10])
s_attr4.name = 'values'
s_attr4.index.name = 'positions'

print(f"s.name: {s_attr4.name}")
print(f"s.index.name: {s_attr4.index.name}")
print(f"s.dtype: {s_attr4.dtype}")
print(f"s.size: {s_attr4.size}")
print(f"type(s.values): {type(s_attr4.values)}")

# Question 5 - Fixing attribute errors
print("\n--- Question 5: Fixing common mistakes ---")
s_attr5 = pd.Series([5, 10, 15, 20, 25], index=['a', 'b', 'c', 'd', 'e'])

print("CORRECT usage (no parentheses):")
print(f"s.values: {s_attr5.values}")
print(f"s.size: {s_attr5.size}")
print(f"s.shape: {s_attr5.shape}")
print(f"s.dtype: {s_attr5.dtype}")
print(f"s.is_unique: {s_attr5.is_unique}")
print("\nAttributes are NOT methods - they don't use parentheses!")

# Question 6 - Various attributes
print("\n--- Question 6: Attribute exploration ---")
s_attr6 = pd.Series([2, 4, 6, 8, 10, 12],
                    index=['a', 'b', 'c', 'd', 'e', 'f'])

print(f"Memory usage (nbytes): {s_attr6.nbytes} bytes")
print(f"Is empty? {s_attr6.empty}")
print(f"Number of dimensions: {s_attr6.ndim}")
print(f"Size: {s_attr6.size}")
print(f"Length using len(): {len(s_attr6)}")
print(f"index.name (not set): {s_attr6.index.name}")

print("\n" + "=" * 60)
print("END OF Part 1!")
print("=" * 60)