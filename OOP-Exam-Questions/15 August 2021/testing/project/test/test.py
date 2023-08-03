from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.shop1 = PetShop("shop1")

    def test_correct_initialization(self):
        self.assertEqual("shop1", self.shop1.name)
        self.assertEqual({}, self.shop1.food)
        self.assertEqual([], self.shop1.pets)

    def test_add_food_zero_and_lower_quantity_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop1.add_food("food1", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))
        self.assertEqual({}, self.shop1.food)

        with self.assertRaises(ValueError) as ve:
            self.shop1.add_food("food1", -1)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))
        self.assertEqual({}, self.shop1.food)

    def test_add_food_adds_food_correctly(self):
        # add new food
        result1 = self.shop1.add_food("rawcatfood1", 1)
        self.assertEqual("Successfully added 1.00 grams of rawcatfood1.", result1)
        self.assertEqual({"rawcatfood1": 1}, self.shop1.food)

        # add one more new food
        result2 = self.shop1.add_food("rawdogfood1", 2)
        self.assertEqual("Successfully added 2.00 grams of rawdogfood1.", result2)
        self.assertEqual({"rawcatfood1": 1, "rawdogfood1": 2}, self.shop1.food)

        # increase food quantity
        result3 = self.shop1.add_food("rawcatfood1", 3.00)
        self.assertEqual("Successfully added 3.00 grams of rawcatfood1.", result3)
        self.assertEqual({"rawcatfood1": 4.00, "rawdogfood1": 2}, self.shop1.food)

    def test_add_pet_adds_new_pet(self):
        result1 = self.shop1.add_pet("Gizmo")
        self.assertEqual("Successfully added Gizmo.", result1)
        self.assertEqual(["Gizmo"], self.shop1.pets)

        result2 = self.shop1.add_pet("")
        self.assertEqual("Successfully added .", result2)
        self.assertEqual(["Gizmo", ""], self.shop1.pets)

    def test_add_pet_raises_exception_when_try_add_existing_pet_name(self):
        self.shop1.pets = ["Gizmo", "Kaju", "Loki"]
        with self.assertRaises(Exception) as ex:
            self.shop1.add_pet("Kaju")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(["Gizmo", "Kaju", "Loki"], self.shop1.pets)

    def test_feed_pet_raises_exception_when_no_such_pet(self):
        self.shop1.food = {"rawcatfood1": 3, "rawdogfood": 4}
        with self.assertRaises(Exception) as ex:
            self.shop1.feed_pet("rawcatfood1", "Gizmo")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))
        self.assertEqual({"rawcatfood1": 3, "rawdogfood": 4}, self.shop1.food)

        # no food
        self.shop1.food = {}
        with self.assertRaises(Exception) as ex:
            self.shop1.feed_pet("rawcatfood1", "Gizmo")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))
        self.assertEqual({}, self.shop1.food)

    def test_feed_pet_returns_no_such_food_message_if_not_such_food(self):
        self.shop1.pets = ["Gizmo", "Kaju", "Loki"]
        self.shop1.food = {"rawcatfood1": 3, "rawdogfood": 4}
        result1 = self.shop1.feed_pet("rawcatfood2", "Gizmo")
        self.assertEqual("You do not have rawcatfood2", result1)
        self.assertEqual({"rawcatfood1": 3, "rawdogfood": 4}, self.shop1.food)

        #no food
        self.shop1.pets = ["Gizmo", "Kaju", "Loki"]
        self.shop1.food = {}
        result2 = self.shop1.feed_pet("rawcatfood2", "Gizmo")
        self.assertEqual("You do not have rawcatfood2", result2)
        self.assertEqual({}, self.shop1.food)

    def test_feed_pet_works_properly_with_food_lower_than_100(self):
        self.shop1.pets = ["Gizmo", "Kaju", "Loki"]
        self.shop1.food = {"rawcatfood1": 3, "rawdogfood": 4}
        result = self.shop1.feed_pet("rawcatfood1", "Gizmo")
        self.assertEqual("Adding food...", result)
        self.assertEqual({"rawcatfood1": 1003.00, "rawdogfood": 4}, self.shop1.food)

    def test_feed_pet_works_properly_with_food_not_lower_than_100(self):
        self.shop1.pets = ["Gizmo", "Kaju", "Loki"]
        self.shop1.food = {"rawcatfood1": 100, "rawdogfood": 400.0}
        result = self.shop1.feed_pet("rawcatfood1", "Gizmo")
        self.assertEqual("Gizmo was successfully fed", result)
        self.assertEqual({"rawcatfood1": 0, "rawdogfood": 400.00}, self.shop1.food)
        result2 = self.shop1.feed_pet("rawdogfood", "Loki")
        self.assertEqual("Loki was successfully fed", result2)
        self.assertEqual({"rawcatfood1": 0, "rawdogfood": 300.00}, self.shop1.food)

    def test_repr_returns_correct_message(self):
        # no pets
        expected = "Shop shop1:\nPets: "
        self.assertEqual(expected, repr(self.shop1))

        # with pets
        self.shop1.pets = ["Gizmo", "Kaju", "Loki"]
        expected = "Shop shop1:\nPets: Gizmo, Kaju, Loki"
        self.assertEqual(expected, repr(self.shop1))


if __name__ == "__main__":
    main()
