from django import forms

from Petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model= Photo
        fields = '__all__'


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta(PhotoBaseForm.Meta):
        exclude = ['photo']


class PhotoDeleteForm(PhotoBaseForm):
    pass