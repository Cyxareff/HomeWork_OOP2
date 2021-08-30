# Задача 1
#
# from pprint import pprint
# cook_book = {}
# b = ['ingredient_name', 'quantity', 'measure']
# menu = open('recipes.txt', "r", encoding="utf-8")
#
# for line in menu:
#     dish = line.strip()
#     count_ingridients = menu.readline().strip()
#     cook_book[dish] = []
#     for i in range(int(count_ingridients)):
#         a = menu.readline().strip().split('|')
#         z = dict(zip(b, a))
#         cook_book[dish].append(z)
#     menu.readline()
# pprint(cook_book)
# print()
# menu.close()
# # Задача 2
#
# def lis(person_count, *dish):
#     ing_dict = {}
#     for j in dish:
#         for i in cook_book[j]:
#             if i['ingredient_name'] not in ing_dict:
#                 ing_dict[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
#             else:
#                 ing_dict[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count
#     pprint(ing_dict)
#
# lis(5, 'Омлет', 'Утка по-пекински', 'Запеченный картофель')

# Задача 3

import os
a = os.listdir(path=".")
b = []
for i in a:
    if '.txt' in i:
        b.append(i)
def open_file():
    with open(i, 'r', encoding='utf-8') as f:
        data = f.readlines()
        count_str1 = len(data)
        a = []
        a.append(i)
        z = dict(zip(a, str(count_str1)))
        for key, value in sorted(z.items(), reverse=True):
            print(f"{key} \n{value}")
        s = 0
        for x in range(count_str1):
            s += 1
            print(f"Строка номер {s} файл номер {i}")

for i in b:
    open_file()



 #     in sorted(list_z.items(), key=lambda para: (para[1], para[0])):
            # print(g)


# print(f"{i}  \n{count_str1}")
        # s = 0
        # for x in range(count_str1):
        #     s += 1
        #     print(f"Строка номер {s} файл номер 1")


#

# print( "====>", os.getcwd())
# print(os.listdir(path="."))
# path = os.listdir(path=".")
# print(path[1])

# def open_file1():
#
#     with open('1.txt', 'r', encoding='utf-8') as f:
#         data = f.readlines()
#         count_str1 = len(data)
#         print(f"1.txt \n{count_str1}")
#         s = 0
#         for i in range(count_str1):
#             s += 1
#             print(f"Строка номер {s} файл номер 1")
# open_file1()
# #
# with open('2.txt', 'r', encoding='utf-8') as f:
#     data = f.readlines()
#     count_str2 = len(data)
#     print(f"\n2.txt \n{count_str2}")
#     s = 0
#     for i in range(count_str2):
#         s += 1
#         print(f"Строка номер {s} файл номер 2")
#
# with open('3.txt', 'r', encoding='utf-8') as f:
#     data = f.readlines()
#     count_str3 = len(data)
#     print(f"\n3.txt \n{count_str3}")
#     s = 0
#     for i in range(count_str3):
#         s += 1
#         print(f"Строка номер {s} файл номер 3")



