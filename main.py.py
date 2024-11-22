import json

with open("file.json", "r", encoding="utf-8") as a:
    file = json.load(a)

brik = 0
while brik < 1:
    print("""==================================
1 - Вывести все записи
2 - Вывести запись по ключу
3 - Добавить запись
4 - Удалить запись по ключу
5 - Выйти из программы
==================================""")
    
    user_input = int(input("Вы ввели: "))
    print("==================================")
#выводит все значения
    if user_input == 1:
        for i in file:
            print(f"""
            ID: {i["id"]}, 
            Имя: {i["name"]},                       
            Facture: {i["manufacturer"]}, 
            Benzin: {i["is_petrol"]},    
            v3: {i["tank_volume"]}
            """)
#выводит значение по ключу
    elif user_input == 2:
        id_input = input("Введите ключ: ")
        found = False
        for i in file:
            if id_input == i["id"]:  
                print(f"""
                ID: {i["id"]}, 
                Имя: {i["name"]},                       
                Facture: {i["manufacturer"]}, 
                Benzin: {i["is_petrol"]},    
                v3: {i["tank_volume"]}
                """)
                found = True
                break
        if not found:
            print("Такой записи нет :(")
#добавляет значение
    elif user_input == 3:
        add_input = input("Введите ключ для добавления: ")
        found_2 = False
        for i in file:
            if i["id"] == add_input:
                found_2 = True
                print("Такой ключ уже есть")
                break
        else:
            add_name_input = input("Введите название машины: ")
            add_creator_input = input("Введите название производителя: ")
            add_bool_input = input("Заправляется ли машина бензином (да/нет): ")
            add_cub_input = input("Введите объём бака в литрах: ")

            repository = {
                "id": add_input,
                "name": add_name_input,
                "manufacturer": add_creator_input,
                "is_petrol": True if add_bool_input == "да" else False,
                "tank_volume": add_cub_input,   
            }
            file.append(repository)
            with open("file.json", "w", encoding="utf-8") as b:
                json.dump(file, b)  
#удаляет по ключу
    elif user_input == 4:
        del_input = int(input("Введите ключ для удаления: "))
        found_3 = False
        try:
            for i in file:
                if del_input == i["id"]:
                    file.remove(i)
            with open("file.json", "w", encoding="utf-8") as b:
                json.dump(file, b)
        except StopIteration:
            print("Такой записи нет")
#закрывает программу (цикл)
    elif user_input == 5:
        brik += 1
