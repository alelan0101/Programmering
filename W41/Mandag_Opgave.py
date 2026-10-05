#Opret en database med navnet users.db og en tabel users med følgende kolonner:
# id (heltal, primærnøgle)
# username (tekst)
# dateofbirth (tekst)
# login_attempts (heltal)

# Indsæt 10 brugere med forskellige værdier for login_attempts, og gem med commit().
# Lav derefter følgende forespørgsler:
# 1. Hent alle brugere og udskriv dem.
# 2. Hent kun brugernavnene og udskriv dem.
# 3. Hent alle brugere hvor login_attempts er større end 10.
# 4. Luk databasen.

import sqlite3

db_path = "users.db"

def get_connection():
    """Open a connection to the SQLite database (creates file if missing)."""
    return sqlite3.connect(db_path)

def create_users_table(conn=None):
    """Create the users table if it does not exist."""
    close_after = conn is None
    conn = conn or get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            dateofbirth TEXT,
            login_attempts INTEGER
        )
        """
    )
    conn.commit()
    if close_after:
        conn.close()

def insert_user(username, dateofbirth, login_attempts, conn=None):
    """Insert a single user. Returns the new row id."""
    close_after = conn is None
    conn = conn or get_connection()
    cur = conn.execute(
        "INSERT INTO users (username, dateofbirth, login_attempts) VALUES (?, ?, ?)",
        (username, dateofbirth, login_attempts),
    )
    conn.commit()
    if close_after:
        conn.close()
    return cur.lastrowid

def get_all_users(conn=None):
    """Fetch all users (returns list of dicts)."""
    close_after = conn is None
    conn = conn or get_connection()
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM users").fetchall()
    if close_after:
        conn.close()
    return [dict(r) for r in rows]

def get_all_usernames(conn=None):
    """Fetch only the usernames (returns list of strings)."""
    close_after = conn is None
    conn = conn or get_connection()
    rows = conn.execute("SELECT username FROM users").fetchall()
    if close_after:
        conn.close()
    return [r[0] for r in rows]

def get_users_with_many_attempts(threshold=10, conn=None):
    """Fetch all users where login_attempts is greater than threshold."""
    close_after = conn is None
    conn = conn or get_connection()
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT * FROM users WHERE login_attempts > ?", (threshold,)
    ).fetchall()
    if close_after:
        conn.close()
    return [dict(r) for r in rows]

def close_database(conn):
    """Close the database connection."""
    conn.close()

if __name__ == "__main__":
    create_users_table()

    # Indsæt 10 brugere med forskellige login_attempts (én connection, commit i insert_user).
    conn = get_connection()
    users = [
        ("alice",   "1990-03-12", 3),
        ("bob",     "1985-07-04", 7),
        ("carla",   "1992-11-23", 12),
        ("david",   "1979-01-30", 0),
        ("eva",     "2001-05-18", 15),
        ("frank",   "1995-09-09", 2),
        ("grethe",  "1988-12-01", 42),
        ("henrik",  "1973-06-25", 10),
        ("ida",     "1998-02-14", 25),
        ("jonas",   "2000-10-31", 5),
    ]
    for username, dob, attempts in users:
        insert_user(username, dob, attempts, conn=conn)

    # 1. Hent alle brugere og udskriv dem.
    print("Alle brugere:")
    for user in get_all_users(conn):
        print(user)

    # 2. Hent kun brugernavnene og udskriv dem.
    print("\nBrugernavne:")
    for username in get_all_usernames(conn):
        print(username)

    # 3. Hent alle brugere hvor login_attempts er større end 10.
    print("\nBrugere med login_attempts > 10:")
    for user in get_users_with_many_attempts(10, conn=conn):
        print(user)

    # 4. Luk databasen.
    close_database(conn)
