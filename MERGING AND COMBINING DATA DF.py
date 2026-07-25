import pandas as pd

print("=" * 60)
print("TOPIC 12: MERGING AND COMBINING DATA")
print("=" * 60)

# ============================================
# QUESTION 1: Customer Orders - Inner, Left, Right Joins
# ============================================
print("\n" + "=" * 60)
print("QUESTION 1: Customer Orders - Inner, Left, Right Joins")
print("=" * 60)

# Customer data
customers = pd.DataFrame({
    'customer_id': [101, 102, 103, 104, 105],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'city': ['NYC', 'LA', 'Chicago', 'NYC', 'LA'],
    'signup_date': ['2024-01-01', '2024-01-15', '2024-02-01', '2024-02-15', '2024-03-01']
})

# Order data
orders = pd.DataFrame({
    'order_id': [1001, 1002, 1003, 1004, 1005, 1006],
    'customer_id': [101, 102, 101, 103, 104, 106],
    'order_date': ['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04', '2024-06-05', '2024-06-06'],
    'amount': [150, 200, 100, 300, 250, 75],
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Tablet', 'USB Cable']
})

print("\nCustomers:")
print(customers)
print("\nOrders:")
print(orders)

# 1a - Inner join
inner_join = pd.merge(customers, orders, on='customer_id', how='inner')
print("\n1a. Inner Join (customers with orders):")
print(inner_join)

# 1b - Left join
left_join = pd.merge(customers, orders, on='customer_id', how='left')
print("\n1b. Left Join (all customers):")
print(left_join)

# 1c - Right join
right_join = pd.merge(customers, orders, on='customer_id', how='right')
print("\n1c. Right Join (all orders):")
print(right_join)

# 1d - Customers with no orders
no_orders = left_join[left_join['order_id'].isnull()]
print("\n1d. Customers with no orders:")
print(no_orders[['customer_id', 'customer_name', 'city']])

# ============================================
# QUESTION 2: Employee and Department Data - Multiple Joins
# ============================================
print("\n" + "=" * 60)
print("QUESTION 2: Employee and Department Data - Multiple Joins")
print("=" * 60)

# Employee data
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5, 6],
    'emp_name': ['John', 'Sarah', 'Mike', 'Emily', 'David', 'Lisa'],
    'dept_id': [10, 20, 10, 30, 20, 40],
    'salary': [60000, 55000, 65000, 52000, 58000, 62000]
})

# Department data
departments = pd.DataFrame({
    'dept_id': [10, 20, 30, 50],
    'dept_name': ['Sales', 'IT', 'HR', 'Finance'],
    'location': ['NYC', 'LA', 'Chicago', 'Boston']
})

# Project assignments
projects = pd.DataFrame({
    'emp_id': [1, 2, 3, 5, 6],
    'project_name': ['Project A', 'Project B', 'Project C', 'Project D', 'Project E'],
    'hours': [40, 35, 45, 30, 50]
})

print("\nEmployees:")
print(employees)
print("\nDepartments:")
print(departments)
print("\nProjects:")
print(projects)

# 2a - Merge employees with departments
emp_dept_data = pd.merge(employees, departments, on='dept_id', how='inner')
print("\n2a. Employees with departments:")
print(emp_dept_data)

# 2b - Merge with projects (left join)
full_data = pd.merge(emp_dept_data, projects, on='emp_id', how='left')
print("\n2b. Full data (with projects):")
print(full_data)

# 2c - Employees with projects (drop NaN)
has_projects = full_data.dropna(subset=['project_name'])
print("\n2c. Employees with projects:")
print(has_projects)

# 2d - Display department, employee, project
print("\n2d. Department, Employee, Project:")
print(has_projects[['dept_name', 'emp_name', 'project_name']])

# ============================================
# QUESTION 3: Sales Data - Concatenation and Merging
# ============================================
print("\n" + "=" * 60)
print("QUESTION 3: Sales Data - Concatenation and Merging")
print("=" * 60)

# Sales data for Q1, Q2, Q3
sales_q1 = pd.DataFrame({
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'q1_sales': [10000, 5000, 3000, 8000],
    'region': ['North', 'South', 'East', 'West']
})

sales_q2 = pd.DataFrame({
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'q2_sales': [12000, 4500, 3500, 8500],
    'region': ['North', 'South', 'East', 'West']
})

sales_q3 = pd.DataFrame({
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'q3_sales': [11000, 5500, 3200, 8200],
    'region': ['North', 'South', 'East', 'West']
})

# Product prices
prices = pd.DataFrame({
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Tablet'],
    'unit_price': [1000, 25, 75, 200, 500],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics']
})

print("\nQ1 Sales:")
print(sales_q1)
print("\nQ2 Sales:")
print(sales_q2)
print("\nQ3 Sales:")
print(sales_q3)
print("\nPrices:")
print(prices)

# 3a - Concatenate vertically
all_sales = pd.concat([sales_q1, sales_q2, sales_q3], axis=0, ignore_index=True)
print("\n3a. All sales combined (wide format):")
print(all_sales)

# 3b - Melt to long format
all_sales_melted = all_sales.melt(
    id_vars=["product", "region"],
    value_vars=["q1_sales", "q2_sales", "q3_sales"],
    var_name="quarter",
    value_name="sales"
)
print("\n3b. All sales (long format):")
print(all_sales_melted)

# 3c - Merge with prices
all_sales_merged = pd.merge(all_sales_melted, prices, how='left', on='product')
print("\n3c. Merged with prices:")
print(all_sales_merged)

# 3d - Calculate units sold
all_sales_merged['units_sold'] = all_sales_merged['sales'] / all_sales_merged['unit_price']
print("\n3d. With units sold:")
print(all_sales_merged)

# 3e - Group by category
category_summary = all_sales_merged.groupby('category').agg({
    'sales': 'sum',
    'units_sold': 'sum'
}).reset_index()
print("\n3e. Category summary:")
print(category_summary)
