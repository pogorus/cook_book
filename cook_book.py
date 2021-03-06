import datetime

def logger_decorator(path_to_log):
    def logger(old_function):
        def new_function(*args, **kwargs):
            with open(path_to_log, 'a') as f:
                f.write(f'Date - {datetime.datetime.now()}; Function name - {old_function.__name__}; Arguments - {args} {kwargs}; ')
                result = old_function(*args, **kwargs)
                f.write(f'Result - {result}\n')
                return result
        return new_function
    return logger

def get_ingredients(line):
    ingredients = {}
    ingredients['ingredient_name'] = line.split('|')[0].strip()
    ingredients['quantity'] = line.split('|')[1].strip()
    ingredients['measure'] = line.split('|')[2].strip()
    return ingredients

@logger_decorator('log.txt')
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