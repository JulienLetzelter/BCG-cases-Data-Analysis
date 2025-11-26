import pandas as pd
import os
import sys

# Add parent directory to path to import from utils
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.department_info import DEPARTMENT_NUMBERS

def correct_barley_yield_data():
    """
    Corrects barley yield data by adding:
    - Department number
    - Yield (productivity) calculated as production/area if missing
    """
    # Get the directory where this script is located
    script_dir = os.path.dirname(__file__)
    
    # File paths (relative to script)
    input_file = os.path.join(script_dir, 'original_data', 'barley_yield_from_1982.csv')
    output_file = os.path.join(script_dir, 'barley_yield_from_1982.csv')
    
    # Check that input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File {input_file} does not exist")
    
    # Read original CSV file
    df = pd.read_csv(input_file, sep=';')
    
    
    # Add department number
    df['department_number'] = df['department'].map(DEPARTMENT_NUMBERS)
    
    # Remove unmapped departments
    initial_count = len(df)
    df = df[df['department_number'].notna()].copy()
    removed_count = initial_count - len(df)
    
    # Convert numeric columns
    df['area'] = pd.to_numeric(df['area'], errors='coerce')
    df['production'] = pd.to_numeric(df['production'], errors='coerce')
    df['yield'] = pd.to_numeric(df['yield'], errors='coerce')
    
    # If area or production is null/missing, set yield, area and production to empty
    invalid_data = df['area'].isna() | df['production'].isna() | (df['area'] == 0) | (df['production'] == 0)
    if invalid_data.sum() > 0:
        df.loc[invalid_data, 'yield'] = pd.NA
        df.loc[invalid_data, 'area'] = pd.NA
        df.loc[invalid_data, 'production'] = pd.NA
    
    # Calculate yield (productivity) if missing
    missing_yield = df['yield'].isna()
    can_calculate = missing_yield & df['area'].notna() & df['production'].notna() & (df['area'] > 0) & (df['production'] > 0)
    
    if can_calculate.sum() > 0:
        df.loc[can_calculate, 'yield'] = (df.loc[can_calculate, 'production'] / df.loc[can_calculate, 'area']).round(5)
    
    # Reorder columns: id, department, department_number, year, yield, area, production
    columns_order = ['id', 'department', 'department_number', 'year', 'yield', 'area', 'production']
    df = df[columns_order]
    
    # Save corrected file
    # Use na_rep='' to write NaN values as empty fields
    df.to_csv(output_file, sep=';', index=False, na_rep='')
    
    print(f"Number of rows: {len(df)}")
    print(f"Number of unique departments: {df['department'].nunique()}")
    print(f"Number of calculated yield values: {can_calculate.sum() if can_calculate.sum() > 0 else 0}")
    
    return df

if __name__ == "__main__":
    df_corrected = correct_barley_yield_data()

