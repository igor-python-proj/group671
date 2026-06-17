def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)

def add_student(
        conn,
        name,
        age,
        city
):
    conn.execute("""
    INSERT INTO students VALUES
    (?, ?, ?)
    """,
        (name, age, city))
    conn.commit()