from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from forumApp.accounts.forms import CustomUserForm, CustomUserChangeForm

UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    add_form = CustomUserForm
    form = CustomUserChangeForm

    list_display = ['username', 'email',]

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
            },
        ),
    )

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',),}),
    )

    filter_horizontal = ('groups', 'user_permissions')
