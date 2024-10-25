from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PlantNameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Plant name should contain only letters!'
        else:
            self.__message = value

    def __call__(self, value):
        for char in value:
            if not char.isalpha():
                raise ValidationError(self.message)
