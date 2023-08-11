from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car1 = SecondHandCar("m1", "type1", 500, 100)
        self.car2 = SecondHandCar("m2", "type2", 500, 100)
        self.car3 = SecondHandCar("m3", "type1", 500, 90)
        self.car4 = SecondHandCar("m4", "type1", 500, 120)
        self.car5 = SecondHandCar("m5", "type1", 500, 100)
    def test_correct_initialization(self):
        self.assertEqual("m1", self.car1.model)
        self.assertEqual("type1", self.car1.car_type)
        self.assertEqual(500, self.car1.mileage)
        self.assertEqual(100, self.car1.price)
        self.assertEqual([], self.car1.repairs)

    def test_invalid_price_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.price = 1
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car1.price = 0
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_invalid_mileage_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.mileage = 100
        self.assertEqual("Please, second-hand cars only!"
                         " Mileage must be greater than 100!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car1.mileage = 99
        self.assertEqual("Please, second-hand cars only!"
                         " Mileage must be greater than 100!", str(ve.exception))

    def test_promotional_higher_price_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.set_promotional_price(100)
        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car1.set_promotional_price(101)
        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_promotional_lower_prices_sets_price_correctly(self):
        result = self.car1.set_promotional_price(99)
        self.assertEqual("The promotional price has been successfully set.", result)
        self.assertEqual(99, self.car1.price)

    def test_need_repair_not_possible_warning_returned_correctly(self):
        result1 = self.car1.need_repair(51, "wheel")
        self.assertEqual("Repair is impossible!", result1)
        self.assertEqual(100, self.car1.price)
        self.assertEqual([], self.car1.repairs)

    def test_need_repair_repairs_correctly(self):
        result1 = self.car1.need_repair(30, "wheel")
        self.assertEqual("Price has been increased due to repair charges.", result1)
        self.assertEqual(130, self.car1.price)
        self.assertEqual(["wheel"], self.car1.repairs)

        result2 = self.car1.need_repair(20, "break")
        self.assertEqual("Price has been increased due to repair charges.", result2)
        self.assertEqual(150, self.car1.price)
        self.assertEqual(["wheel", "break"], self.car1.repairs)

    def test_gt_mismatch_warning_raised_correctly(self):
        result = self.car1 > self.car2
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test_gt_returns_correct_message_for_higher_price_self(self):
        result1 = self.car1 > self.car3
        self.assertEqual(True, result1)
        self.assertTrue(result1)

        result2 = self.car1 > self.car4
        self.assertEqual(False, result2)
        self.assertFalse(result2)

        result3 = self.car1 > self.car5
        self.assertEqual(False, result3)
        self.assertFalse(result3)

    def test_str_returns_correct_message(self):
        expected1 = """Model m1 | Type type1 | Milage 500km
Current price: 100.00 | Number of Repairs: 0"""
        self.assertEqual(expected1, str(self.car1))

        self.car1.repairs = ["wheel", "motor", "brakes"]
        self.car1.price = 200
        expected2 = """Model m1 | Type type1 | Milage 500km
Current price: 200.00 | Number of Repairs: 3"""
        self.assertEqual(expected2, str(self.car1))


if __name__ == "__main__":
    main()
