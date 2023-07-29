from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store_1 = ToyStore()

    def test_correct_initialization(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store_1.toy_shelf)

    def test_add_toy_raises_exception_for_non_existent_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store_1.add_toy("O", "panda")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_raises_exception_for_already_present_toy(self):
        self.store_1.toy_shelf = {
            "A": "panda",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        with self.assertRaises(Exception) as ex:
            self.store_1.add_toy("A", "panda")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_raises_exception_for_taken_shelf(self):
        self.store_1.toy_shelf = {
            "A": "panda",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        with self.assertRaises(Exception) as ex:
            self.store_1.add_toy("A", "pinnocio")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_correctly_adds_toy(self):
        result = self.store_1.add_toy("A", "panda")
        self.assertEqual({
            "A": "panda",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store_1.toy_shelf)
        self.assertEqual("Toy:panda placed successfully!", result)

    def test_remove_toy_raises_error_for_nonexistent_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store_1.remove_toy("O", "panda")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_raises_error_for_nonexistent_toy(self):
        with self.assertRaises(Exception) as ex:
            self.store_1.remove_toy("A", "panda")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_removes_toy_correctly(self):
        self.store_1.toy_shelf = {
            "A": "panda",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        result = self.store_1.remove_toy("A", "panda")
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store_1.toy_shelf)
        self.assertEqual("Remove toy:panda successfully!", result)



if __name__ == "__main__":
    main()