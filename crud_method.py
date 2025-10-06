import sqlite3
from contextlib import closing

DB_PATH = "escola.db"

def connect_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_table(conn):
    with conn:
        conn.execute()
