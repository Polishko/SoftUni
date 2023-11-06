from datetime import timedelta

from django.db import models
from django.core.exceptions import ValidationError
from abc import abstractmethod


# 1.	Character Classes

class BaseCharacter(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField()

    class Meta:
        abstract = True


class Mage(BaseCharacter):
    elemental_power = models.CharField(
        max_length=100
    )
    spellbook_type = models.CharField(
        max_length=100
    )


class Assassin(BaseCharacter):
    weapon_type = models.CharField(
        max_length=100
    )
    assassination_technique = models.CharField(
        max_length=100
    )


class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(
        max_length=100
    )
    demon_slaying_ability = models.CharField(
        max_length=100
    )


class TimeMage(Mage):
    time_magic_mastery = models.CharField(
        max_length=100
    )
    temporal_shift_ability = models.CharField(
        max_length=100
    )


class Necromancer(Mage):
    raise_dead_ability = models.CharField(
        max_length=100
    )


class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(
        max_length=100
    )
    venomous_bite_ability = models.CharField(
        max_length=100
    )


class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(
        max_length=100
    )


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(
        max_length=100
    )
    retribution_ability = models.CharField(
        max_length=100
    )


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(
        max_length=100
    )

# 2.	Chat App

class UserProfile(models.Model):
    username = models.CharField(
        max_length=70,
        unique=True
    )
    email = models.EmailField(
        unique=True
    )
    bio = models.TextField(
        blank=True,
        null=True
    )


class Message(models.Model):
    sender = models.ForeignKey(
        to=UserProfile,
        related_name="sent_messages",
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        to=UserProfile,
        related_name="received_messages",
        on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    is_read = models.BooleanField(
        default=False
    )

    def mark_as_read(self):
        self.is_read = True

    def mark_as_unread(self):
        self.is_read = False

    def reply_to_message(self, reply_content, receiver):
        reply_message = Message.objects.create(
            sender=self.receiver,
            receiver=receiver,
            content=reply_content)
        # not tested but need to save the message: reply_message.save()
        return reply_message

    def forward_message(self, sender, receiver):
        forwarded_message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            content=self.content)
        # not tested but need to save the message: forwarded_message.save()
        return forwarded_message


# 3.	Student Information
class StudentIDField(models.PositiveIntegerField):

    def get_prep_value(self, value): # this method inherits from positiveinteger
        return int(value)

# better alternative to just use to_python
def to_python(self, value):
    try:
        return int(value)
    except ValueError:
        pass # better raise ValidationError in real life (can cause issue in Judge)

class Student(models.Model):
    name = models.CharField(
        max_length=100
    )
    student_id = StudentIDField()

# 4.	Credit Card Masking
class MaskedCreditCardField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 20
        super().__init__(*args, **kwargs)

    def to_python (self, value):
        if not isinstance(value, str):
            raise ValidationError("The card number must be a string")
        elif not value.isdigit():
            raise ValidationError("The card number must contain only digits")
        elif len(value) != 16:
            raise ValidationError("The card number must be exactly 16 characters long")
        return f"****-****-****-{value[-4:]}"

class CreditCard(models.Model):
    card_owner = models.CharField(
        max_length=100
    )
    card_number = MaskedCreditCardField()

# Hotel Reservation System
Question 5 needs correction

class Hotel(models.Model):
    name = models.CharField(
        max_length=100
    )
    address = models.CharField(
        max_length=200
    )


class Room(models.Model):
    hotel = models.ForeignKey(
        to=Hotel,
        on_delete=models.CASCADE
    )
    number = models.CharField(
        max_length=100,
        unique=True
    )
    capacity = models.PositiveIntegerField()
    total_guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def clean(self):
        if self.total_guests > self.capacity:
            raise ValidationError("Total guests are more than the capacity of the room")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs) #saves in the DB
        return f"Room {self.number} created successfully"


class BaseReservation(models.Model):
    room = models.ForeignKey(
        to=Room,
        on_delete=models.CASCADE,
    )
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        abstract = True

    @property
    def reserved_days(self):
        return self.reservation_period()

    @abstractmethod
    def room_type(self):
        return self.room_type

    def reservation_period(self):
        return (self.end_date - self.start_date).days  #object.days -> days as integer

    def calculate_total_cost(self):
        return f"{round(self.room.price_per_night * self.reserved_days), 1}"

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date cannot be after or in the same end date")

        regular_reservations = self.room.regularreservation_set.all()
        special_reservations = self.room.specialreservation_set.all()

        def is_reserved_valid():
            for reservation in regular_reservations:
                if not (self.start_date > reservation.end_date or self.end_date < reservation.start_date):
                    return False
            for reservation in special_reservations:
                if not (self.start_date > reservation.end_date or self.end_date < reservation.start_date):
                    return False
            return True

        if not is_reserved_valid():
            raise ValidationError(f"Room {self.room.number} cannot be reserved")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        return f"{self.room_type} reservation for room {self.room.number}"


class RegularReservation(BaseReservation):
    ROOM_TYPE = "Regular"

    @property
    def room_type(self):
        return self.ROOM_TYPE


class SpecialReservation(BaseReservation):
    ROOM_TYPE = "Special"

    @property
    def room_type(self):
        return self.ROOM_TYPE

    def extend_reservation(self, days: int):
        special_reservations = self.room.regularreservation_set.all()
        regular_reservations = self.room.specialreservation_set.all()

        def check_valid_extension():
            if self not in special_reservations or self not in regular_reservations:
                return False

            new_end_date = self.end_date + timedelta(days=days)

            for reservation in special_reservations:
                if new_end_date <= reservation.end_date:
                    return False
            for reservation in regular_reservations:
                if new_end_date <= reservation.end_date:
                    return False
            return True

        if not check_valid_extension():
            raise ValidationError("Error during extending reservation")
        return f"Extended reservation for room {self.room.number} with {days} days"
