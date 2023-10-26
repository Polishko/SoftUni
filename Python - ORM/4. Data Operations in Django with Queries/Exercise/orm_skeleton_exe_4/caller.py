import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions
# 1. Pet


def create_pet(name: str, species: str):
    pet_1 = Pet.objects.create(name=name, species=species)
    pet_1.save()
    return f"{name} is a very cute {species}!"

# print function outputs
# print(create_pet('Rocky', 'Hamster'))

# 2.	Artifact


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    artifact.save()
    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300,
# 'A magical amulet believed to bring good fortune', True))

#3. Location


def show_all_locations():
    collection = []
    locations = Location.objects.all().order_by("-id")

    for location in locations:
        collection.append(f"{location.name} has a population of {location.population}!")

    return "\n".join(collection)

# or create a __str__ for the class with the information wanted then return "\n".join(str(l) for l in locations)

def new_capital():
    locations = Location.objects.all()

    if locations:
        first_location = locations[0]
        first_location.is_capital = True
        first_location.save()
        
 #use first(), it's faster also good to use filter to filter the first object and the use update on it

def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    locations = Location.objects.all()
    if locations:
        locations[0].delete() #use first(), it's faster

# print(show_all_locations())
# print(new_capital())
# print(get_capitals())

# 4. Car
#
def apply_discount():
    cars = Car.objects.all()

    if cars:
        for car in cars:
            sum_digits = sum(int(digit) for digit in list(str(car.year)))
            car.price_with_discount = float(car.price) * (1 - sum_digits/100)
            car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values("model", "price_with_discount")


def delete_last_car():
    cars = Car.objects.all()

    if cars:
        cars.last().delete()


# def delete_last_car():
#     cars = list(Car.objects.all())
#
#     if cars:
#         cars[-1].delete()

# apply_discount()
# print(get_recent_cars())
#
# 5. Task Encoder
#
def show_unfinished_tasks():
    tasks = Task.objects.all()
    uncompleted_tasks = []

    for task in tasks:
        if task.is_finished is False:
            uncompleted_tasks.append(f"Task - {task.title} needs to be done until {task.due_date}!")

    return "\n".join(uncompleted_tasks)


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    text = "".join([chr(ord(char) - 3) for char in text])
    tasks = Task.objects.all()
    task = tasks.filter(title=task_title).update(description=text)
#
# print(show_unfinished_tasks())
# complete_odd_tasks()

# encode_and_replace("Zdvk#wkh#glvkhv$", "Some Task")
# print(Task.objects.get(title='Some Task').description)
#
# 6. Hotel room


def create_room(room_number, room_type, capacity, amenities, price_per_night):
    room = HotelRoom.objects.create(
        room_number=room_number,
        room_type = room_type,
        capacity=capacity,
        amenities=amenities,
        price_per_night=price_per_night
    )


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

# 7. Character


character1 = Character.objects.create(
    name="Gandalf",
    class_name="Mage",
    level=10,
    strength=15,
    dexterity=20,
    intelligence=25,
    hit_points=100,
    inventory="Staff of Magic, Spellbook",
)

character2 = Character.objects.create(
    name="Hector",
    class_name="Warrior",
    level=12,
    strength=30,
    dexterity=15,
    intelligence=10,
    hit_points=150,
    inventory="Sword of Troy, Shield of Protection",
)


def update_characters():
    characters = Character.objects.all()

    for character in characters:
        if character.class_name == "Mage":
            character.level += 3
            character.intelligence -= 7
        elif character.class_name == "Warrior":
            character.hit_points *= 0.5
            character.dexterity += 4
        else:
            character.inventory = "The inventory is empty"

        character.save()

# update_characters()


def fuse_characters(first_character, second_character):
    new_inventory = ""

    if first_character.class_name == "Mage" or first_character.class_name == "Scout":
        new_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        new_inventory = "Dragon Scale Armor, Excalibur"

    new_character = Character.objects.create(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level=int((first_character.level + second_character.level) // 2),
        strength=int((first_character.strength + second_character.strength) * 1.2),
        dexterity=int((first_character.dexterity + second_character.dexterity) * 1.4),
        intelligence=int((first_character.intelligence + second_character.intelligence) * 1.5),
        hit_points=int((first_character.hit_points + second_character.hit_points)),
        inventory=new_inventory
    )

    first_character.delete()
    second_character.delete()

#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()
