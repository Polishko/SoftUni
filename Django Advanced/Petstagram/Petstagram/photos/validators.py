from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

# Option 1: function validator
# def validate_file_size(image_object):
#     if image_object.size > 5242880:
#         raise ValidationError('The maximum allowed size for upload is 5MB')

# Option 2: customizable class based validator
# deconstructible: convertable to serializable format and back by Django
@deconstructible
class FileSizeValidator:
    def __init__(self, file_size_mb: int, message=None):
        self.file_size_mb = file_size_mb
        self.message = message


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"File size must be below or equal to {self.file_size_mb}MB"
        else:
            self.__message = value

    # allow the class to be callable and act as a function when its instance is invoked
    def __call__(self, value):
        if value.size > self.file_size_mb * 1024 * 1024:
            raise ValidationError(self.message)
