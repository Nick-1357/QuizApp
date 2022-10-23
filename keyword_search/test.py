import pandas as pd
from sqlalchemy import create_engine
import py_mysql_connector

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/its")
query = pd.read_sql_query('SELECT content FROM eSPFirst WHERE chapter = 1', engine)
df = pd.DataFrame(query)
print(df["content"].tolist())
