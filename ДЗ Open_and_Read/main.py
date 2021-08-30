# Задача 1.

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

# Задача 2.

def order(person_count, *dish):
  ing_dict = {}
  for j in dish:
    for i in cook_book[j]:
      if i['ingredient_name'] not in ing_dict:
        ing_dict[i['ingredient_name']] = {'measure': i['measure'],
                                          'quantity': int(i['quantity']) * person_count}
      else:
        ing_dict[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count


order(8, 'Омлет', 'Утка по-пекински', 'Запеченный картофель')


# Задача 3.
