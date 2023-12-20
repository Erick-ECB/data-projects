import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def connection():
    return psycopg2.connect(
        host = os.getenv('HOST'),
        database = os.getenv('DATABASE'),
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD')
    )