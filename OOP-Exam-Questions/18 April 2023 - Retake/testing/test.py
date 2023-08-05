from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot_1 = Robot("100", "Humanoids", 5, 1000)
        self.robot_2 = Robot("90", "Military", 3, 900)
        self.robot_3 = Robot("200", "Entertainment", 10, 2000)
        self.robot_4 = Robot("80", "Military", 3, 900)

    def test_correct_class_attributes(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'],
                         self.robot_1.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.robot_1.PRICE_INCREMENT)

    def test_correct_initialization(self):
        self.assertEqual("100", self.robot_1.robot_id)
        self.assertEqual("Humanoids", self.robot_1.category)
        self.assertEqual(5, self.robot_1.available_capacity)
        self.assertEqual(1000, self.robot_1.price)
        self.assertEqual([], self.robot_1.hardware_upgrades)
        self.assertEqual([], self.robot_1.software_updates)

    def test_wrong_category_set_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot_1.category = "Carnival"
        self.assertEqual("Category should be one of"
                         " '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ve.exception))

    def test_negative_price_set_raises_val_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot_1.price = -1
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_if_hardware_already_upgraded_returns_correct_message(self):
        self.robot_1.hardware_upgrades = ["Ram", "CPU"]
        result = self.robot_1.upgrade("Ram", 600.6)
        self.assertEqual("Robot 100 was not upgraded.", result)
        self.assertEqual(["Ram", "CPU"], self.robot_1.hardware_upgrades)

    def test_if_new_hardware_adds_to_hardware_list_increases_price(self):
        result = self.robot_1.upgrade("Ram", 600.6)
        self.assertEqual("Robot 100 was upgraded with Ram.", result)
        self.assertEqual(["Ram"], self.robot_1.hardware_upgrades)
        self.assertEqual(1900.9, self.robot_1.price)

    def test_low_version_gives_correct_return(self):
        self.robot_1.software_updates = [10, 20, 30]
        result = self.robot_1.update(10.1, 5)
        self.assertEqual("Robot 100 was not updated.", result)
        self.assertEqual([10, 20, 30], self.robot_1.software_updates)

    def test_low_capacity_gives_correct_return(self):
        result = self.robot_1.update(30, 8)
        self.assertEqual("Robot 100 was not updated.", result)
        self.assertEqual([], self.robot_1.software_updates)

    def test_correct_version_added_and_capacity_updated(self):
        self.robot_1.software_updates = [10, 20, 30]
        result = self.robot_1.update(40, 5)
        self.assertEqual("Robot 100 was updated to version 40.", result)
        self.assertEqual([10, 20, 30, 40], self.robot_1.software_updates)
        self.assertEqual(0, self.robot_1.available_capacity)

    def test_gt_returns_correct_message_when_other_greater(self):
        result = self.robot_1.__gt__(self.robot_2)
        self.assertEqual("Robot with ID 100 is more expensive than Robot with ID 90.", result)

    def test_gt_returns_correct_message_when_other_smaller(self):
        result = self.robot_1.__gt__(self.robot_3)
        self.assertEqual("Robot with ID 100 is cheaper than Robot with ID 200.", result)

    def test_gt_returns_correct_message_when_other_equal(self):
        result = self.robot_2.__gt__(self.robot_4)
        self.assertEqual("Robot with ID 90 costs equal to Robot with ID 80.", result)


if __name__ == "__main__":
    main()
