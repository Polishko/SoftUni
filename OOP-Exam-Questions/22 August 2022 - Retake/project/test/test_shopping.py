from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.shop_1 = ShoppingCart("Narciss", 1000)
        self.shop_2 = ShoppingCart("Market", 2000)

    def test_correct_initialization(self):
        self.assertEqual("Narciss", self.shop_1.shop_name)
        self.assertEqual(1000, self.shop_1.budget)
        self.assertEqual({}, self.shop_1.products)

    def test_name_doesnt_start_upper_case_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop_1.shop_name = "narciss"
        self.assertEqual("Shop must contain only letters and must start with capital letter!",
                         str(ve.exception))

    def test_name_with_non_letters_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop_1.shop_name = "N1rciss"
        self.assertEqual("Shop must contain only letters and must start with capital letter!",
                         str(ve.exception))

    def test_name_sets_correctly(self):
        self.shop_1.shop_name = "CornerShop"
        self.assertEqual("CornerShop", self.shop_1.shop_name)

    def test_add_to_cart_high_product_price_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop_1.add_to_cart("olive paste", 100)
        self.assertEqual("Product olive paste cost too much!", str(ve.exception))
        self.assertEqual({}, self.shop_1.products)

    def test_add_to_cart_adds_product(self):
        result = self.shop_1.add_to_cart("olive paste", 99)
        self.assertEqual("olive paste product was successfully added to the cart!", result)
        self.assertEqual({"olive paste": 99}, self.shop_1.products)

    def test_remove_product_raises_val_error_non_existent_product(self):
        self.shop_1.products = {"sour bread": 4}
        with self.assertRaises(ValueError) as ve:
            self.shop_1.remove_from_cart("olive paste")
        self.assertEqual("No product with name olive paste in the cart!", str(ve.exception))
        self.assertEqual({"sour bread": 4}, self.shop_1.products)

    def test_remove_product_removes_product(self):
        self.shop_1.products = {"olive paste": 99, "sour bread": 4}
        result = self.shop_1.remove_from_cart("olive paste")
        self.assertEqual({"sour bread": 4}, self.shop_1.products)
        self.assertEqual("Product olive paste was successfully removed from the cart!", result)

    def test_add_other_shop_successful(self):
        self.shop_1.products = {"olive paste": 6}
        self.shop_2.products = {"sour bread": 4}
        result = self.shop_1 + self.shop_2
        self.assertEqual("NarcissMarket", result.shop_name)
        self.assertEqual(3000, result.budget)
        self.assertEqual({"olive paste": 6, "sour bread": 4}, result.products)
        self.assertTrue(isinstance(result, ShoppingCart))

    def test_buy_product_raises_val_error_insufficient_budget(self):
        self.shop_1.products = {"aged kobe": 3000, "truffles": 2500}

        with self.assertRaises(ValueError) as ve:
            self.shop_1.buy_products()
        self.assertEqual("Not enough money to buy the products!"
                         " Over budget with 4500.00lv!", str(ve.exception))

    def test_buy_products_buys_products(self):
        self.shop_1.products = {"olive paste": 6, "sour bread": 4, "goat cheese": 10}
        result = self.shop_1.buy_products()
        self.assertEqual("Products were successfully bought!"
                         " Total cost: 20.00lv.", result)


if __name__ == "__main__":
    main()
