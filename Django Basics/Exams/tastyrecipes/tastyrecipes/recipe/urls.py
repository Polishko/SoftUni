from django.urls import path, include

from tastyrecipes.recipe.views import RecipeListView, RecipeCreateView, RecipeDetailView, RecipeEditView, \
    RecipeDeleteView

urlpatterns = [
    path('catalogue/', RecipeListView.as_view(), name='recipe_catalogue'),
    path('create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('<int:recipe_id>/', include([
       path('details/', RecipeDetailView.as_view(), name='recipe_details'),
       path('edit/', RecipeEditView.as_view(), name='recipe_edit'),
       path('delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    ])),
]
