from django.contrib import admin
from services.models import service

class servicesadmin(admin.ModelAdmin):
    list_display = ('service_blogt','service_blogc')

admin.site.register(service,servicesadmin)
# Register your models here.
