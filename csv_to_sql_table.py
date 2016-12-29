# turn a csv to a table in postgresql database
import os
import pandas
from sqlalchemy import create_engine

#db_string = os.environ['DATABASE_URL']
from os.path import expanduser

with open(expanduser('~/.pgpass'), 'r') as f:
    host, port, database, user, password = f.read().replace('\n','').split(':')
    database_uri = 'postgresql://{}:{}@{}/{}'.format(user, password, host, database)

conn = create_engine(database_uri).connect()

df = pandas.read_csv("./group_data.csv")
df.to_sql('demo_sales', conn, index=False)



