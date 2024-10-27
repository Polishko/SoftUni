from django import forms

from furryfunnies.mixins import PlaceHolderMixin
from furryfunnies.userprofile.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorCreateForm(PlaceHolderMixin, AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['info', 'image_url']
        widgets = {
            'passcode': forms.PasswordInput(),
        }


class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ['passcode',]


class AuthorDeleteForm(AuthorBaseForm):
    pass
