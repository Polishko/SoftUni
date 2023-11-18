import os

import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions
from main_app.models import Profile, Product, Order
from datetime import datetime, timezone, timedelta


# # Create profiles
# profile1 = Profile.objects.create(
#     full_name="Profile 1",
#     email="profile_1@profile.com",
#     phone_number="123456789",
#     address="Address_1"
# )
#
# profile2 = Profile.objects.create(
#     full_name="Profile_2",
#     email="profile_2@profile.com",
#     phone_number="22345678",
#     address="Address_2"
# )
#
# profile3 = Profile.objects.create(
#     full_name="Profile_3",
#     email="profile_3@profile.com",
#     phone_number="32296754",
#     address="Address_3"
# )
#
# profile4 = Profile.objects.create(
#     full_name="Profile_4",
#     email="profile_4@profile.com",
#     phone_number="423456789",
#     address="Address_4"
# )
#
# # Create products
# product1 = Product.objects.create(
#     name="Product_1",
#     description="Description_1",
#     price=10.00,
#     in_stock=20
# )
#
# product2 = Product.objects.create(
#     name="Product_2",
#     description="Description_2",
#     price=15.00,
#     in_stock=10
# )
#
# product3 = Product.objects.create(
#     name="Product_3",
#     description="Description_3",
#     price=5.00,
#     in_stock=5
# )
#
# # Create orders
# order1 = Order.objects.create(
#     profile=profile1,
#     total_price=25.00
# )
# order1.products.add(product1, product2)
#
# order2 = Order.objects.create(
#     profile=profile2,
#     total_price=20.00
# )
# order2.products.add(product2, product3)
#
# order3 = Order.objects.create(
#     profile=profile1,
#     total_price=20.00
# )
# order2.products.add(product2, product3)
#
# order4 = Order.objects.create(
#     profile=profile3,
#     total_price=30.00
# )
# order2.products.add(product2, product3, product1)
#
# order5 = Order.objects.create(
#     profile=profile4,
#     total_price=5.00
# )
# order2.products.add(product3)

# profile = Profile.objects.first()
# product = Product.objects.first()
# order6 = Order.objects.create(
#     profile=profile,
#     total_price=10.00
# )
# order6.products.add(product)

# Test ProfileManager
# print(Profile.objects.get_regular_customers().all())


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    query = (Q(full_name__icontains=search_string) |
             Q(email__icontains=search_string) |
             Q(phone_number__icontains=search_string))

    profiles = (Profile.
                objects.prefetch_related("profile_orders").
                filter(query).
                annotate(num_orders=Count("profile_orders")).
                order_by("full_name"))

    if not profiles:
        return ""

    result = []
    for profile in profiles:
        result.append(f"Profile: {profile.full_name},"
                      f" email: {profile.email},"
                      f" phone number: {profile.phone_number},"
                      f" orders: {profile.num_orders}")

    return "\n".join(result)


# print(get_profiles(search_string="proF"))


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers().all()

    if not profiles:
        return ""

    result = []
    for profile in profiles:
        result.append(f"Profile: {profile.full_name}, orders: {profile.num_orders}")

    return "\n".join(result)


# print(get_loyal_profiles())


def get_last_sold_products():
    order = (Order.objects.
             prefetch_related("products").
             order_by("-creation_date").
             first())

    if order is None:
        return ""

    if order:
        products = (order.
                    products.order_by("name").
                    values_list("name", flat=True))
        if products:
            product_list = ", ".join(products)
            return f"Last sold products: {product_list}"

        return ""


# date_time = datetime(2023, 11, 19, 9, 47, 54, 203769, timezone.utc)
# order = Order.objects.all()[0]
# order.creation_date = date_time
# order.save()
# print(get_last_sold_products())


def get_top_products():

    products = (Product.objects.
                prefetch_related("product_in_orders").
                annotate(num_orders=Count("product_in_orders")).
                filter(num_orders__gt=0).
                order_by("-num_orders", "name"))[:5]

    if not products or not Order.objects.all:
        return ""

    result = [f"Top products:"]
    for product in products:
        result.append(f"{product.name}, sold {product.num_orders} times")

    return "\n".join(result)


# print(get_top_products())


def apply_discounts():
    orders = (Order.objects.
              prefetch_related("products").
              annotate(num_products=Count("products")).
              filter(num_products__gt=2).
              filter(is_completed=False))

    discounted_orders = orders.update(total_price=F("total_price") * 0.90)

    return f"Discount applied to {discounted_orders} orders."


# print(apply_discounts())


def complete_order():
    try:
        order = (Order.objects.
                 prefetch_related("products").
                 filter(is_completed=False).
                 earliest("creation_date"))

        for product in order.products.all():
            new_amount = max(0, product.in_stock - 1)
            product.in_stock = new_amount

            if new_amount == 0:
                product.is_available = False

            product.save()

        order.is_completed = True
        order.save()

        return "Order has been completed!"

    except Order.DoesNotExist:
        return ""


# print(complete_order())
