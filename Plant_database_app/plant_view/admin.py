from django.contrib import admin
from .models import PlantType, PlantEvent, Plant

# Register your models here.
admin.site.register(Plant)
admin.site.register(PlantType)
admin.site.register(PlantEvent)