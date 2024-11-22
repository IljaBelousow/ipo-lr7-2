import json

# Запрашиваем ввод пользователя
user_input = input("Введите номер: ")

# Флаг для проверки наличия записи
found = False

# Читаем данные из JSON-файла
with open("dump.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

    # Поиск записи по model и code
    for i in data:
        if i.get("model") == "data.skill" and i["fields"].get("code") == user_input:
            skill_code = i["fields"].get("code")
            skill_title = i["fields"].get("title")
            specialty_id = i["fields"].get("specialty")
            found = True

            # Ищем соответствующую специальность
            for specialty_i in data:
                if specialty_i.get("pk") == specialty_id and specialty_i.get("model") == "data.specialty":
                    specialty_code = specialty_i["fields"].get("code")
                    specialty_title = specialty_i["fields"].get("title")
                    specialty_depend = specialty_i["fields"].get("c_type")

            break

# Проверяем и выводим результаты
if not found:
    print("=============== Не Найдено ===============")
else:
    print("=============== Найдено ===============")
    print(f"{specialty_code} >> Специальность {specialty_title} , {specialty_depend}")
    print(f"{skill_code} >> Квалификация {skill_title}")
