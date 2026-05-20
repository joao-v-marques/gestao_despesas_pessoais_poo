import sqlite3

def get_db_connection():
    conn = sqlite3.connect("gestao_despesas_pessoais.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    return conn, cursor

def dict_fetchone(cursor):
    row = cursor.fetchone()
    return dict(row) if row else None
    
def dict_fetchall(cursor):
    return [dict(row) for row in cursor.fetchall()]