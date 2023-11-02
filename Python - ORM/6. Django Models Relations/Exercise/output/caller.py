import os

import django
from datetime import timedelta, date

from django.utils import timezone

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import (Author, Book, Artist, Song, Product,
                             Review, Driver, DrivingLicense, Owner, Car, Registration)

# 1. Library

# Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")

# Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )

# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )


# Create queries within functions
def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by("id")

    result = []
    for author in authors: # to avoid two requests better to use prefetch -> next lectures
        if author.book_set.count() == 0:
            continue

        author_books = ", ".join(book.title for book in author.book_set.all())
        result.append(f"{author.name} has written - {author_books}!")

    return "\n".join(result)


# Display authors and their books
# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


# Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())


# 2. Song


# Create artists
# artist1 = Artist.objects.create(name="Daniel Di Angelo")
# artist2 = Artist.objects.create(name="Indila")

# Create songs
# song1 = Song.objects.create(title="Lose Face")
# song2 = Song.objects.create(title="Tourner Dans Le Vide")
# song3 = Song.objects.create(title="Loyalty")


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.filter(name=artist_name).first()
    song = Song.objects.filter(title=song_title).first()

    if artist and song:
        artist.songs.add(song)


# Add a song to an artist
# add_song_to_artist("Daniel Di Angelo", "Lose Face")
# add_song_to_artist("Daniel Di Angelo", "Loyalty")
# add_song_to_artist("Indila", "Tourner Dans Le Vide")


def get_songs_by_artist(artist_name: str):
    return Artist.objects.filter(name=artist_name).first().songs.all().order_by("-id")


# Get all songs by a specific artist
# songs = get_songs_by_artist("Daniel Di Angelo")
# for song in songs:
#     print(f"Daniel Di Angelo: {song.title}")

# Get all songs by a specific artist
# songs = get_songs_by_artist("Indila")
# for song in songs:
#     print(f"Indila: {song.title}")


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.filter(name=artist_name).first()
    song = Song.objects.filter(title=song_title).first()

    if artist and song:
        artist.songs.remove(song)

# Remove a song from an artist
# remove_song_from_artist("Daniel Di Angelo", "Lose Face")

# Check if the song is removed
# songs = get_songs_by_artist("Daniel Di Angelo")
#
# for song in songs:
#     print(f"Songs by Daniel Di Angelo after removal: {song.title}")


# 3. Shop
# Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
#
# # Create some reviews for products
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)


def calculate_average_rating_for_product_by_name(product_name: str):
    searched_product = Product.objects.filter(name=product_name).first()
    searched_reviews = Review.objects.filter(product=searched_product).all()
    return sum(review.rating for review in searched_reviews)/searched_reviews.count()


# Calculate and print the average rating
# print(calculate_average_rating_for_product_by_name("Laptop"))


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


# reviews_with_rating_above_threshold = get_reviews_with_high_ratings(4)
# print(f"Reviews with rating above threshold: {', '.join([str(r.rating) for r in reviews_with_rating_above_threshold])}")


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


# Run the function to get products without reviews
# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


# Run the function to delete products without reviews
# delete_products_without_reviews()
# print(f"Products left: {Product.objects.count()}")


# 4. License

# Create drivers
# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
# Create licenses associated with drivers
# license1 = DrivingLicense.objects.create(license_number="123", issue_date=date(2022, 10, 6), driver=driver1)
# license2 = DrivingLicense.objects.create(license_number="456", issue_date=date(2022, 1, 1), driver=driver2)

def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.all().order_by("-license_number")

    info = []
    for driver_license in licenses:
        expire_date = driver_license.issue_date + timedelta(days=365)
        info.append(f"License with id: {driver_license.license_number}"
                    f" expires on {expire_date}!")

    return "\n".join(info)


# Calculate licenses expiration dates
# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)


def get_drivers_with_expired_licenses(due_date):
    licenses = DrivingLicense.objects.all()

    info = []
    for driver_license in licenses:
        expire_date = driver_license.issue_date + timedelta(days=365)
        if expire_date > due_date:
            license_holder = driver_license.driver
            info.append(license_holder)

    return info


# Get drivers with expired licenses
# drivers_with_expired_licenses = get_drivers_with_expired_licenses(date(2023, 1, 1))
# for driver in drivers_with_expired_licenses:
#     print(f"{driver.first_name} {driver.last_name} has to renew their driving license!")


# 5. Car Registration
# Create instances of the Owner model
# owner1 = Owner.objects.create(name='Ivelin Milchev')
# owner2 = Owner.objects.create(name='Alice Smith')

# Create instances of the Car model and associate them with owners
# car1 = Car.objects.create(model='Citroen C5', year=2004)
# car2 = Car.objects.create(model='Honda Civic', year=2021)
#
# car1.owner_id = owner1.id
# car2.owner_id = owner2.id

# Create instances of the Registration model for the cars
# registration1 = Registration.objects.create(registration_number='TX0044XA')
# registration2 = Registration.objects.create(registration_number='XYZ789')


def register_car_by_owner(owner: object):
    registration = Registration.objects.filter(car_id__isnull=True).first()
    all_registered_cars_id_list = [r.car_id for r in Registration.objects.all()]
    car = Car.objects.exclude(id__in=all_registered_cars_id_list).first()

    registration.car_id = car.id
    registration.registration_date = timezone.now().date()

    registration.save()
    car.save()

    return (f"Successfully registered {car.model} to {owner.name}"
            f" with registration number {registration.registration_number}.")


# print(register_car_by_owner(owner1))


# 6. Car Admin Setup
