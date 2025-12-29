import pandas as pd
import os

# Use relative path - better for portability
csv_file = "Citywide_Payroll_Data__Fiscal_Year_.csv"

# Check if file exists
if not os.path.exists(csv_file):
    print(f"Error: File '{csv_file}' not found!")
    print(f"Current directory: {os.getcwd()}")
else:
    print(f"Loading data from: {csv_file}")
    
    # Load the data
    try:
        data = pd.read_csv(csv_file)
        print("\n✓ Data loaded successfully!")
        
        # Basic data validation
        print(f"\nData shape: {data.shape[0]:,} rows × {data.shape[1]} columns")
        print(f"\nColumn names:")
        for i, col in enumerate(data.columns, 1):
            print(f"  {i}. {col}")
        
        print(f"\nFirst few rows:")
        print(data.head())
        
        print(f"\nData types:")
        print(data.dtypes)
        
        print(f"\nBasic info:")
        print(data.info())
        
    except Exception as e:
        print(f"Error loading data: {e}")