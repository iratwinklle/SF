#15.1.1 открыть файл
# myfile = open('filename.txt.txt', 'rt', encoding="utf8")
# print(myfile.read()) #печатает весь текст

# myfile = open('filename.txt.txt', 'rt', encoding="utf8")
# print(myfile.readline()) #печатает строку из текста
# print(myfile.readline()) #повтор данной команды = 2 строка из текста

# myfile = open('filename.txt.txt', 'rt', encoding="utf8")
# for line in myfile:
#     print(line)

#15.1.2 открыть файл
# myfile = open('namefile.txt', 'w') #создал файл namefile
# myfile.write('tttt') #записал в файл 'tttt'
# print('zzzz', file=myfile)
# print(myfile.read())


#15.1.3 шифр цезаря
# alpha = 'абвгдеёжзийклмнопрстуфхцчщъыьэюя'
# alphaup = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩЪЫЬЭЮЯ'
# number = int(input("Введите число, на которое нужно сдвинуть текст:"))
# summary = ''
# def changechar(char):
#     if char in alpha:
#         return alpha[(alpha.index(char) + number) % len(alpha)]
#     elif char in alphaup:
#         return alphaup[(alphaup.index(char) + number) % len(alphaup)]
#     else:
#         return char
# with open("filename.txt.txt", encoding="utf8") as myfile:
#     for line in myfile:
#         for char in line:
#             summary += changechar(char)
#
# with open ("output.txt", 'w', encoding="utf8") as myfile:
#     myfile.write(summary)

# w = open("filename.txt.txt", 'r', encoding="utf8")
# print(w.read())
#
# q = open("namefile.txt")
# print(q.read())

#15.3 Работа с json файлами

# Как считать json:
# 1 способ:
# import json
# with open('json_example.json', encoding='utf8') as f:
#     templates = json.load(f)    #в исходном файле были данные "true" и "null", они поменялись на "True" и "None"
# print(templates)
# print(type(templates))
# #дальше уже можно работать как со словарем.

# 2 способ:

# import json
# with open('json_example.json', encoding='utf8') as f:
#     strfile = f.read()  #читаем файл в строку
#     templates = json.loads(strfile)  #преобразовывание строки в словарь
# print(templates)
# print(type(templates))


#3. Запись в json:
import json
template = {
    'firstname': 'Иван',
    'lastname': 'Иванов',
    'isAlive': True,
    'age': 32,
    'address': {
        'streetAddress': 'Нейбута 32',
        'city': 'Владивосток',
        'state': '',
        'postalcode': ''
    },
    'phoneNumbers': [
        {
            'type': 'mob',
            'number': '123-333-4455'
        },
        {
            'type': 'office',
            'number': '123 111-4567'
        }
    ],
    'children': [],
    'spouse': None
}

with open('to_json_example.json', 'w', encoding='utf8') as f:
    json.dump(template, f, ensure_ascii=False, indent=4)

with open('to_json_example.json', encoding='utf8') as f:
    print(f.read())