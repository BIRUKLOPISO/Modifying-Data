import pandas as pd
import numpy as np

df = pd.DataFrame({
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT'],
    'bonus': [5000, -1000, 7000, 3000, -500],
    'salary': [60000, -55000, 65000, 52000, 58000]  # ← Bob now has NEGATIVE salary!
})
#Task 1 (.mask()): Using .mask(), replace any negative salary with 0. Create a new column called salary_clean.
#Task 2 (.mask()): Using .mask(), replace bonus values less than 1000 with 1000. Create a new column called bonus_min.
#Task 3 (.where()): Using .where(), keep department 'Sales' as-is, but replace all other departments with 'Other'. Create a new column called dept_clean.
#Task 4 (.where()): Using .where(), keep salaries between 55000 and 65000 (inclusive) as-is, but replace others with np.nan. Create a new column called salary_mid.

df['salary_clean']=df['salary'].mask(df['salary']<0,0)
df['bonus_min']=df['bonus'].mask(df['bonus']<1000,1000)
df['dept_clean']=df['department'].where(df['department'] == 'Sales','Other')
df['salary_mid']=df['salary'].where((65000 >= df['salary']) & (df['salary'] >=55000),np.nan)
print(df)
