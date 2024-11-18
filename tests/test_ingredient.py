import pytest
from unittest.mock import patch
from praktikum.ingredient import Ingredient
from data import INGREDIENT_DATA, PRICE_DATA, NAME_DATA, TYPE_DATA


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
    def test_get_type_returns_correct_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
    def test_get_name_returns_correct_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
    def test_get_price_returns_correct_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, price", PRICE_DATA)
    def test_get_price_returns_expected_price(self, ingredient_type, price):
        ingredient = Ingredient(ingredient_type, "Test Ingredient", price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name", NAME_DATA)
    def test_get_name_returns_expected_name(self, ingredient_type, name):
        ingredient = Ingredient(ingredient_type, name, 100.0)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type", TYPE_DATA)
    def test_get_type_returns_expected_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Test Ingredient", 100.0)
        assert ingredient.get_type() == ingredient_type

    @patch("praktikum.ingredient.Ingredient.get_price")
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
    def test_get_price_with_mock_returns_correct_price(self, mock_get_price, ingredient_type, name, price):
        mock_get_price.return_value = price
        ingredient = Ingredient(ingredient_type, name, 0.0)
        assert ingredient.get_price() == price
