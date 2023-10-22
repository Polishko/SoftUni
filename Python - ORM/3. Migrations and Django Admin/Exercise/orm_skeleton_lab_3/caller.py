import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Person, Item, Smartphone, Order


# # Create and check models
# def add_initial_products():
#     # Adding the first product
#     product1 = Product(
#         name="Smartphone",
#         description="A high-end smartphone with a powerful camera and fast processor.",
#         price=799.99,
#         category="Electronics",
#         supplier="TechGadget Inc."
#     )
#     product1.save()
#
#     # Adding the second product
#     product2 = Product(
#         name="Running Shoes",
#         description="Comfortable running shoes with cushioned soles for long-distance runs.",
#         price=79.99,
#         category="Footwear",
#         supplier="Sports Gear Co."
#     )
#     product2.save()
#
#     # Adding the third product
#     product3 = Product(
#         name="Coffee Maker",
#         price=149.95,
#         category="Appliances",
#         supplier="Kitchen Essentials Ltd."
#     )
#     product3.save()
#     return "3 products were added successfully to the database"
#
# def add_new_product_with_time_of_creation_and_edition():
#     # Adding the first product
#     product4 = Product(
#         name="LED TV",
#         description="A 55-inch LED TV with 4K resolution and smart TV capabilities.",
#         price=699.99,
#         category="Electronics",
#         supplier="ElectroTech Inc."
#     )
#     product4.save()
#     return "1 product with time of creation and edition was added to the database"
#
# def add_products_with_count_value():
#     product5 = Product(
#         name="Laptop Bag",
#         description="A stylish and durable laptop bag with multiple compartments.",
#         price=49.95,
#         category="Accessories",
#         supplier="FashionStyle Co.",
#         count=126
#     )
#     product5.save()
#
#     product6 = Product(
#         name="Stainless Steel Water Bottle",
#         description="A 32 oz stainless steel water bottle with double-wall insulation.",
#         price=19.99,
#         category="Kitchenware",
#         supplier="HealthyLiving Supplies"
#     )
#     product6.save()
#     return "2 products with count were added to the database"


def add_people():
    person1 = Person.objects.create(name="Defne", age=12)
    person2 = Person.objects.create(name="Bade", age=17)
    person3 = Person.objects.create(name="Leman", age=43)

    return "3 people were added to the database"


def add_items():
    item1 = Item.objects.create(name="pilates_ball", price=10, quantity=2)
    item2 = Item.objects.create(name="weights_3kg", price=5, quantity=1)
    item3 = Item.objects.create(name="weights_5kg", price=8, quantity=1)
    item4 = Item.objects.create(name="matt", price=20, quantity=1)
    item5 = Item.objects.create(name="resistance_band", price=6, quantity=4)

    return "Added 3 items to table item"


def add_smartphone():
    phone1 = Smartphone.objects.create(brand="Yoga")
    phone2 = Smartphone.objects.create(brand="Xiomi")
    phone3 = Smartphone.objects.create(brand="Samsung")
    phone4 = Smartphone.objects.create(brand="iPhone")

    return "Added 4 items to the database"


def add_order():
    order1 = Order.objects.create(
        product_name="pizza",
        customer_name="Genc",
        order_date="2023-12-02",
        status="Pending",
        product_price=14
    )
    order2 = Order.objects.create(
        product_name="coffee",
        customer_name="Genc",
        order_date="2023-12-05",
        status="Cancelled",
        product_price=5
    )
    order3 = Order.objects.create(
        product_name="salad",
        customer_name="Genc",
        order_date="2023-12-15",
        status="Completed",
        product_price=8
    )

    return "3 items added in the db"


def delete_test_fnc():
    all_orders = Order.objects.all()

    for order in all_orders:
        if order.status == "Cancelled":
            order.delete()


def delete_all_rows():
    Order.objects.all().delete()

# Run and print your queries

# print(add_initial_products())

# print(add_new_product_with_time_of_creation_and_edition())

# print(add_products_with_count_value())

# print(add_people())

# print(add_items())

# print(add_smartphone())

# print(add_order())

# delete_test_fnc()

# delete_all_rows()