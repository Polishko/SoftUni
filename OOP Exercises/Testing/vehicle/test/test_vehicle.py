from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(50.0, 138.0)

    def test_correct_class_attr_def_fuel_consumption(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialization(self):
        self.assertEqual(50.0, self.vehicle.fuel)
        self.assertEqual(138.0, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_car_not_enough_fuel_raises_exception(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_car_consumes_fuel_correctly(self):
        self.vehicle.drive(40)
        self.assertEqual(0, self.vehicle.fuel)

    def test_over_capacity_refuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_increases_fuel_amount_correctly(self):
        self.vehicle.fuel = 20.0
        self.vehicle.refuel(30)
        self.assertEqual(50.0, self.vehicle.fuel)

    def test_str_method_returns_correct_message(self):
        self.assertEqual("The vehicle has 138.0 horse power with"
                         " 50.0 fuel left and 1.25 fuel consumption",
                         self.vehicle.__str__())


if __name__ == "__main__":
    main()
