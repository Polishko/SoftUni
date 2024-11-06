from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(ModelAdmin):
    list_display = ['username', 'email',]
