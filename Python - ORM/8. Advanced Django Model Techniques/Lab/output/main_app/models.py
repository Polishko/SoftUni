from django.db import models
from django.core.validators import (MinLengthValidator, MaxLengthValidator,
                                    MinValueValidator, MaxValueValidator)

from main_app.validators import validate_menu_categories


# Create your models here.
# 1.	Restaurant
class Restaurant(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(2, "Name must be at least 2 characters long."),
            MaxLengthValidator(100, "Name cannot exceed 100 characters.")
        ]
    )
    location = models.CharField(
        max_length=250,
        validators=[
            MinLengthValidator(2, "Location must be at least 2 characters long."),
            MaxLengthValidator(200, "Location cannot exceed 200 characters.")
        ]
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0, "Rating must be at least 0.00."),
            MaxValueValidator(5, "Rating cannot exceed 5.00.")
        ]
    )


# 2. Menu
class Menu(models.Model):
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField(
        validators=[validate_menu_categories]
    )
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE
    )


# 3. RestaurantReview
# class RestaurantReview(models.Model):
#     reviewer_name = models.CharField(
#         max_length=100
#     )
#     review_content = models.TextField()
#     rating = models.PositiveIntegerField(
#         validators=[MaxValueValidator(5)]
#     )
#     restaurant = models.ForeignKey(
#         to=Restaurant,
#         on_delete=models.CASCADE
#     )
#
#     class Meta:
#
#         ordering = ["-rating"]
#         verbose_name = "Restaurant Review"
#         verbose_name_plural = "Restaurant Reviews"
#         unique_together = ["reviewer_name", "restaurant"]


# # 4. Restaurant Review Types
# class RestaurantReview(models.Model):
#     reviewer_name = models.CharField(
#         max_length=100
#     )
#     review_content = models.TextField()
#     rating = models.PositiveIntegerField(
#         validators=[MaxValueValidator(5)]
#     )
#     restaurant = models.ForeignKey(
#         to=Restaurant,
#         on_delete=models.CASCADE
#     )
#
#     class Meta:
#         abstract = True
#         ordering = ["-rating"]
#         verbose_name = "Restaurant Review"
#         verbose_name_plural = "Restaurant Reviews"
#         unique_together = ["reviewer_name", "restaurant"]
#
#
# class RegularRestaurantReview(RestaurantReview):
#     ...
#
#
# class FoodCriticRestaurantReview(RestaurantReview):
#     food_critic_cuisine_area = models.CharField(
#         max_length=100
#     )
#
#     class Meta:
#         ordering = ["-rating"]
#         verbose_name = "Food Critic Review"
#         verbose_name_plural = "Food Critic Reviews"
#         unique_together = ["reviewer_name", "restaurant"]
#
#
# # 5.	Menu Review
# class MenuReview(models.Model):
#     reviewer_name = models.CharField(
#         max_length=100
#     )
#     menu = models.ForeignKey(
#         to=Menu,
#         on_delete=models.CASCADE
#     )
#     review_content = models.TextField()
#     rating = models.PositiveIntegerField(
#         validators=[MaxValueValidator(5)]
#     )
#
#     class Meta:
#         ordering = ["-rating"]
#         verbose_name = "Menu Review"
#         verbose_name_plural = "Menu Reviews"
#         unique_together = ["reviewer_name", "menu"]
#         indexes = [
#             models.Index(fields=["menu"], name="main_app_menu_review_menu_id")
#         ]

# 6. Rating and Review Content

class ReviewMixin(models.Model):
    reviewer_name = models.CharField(
        max_length=100
    )
    review_content = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5, "Rating cannot exceed 5.00.")]
    )

    class Meta:
        abstract = True
        ordering = ["-rating"]


class RestaurantReview(ReviewMixin):
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE
    )

    class Meta(ReviewMixin.Meta):
        abstract = True
        verbose_name = "Restaurant Review"
        verbose_name_plural = "Restaurant Reviews"
        unique_together = ('reviewer_name', 'restaurant')


class RegularRestaurantReview(RestaurantReview):
    ...


class FoodCriticRestaurantReview(RestaurantReview):
    food_critic_cuisine_area = models.CharField(
        max_length=100
    )

    class Meta(RestaurantReview.Meta):
        verbose_name = "Food Critic Review"
        verbose_name_plural = "Food Critic Reviews"
        unique_together = ("reviewer_name", "restaurant")


class MenuReview(ReviewMixin):
    menu = models.ForeignKey(
        to=Menu,
        on_delete=models.CASCADE
    )

    class Meta(ReviewMixin.Meta):
        verbose_name = "Menu Review"
        verbose_name_plural = "Menu Reviews"
        unique_together = ("reviewer_name", "menu")
        indexes = [
            models.Index(fields=["menu"], name="main_app_menu_review_menu_id")
        ]
