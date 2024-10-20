from django import forms
from musicapp.userprofile.models import Profile


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        }

class AddUserProfile(UserBaseForm):
    pass

class DeleteUserProfile(UserBaseForm):
    pass