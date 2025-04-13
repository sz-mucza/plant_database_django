from django.contrib import admin
from .models import PlantType, Plant

# Register your models here.
admin.site.register(Plant)
admin.site.register(PlantType)