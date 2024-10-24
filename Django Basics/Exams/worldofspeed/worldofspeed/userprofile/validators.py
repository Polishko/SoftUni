from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class UserNameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Username must contain only letters, digits, and underscores!'
        else:
            self.__message = value

    def __call__(self, value):
        for char in value:
            if not (char.isalnum() or char == '_'):
                raise ValidationError(self.message)


@deconstructible
class CarYearValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Year must be between 1999 and 2030!'
        else:
            self.__message = value

    def __call__(self, value):
        if value < 1999 or value > 2030:
            raise ValidationError(self.message)
