import pandas as pd
import numpy as np

print("=" * 60)
print("TOPIC 4: DATA TYPE CONVERSION")
print("=" * 60)

# ============================================
# QUESTION 1: Fixing Numeric Data Stored as Text
# ============================================
print("\n" + "=" * 60)
print("QUESTION 1: Fixing Numeric Data Stored as Text")
print("=" * 60)

sales = pd.DataFrame({
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Cable'],
    'price': ['$999.99', '$25.50', '$49.95', '$199.00', '$12.75'],
    'quantity': ['5', '12', '8', '3', '50'],
    'discount': ['10%', 'N/A', '15%', 'N/A', '5%']
})

print("\nOriginal Data:")
print(sales)
print("\nData Types:")
print(sales.dtypes)

# 1a - Convert price to float
sales['price'] = sales['price'].str.replace('$', '')
sales['price'] = pd.to_numeric(sales['price'], errors='coerce').astype(float)

# 1b - Convert quantity to integer
sales['quantity'] = pd.to_numeric(sales['quantity'], errors='coerce')

# 1c - Convert discount to float
sales['discount'] = sales['discount'].str.replace('%', '')
sales['discount'] = pd.to_numeric(sales['discount'], errors='coerce').astype(float)

# 1d - Calculate final price after discount
sales['final_price'] = sales['price'] * (1 - sales['discount']/100)

print("\nAfter conversion:")
print(sales)
print("\nData Types After Conversion:")
print(sales.dtypes)

# ============================================
# QUESTION 2: Cleaning Messy Numeric Data
# ============================================
print("\n" + "=" * 60)
print("QUESTION 2: Cleaning Messy Numeric Data")
print("=" * 60)

inventory = pd.DataFrame({
    'item_id': [101, 102, 103, 104, 105],
    'weight_kg': ['10.5', 'unknown', '7.8', 'N/A', '12.3'],
    'stock_count': ['50', '30', 'not available', '20', '100'],
    'price_per_kg': ['$5.99', '$6.50', 'missing', '$7.25', '$5.50']
})

print("\nRaw Inventory Data:")
print(inventory)

# 2a - Convert weight_kg to float
inventory['weight_kg'] = pd.to_numeric(inventory['weight_kg'], errors="coerce").astype('float')

# 2b - Convert stock_count to integer
inventory['stock_count'] = pd.to_numeric(inventory['stock_count'], errors="coerce").astype("Int64")

# 2c - Convert price_per_kg to float
inventory['price_per_kg'] = inventory['price_per_kg'].str.replace('$', '')
inventory['price_per_kg'] = pd.to_numeric(inventory['price_per_kg'], errors="coerce").astype(float)

# 2d - Count missing values
print("\n2d. Missing values after conversion:")
print(inventory.isnull().sum())

print("\nCleaned Inventory Data:")
print(inventory)

# ============================================
# QUESTION 3: Converting and Working with Dates
# ============================================
print("\n" + "=" * 60)
print("QUESTION 3: Converting and Working with Dates")
print("=" * 60)

employee_data = pd.DataFrame({
    'emp_name': ['John Smith', 'Sarah Jones', 'Mike Brown', 'Lisa Wong', 'David Lee'],
    'start_date': ['2024-01-15', 'Jan 20, 2024', '2024/03/10', '04-01-2024', '2024-05-05'],
    'birth_date': ['1990-05-12', '1985-08-20', '1992-11-03', '1988-02-28', '1995-07-15'],
    'review_date': ['2024-12-01', '2025-01-15', 'invalid', '2024-11-30', '2024-12-31']
})

print("\nEmployee Data:")
print(employee_data)

# 3a - Convert dates to datetime
for col in ['start_date', 'review_date', 'birth_date']:
    employee_data[col] = pd.to_datetime(employee_data[col], errors='coerce')

# 3b - Calculate age
today = pd.Timestamp.now()
employee_data["age"] = (today - employee_data['birth_date']).dt.days // 365

# 3c - Calculate tenure in months
employee_data["tenure_months"] = (today - employee_data['start_date']).dt.days // 30

# 3d - Extract month name and year
employee_data["month_name"] = employee_data['start_date'].dt.month_name()
employee_data['year'] = employee_data['start_date'].dt.year

print("\nAfter date conversion and calculations:")
print(employee_data)
print("\nData Types:")
print(employee_data.dtypes)

# ============================================
# QUESTION 4: Converting to Categorical (Memory Optimization)
# ============================================
print("\n" + "=" * 60)
print("QUESTION 4: Converting to Categorical")
print("=" * 60)

orders = pd.DataFrame({
    'order_id': range(1, 101),
    'status': ['Pending', 'Shipped', 'Delivered', 'Cancelled', 'Pending', 'Shipped', 'Delivered', 'Pending', 'Shipped', 'Delivered'] * 10,
    'priority': ['High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High'] * 10,
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'] * 10
})

print("\nMemory usage before conversion:")
print(orders.memory_usage(deep=True))

# 4a - Convert to categorical
rating = ['status', 'priority', 'region']
orders[rating] = orders[rating].astype('category')

# 4b - Check memory usage after conversion
print("\nMemory usage after conversion:")
print(orders.memory_usage(deep=True))

# 4c - Display categories and codes
print("\n4c. Status categories and codes:")
print("Categories:")
print(orders['status'].cat.categories)
print("\nCodes (first 10):")
print(orders['status'].cat.codes.head(10))

# 4d - Filter categorical data
print("\n4d. Filter orders with priority 'High':")
high_priority_orders = orders[orders['priority'] == 'High']
print(high_priority_orders.head())

# ============================================
# QUESTION 5: Mixed Data Types in Same Column
# ============================================
print("\n" + "=" * 60)
print("QUESTION 5: Mixed Data Types in Same Column")
print("=" * 60)

transaction_log = pd.DataFrame({
    'transaction_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'amount': ['100.50', '200', 'N/A', '150.75', '300', 'unknown', '75.25', '400'],
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', '01/04/2024', 'Jan 5, 2024', '2024-01-06', '01/07/2024', '2024-01-08'],
    'quantity': ['1', 'two', '3', '4', 'five', '6', 'seven', '8']
})

print("\nTransaction Data:")
print(transaction_log)

# 5a - Convert amount to float
transaction_log['amount'] = pd.to_numeric(transaction_log['amount'], errors='coerce')

# 5b - Convert date to datetime
transaction_log['date'] = pd.to_datetime(transaction_log['date'], errors='coerce')

# 5c - Convert quantity to integer (with word mapping)
quantity_map = {'two': 2, 'five': 5, 'seven': 7}
transaction_log['quantity'] = transaction_log['quantity'].replace(quantity_map)
transaction_log['quantity'] = pd.to_numeric(transaction_log['quantity'], errors='coerce').astype('Int64')

# 5d - Calculate total value
transaction_log['total_value'] = transaction_log['amount'] * transaction_log['quantity']

# 5e - Drop rows with missing values
transaction_log_clean = transaction_log.dropna(subset=['amount', 'quantity'])

print("\nAfter cleaning:")
print(transaction_log_clean)
print("\nData Types:")
print(transaction_log_clean.dtypes)
