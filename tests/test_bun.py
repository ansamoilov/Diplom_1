from praktikum.bun import Bun
from data import BUNS_DATA


class TestBun:

    def test_name_initialization_sets_correct_name(self):
        test_data = BUNS_DATA[0]
        bun = Bun(test_data["name"], test_data["price"])
        assert bun.name == test_data["name"]

    def test_price_initialization_sets_correct_price(self):
        test_data = BUNS_DATA[0]
        bun = Bun(test_data["name"], test_data["price"])
        assert bun.price == test_data["price"]

    def test_get_name_returns_correct_name(self):
        test_data = BUNS_DATA[1]
        bun = Bun(test_data["name"], test_data["price"])
        assert bun.get_name() == test_data["name"]

    def test_get_price_returns_correct_price(self):
        test_data = BUNS_DATA[2]
        bun = Bun(test_data["name"], test_data["price"])
        assert bun.get_price() == test_data["price"]
