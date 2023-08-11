class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):

        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage


storage = Storage(5)
storage.add_product("pidi")
storage.add_product("kedi")
storage.add_product("cucu")
storage.add_product("kutu")
storage.add_product("kitap")
print(storage.get_products())
