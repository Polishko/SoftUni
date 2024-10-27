from furryfunnies.userprofile.models import Author


def get_user_object():
    return Author.objects.first()
