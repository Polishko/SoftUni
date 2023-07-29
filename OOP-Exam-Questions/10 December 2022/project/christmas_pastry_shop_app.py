from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    DELICACY_TYPES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0

    def find_delicacy(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy

    def find_booth(self, number):
        for booth in self.booths:
            if booth.booth_number == number:
                return booth

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.find_delicacy(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy_obj = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy_obj)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.find_booth(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth_obj = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth_obj)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            booth_obj = next(booth for booth in self.booths if not booth.is_reserved
                             and booth.capacity >= number_of_people)
            booth_obj.reserve(number_of_people)
            return f"Booth {booth_obj.booth_number} has been reserved for {number_of_people} people."
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth_obj = self.find_booth(booth_number)
        delicacy_obj = self.find_delicacy(delicacy_name)

        if not booth_obj:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy_obj:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth_obj.delicacy_orders.append(delicacy_obj)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth_obj = self.find_booth(booth_number)
        total_income = booth_obj.price_for_reservation + sum(delicacy.price for delicacy in booth_obj.delicacy_orders)
        self.income += total_income
        booth_obj.delicacy_orders.clear()
        booth_obj.is_reserved = False
        booth_obj.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {total_income:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
