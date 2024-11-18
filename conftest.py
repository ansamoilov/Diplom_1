import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


@pytest.fixture
def mock_bun():
    """Мок для булочки."""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Black Bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient():
    """Мок для ингредиента."""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "Hot Sauce"
    ingredient.get_price.return_value = 50.0
    ingredient.get_type.return_value = "SAUCE"
    return ingredient


@pytest.fixture
def burger(mock_bun):
    """Создаем базовый бургер с булкой."""
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger


@pytest.fixture
def mock_ingredient():
    """Фикстура для ингредиента"""
    return Ingredient("sauce", "hot sauce", 50.0)


@pytest.fixture
def db():
    """Создаем экземпляр класса Database для использования в тестах"""
    return Database()
