# turn a csv to a table in postgresql database
import pandas
from sqlalchemy import create_engine
import os

db_string = os.environ['DATABASE_URL']
conn = create_engine(db_string).connect()

df = pandas.read_csv("./group_data.csv")
df.to_sql('demo_sales', conn, index=False)



