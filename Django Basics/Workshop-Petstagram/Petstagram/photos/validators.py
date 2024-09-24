from django.core.exceptions import ValidationError

def validate_file_size(image_object):
    if image_object.size > 5242880:
        raise ValidationError('The maximum allowed size for upload is 5MB')