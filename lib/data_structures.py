spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names_list = []
    for i in spicy_foods:
        names_list.append(i.get("name"))
    return names_list

def get_spiciest_foods(spicy_foods):
    spicy_list = []

    for i in spicy_foods:
        if i.get("heat_level") > 5:
            spicy_list.append(i)
        else:
            None
    return spicy_list

def print_spicy_foods(spicy_foods):
    for i in spicy_foods:
        heat = i.get("heat_level") * "🌶"
        name = i.get("name")
        place = i.get("cuisine")
        print(f"{name} ({place}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in spicy_foods:
        if i.get("cuisine") == cuisine:
            return i
        else: 
            None

def print_spiciest_foods(spicy_foods):

    for food in spicy_foods:
        word_output =""
        if food.get("heat_level") > 5:
            word_output += food.get("name") + " " + "(" + food.get("cuisine") + ")" + " " + "|" + " " + "Heat Level: " + ("🌶" * food.get("heat_level"))
            print(word_output)


def get_average_heat_level(spicy_foods):

    food_sum=0
    count=0

    for food in spicy_foods:
        food_sum += food.get("heat_level")
        count += 1
    return int(food_sum / count)


def create_spicy_food(spicy_foods, spicy_food):

    spicy_foods.append(spicy_food)
    return spicy_foods
