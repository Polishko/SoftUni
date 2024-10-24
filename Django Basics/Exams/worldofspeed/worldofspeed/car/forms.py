from django import forms

from worldofspeed.car.models import Car
from worldofspeed.mixins import ReadOnlyMixin


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner',]
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }
        error_messages = {
            'image_url': {
                'unique': 'This image URL is already in use! Provide a new one.',
            }
        }

class CarCreateForm(CarBaseForm):
    pass

class CarEditForm(CarBaseForm):
    pass

class CarDeleteForm(ReadOnlyMixin, CarBaseForm):
    readonly_fields = ['type', 'year', 'model', 'price', 'image_url',]
