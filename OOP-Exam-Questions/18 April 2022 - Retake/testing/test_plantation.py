from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(5)
        self.plantation.plants = {
            "Genc": ["banana", "avocado"],
            "Taner": ["coriander", "lemongrass"]}
        self.plantation.workers = ["Taner", "Genc", "Gokhan", "Cem"]

    def test_correct_initialization(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({
            "Genc": ["banana", "avocado"],
            "Taner": ["coriander", "lemongrass"]
        }, self.plantation.plants)
        self.assertEqual(["Taner", "Genc", "Gokhan", "Cem"],
                         self.plantation.workers)

    def test_size_raises_val_error_with_negative_number(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_size_sets_value_correctly(self):
        self.assertEqual(5, self.plantation.size)
        self.plantation.size = 8
        self.assertEqual(8, self.plantation.size)

    def test_hire_worker_raises_val_error_with_existing_worker(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Gokhan")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_adds_new_worker_to_workers(self):
        result = self.plantation.hire_worker("Eren")
        self.assertEqual(["Taner", "Genc", "Gokhan", "Cem", "Eren"],
                         self.plantation.workers)
        self.assertEqual("Eren successfully hired.", result)

    def test_plants_counted_correctly_by_len(self):
        result = len(self.plantation)
        self.assertEqual(4, result)

    def test_planting_raises_val_error_if_worker_not_hired(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Eren", "celery")
        self.assertEqual("Worker with name Eren is not hired!", str(ve.exception))

    def test_planting_raises_val_error_if_capacity_for_plants_full(self):
        self.plantation.size = 4

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Genc", "kaffirlime")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_if_worker_in_plants_list_plants_new_plant(self):
        result = self.plantation.planting("Genc", "kaffirlime")
        self.assertEqual("Genc planted kaffirlime.", result)
        self.assertEqual({
            "Genc": ["banana", "avocado", "kaffirlime"],
            "Taner": ["coriander", "lemongrass"]
        }, self.plantation.plants)

    def test_if_worker_plants_first_plant_correctly_added(self):
        result = self.plantation.planting("Gokhan", "cucumber")
        self.assertEqual("Gokhan planted it's first cucumber.", result)
        self.assertEqual({
            "Genc": ["banana", "avocado"],
            "Taner": ["coriander", "lemongrass"],
            "Gokhan": ["cucumber"]
        }, self.plantation.plants)

    def test_str_returns_correct_info(self):
        self.assertEqual("Plantation size: 5\nTaner, Genc, Gokhan, Cem\n"
                         "Genc planted: banana, avocado\n"
                         "Taner planted: coriander, lemongrass", str(self.plantation))

    def test_repr_returns_correct_info(self):
        self.assertEqual("Size: 5\nWorkers: Taner, Genc, Gokhan, Cem",
                         repr(self.plantation))


if __name__ == "main":
    main()
