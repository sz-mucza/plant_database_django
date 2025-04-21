from django import forms

from .models import Plant

class PlantCreateForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'plant_type']