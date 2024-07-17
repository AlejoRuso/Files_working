import pprint
cook_book = {}

with open ('recipes.txt', encoding = 'utf-8') as f:
    for line in f:
        dish = line.strip()
        ing_numb = int(f.readline())
        ing_dish = []
        for r in range(ing_numb):
            numb = f.readline().strip()
            ingredient_name, quantity, measure = numb.split(' | ')
            ing_dish.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish] = ing_dish
        f.readline()
    pprint.pprint(f' Cook_book= {cook_book}')

print('')
    
    

def get_shop_list_by_dishes(dishes, person_count):
    ings_shop_list = {}
    for dish in dishes:
        for ing_dish in cook_book[dish]:
            if dish in cook_book:
                prod = ing_dish['ingredient_name']
                ings_shop_list.setdefault(prod, [])
                ings = int(ing_dish['quantity']) * person_count
                ing_list = []
                ing_list.append({'quantity': ings, 'measure': ing_dish['measure']})
                ings_shop_list[prod] = ing_list
    pprint.pprint(ings_shop_list)
    return ings_shop_list

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)