from connection import connection


def main():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute("SELECT version();")
    result = cursor.fetchone()

    print(f"PostgreSQL version: {result[0]}")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
