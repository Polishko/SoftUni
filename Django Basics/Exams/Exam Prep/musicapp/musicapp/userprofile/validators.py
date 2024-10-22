from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
# from django.utils.text import slugify


# Ensure this value contains only letters, numbers, and underscore.
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
            self.__message = 'Ensure this value contains only letters, numbers, and underscore.'
        else:
            self.__message = value

    def __call__(self, value):
        for char in value:
            if not (char.isalnum() or char == '_'):
            # if '-' in value or value.lower() != slugify(value): # alternative
                raise ValidationError(self.message)
