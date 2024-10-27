from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Your name must contain letters only!'
        else:
            self.__message = value

    def __call__(self, value):
        for char in value:
            if not char.isalpha():
                raise ValidationError(self.message)


@deconstructible
class PassCodeValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Your passcode must be exactly 6 digits!'
        else:
            self.__message = value

    def __call__(self, value):
        if not (value.isdigit() and len(value) == 6):
            raise ValidationError(self.message)
