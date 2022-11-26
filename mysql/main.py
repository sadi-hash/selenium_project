import mysql.connector
from db.group_sql import Group
from group_utils import group_action
from student_utils import student_action
import os


db = mysql.connector.connect(
host = "localhost",
user = "root",
password = "qwerty",
autocommit = True,
db = "students_db",
)

cursor = db.cursor()


print("Выберите действие: ")
print("""
    1. Редактирование групп
    2. Редактирование студента
""")

action_number = int(input("Введите номер действия: "))
if action_number == 1:
    group_action(cursor)
elif action_number == 2:
    student_action(cursor)


