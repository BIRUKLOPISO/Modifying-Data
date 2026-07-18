import pandas as pd

print("=" * 60)
print("TOPIC 9: APPLYING FUNCTIONS FOR CUSTOM CLEANING")
print("=" * 60)

# ============================================
# QUESTION 1: The apply() Method - Employee Bonus Data
# ============================================
print("\n" + "=" * 60)
print("QUESTION 1: The apply() Method - Employee Bonus Data")
print("=" * 60)

employees = pd.DataFrame({
    'employee_id': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'base_salary': [50000, 55000, 60000, 52000, 58000],
    'bonus': [5000, 3000, 7000, 4000, 6000],
    'sales': [100000, 150000, 80000, 120000, 90000]
})

print("\nEmployee Data:")
print(employees)

# 1a - Calculate total compensation using apply()
employees['total_compensation'] = employees.apply(lambda row: row['base_salary'] + row['bonus'], axis=1)

# 1b - Create performance rating using custom function
def performance_rating(x):
    if x['sales'] >= 120000:
        return 'Excellent'
    elif x['sales'] >= 90000:
        return 'Good'
    else:
        return 'Needs Improvement'

employees['performance_rating'] = employees.apply(performance_rating, axis=1)

# 1c - Calculate bonus percentage using apply()
employees['bonus_percentage'] = employees.apply(lambda x: (x['bonus'] / x['total_compensation']) * 100, axis=1)

print("\nAfter applying functions:")
print(employees)

# ============================================
# QUESTION 2: The map() Method - Product Inventory Data
# ============================================
print("\n" + "=" * 60)
print("QUESTION 2: The map() Method - Product Inventory Data")
print("=" * 60)

products = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Cable'],
    'stock_status': ['In Stock', 'Out of Stock', 'In Stock', 'Backordered', 'In Stock'],
    'priority': ['High', 'Medium', 'Low', 'High', 'Medium'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories']
})

print("\nProduct Data:")
print(products)

# 2a - Map stock status to codes
stock_code = {
    'In Stock': 1,
    'Out of Stock': 0,
    'Backordered': 2
}
products["stock_code"] = products['stock_status'].map(stock_code)

# 2b - Map priority to scores
priority_score = {
    'High': 3,
    'Medium': 2,
    'Low': 1
}
products["priority_score"] = products['priority'].map(priority_score)

# 2c - Map category to abbreviation using function
def category_abbr(s):
    return s[0:3].upper()

products["category_abbr"] = products['category'].map(category_abbr)

print("\nAfter mapping:")
print(products)

# ============================================
# QUESTION 3: The replace() Method - Customer Feedback Data
# ============================================
print("\n" + "=" * 60)
print("QUESTION 3: The replace() Method - Customer Feedback Data")
print("=" * 60)

customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Sarah', 'Mike', 'Emily', 'David'],
    'email': ['john@gmail.com', 'sarah@yahoo.com', 'mike@hotmail.com', 'emily@gmail.com', 'david@outlook.com'],
    'phone': ['(212) 555-1234', '212-555-5678', '212.555.9012', '(323) 555-3456', '310-555-7890'],
    'status': ['Active', 'Inactive', 'N/A', 'Active', 'Pending'],
    'country': ['USA', 'United States', 'US', 'USA', 'United States']
})

print("\nCustomer Data:")
print(customers)

# 3a - Clean phone column using regex replace
customers['phone_clean'] = customers['phone'].str.replace(r'\D', '', regex=True)

# 3b - Standardize country using replace() with dictionary
customers['country'] = customers['country'].replace({
    'USA': 'United States',
    'US': 'United States'
})

# 3c - Clean status using replace() with dictionary
customers['status'] = customers['status'].replace({
    'N/A': 'Unknown',
    'Pending': 'Inactive'
})

print("\nAfter cleaning with replace():")
print(customers)
