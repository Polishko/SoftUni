from project.vehicles.base_vehicle import BaseVehicle


class CargoVan (BaseVehicle):
    _Max_Mileage = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self._Max_Mileage)
