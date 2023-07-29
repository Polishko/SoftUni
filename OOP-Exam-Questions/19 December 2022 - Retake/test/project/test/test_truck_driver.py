from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Genc", 0.5)

    def test_correct_initialization(self):
        self.assertEqual("Genc", self.driver.name)
        self.assertEqual(0.5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_monet_setter_raises_val_error_upon_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual("Genc went bankrupt.", str(ve.exception))

    def test_earned_monet_setter_sets_earned_money_correctly(self):
        self.driver.earned_money = 10
        self.assertEqual(10, self.driver.earned_money)

    def test_add_cargo_offer_raises_exception_upon_already_added_cargo(self):
        self.driver.available_cargos = {"Varna", 200}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Varna", 200)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_correctly_adds_cargo(self):
        result = self.driver.add_cargo_offer("Varna", 200)
        self.assertEqual({"Varna": 200}, self.driver.available_cargos)
        self.assertEqual("Cargo for 200 to Varna was added as an offer.", result)

    def test_drive_best_offer_raises_val_error_when_no_offers(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_offer_correctly_drives_best_offer(self):
        self.driver.money_per_mile = 10
        self.driver.available_cargos = {
            "Varna": 200,
            "Burgas": 250,
            "Bucurest": 10500,
            "Plovdiv": 50
        }

        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(92710, self.driver.earned_money)
        self.assertEqual(10500, self.driver.miles)
        self.assertEqual("Genc is driving 10500 to Bucurest.", result)

    def test_repr_returns_correct_info(self):
        self.assertEqual("Genc has 0 miles behind his back.", repr(self.driver))


if __name__ == "__main__":
    main()