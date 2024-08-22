import os
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from sqlalchemy import create_engine

stock_code = os.environ.get('STOCK_CODE')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
host_ip = os.environ.get('HOST_IP')

# Print credentials to debug
print(f"STOCK_CODE: {stock_code}")
print(f"USERNAME: {username}")
print(f"PASSWORD: {password}")
print(f"HOST_IP: {host_ip}")

url = "https://www.screener.in/company/RELIANCE/consolidated/"
webpage = requests.get(url)
soup = bs(webpage.text,'html.parser')
data = soup.find('section', id="profit-loss")
tdata= data.find("table")
table_data = []

for row in tdata.find_all('tr'):
    row_data = []
    for cell in row.find_all(['th','td']):
        row_data.append(cell.text.strip())
    table_data.append(row_data)

df_table = pd.DataFrame(table_data)
df_table.iloc[0,0] = 'Section'
df_table.columns = df_table.iloc[0]
df_table = df_table[1:]

df_table['Stock'] = "reliance" 
df_table = df_table.reset_index()

db_host = "host_ip"
db_name = "db"
db_user = "username"
db_password = "password"
db_port = "5432"

engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
df_table.to_sql('profit_loss_data', engine, if_exists='replace', index=False)

print("Data loaded successfully into PostgreSQL database!")
