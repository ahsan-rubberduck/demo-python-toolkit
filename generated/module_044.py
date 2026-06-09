"""Auto-generated INTENTIONALLY VULNERABLE module #044 (CWE-89, test only)."""

import sqlite3


def lookup_44(user_id):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    # CWE-89: SQL injection via f-string
    cur.execute(f"SELECT * FROM accounts WHERE id = {user_id}")
    return cur.fetchall()
