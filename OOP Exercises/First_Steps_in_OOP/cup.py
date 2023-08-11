class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, new_amount):
        if self.quantity + new_amount <= self.size:
            self.quantity += new_amount

    def status(self):
        return self.size - self.quantity
