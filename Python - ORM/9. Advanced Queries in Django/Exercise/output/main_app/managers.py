from django.db import models
from decimal import Decimal

from django.db.models import Q, Count, F, Max, Min, Avg


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type: str):

        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        query = Q(price__range=(min_price, max_price))

        return self.filter(query)

    def with_bedrooms(self, bedrooms_count: int):

        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):
        location_counts = self.values("location").annotate(location_count=Count("id")).order_by("-location_count", "location")[:2]

        return location_counts


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre: str):

        return self.filter(genre=genre)

    def recently_released_games(self, year: int):

        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        highest_rating = self.aggregate(max_rate=Max("rating"))["max_rate"]

        return self.get(rating=highest_rating)

    def lowest_rated_game(self):
        lowest_rating = self.aggregate(min_rate=Min("rating"))["min_rate"]

        return self.get(rating=lowest_rating)

    def average_rating(self):
        average_rate = self.aggregate(ave_rate=Avg("rating"))["ave_rate"]

        return f"{average_rate:.1f}"

