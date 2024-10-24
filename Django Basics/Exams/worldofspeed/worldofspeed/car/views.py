from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from worldofspeed.car.forms import CarCreateForm, CarEditForm, CarDeleteForm
from worldofspeed.car.models import Car
from worldofspeed.utils import get_user_object


class CarListView(ListView):
    model = Car
    template_name = 'common/catalogue.html'
    context_object_name = 'cars'


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('car-catalogue')

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = get_user_object()
        car.save()

        return super().form_valid(form)


class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car-details.html'
    pk_url_kwarg = 'id'


class CarEditView(UpdateView):
    model = Car
    form_class = CarEditForm
    template_name = 'car/car-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('car-catalogue')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/car-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('car-catalogue')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CarDeleteForm(instance=self.object)

        return context
