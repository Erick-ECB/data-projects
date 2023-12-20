import pandas as pd
import psycopg2
from psycopg2 import sql


def get_columns(cursor, table_name: str) -> list:
    """Retrieve the column names for a given table."""
    query = f"SELECT column_name \
            FROM information_schema.columns \
            WHERE table_name = '{table_name}' \
            ORDER BY ordinal_position;"

    cursor.execute(query)

    column_name = [row[0] for row in cursor.fetchall()]

    return column_name


def insert_rows(cursor, df: pd.DataFrame, table_name: str, columns: tuple):
    """Insert rows into a database table."""
    query = insert_query(table_name, columns)

    for (
        index,
        row,
    ) in df.iterrows():
        try:
            cursor.execute(query, tuple(row))
        except Exception as e:
            print(f"Error inserting row {index}: {e}")
            print("Row values:", tuple(row))
            print("Generated query:", cursor.mogrify(query, tuple(row)))
            raise e


def insert_query(table_name: str, columns: tuple):
    """Generate an SQL insert query."""
    return sql.SQL("INSERT INTO {table} ({columns}) VALUES ({values})").format(
        table=sql.Identifier(table_name),
        columns=sql.SQL(", ").join(map(sql.Identifier, columns)),
        values=sql.SQL(", ").join(sql.Placeholder() * len(columns)),
    )


def close_connection(conn, cursor):
    conn.commit()
    cursor.close()
    conn.close()
