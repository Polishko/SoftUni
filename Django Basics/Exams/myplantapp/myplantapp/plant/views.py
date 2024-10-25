from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView

from myplantapp.plant.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from myplantapp.plant.models import Plant
from myplantapp.utils import get_user_object


class PlantListView(ListView):
    model = Plant
    context_object_name = 'plants'
    template_name = 'plant/catalogue.html'


class PlantCreateView(CreateView):
    model = Plant
    form_class = PlantCreateForm
    pk_url_kwarg = 'plant_id'
    template_name = 'plant/create-plant.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        plant = form.save(commit=False)
        plant.owner = get_user_object()
        plant.save()

        return super().form_valid(form)


class PlantDetailView(DetailView):
    model = Plant
    pk_url_kwarg = 'plant_id'
    template_name = 'plant/plant-details.html'


class PlantEditView(UpdateView):
    model = Plant
    form_class = PlantEditForm
    pk_url_kwarg = 'plant_id'
    template_name = 'plant/edit-plant.html'
    success_url = reverse_lazy('catalogue')


class PlantDeleteView(DeleteView):
    model = Plant
    pk_url_kwarg = 'plant_id'
    template_name = 'plant/delete-plant.html'
    success_url = reverse_lazy('catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PlantDeleteForm(instance=self.object)

        return context
