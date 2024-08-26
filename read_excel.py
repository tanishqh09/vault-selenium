import pandas as pd
from xlwings import Reader

# Open the workbook using xlwings Reader
with Reader('Reliance Industr.xlsx') as reader:
    # Read the Excel file
    df = reader.read('Profit & Loss')

# Print the DataFrame
print(df)
