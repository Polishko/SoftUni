from django import forms
from django.core.exceptions import ValidationError

from tastyrecipes.mixins import ReadOnlyMixin
from tastyrecipes.recipe.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)
        widgets = {
            'ingredients': forms.Textarea(attrs={'placeholder': 'ingredient1, ingredient2, ...'}),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Optional image URL here...'}),
        }
        help_texts = {
            'cooking_time': 'Provide the cooking time in minutes.'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if Recipe.objects.filter(title=title).exclude(pk=self.instance.pk).exists():
            raise ValidationError('We already have a recipe with the same title!')

        return title

class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(ReadOnlyMixin, RecipeBaseForm):
    readonly_fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url',]
