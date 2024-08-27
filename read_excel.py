import pandas as pd
file_path = "Reliance Industr.xlsx"
try:
    df = pd.read_excel(file_path, engine="openpyxl")
    print("Excel file contents:")
    print(df)
except Exception as e:
    print(f"Failed to read the Excel file: {e}")' 
