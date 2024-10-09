from django import forms

from Petstagram.pets.mixins import DisableFieldsMixin
from Petstagram.pets.models import Pet

class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select a date'}),
            'personal_photo': forms.TextInput(attrs={'placeholder': 'Pet image'}),
        }
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image',
        }

class PetCreateForm(PetBaseForm):
    pass

class PetEditForm(PetBaseForm):
    pass

class PetDeleteForm(PetBaseForm, DisableFieldsMixin):
    pass
    disabled_fields = ('__all__',)
    readonly_fields = ('__all__',)
