from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from tastyrecipes.recipe.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from tastyrecipes.recipe.models import Recipe
from tastyrecipes.utils import get_user_object


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'common/catalogue.html'


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe/create-recipe.html'
    success_url = reverse_lazy('recipe_catalogue')

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = get_user_object()
        recipe.save()

        return super().form_valid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe/details-recipe.html'
    pk_url_kwarg = 'recipe_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredients = self.get_object().ingredients.split(', ')
        context['ingredient_list'] = [ingredient.capitalize() for ingredient in ingredients]

        return context


class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeEditForm
    template_name = 'recipe/edit-recipe.html'
    success_url = reverse_lazy('recipe_catalogue')
    pk_url_kwarg = 'recipe_id'


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe/delete-recipe.html'
    success_url = reverse_lazy('recipe_catalogue')
    pk_url_kwarg = 'recipe_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeDeleteForm(instance=self.object)

        return context
