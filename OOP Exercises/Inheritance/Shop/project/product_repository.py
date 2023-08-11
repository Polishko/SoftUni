from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product or None:  # Optional[Product] old vers.; 3.1+ Product | None
        try:
            return next(filter(lambda x: x.name == product_name, self.products))
        except StopIteration:
            pass

    def remove(self, product_name: str) -> None:
        # try:
        #     product = next(filter(lambda x: x.name == product_name, self.products))
        #     self.products.remove(product)
        # except StopIteration:
        #     pass

        product = self.find(product_name)
        if product:
            self.products.remove(product)            

    def __repr__(self) -> str:
        return "\n".join([f"{info.name}: {info.quantity}" for info in self.products])
