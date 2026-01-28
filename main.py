import re


from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Обрабатываем ФИО
for contact in contacts_list[1:]:
    # Собираем первые три элемента (фамилия, имя, отчество)
    fio_parts = []

    # Добавляем части ФИО из первых трех полей, если они не пустые
    for i in range(3):
        if contact[i]:
            fio_parts.append(contact[i])
    # print(fio_parts)

    # Объединяем все части в одну строку
    fio_string = " ".join(fio_parts)
    # print(fio_string)

    # Разбиваем строку ФИО на отдельные компоненты
    fio_components = fio_string.split(" ")
    # print(fio_components)

    # Заполняем поля lastname, firstname, surname
    if len(fio_components) >= 1:
        contact[0] = fio_components[0]
    if len(fio_components) >= 2:
        contact[1] = fio_components[1]
    if len(fio_components) >= 3:
        contact[2] = fio_components[2]

# pprint(contacts_list)

# Заменяем нгомера телефонов по шаблону +7(999)999-99-99 доб.9999

# pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[\s\-]*(\d{3})[\s\-]*(\d{2})[\s\-]*(\d{2})(?:\s*\(?(доб\.?)\s*(\d+)\)?)?"
# replacement = r"+7(\2)\3-\4-\5 \6\7"  # правильно, но оставляет пробел после номера при отсутствии добавочного


for row in contacts_list[1:]:
    # row[5] = re.sub(pattern, replacement, row[5])

    pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[\s\-]*(\d{3})[\s\-]*(\d{2})[\s\-]*(\d{2})"
    replacement = r"+7(\2)\3-\4-\5"
    row[5] = re.sub(pattern, replacement, row[5])

    # Вторая проходка только для добавочного
    pattern_2 = r"\s*\(?(доб\.?)\s*(\d+)\)?"
    replacement_2 = r" доб.\2"
    row[5] = re.sub(pattern_2, replacement_2, row[5])

    # print(row[5])
# pprint(contacts_list)

# Объединение дублирующих записей
merged = {}

for contact in contacts_list:
    key = (contact[0], contact[1])  # Фамилия + Имя

    if key not in merged:
        merged[key] = contact
    else:
        for i in range(len(contact)):
            if not merged[key][i]:
                merged[key][i] = contact[i]

result = list(merged.values())

# pprint(result)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
    datawriter = csv.writer(f, delimiter=",")
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(result)
