import pandas as pd
from sqlalchemy import create_engine

# the csv file is : interfaces.csv
#database will be : database.db
# the table name is  : interfaces

df = pd.read_csv('interfaces.csv')
engine = create_engine('sqlite:///database.db')
df.to_sql('interfaces', engine) #With this one the table and database must not already exists
#df.to_sql('interfaces', con=engine, if_exists='append')   #with this one you can append data to an existing database
#df.to_sql('interfaces', con=engine, if_exists='replace')   #with this one you can truncat an existing database