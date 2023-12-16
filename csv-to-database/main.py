import pandas as pd
from connection import connection


def read_csv(csv_file) -> pd.DataFrame:
    return pd.read_csv(csv_file, skiprows=1)


def get_columns(cursor, table_name: str) -> tuple:
    query = f"SELECT column_name \
            FROM information_schema.columns \
            WHERE table_name = '{table_name}';"

    cursor.execute(query)

    column_name = [row[0] for row in cursor.fetchall()]

    return tuple(column_name)


def insert_rows(cursor, df: pd.DataFrame, table_name: str, columns):
    str_columns = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(columns))
    for index, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {table_name} ({str_columns}) \
                       VALUES (%s)",
            tuple(row),
        )


def close_connection(conn, cursor):
    conn.commit()
    cursor.close()
    conn.close()


def main():
    csv = "data/books.csv"
    table_name = "books"

    conn = connection()
    cursor = conn.cursor()

    columns = get_columns(cursor, table_name)
    df = read_csv()

    insert_rows(cursor, df, table_name, columns)

    close_connection(conn, cursor)


if __name__ == "__main__":
    main()
