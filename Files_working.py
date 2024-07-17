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
    print(f' Cook_book= {cook_book}')