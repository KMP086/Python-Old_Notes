#pip install pyodbc
#pip install sqlalchemy
# pip install pandas
import urllib.parse
import pandas as pd
import pyodbc
from sqlalchemy import *

#s for single data or m for multiple data or n for no display
def readsql(drive,servername,dbname, uname, pword, query, sm):
    conscript = "Driver=" + drive + ";Server=" + servername + ";Database=" + dbname + ";UID=" + uname + ";PWD=" + pword
    #print(conscript)
    cndb = pyodbc.connect(conscript)
    cursor = cndb.cursor()
    #stored proc query = 'exec sp_sproc(123, 'abc')'
    cursor.execute(query)
    for item in cursor:
        if sm == 's':
            return item[0]
        elif sm == 'm':
            return item

#for insert into or update set (single entry only)
def altersql(drive,servername,dbname, uname, pword, query, val):
    #query = 'insert into table(a,b,c) value(?,?,?)'
    #values = [(a,b,c)]
    conscript = "Driver=" + drive + ";Server=" + servername + ";Database=" + dbname + ";UID=" + uname + ";PWD=" + pword
    #print(conscript)
    cndb = pyodbc.connect(conscript)
    cursor = cndb.cursor()
    cursor.execute(query, val)
    cndb.commit()

#insert and update multiple rows
# sqltype type append or replace
#note dataframe column name must be identical SQL Column Name
def bulksql(drive,servername,dbname, uname, pword, dataf, sqltable, sqltype):
    sqlparam = urllib.parse.quote_plus(f"Driver={drive};Server={servername};Database={dbname};UID={uname};PWD={pword}")
    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(sqlparam), use_setinputsizes=False)
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(dataf)
    df = df.astype(str)
    print(df)
    df.to_sql(con=engine, name=sqltable, if_exists=sqltype, index=False, chunksize=1000)


