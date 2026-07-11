import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Customer_ID': [101, 102, 103, 104, 105, 106],
    'Customer_Name': ['John', np.nan, 'Sarah', 'Mike', np.nan, 'Emma'],
    'Age': [45, 32, np.nan, 29, 35, np.nan],
    'Order_Amount': [250, np.nan, 300, np.nan, 400, 350],
    'City': ['NYC', 'LA', np.nan, 'LA', 'NYC', np.nan],
    'Membership_Tier': ['Gold', 'Silver', np.nan, 'Gold', np.nan, 'Bronze']
})

def clean_dataframe(df):
    """Complete missing data cleaning workflow (future-proof)"""
    print("Step 1: Initial assessment")
    print(f"Shape: {df.shape}")
    print(f"Missing values:\n{df.isna().sum()}")

    print("\nStep 2: Check if we can drop columns with too many missing")
    missing_pct = (df.isna().sum() / len(df)) * 100
    cols_to_drop = missing_pct[missing_pct > 60].index.tolist()
    if cols_to_drop:
        print(f"Dropping columns: {cols_to_drop}")
        df = df.drop(cols_to_drop, axis=1)

    print("\nStep 3: Fill numerical missing with median")
    # Use 'number' to catch all numeric types (int, float, etc.)
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].mean())

    print("\nStep 4: Fill categorical missing with mode")
    cat_cols = df.select_dtypes(include=['object', 'string']).columns

    for col in cat_cols:
        mode_val = df[col].mode()
        df[col] = df[col].fillna(mode_val[0] if not mode_val.empty else 'Unknown')

    print("\nStep 5: Final assessment")
    print(f"Remaining missing: {df.isna().sum().sum()}")
    return df

print(clean_dataframe(df))
