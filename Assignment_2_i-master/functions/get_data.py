import logging

from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
import logging
import datetime

logging.basicConfig(filename="logs/logs.log", encoding="utf-8", level=logging.DEBUG)


# connect to Snowflake
# ---------------------------------------------------------------

# This function executes the query and returns a dataframe
def get_query_data(query) -> pd.DataFrame:
    logging.info(f"{datetime.datetime.now()}: Creating engine...")
    engine = create_engine(
        'snowflake://{user}:{password}@{account_identifier}/{database}/{schema}'.format(
            user=st.secrets.user,
            password=st.secrets.password,
            account_identifier=st.secrets.account_identifier,
            database=st.secrets.database,
            schema=st.secrets.schema,
            connect_args={'connect_timeout': 1000, 'read_timeout': 1000}
        )
    )
    logging.info(f"{datetime.datetime.now()}: Connecting engine...")
    engine.connect()
    logging.info(f"{datetime.datetime.now()}: Executing query...")
    df = pd.read_sql_query(query, engine)
    logging.info(f"{datetime.datetime.now()}: Dataframe retrieved..")
    engine.dispose()
    return df

# This function only executes the query. Nothing is returned
def execute_query(query):

    try:
        logging.info(f"{datetime.datetime.now()}: Creating engine...")
        engine = create_engine(
            'snowflake://{user}:{password}@{account_identifier}/{database}/{schema}'.format(
                user=st.secrets.user,
                password=st.secrets.password,
                account_identifier=st.secrets.account_identifier,
                database=st.secrets.database,
                schema=st.secrets.schema,
                connect_args={'connect_timeout': 1000, 'read_timeout': 1000}
            )
        )
        logging.info(f"{datetime.datetime.now()}: Connecting engine...")
        connection = engine.connect()
        logging.info(f"{datetime.datetime.now()}: Executing query...")
        connection.execute(query)

    finally:
        logging.info(f"{datetime.datetime.now()}: Execution finished...")
        connection.close()
        engine.dispose()