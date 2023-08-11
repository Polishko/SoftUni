from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    VALID_COMPUTERS = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }

    def __init__(self):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        try:
            computer = self.VALID_COMPUTERS[type_computer](manufacturer, model)
        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):

        for computer in self.warehouse:
            if wanted_processor == computer.processor and \
                    wanted_ram <= computer.ram and \
                    computer.price <= client_budget:
                
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)

                return f"{computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")


# from project.computer_types.desktop_computer import DesktopComputer
# from project.computer_types.laptop import Laptop


# class ComputerStoreApp:
#     def __init__(self):
#         self.warehouse: list = []
#         self.profits: int = 0

#     def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
#         if type_computer == "Desktop Computer":
#             computer = DesktopComputer(manufacturer, model)

#         elif type_computer == "Laptop":
#             computer = Laptop(manufacturer, model)

#         else:
#             raise ValueError(f"{type_computer} is not a valid type computer!")

#         configuration = computer.configure_computer(processor, ram)
#         self.warehouse.append(computer)
#         return configuration

#     def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):

#         suitable_computers = []
#         for computer in self.warehouse:
#             if wanted_processor == computer.processor and wanted_ram <= computer.ram and \
#                     wanted_ram in computer.valid_rams \
#                     and computer.price <= client_budget:
#                 suitable_computers.append((computer.price, computer))

#         if len(suitable_computers) == 0:
#             raise Exception("Sorry, we don't have a computer for you.")

#         target_computer = sorted(suitable_computers, key=lambda x: x[0])[0][1]
#         self.profits += client_budget - target_computer.price
#         self.warehouse.remove(target_computer)

#         return f"{target_computer} sold for {client_budget}$."
