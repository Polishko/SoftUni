from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    _SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    _ROBOT_TYPES = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots: list = []
        self.services: list = []

    def __find_service(self, service_name):
        return next(s for s in self.services if s.name == service_name)

    def add_service(self, service_type: str, name: str):
        if service_type not in self._SERVICE_TYPES:
            raise Exception("Invalid service type!")

        service = self._SERVICE_TYPES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self._ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        robot = self._ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(r for r in self.robots if r.name == robot_name)
        service = self.__find_service(service_name)

        if robot.__class__.__name__ == "FemaleRobot" and service.service_type == "Main Service" \
                or (robot.__class__.__name__ == "MaleRobot" and service.service_type == "Secondary Service"):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_service(service_name)

        try:
            robot = next(r for r in service.robots if r.name == robot_name)
            service.robots.remove(robot)
            self.robots.append(robot)
            return f"Successfully removed {robot_name} from {service_name}."
        except StopIteration:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service(service_name)
        [r.eating() for r in service.robots]

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service(service_name)
        price_robots = sum(r.price for r in service.robots)

        return f"The value of service {service_name} is {price_robots:.2f}."

    def __str__(self):
        return "\n".join([service.details() for service in self.services])
