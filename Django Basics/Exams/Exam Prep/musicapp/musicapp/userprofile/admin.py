from django.contrib import admin

from musicapp.userprofile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
