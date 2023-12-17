import pandas as pd
from connection import connection
from psycopg2 import sql


def read_csv(csv_file: str) -> pd.DataFrame:
    return pd.read_csv(csv_file)


def get_columns(cursor, table_name: str) -> list:
    query = f"SELECT column_name \
            FROM information_schema.columns \
            WHERE table_name = '{table_name}' \
            ORDER BY ordinal_position;"

    cursor.execute(query)

    column_name = [row[0] for row in cursor.fetchall()]

    return column_name


def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = df.copy()

    df_copy[
        ["subtitle", "authors", "categories", "thumbnail", "description"]
    ] = df_copy[
        ["subtitle", "authors", "categories", "thumbnail", "description"]
    ].fillna(
        ""
    )

    df_copy["published_year"].fillna(df_copy["published_year"].mean(), inplace=True)
    df_copy["average_rating"].fillna(df_copy["average_rating"].mean(), inplace=True)
    df_copy["num_pages"].fillna(df_copy["num_pages"].mean(), inplace=True)
    df_copy["ratings_count"].fillna(df_copy["ratings_count"].mean(), inplace=True)

    df_copy["isbn13"] = df_copy["isbn13"].astype(str)
    df_copy["isbn10"] = df_copy["isbn10"].astype(str)
    df_copy["title"] = df_copy["title"].astype(str)
    df_copy["subtitle"] = df_copy["subtitle"].astype(str)
    df_copy["authors"] = df_copy["authors"].str.split("; ")
    df_copy["categories"] = df_copy["categories"].str.split("; ")
    df_copy["thumbnail"] = df_copy["thumbnail"].astype(str)
    df_copy["description"] = df_copy["description"].astype(str)
    df_copy["published_year"] = df_copy["published_year"].astype(int)
    df_copy["num_pages"] = df_copy["num_pages"].astype(int)
    df_copy["ratings_count"] = df_copy["ratings_count"].astype(int)

    return df_copy


def insert_rows(cursor, df: pd.DataFrame, table_name: str, columns: tuple):
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
    return sql.SQL("INSERT INTO {table} ({columns}) VALUES ({values})").format(
        table=sql.Identifier(table_name),
        columns=sql.SQL(", ").join(map(sql.Identifier, columns)),
        values=sql.SQL(", ").join(sql.Placeholder() * len(columns)),
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
    df = read_csv(csv)
    df_processed = preprocess_dataframe(df)

    insert_rows(cursor, df_processed, table_name, columns)

    close_connection(conn, cursor)


if __name__ == "__main__":
    main()
