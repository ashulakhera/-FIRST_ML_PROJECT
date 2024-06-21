import os
import sys
from src.mlprojects.exception import CustomException
from src.mlprojects.logger import logging
import pandas as pd
from dotenv import load_dotenv

import pymysql


load_dotenv()

host=os.getenv("host") 
User=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    from src.mlprojects.utils import read_sql_data
    logging.info("Reading sql database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=User,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('select * from students',mydb)
        print(df.head())

        return df
    except Exception as ex:
        raise CustomException(ex)