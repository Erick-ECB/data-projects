import pandas as pd
from utils.data_reader import create_dataset
from utils.data_processing import process_data
from utils.connection import connection
from utils.db_operations import get_columns, insert_rows, close_connection


def main():
    table_name = "wine_reviews"
    df = create_dataset()
    df = process_data(df)

    conn = connection()
    cursor = conn.cursor()

    cols = get_columns(cursor, table_name)
    insert_rows(cursor, df, table_name, cols[1:])
    close_connection(conn, cursor)


if __name__ == "__main__":
    main()
