from project.train.train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train1 = Train("train1", 4)

    def test_correct_initialization(self):
        self.assertEqual("train1", self.train1.name)
        self.assertEqual(4, self.train1.capacity)
        self.assertEqual([], self.train1.passengers)
        self.assertEqual("Train is full", self.train1.TRAIN_FULL)
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train1.PASSENGER_EXISTS)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train1.PASSENGER_NOT_FOUND)
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train1.PASSENGER_ADD)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train1.PASSENGER_REMOVED)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train1.ZERO_CAPACITY)
        self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_add_passenger_raises_val_error_for_full_capacity(self):
        self.train1.passengers = ["pass1", "pass2", "pass3", "pass4"]
        with self.assertRaises(ValueError) as ve:
            self.train1.add("pass2")
        self.assertEqual("Train is full", str(ve.exception))
        self.assertEqual(["pass1", "pass2", "pass3", "pass4"],
                         self.train1.passengers)

    def test_add_passenger_raises_val_error_if_passenger_already_present(self):
        self.train1.passengers = ["pass1", "pass2", "pass3"]
        with self.assertRaises(ValueError) as ve:
            self.train1.add("pass2")
        self.assertEqual("Passenger pass2 Exists", str(ve.exception))
        self.assertEqual(["pass1", "pass2", "pass3"],
                         self.train1.passengers)

    def test_add_passenger_adds_new_passenger(self):
        self.train1.passengers = ["pass1", "pass2", "pass3"]
        result = self.train1.add("pass4")
        self.assertEqual("Added passenger pass4", result)
        self.assertEqual(["pass1", "pass2", "pass3", "pass4"],
                         self.train1.passengers)

    def test_remove_passenger_raises_error_for_non_existent_passenger(self):
        # from empty passenger list
        with self.assertRaises(ValueError) as ve:
            self.train1.remove("pass1")
        self.assertEqual("Passenger Not Found", str(ve.exception))
        self.assertEqual([], self.train1.passengers)

        # from non-empty passenger list
        self.train1.passengers = ["pass1", "pass2", "pass3"]
        with self.assertRaises(ValueError) as ve:
            self.train1.remove("pass4")
        self.assertEqual("Passenger Not Found", str(ve.exception))
        self.assertEqual(["pass1", "pass2", "pass3"], self.train1.passengers)

    def test_remove_passenger_removes_correct_passenger(self):
        self.train1.passengers = ["pass1", "pass2", "pass3"]
        result = self.train1.remove("pass2")
        self.assertEqual("Removed pass2", result)
        self.assertEqual(["pass1", "pass3"], self.train1.passengers)

        # remove one more
        result2 = self.train1.remove("pass1")
        self.assertEqual("Removed pass1", result2)
        self.assertEqual(["pass3"], self.train1.passengers)


if __name__ == "__main__":
    main()