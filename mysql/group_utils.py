from db.group_sql import Group
from db.utils import clear_terminal

def group_action(cursor):
    group = Group(cursor)
    group._create_table()

    clear_terminal()

    print("Выберите действие с группами: ")
    print("""
        1 - Добавить группу
        2 - Получить все группы
        3 - Получить информацию о группе
    """)

    n = int(input("Введите номер действия: "))

    if n == 1:
        clear_terminal()
        name = input("Введите название группы: ").strip()
        start = input("Введите дату начало обучения: ").strip()
        finish = input("Введите дату конца обучения: ").strip()
        data = {
            "name":name,
            "start":start,
            "finish":finish
        }
        group.add_new_group(data=data)
        print("Группа успешно создано!")
    elif n == 2:
        clear_terminal()
        groups=group.get_all_groups()
        print(f"Количество: {len(groups)}")
        for g in groups:
            print("--------------------------------------")
            print(f"Номер группы: {g[0]}")
            print(f"Название: {g[1]}")
            print(f"Начало обучения: {g[2]}")
            print(f"Конец обучения: {g[3]}")

    elif n == 3:
        clear_terminal()
        group_id = int(input("Напишите номер группы: "))
        data = group.get_group(group_id)
        if data:
            print("--------------------------------------")
            print(f"Номер группы: {data[0]}")
            print(f"Название: {data[1]}")
            print(f"Начало обучения: {data[2]}")
            print(f"Конец обучения: {data[3]}")    
        else:
            print("Такой группы не существует.")