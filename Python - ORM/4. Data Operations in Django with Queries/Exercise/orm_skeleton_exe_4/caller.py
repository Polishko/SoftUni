import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


# Create queries within functions
# def create_pet(name: str, species: str):
#     pet_1 = Pet.objects.create(name=name, species=species)
#     pet_1.save()
#     return f"{name} is a very cute {species}!"
#
#
# def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
#     artifact = Artifact.objects.create(
#         name=name,
#         origin=origin,
#         age=age,
#         description=description,
#         is_magical=is_magical
#     )
#     artifact.save()
#     return f"The artifact {name} is {age} years old!"
#
#
# def delete_all_artifacts():
#     Artifact.objects.all().delete()
#
#
# def show_all_locations():
#     collection = []
#     locations = Location.objects.all().order_by("-id")
#
#     for location in locations:
#         collection.append(f"{location.name} has a population of {location.population}!")
#
#     return "\n".join(collection)
#
#
# def new_capital():
#     locations = Location.objects.all()
#
#     if locations:
#         first_location = locations[0]
#         first_location.is_capital = True
#         first_location.save()
#
#
# def get_capitals():
#     return Location.objects.filter(is_capital=True).values("name")
#
#
# def delete_first_location():
#     locations = Location.objects.all()
#     if locations:
#         locations[0].delete()
#
#
# def apply_discount():
#     cars = Car.objects.all()
#
#     if cars:
#         for car in cars:
#             sum_digits = sum(int(digit) for digit in list(str(car.year)))
#             car.price_with_discount = float(car.price) * (1 - sum_digits/100)
#             car.save()
#
#
# def get_recent_cars():
#     return Car.objects.filter(year__gte=2020).values("model", "price_with_discount")
#
#
# def delete_last_car():
#     cars = Car.objects.all()
#
#     if cars:
#         cars.last().delete()
#
#
# # def delete_last_car():
# #     cars = list(Car.objects.all())
# #
# #     if cars:
# #         cars[-1].delete()
#
#
# def show_unfinished_tasks():
#     tasks = Task.objects.all()
#     uncompleted_tasks = []
#
#     for task in tasks:
#         if task.is_finished is False:
#             uncompleted_tasks.append(f"Task - {task.title} needs to be done until {task.due_date}!")
#
#     return "\n".join(uncompleted_tasks)
#
#
# def complete_odd_tasks():
#     tasks = Task.objects.all()
#
#     for task in tasks:
#         if task.id % 2 != 0:
#             task.is_finished = True
#             task.save()
#
#
# def encode_and_replace(text: str, task_title: str):
#     text = "".join([chr(ord(char) - 3) for char in text])
#     tasks = Task.objects.all()
#     task = tasks.filter(title=task_title).update(description=text)
#
#
# def create_room(room_number, room_type, capacity, amenities, price_per_night):
#     room = HotelRoom.objects.create(
#         room_number=room_number,
#         room_type = room_type,
#         capacity=capacity,
#         amenities=amenities,
#         price_per_night=price_per_night
#     )


def get_deluxe_rooms():
    deluxe_rooms_with_even_id = []
    rooms = HotelRoom.objects.filter(room_type="Deluxe")

    for room in rooms:
        if room.pk % 2 == 0:
            deluxe_rooms_with_even_id.append(f"Deluxe room with number {room.room_number}"
                                             f" costs {room.price_per_night}$ per night!")

    return "\n".join(deluxe_rooms_with_even_id)


def increase_room_capacity():
    rooms = HotelRoom.objects.order_by("id")

    for i in range(len(rooms)):
        room = rooms[i]

        if not room.is_reserved:
            continue

        if i == 0:
            room.capacity += room.id
        else:
            room.capacity += rooms[i-1].capacity

        room.save()


def reserve_first_room():
    room = HotelRoom.objects.first()

    if room:
        room.is_reserved = True
        room.save()


def delete_last_room():
    room = HotelRoom.objects.last()

    if room and room.is_reserved:
        room.delete()


# print function outputs
# print(create_pet('Rocky', 'Hamster'))

# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))
# print(show_all_locations())
# print(new_capital())
# print(get_capitals())

# apply_discount()
# print(get_recent_cars())
# print(show_unfinished_tasks())
# complete_odd_tasks()

# encode_and_replace("Zdvk#wkh#glvkhv$", "Some Task")
# print(Task.objects.get(title='Some Task').description)


# create_room(101,"Standard", 2,	"Tv", 100.00)
# create_room(201,"Deluxe", 3,	"Wi-Fi", 200.00)
# create_room(501,"Deluxe", 6,	"Jakuzzi", 400.00)

# print(get_deluxe_rooms())

# reserve_first_room()

# increase_room_capacity()

# delete_last_room()

# room = HotelRoom.objects.last()
# room.is_reserved = True
# room.save()
# delete_last_room()


# print(HotelRoom.objects.get(room_number=101).is_reserved)
