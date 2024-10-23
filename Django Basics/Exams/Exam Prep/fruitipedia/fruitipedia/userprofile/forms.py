from django import forms

from fruitipedia.mixins import PlaceHolderMixin, LabelRemoveMixin
from fruitipedia.userprofile.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(LabelRemoveMixin, PlaceHolderMixin, ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['image_url', 'age', ]

class ProfileEditForm(PlaceHolderMixin, ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ['password', 'email',]

class ProfileDeleteForm(PlaceHolderMixin, ProfileBaseForm):
    pass

