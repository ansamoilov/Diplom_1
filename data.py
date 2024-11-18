from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Данные для булочек и тестов булочек
BUNS_DATA = [
    {"name": "black bun", "price": 100.0},
    {"name": "white bun", "price": 150.0},
    {"name": "red bun", "price": 200.0}
]

# Данные для тестов ингредиентов
INGREDIENT_DATA = [
    {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100.0},
    {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 150.0},
    {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 200.0},
    {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 250.0}
]

# Данные для тестов метода get_price
PRICE_DATA = [
    {"type": INGREDIENT_TYPE_SAUCE, "price": 100.0},
    {"type": INGREDIENT_TYPE_FILLING, "price": 200.0}
]

# Данные для тестов метода get_name
NAME_DATA = [
    {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce"},
    {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet"}
]

# Данные для тестов метода get_type
TYPE_DATA = [
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
]
