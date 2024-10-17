from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

# Ensure this value contains only letters, numbers, and underscore.
@deconstructible
class UserNameValidator:
    def __init__(self, message=None):
        self.message = message or 'Ensure this value contains only letters, numbers, and underscore.'

    def __call__(self, value):
        for char in value:
            if not (char.isalnum() or char == '_'):
                raise ValidationError(self.message)
