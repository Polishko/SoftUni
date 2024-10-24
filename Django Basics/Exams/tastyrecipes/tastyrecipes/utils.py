from tastyrecipes.userprofile.models import Profile

def get_user_object():
    return Profile.objects.first()