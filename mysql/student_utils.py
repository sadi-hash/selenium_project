from db.student_sql import Student
from db.utils import clear_terminal

def get_students(students):
    print(f"Количество студентов: {len(students)}")
    for n,s in enumerate(students, start=1):
        print(f"{n}){s[1]} {s[2]}-{s[3]}-{s[4]}")


def student_action(cursor):
    student = Student(cursor)
    student.create_table()
    clear_terminal()

    print("Выберите действие: ")
    print("""
        1. Добавить нового студента
        2. Получить список всех студентов
        3. Получпть студентов по группе:
        4. Получить данные студента
        5. Удалить студента
    """)
    action_number = int(input("Номер действия: "))
    clear_terminal()
    if action_number == 1:
        print("Заполните данные нового студента: ")
        first_name = input("Напишите имя студента: ")
        last_name = input("Напишите фамилию студента: ")
        email = input("Напишите Email студента: ")
        group_id = input("Напишите номер группы студента: ")
        data = {
            "first_name":first_name,
            "last_name":last_name,
            "email": email,
            "group_id":group_id
            }
        student.add_new_student(data=data)
        clear_terminal()
        print("Студент успешно создан!")
    elif action_number == 2:
        students = student.get_all_students()
        get_students(students)

    
    elif action_number == 3:
        group_number = int(input("Введите номер группы:"))
        students = student.get_students_by_group(group_number)
        get_students(students)


    elif action_number == 5:
        student_id = int(input("Напишите id студента для удаления: "))
        student.delete_student(student_id=student_id)
        clear_terminal()
        print("Студент успешно удален!")
