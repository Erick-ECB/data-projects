import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def connection():
    return psycopg2.connect(
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
    )
