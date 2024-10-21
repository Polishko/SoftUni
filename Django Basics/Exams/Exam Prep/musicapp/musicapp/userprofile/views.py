from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from musicapp.userprofile.models import Profile


class ProfileDetails(DetailView):
    model = Profile
    template_name = 'userprofile/profile-details.html'

    def get_object(self, queryset=None):
        profile_pk = self.request.session.get('profile_id')

        if profile_pk is None:
            raise Http404("Profile not found. The session may have expired.")

        return get_object_or_404(Profile, pk=profile_pk)


class ProfileDelete(DeleteView):
    model = Profile
    template_name = 'userprofile/profile-delete.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        profile_pk = self.request.session.get('profile_id')

        if profile_pk is None:
            raise Http404("Profile not found. The session may have expired.")

        return get_object_or_404(Profile, pk=profile_pk)

    def post(self, request, *args, **kwargs):
        response =  super().post(request, *args, **kwargs)
        self.request.session.pop('profile_id', None)
        self.request.session.pop('has_profile', None)

        return response

# FBVs
# def profile_details(request):
#     profile_pk = request.session.get('profile_id')
#
#     if profile_pk is None:
#         raise Http404("Profile not found. The session may have expired.")
#
#     profile = get_object_or_404(Profile, pk=profile_pk)
#
#     return render(request, 'userprofile/profile-details.html', {'profile': profile})
#
# def profile_delete(request):
#     profile_pk = request.session.get('profile_id')
#
#     if profile_pk is None:
#         raise Http404("Profile not found. The session may have expired.")
#
#     profile =  get_object_or_404(Profile, pk=profile_pk)
#
#     if request.method == 'POST':
#         profile.delete()
#         request.session.pop('profile_id', None)
#         request.session.pop('has_profile', None)
#         return redirect('home-page')
#
#     return render(request, 'userprofile/profile-delete.html')
