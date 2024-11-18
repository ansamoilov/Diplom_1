import pytest
from unittest.mock import patch
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:

    @pytest.mark.parametrize(
        "buns_data, expected_length",
        [
            ([Bun("black bun", 100), Bun("white bun", 200), Bun("red bun", 300)], 3)
        ]
    )
    @patch('praktikum.database.Bun')
    def test_available_buns_length_is_3(self, MockBun, buns_data, expected_length, db):
        MockBun.side_effect = buns_data
        buns = db.available_buns()
        assert len(buns) == expected_length

    @pytest.mark.parametrize(
        "ingredients_data, expected_length",
        [
            (
                [
                    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                    Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                    Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
                ],
                6
            )
        ]
    )
    @patch('praktikum.database.Ingredient')
    def test_available_ingredients_length_is_6(self, MockIngredient, ingredients_data, expected_length, db):
        MockIngredient.side_effect = ingredients_data
        ingredients = db.available_ingredients()
        assert len(ingredients) == expected_length

    @pytest.mark.parametrize(
        "buns_data, expected_first_bun_name",
        [
            ([Bun("black bun", 100), Bun("white bun", 200), Bun("red bun", 300)], "black bun")
        ]
    )
    @patch('praktikum.database.Bun')
    def test_first_bun_name_is_black_bun(self, MockBun, buns_data, expected_first_bun_name, db):
        MockBun.side_effect = buns_data
        buns = db.available_buns()
        assert buns[0].name == expected_first_bun_name

    @pytest.mark.parametrize(
        "ingredients_data, expected_first_ingredient_name",
        [
            (
                [
                    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                    Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                    Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
                ],
                "hot sauce"
            )
        ]
    )
    @patch('praktikum.database.Ingredient')
    def test_first_ingredient_name_is_hot_sauce(self, MockIngredient, ingredients_data, expected_first_ingredient_name, db):
        MockIngredient.side_effect = ingredients_data
        ingredients = db.available_ingredients()
        assert ingredients[0].name == expected_first_ingredient_name

    @pytest.mark.parametrize(
        "buns_data, expected_bun_names",
        [
            ([Bun("black bun", 100), Bun("white bun", 200), Bun("red bun", 300)], ["black bun", "white bun", "red bun"])
        ]
    )
    @patch('praktikum.database.Bun')
    def test_bun_names_included_in_list(self, MockBun, buns_data, expected_bun_names, db):
        MockBun.side_effect = buns_data
        buns = db.available_buns()
        bun_names = [bun.name for bun in buns]
        for name in expected_bun_names:
            assert name in bun_names

    @pytest.mark.parametrize(
        "ingredients_data, expected_ingredient_names",
        [
            (
                [
                    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                    Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                    Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
                ],
                ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
            )
        ]
    )
    @patch('praktikum.database.Ingredient')
    def test_ingredient_names_included_in_list(self, MockIngredient, ingredients_data, expected_ingredient_names, db):
        MockIngredient.side_effect = ingredients_data
        ingredients = db.available_ingredients()
        ingredient_names = [ingredient.name for ingredient in ingredients]
        for name in expected_ingredient_names:
            assert name in ingredient_names
