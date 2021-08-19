from django.contrib import admin
from mainapp.models import Profile, BatteryWarranty

# Register your models here.

admin.site.register(BatteryWarranty)
admin.site.register(Profile)