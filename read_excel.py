import pandas as pd

def read_profit_loss_sheet():
    try:
        # Read the Excel file
        df = pd.read_excel('Reliance Industr.xlsx', sheet_name='Data Sheet')
        print(df)
    except Exception as e:
        print(f"Error reading Excel file: {e}")

if __name__ == "__main__":
    read_profit_loss_sheet()
