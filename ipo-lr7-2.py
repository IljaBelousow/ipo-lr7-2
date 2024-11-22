import json
import codecs
user_input = str(input("Введите номер: "))
brik = False
with open("dump.json", 'r', encoding='utf-8') as a: 
    file = json.load(a)
    for i in file:
        if i.get("model") == "data.skill": #если по ключу model значение i == "data.specialty"
            if i["fields"].get("code") == user_input: #если  изер_инпут есть в коде
                i_code = i["fields"].get("code") #= значение fields по ключу code
                i_title = i["fields"].get("title") #= значение fields по ключу title          
                brik = True

                for j in file:
                    if j.get("model") == "data.specialty":
                        j_code = j["fields"].get("code")
                        if j_code in user_input:
                            j_title = j["fields"].get("title")
                            j_depend = j["fields"].get("c_type")
                break
if not brik:
    print("=============== Не Найдено ===============")
else:
    print("=============== Найдено ===============") 
    print(f"{j_code} >> Специальность {j_title} , {j_depend}")
    print(f"{i_code} >> Квалификация {i_title}")

