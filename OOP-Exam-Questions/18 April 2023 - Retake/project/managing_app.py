from project.user import User
from project.vehicles.passenger_car import PassengerCar
from project.vehicles.cargo_van import CargoVan
from project.route import Route


class ManagingApp:
    _Valid_Vehicles = ["PassengerCar", "CargoVan"]

    def __init__(self):
        self.users: list = []
        self.vehicles: list = []
        self.routes: list = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        try:
            next(u for u in self.users if u.driving_license_number == driving_license_number)
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            user = User(first_name, last_name, driving_license_number)
            self.users.append(user)
            
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        
        if vehicle_type not in ManagingApp._Valid_Vehicles:            
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            next(v for v in self.vehicles if v.license_plate_number == license_plate_number)
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            vehicle = PassengerCar(brand, model, license_plate_number) if vehicle_type == "PassengerCar"\
                else CargoVan(brand, model, license_plate_number)

            self.vehicles.append(vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        
        for route in self.routes:            
            if route.start_point == start_point and route.end_point == end_point:
                
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                else:
                    route.is_locked = True
                    break

        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)
        
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str,
                  route_id: int,  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = [r for r in self.routes if r.route_id == route_id][0]

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        sorted_damaged = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))
        repair_count = count if len(sorted_damaged) > count else len(sorted_damaged)

        for i in range(repair_count):
            vehicle = sorted_damaged[i]
            vehicle.change_status()
            vehicle.recharge()

        return f"{repair_count} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)
        result = ["*** E-Drive-Rent ***"]
        [result.append(str(u)) for u in sorted_users]

        return "\n".join(result)
