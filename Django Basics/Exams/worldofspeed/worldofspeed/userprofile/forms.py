from django import forms

from worldofspeed.userprofile.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        error_messages = {
            'username': {
                'min_length': 'Username must be at least 3 chars long!'
            },
            'age': {
                'min_value': 'Age must be 21 or above!',
            },
        },


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        widgets = {
            'password': forms.PasswordInput(),
        }
        exclude = ['firstname', 'lastname', 'profile_picture']

class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        widgets = {
            'password': forms.PasswordInput(),
        }
