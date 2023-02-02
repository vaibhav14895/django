from django.contrib import admin
from app.models import forms


class servicesadmin(admin.ModelAdmin):
    list_display = ('s_name','s_roll','s_sec','s_CGPA')


admin.site.register(forms, servicesadmin)
# Register your models here.
