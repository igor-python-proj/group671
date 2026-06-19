import sqlite3

from lessons.database import (
    create_tables,
    add_student,
    get_students,
    get_student_by_name,
    get_student_by_id,
    delete_student,
    update_student,
)

if __name__ == "__main__":
    connection = sqlite3.connect(
        "database.db"
    )

    create_tables(connection)
    add_student(
        connection,
        'Artur',
        19,
        'Karakol'
    )
    add_student(
        connection,
        'Aijamal',
        23,
        'Naryn'
    )
    add_student(
        connection,
        'Igor',
        25,
        'Karakol'
    )
    add_student(
        connection,
        'Igor',
        32,
        'Bishkek'
    )
    print("== get students ==")
    students = get_students(connection)
    for st in students:
        print(st)

    print("== search by name ==")
    student = get_student_by_name(
        connection,
        'Igor',
    )
    print(student)
    student2 = get_student_by_name(
        connection,
        'Dastan',
    )
    print(student2)
    student3 = get_student_by_id(
        connection,
        10,
    )
    print(student3)

    print("== delete students ==")
    delete_student(
        connection,
        4
    )
    print(get_students(connection))

    print("== update students ==")
    update_student(
        connection,
        'Artur',
        20,
        'Kara-Balta',
        1
    )
    print(get_student_by_id(
        connection,
        1
    ))

    connection.close()
