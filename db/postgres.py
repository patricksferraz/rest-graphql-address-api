import psycopg2
import os

POSTGRES_URL = os.environ["POSTGRES_URL"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PW = os.environ["POSTGRES_PW"]
POSTGRES_DB = os.environ["POSTGRES_DB"]


def connect():
    try:
        return psycopg2.connect(
            host=POSTGRES_URL,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PW,
        )
    except Exception as e:
        return e
