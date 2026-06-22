import pandas as pd

product_data = pd.DataFrame({
    'prod_code': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'USB Cable'],
    'price': [999.99, 25.50, 75.00, 199.00, 12.75],
    'stock_qty': [50, 200, 150, 30, 500],
    'supplier_info': ['Supplier A', 'Supplier B', 'Supplier A', 'Supplier C', 'Supplier B'],
    'warehouse_id': ['WH1', 'WH2', 'WH1', 'WH3', 'WH2']
})


"""

Tasks:

2a. Rename the columns to:
'prod_code' → 'Product ID'
'product_name' → 'Name'
'stock_qty' → 'Stock'
'supplier_info' → 'Supplier'
'warehouse_id' → 'Warehouse'
2b. Reorder the columns so the order is: ['Product ID', 'Name', 'Price', 'Stock', 'Supplier', 'Warehouse']
2c. Rename the index labels from 0,1,2,3,4 to 'Row1', 'Row2', 'Row3', 'Row4', 'Row5'


"""

renamed = product_data.rename(columns={
'prod_code' : 'Product ID',
'product_name' : 'Name',
'stock_qty' : 'Stock',
'supplier_info' : 'Supplier',
'warehouse_id' : 'Warehouse'
})
print('\n\n renamed:\n')

print(renamed)