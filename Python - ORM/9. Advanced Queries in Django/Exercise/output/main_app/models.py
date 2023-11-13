from datetime import timedelta

from django.db import models
from django.db.models import Q, F, Func
from django.forms import CharField

from main_app.managers import RealEstateListingManager, VideoGameManager
from main_app.validators import validate_rate, validate_release_year


# Create your models here.


class RealEstateListing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('House', 'House'),
        ('Flat', 'Flat'),
        ('Villa', 'Villa'),
        ('Cottage', 'Cottage'),
        ('Studio', 'Studio'),
    ]

    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    objects = RealEstateListingManager()


class VideoGame(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'RPG'),
        ('Adventure', 'Adventure'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField(
        validators=[validate_release_year]
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[validate_rate]
    )
    objects = VideoGameManager()

    def __str__(self):
        return self.title


class BillingInfo(models.Model):
    address = models.CharField(max_length=200)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    billing_info = models.OneToOneField(BillingInfo, on_delete=models.CASCADE)

     # join for faster queries
   @classmethod
    def get_invoices_with_prefix(cls, prefix):
        return cls.objects.select_related("billing_info").filter(invoice_number__startswith=prefix)

    @classmethod
    def get_invoices_sorted_by_number(cls):
        return cls.objects.select_related("billing_info").order_by("invoice_number")

    @classmethod
    def get_invoice_with_billing_info(cls, invoice_number: str):
        return cls.objects.select_related("billing_info").get(invoice_number=invoice_number)

    # these are slower    
    # @staticmethod
    # def get_invoices_with_prefix(prefix):
    #     query = Q(invoice_number__startswith=prefix)

    #     return Invoice.objects.filter(query)

    # @staticmethod
    # def get_invoices_sorted_by_number():
    #     return Invoice.objects.order_by("invoice_number")

    # @staticmethod
    # def get_invoice_with_billing_info(invoice_number: str):
    #     return Invoice.objects.get(invoice_number=invoice_number)


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')

    def get_programmers_with_technologies(self):
        return self.programmers.prefetch_related("projects__technologies_used")
        
# # this is slow
    # def get_programmers_with_technologies(self):
    #     return self.programmers.all()


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')

def get_projects_with_technologies(self):
        return self.projects.prefetch_related("technologies_used")    

# def get_projects_with_technologies(self):
    #     return self.projects.all()


class Task(models.Model):
    PRIORITIES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITIES)
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateField()
    completion_date = models.DateField()

    @staticmethod
    def overdue_high_priority_tasks():
        query = (Q(priority__iexact="high") &
                 Q(is_completed=False) &
                 Q(completion_date__gt=F("creation_date")))

        return Task.objects.filter(query)

    @staticmethod
    def completed_mid_priority_tasks():
        query = Q(priority__iexact="medium") & Q(is_completed=True)

        return Task.objects.filter(query)

    @staticmethod
    def search_tasks(query: str):
        query = Q(title__icontains=query) | Q(description__icontains=query)

        return Task.objects.filter(query)

    # @staticmethod
    # def recent_completed_tasks(days: int):
    #     query = Q(is_completed=True) & Q(completion_date__gte=F("creation_date") - timedelta(days=days))

    #     return Task.objects.filter(query)


    def recent_completed_tasks(self, days: int):
        query = Q(is_completed=True) & Q(completion_date__gte=self.creation_date - timedelta(days=days))

        return Task.objects.filter(query)
    
    
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    @staticmethod # or use classmethod with cls
    def get_long_and_hard_exercises():
        query = Q(duration_minutes__gt=30) & Q(difficulty_level__gte=10)

        return Exercise.objects.filter(query)

    @staticmethod
    def get_short_and_easy_exercises():
        query = Q(difficulty_level__lt=5) & Q(duration_minutes__lt=15)

        return Exercise.objects.filter(query)

    @staticmethod
    def get_exercises_within_duration(min_duration: int, max_duration: int):
        query = Q(duration_minutes__gte=min_duration) & Q(duration_minutes__lte=max_duration)

        return Exercise.objects.filter(query)

    @staticmethod
    def get_exercises_with_difficulty_and_repetitions(min_difficulty: int, min_repetitions: int):
        query = Q(difficulty_level__gte=min_difficulty) & Q(repetitions__gte=min_repetitions)

        return Exercise.objects.filter(query)

