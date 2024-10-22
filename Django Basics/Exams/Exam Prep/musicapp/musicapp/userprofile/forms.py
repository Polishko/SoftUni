from django import forms

from musicapp.mixins import PlaceholderMixin
from musicapp.userprofile.models import Profile


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class AddUserProfile(PlaceholderMixin, UserBaseForm):
    pass

class DeleteUserProfile(PlaceholderMixin, UserBaseForm):
    pass