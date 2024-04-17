from io import StringIO
import pandas as pd
import os
import sqlalchemy as db
from sqlalchemy import text
import pandas as pd

engine = db.create_engine("mysql+pymysql://root:M7{$'Oru|&aB{>#@104.197.207.218:3306/bd-sql-1")
conn = engine.connect()

customers_df = pd.read_sql_query(text('SELECT * FROM customer'), con=conn)
customers_df.head()
conn.close()