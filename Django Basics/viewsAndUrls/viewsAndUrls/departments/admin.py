from django.contrib import admin

from viewsAndUrls.departments.models import Department


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass