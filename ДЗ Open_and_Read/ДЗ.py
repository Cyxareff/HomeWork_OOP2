# Задача 1
#
from pprint import pprint
cook_book = {}
b = ['ingredient_name', 'quantity', 'measure']
menu = open('recipes.txt', "r", encoding="utf-8")

for line in menu:
    dish = line.strip()
    count_ingridients = menu.readline().strip()
    cook_book[dish] = []
    for i in range(int(count_ingridients)):
        a = menu.readline().strip().split('|')
        z = dict(zip(b, a))
        cook_book[dish].append(z)
    menu.readline()
pprint(cook_book)
print()
menu.close()

# # Задача 2
#
def lis(person_count, *dish):
    ing_dict = {}
    for j in dish:
        for i in cook_book[j]:
            if i['ingredient_name'] not in ing_dict:
                ing_dict[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
            else:
                ing_dict[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count
    pprint(ing_dict)

lis(5, 'Омлет', 'Утка по-пекински', 'Запеченный картофель')

# Задача 3

import os
a = os.listdir(path=".")
b = []

for i in a:
    if '.txt' in i:
        b.append(i)

z = {}
def open_file():
    with open(i, 'r', encoding='utf-8') as f:
        data = f.readlines()
        count_str1 = len(data)
        q = {}
        z[count_str1] = q
        q[i] = data

for i in b:
    open_file()

with open('task_3.txt', 'w', encoding='utf-8') as file:
    for count, name_text in sorted(z.items()):
        for name, text in name_text.items():
            file.write(name + '\n')
            file.write(str(count) + '\n')
            for str_ in text:
                file.write(str_ + '\n')





