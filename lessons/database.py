def create_tables(conn):
    conn.execute("""
    DROP TABLE IF EXISTS students
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)

# CRUD - create, read, update, delete
# добавление, получение, изменение, удаление

def add_student(
        conn,
        name,
        age,
        city
):
    conn.execute("""
    INSERT INTO students(name, age,city) VALUES
    (?, ?, ?)
    """,
        (name, age, city))
    conn.commit()

def get_students(conn):
    result = conn.execute("""
        SELECT age, name FROM students
    """)
    # return result.fetchone()
    # return result.fetchmany(2)
    return result.fetchall()

def get_student_by_name(
        conn,
        name
):
    result = conn.execute("""
        SELECT * FROM students
        WHERE name = ? AND age < 30
        """,
        (name,)
    )
    return result.fetchall()


def get_student_by_id(
        conn,
        student_id
):
    result = conn.execute("""
        SELECT * FROM students
        WHERE id = ?
        """,
        (student_id,)
    )
    return result.fetchone()

def delete_student(
        conn,
        student_id
):
    conn.execute("""
    DELETE FROM students
    WHERE id = ?
    """, (student_id,)
    )
    conn.commit()

def update_student(
        conn,
        name,
        age,
        city,
        student_id
):
    conn.execute("""
    UPDATE students
    SET name = ?, 
    age = ?, city = ?
    WHERE id = ?
    """,
    (name, age, city, student_id)
    )
    conn.commit()