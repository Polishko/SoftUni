from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from musicapp.userprofile.forms import AddUserProfile
from musicapp.userprofile.models import Profile


class HomePageView(FormMixin, TemplateView):
    form_class = AddUserProfile
    template_name = 'common/home-no-profile.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        if self.request.session.get('has_profile'):
            context['form'] = self.get_form()
            profile_id = self.request.session.get('profile_id')
            profile = get_object_or_404(Profile, pk=profile_id)
            albums = profile.albums.all()
            context['albums'] = albums

        return context

    def get_template_names(self):
        if self.request.session.get('has_profile'):
            return ['common/home-with-profile.html']
        else:
            return self.template_name

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            profile = form.save()
            self.request.session['has_profile'] = True
            self.request.session['profile_id'] = profile.pk

            return redirect(self.success_url)

        return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

# FBV option
# def show_home(request):
#
#     if not request.session.get('has_profile'):
#         form = AddUserProfile(request.POST or None)
#
#
#         if request.method == 'POST':
#             if form.is_valid():
#                 profile = form.save()
#                 request.session['has_profile'] = True
#                 request.session['profile_id'] = profile.pk
#
#                 return redirect('/')
#
#         return render(request, 'common/home-no-profile.html', {'form': form})
#
#     profile_id = request.session.get('profile_id')
#     profile = get_object_or_404(Profile, pk=profile_id)
#     albums = profile.albums.all()
#
#     return render(request, 'common/home-with-profile.html', {'albums': albums})
