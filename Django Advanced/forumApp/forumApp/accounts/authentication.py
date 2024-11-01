from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # username comes from form field if available
        # else check if other credential coming from primary credential field
        identifier = username if username is not None else kwargs.get(UserModel.USERNAME_FIELD)

        # try identification with email
        try:
            user = UserModel.objects.get(email=identifier)
        except UserModel.DoesNotExist:
            # try identification with username: optional but this way django won't waste resources
            # trying to search with the next backend (defined in settings as the ModelBackend):
            try:
                user = UserModel.objects.get(username=identifier)
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
