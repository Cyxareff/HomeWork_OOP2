from main import cook_book
from pprint import pprint

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




