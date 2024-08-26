import pandas as pd
import xlwings as xw

# Open the workbook
wb = xw.Book('Reliance Industr.xlsx')

# Refresh the workbook
wb.refresh()

# Save the workbook
wb.save()

# Read the Excel file
df = pd.read_excel('Reliance Industr.xlsx', sheet_name='Profit & Loss')

# Print the DataFrame
print(df)