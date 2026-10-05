#Lad os modellere en customer tabel

#Først udvælges/findes en masse attributter om en kunde som man gerne vil gemme. Tænk på en forretning som har en kundedatabase.

#Jeg håber vi finder 5-10 attributter (felter).
#En af dem skal være unik og altså blive til primærnøgle. Vi laver enten et kunstigt nummer eller vælger telefonnummeret, måske.

#Proceduren er herefter:
#Lav tabelstrukturen med CREATE TABLE
#Indsæt rækker med INSERT INTO
#Lav et par søgninger med SELECT.

def generateUUID():
    import uuid
    return str(uuid.uuid4())

customerAttributes = [
    "uuid", "name", "age", "email", "phone", "address", "city", "country", "postal_code", "created_at", "updated_at"
]

def generate_customers_sql_table(customerAttributes):
    sql = "CREATE TABLE IF NOT EXISTS customers ("
    for attr in customerAttributes:
        sql += f"{attr} TEXT, "
    sql = sql[:-2] + ", PRIMARY KEY (uuid))"
    print(sql)
    return sql

import sqlite3
from datetime import datetime, timezone

db_path = "customers.db"

def get_connection():
    """Open a connection to the SQLite database (creates file if missing)."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_customer_table(conn=None):
    """Create the customers table if it does not exist."""
    close_after = conn is None
    conn = conn or get_connection()
    conn.execute(generate_customers_sql_table(customerAttributes))
    conn.commit()
    if close_after:
        conn.close()

def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def insert_customer(name, email, uuid=None, age=None, phone=None,
                    address=None, city=None, country=None, postal_code=None,
                    conn=None):
    """Insert a new customer. UUID, created_at and updated_at are auto-generated."""
    uuid = uuid or generateUUID()
    now = _now()
    close_after = conn is None
    conn = conn or get_connection()
    conn.execute(
        "INSERT INTO customers (uuid, name, age, email, phone, address, city, country, postal_code, created_at, updated_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (uuid, name, age, email, phone, address, city, country, postal_code, now, now),
    )
    conn.commit()
    if close_after:
        conn.close()
    return uuid

def update_customer(uuid, **fields):
    """Update any customer fields (name=..., email=..., ...) and refresh updated_at."""
    allowed = set(customerAttributes) - {"uuid", "created_at", "updated_at"}
    unknown = set(fields) - allowed
    if unknown:
        raise ValueError(f"Unknown fields: {unknown}")
    if not fields:
        return 0
    cols = ", ".join(f"{k} = ?" for k in fields)
    params = list(fields.values()) + [_now(), uuid]
    with get_connection() as conn:
        cur = conn.execute(f"UPDATE customers SET {cols}, updated_at = ? WHERE uuid = ?", params)
        conn.commit()
        return cur.rowcount

def get_customer(uuid):
    """Fetch a single customer by uuid (returns dict or None)."""
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute("SELECT * FROM customers WHERE uuid = ?", (uuid,)).fetchone()
        return dict(row) if row else None

def find_customers(search=None, limit=100):
    """List customers, optionally fuzzy-searching name/email/phone/city."""
    with get_connection() as conn:
        conn.row_factory = sqlite3.Row
        if search:
            pattern = f"%{search}%"
            rows = conn.execute(
                "SELECT * FROM customers WHERE name LIKE ? OR email LIKE ? OR phone LIKE ? OR city LIKE ? LIMIT ?",
                (pattern, pattern, pattern, pattern, limit),
            ).fetchall()
        else:
            rows = conn.execute("SELECT * FROM customers LIMIT ?", (limit,)).fetchall()
        return [dict(r) for r in rows]

def delete_customer(uuid):
    """Delete a customer by uuid. Returns number of rows deleted."""
    with get_connection() as conn:
        cur = conn.execute("DELETE FROM customers WHERE uuid = ?", (uuid,))
        conn.commit()
        return cur.rowcount

def count_customers():
    """Return the total number of customers."""
    with get_connection() as conn:
        return conn.execute("SELECT COUNT(*) FROM customers").fetchone()[0]

if __name__ == "__main__":
    create_customer_table()
    print("Tables created.")
    uuid1 = insert_customer("Alice Hansen", "alice@example.com", age=31, city="Aarhus", country="Denmark")
    insert_customer("Bob Jensen", "bob@example.com", phone="12345678", city="København")
    print(f"{count_customers()} customers in db:")
    for c in find_customers("alice"):
        print(c)
