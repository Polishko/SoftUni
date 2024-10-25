from django import forms

from myplantapp.mixins import DisableFieldMixin
from myplantapp.plant.models import Plant


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ['owner',]


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(DisableFieldMixin, PlantBaseForm):
    pass
