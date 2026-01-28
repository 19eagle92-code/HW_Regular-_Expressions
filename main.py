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

pprint(contacts_list)


# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#     datawriter = csv.writer(f, delimiter=",")
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)
