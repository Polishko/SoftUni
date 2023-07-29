from project.client import Client
from project.meals.main_dish import MainDish
from project.meals.starter import Starter
from project.meals.dessert import Dessert


class FoodOrdersApp:
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]

    def __init__(self):
        self.menu: list = []
        self.clients_list: list = []
        self.receipt_id = 0

    def find_client(self, phone_num):
        for client in self.clients_list:
            if client.phone_number == phone_num:
                return client

    def find_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def reset_menu(self, client):
        for i in range(len(client.shopping_cart)):
            meal_client = client.shopping_cart[i]
            meal_in_menu = [meal for meal in self.menu if meal.name == meal_client.name][0]
            meal_in_menu.quantity += client.current_orders_quantity[i]

    def can_client_order(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not self.find_client(client_phone_number):
            self.register_client(client_phone_number)

        client_obj = self.find_client(client_phone_number)

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            meal_obj = self.find_meal(meal_name)

            if not meal_obj:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal_obj.quantity < meal_quantity:
                raise Exception(f"Not enough quantity of {meal_obj.__class__.__name__}: {meal_name}!")

        return client_obj

    def register_client(self, client_phone_number: str):
        if self.find_client(client_phone_number):
            raise Exception("The client has already been registered!")

        client_obj = Client(client_phone_number)
        self.clients_list.append(client_obj)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal_obj in meals:
            if meal_obj.__class__.__name__ not in self.VALID_MEALS:
                continue
            self.menu.append(meal_obj)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        client_obj = self.can_client_order(client_phone_number, **meal_names_and_quantities)

        if client_obj:
            for meal_name, meal_quantity in meal_names_and_quantities.items():
                meal_obj = self.find_meal(meal_name)
                price_meal = meal_quantity * meal_obj.price
                client_obj.shopping_cart.append(meal_obj)
                client_obj.bill += price_meal
                meal_obj.quantity -= meal_quantity
                client_obj.current_orders_quantity.append(meal_quantity)

            return f"Client {client_phone_number} successfully ordered" \
                   f" {', '.join(meal.name for meal in client_obj.shopping_cart)}" \
                   f" for {client_obj.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client_obj = self.find_client(client_phone_number)

        if len(client_obj.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        self.reset_menu(client_obj)
        client_obj.bill = 0
        client_obj.shopping_cart.clear()

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client_obj = self.find_client(client_phone_number)

        if len(client_obj.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        client_obj.shopping_cart.clear()
        paid_money = client_obj.bill
        client_obj.bill = 0
        return f"Receipt #{self.receipt_id} with total amount of {paid_money:.2f} was successfully paid for " \
               f"{client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."








