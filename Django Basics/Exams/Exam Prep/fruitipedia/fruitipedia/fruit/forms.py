from django import forms

from fruitipedia.fruit.models import Fruit
from fruitipedia.mixins import LabelRemoveMixin, PlaceHolderMixin, FieldDisableMixin


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['owner',]

class FruitCreateForm(LabelRemoveMixin, PlaceHolderMixin, FruitBaseForm):
    pass

class FruitEditForm(FruitBaseForm):
    pass

class FruitDeleteForm(FieldDisableMixin, FruitBaseForm):
    class Meta(FruitBaseForm.Meta):
        exclude = FruitBaseForm.Meta.exclude + ['nutrition',]
