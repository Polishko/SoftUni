class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: list = []
        self.bill: float = 0.0
        self.current_orders_quantity = []

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value[0] != "0" or len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid phone number!")
        self.__phone_number = value

