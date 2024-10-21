from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from musicapp.userprofile.models import Profile


class UserDetails(DetailView):
    model = Profile
    template_name = 'userprofile/profile-details.html'

    def get_object(self, queryset=None):
        profile_pk = self.request.session.get('profile_id')

        if profile_pk is None:
            raise Http404("Profile not found. The session may have expired.")

        return get_object_or_404(Profile, pk=profile_pk)




# FBVs
def profile_details(request):
    profile_pk = request.session.get('profile_id')

    if profile_pk is None:
        raise Http404("Profile not found. The session may have expired.")

    profile = get_object_or_404(Profile, pk=profile_pk)

    return render(request, 'userprofile/profile-details.html', {'profile': profile})

def profile_delete(request):
    context = {}
    return render(request, 'userprofile/profile-details.html', context)


