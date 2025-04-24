from django import forms

from .models import Plant, DurationPlantEvent

class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'plant_type']

class DurationPlantEventCreateForm(forms.ModelForm):
    class Meta:
        model = DurationPlantEvent
        fields = ['title', 'description', 'start_date', 'end_date', 'event_type']