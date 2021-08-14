def get_ingredients(line):
    ingredients = {}
    ingredients['ingredient_name'] = line.split('|')[0].strip()
    ingredients['quantity'] = line.split('|')[1].strip()
    ingredients['measure'] = line.split('|')[2].strip()
    return ingredients

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    return shop_list


cook_book = {}
with open('recipes.txt') as file:
    for line in file:
        dish_name = line.strip()
        ingredients = int(file.readline().strip())
        list_of_ingredients = []
        for _ in range(ingredients):
            list_of_ingredients.append(get_ingredients(file.readline()))
        cook_book[dish_name] = list_of_ingredients
        file.readline()

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))