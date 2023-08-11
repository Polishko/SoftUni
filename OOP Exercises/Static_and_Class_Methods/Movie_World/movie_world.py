from project.customer import Customer
from project.dvd import DVD
from typing import List


class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        dvd_capacity = 15
        return dvd_capacity

    @staticmethod
    def customer_capacity() -> int:
        customer_capacity = 10
        return customer_capacity

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < MovieWorld.customer_capacity(): # better to call thtough the class instead of self as static method belongs to the class
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"
        if current_dvd.is_rented:
            return "DVD is already rented"
        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"

        return f"{current_customer.name} does not have that DVD"

    def __repr__(self) -> str:
        result = ""

        for customer in self.customers:
            result += f"{customer}\n"
        for dvd in self.dvds:
            result += f"{dvd}\n"

        return result
