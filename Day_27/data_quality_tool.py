import pandas as pd
import numpy as np

def generate_data_quality_report(file_path):
    print(f"\n{'='*50}")
    print(f"DATA QUALITY REPORT FOR: {file_path}")
    print(f"{'='*50}\n")
    
    # Load dataset
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    total_rows = len(df)
    total_columns = len(df.columns)
    
    print(f"Dataset Overview:")
    print(f"- Total Rows: {total_rows}")
    print(f"- Total Columns: {total_columns}\n")
    
    # 1. Missing Values & Completeness Metrics
    missing_data = df.isnull().sum()
    missing_percentage = (missing_data / total_rows) * 100
    completeness = 100 - missing_percentage
    
    missing_df = pd.DataFrame({
        'Missing Values': missing_data,
        'Missing Percentage (%)': missing_percentage.round(2),
        'Completeness (%)': completeness.round(2)
    })
    
    print("--- 1. Missing Values & Completeness ---")
    print(missing_df[missing_df['Missing Values'] > 0])
    print("\n")

    # 2. Duplicate Records
    duplicate_count = df.duplicated().sum()
    print("--- 2. Duplicate Records ---")
    print(f"Total Duplicate Rows: {duplicate_count}\n")

    # 3. Data Types & Unique-Value Counts
    print("--- 3. Data Types & Unique Values ---")
    dtype_unique_df = pd.DataFrame({
        'Data Type': df.dtypes,
        'Unique Values': df.nunique(),
        'Distinct (%)': (df.nunique() / total_rows * 100).round(2)
    })
    print(dtype_unique_df)
    print("\n")

    # 4. Suspicious Records / Anomalies (Example: Numeric outliers using IQR)
    print("--- 4. Suspicious Records / Outliers (Numeric Columns) ---")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    outlier_summary = {}
    
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        outlier_summary[col] = len(outliers)
        
    outlier_df = pd.DataFrame(list(outlier_summary.items()), columns=['Column', 'Potential Outliers'])
    print(outlier_df)
    print("\n")
    
    # 5. Invalid Record Report (Exporting summary or sample anomalies)
    print("--- 5. Summary Report Generated Successfully ---")
    print("You can extend this script to export these metrics to a CSV or JSON file.")

# Example usage:
# generate_data_quality_report('your_dataset.csv')
