import pandas as pd 
import numpy as np 
from sqlalchemy import create_engine

df = pd.read_csv('Cleaned_Credit_Card_Data.csv')

user = "root"
password = "pri8073"
host = "localhost"
database = "credit_card_Customer_db"

engine = create_engine(f"mysql+pymysql://{'root'}:{'pri8073'}@{'localhost'}/{"credit_card_Customer_db"}")

# Transfer Data to MySQL

df.to_sql('credit_card_customers', con=engine, if_exists='replace', index=False)

print(f"Data loaded successfully into table: {'credit_card_customers'}")