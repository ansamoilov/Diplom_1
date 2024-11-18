class TestBurger:

    def test_set_buns_sets_correct_bun_to_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_ingredient_to_burger(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_removes_ingredient_from_burger(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient_changes_ingredient_position(self, burger, mock_ingredient):
        ingredient_2 = mock_ingredient
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient

    def test_get_price_calculates_correct_total_price(self, burger, mock_ingredient, mock_bun):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        price = burger.get_price()
        assert price == 250.0

    def test_get_receipt_returns_formatted_receipt_with_price(self, burger, mock_ingredient, mock_bun):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert "Price: 250.0" in receipt
