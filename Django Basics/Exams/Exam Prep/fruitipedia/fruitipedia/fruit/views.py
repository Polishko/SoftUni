from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from fruitipedia.fruit.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipedia.fruit.models import Fruit
from fruitipedia.utils import get_user_object


class FruitCreateView(CreateView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'fruit/create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        fruit = form.save(commit=False)
        fruit.owner = get_user_object()
        fruit.save()

        return super().form_valid(form)


class FruitDetailView(DetailView):
    model = Fruit
    pk_url_kwarg = 'fruitId'
    template_name = 'fruit/details-fruit.html'


class FruitEditView(UpdateView):
    model = Fruit
    form_class = FruitEditForm
    pk_url_kwarg = 'fruitId'
    template_name = 'fruit/edit-fruit.html'
    success_url = reverse_lazy('dashboard')

class FruitDeleteView(DeleteView):
    model = Fruit
    pk_url_kwarg = 'fruitId'
    template_name = 'fruit/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FruitDeleteForm(instance=self.object)

        return context
