# from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormMixin

from musicapp.album.models import Album
from musicapp.userprofile.forms import AddUserProfile
# from musicapp.userprofile.models import Profile
from musicapp.utils import get_user_object


# This view is based on the only one profile solution:
class HomePageView(FormMixin, ListView):
    model = Album
    form_class = AddUserProfile
    success_url = reverse_lazy('home-page')

    @property
    def profile(self):
        return get_user_object()

    def get_queryset(self):
        if self.profile:
            return Album.objects.filter(owner=self.profile)
        return Album.objects.none()

    def get_template_names(self):

        if self.profile:
            return ['common/home-with-profile.html']
        return ['common/home-no-profile.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.profile:
            context['form'] = self.get_form()

        return context

    # manually handling post as in FBVs (not provided by ListView or FormMixin)
    # Alternative: combine ListView with BaseFormView to simplify logic and avoid overriding many methods;
    # this will combine 2 views though.
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        return self.render_to_response(self.get_context_data(form=form))


# alternative: using a template view and the session storage approach (the template view was not recommended,
# but I find template more logical, because our view's purpose is to conditionally render two different templates
# and the outcome of one of the conditions is not a list but a form. i.e. we have two different views as an outcome)

# class HomePageView(FormMixin, TemplateView):
#     form_class = AddUserProfile
#     template_name = 'common/home-no-profile.html'
#     success_url = '/'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         if self.request.session.get('has_profile'):
#             context['form'] = self.get_form()
#             profile_id = self.request.session.get('profile_id')
#
#             if not profile_id:
#                 raise Http404('Profile not found. The session may have expired.')
#
#             profile = get_object_or_404(Profile, pk=profile_id)
#             albums = profile.albums.all()
#             context['albums'] = albums
#
#         return context
#
#     def get_template_names(self):
#         if self.request.session.get('has_profile'):
#             return ['common/home-with-profile.html']
#         else:
#             return self.template_name
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#
#         if form.is_valid():
#             profile = form.save()
#             self.request.session['has_profile'] = True
#             self.request.session['profile_id'] = profile.pk
#
#             return redirect(self.success_url)
#
#         return self.form_invalid(form)
#
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=form))

