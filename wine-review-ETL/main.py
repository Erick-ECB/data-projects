import pandas as pd
from utils.data_reader import create_dataset
from utils.data_processing import process_data
from utils.connection import connection
from utils.db_operations import get_columns, insert_rows, close_connection
from utils.logging_config import logger


def main():
    try:
        logger.info("Script_started")
        table_name = "wine_reviews"

        logger.info("Create dataset")
        df = create_dataset()

        logger.info("Process dataset")
        df = process_data(df)

        logger.info("Establish database connection")
        conn = connection()
        cursor = conn.cursor()

        cols = get_columns(cursor, table_name)

        logger.info("Inserting rows into the database")
        insert_rows(cursor, df, table_name, cols[1:])
        logger.info("Data inserted successfully")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        close_connection(conn, cursor)
        logger.info("Script ended")


if __name__ == "__main__":
    main()
