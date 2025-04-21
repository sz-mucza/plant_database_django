from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from plant_view.models import Plant, PlantType

# PLANT RELATED VIEWS
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        plant_list = Plant.objects.all()

        context = {
            'plant_list': plant_list,
        }
        return render(request, 'plant_view/plant_list.html', context)
    

class PlantCreate(LoginRequiredMixin, CreateView):
    # CreateView basically does the same things as above:
    model = Plant
    fields = "__all__"
    success_url = reverse_lazy("plant_view:all")

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = "__all__"
    success_url = reverse_lazy("plant_view:all")

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    fields = "__all__"
    success_url = reverse_lazy("plant_view:all")


# PLANT TYPE RELATED VIEWS
class PlantTypeListView(LoginRequiredMixin, View):
    def get(self, request):
        planttype_list = PlantType.objects.all()

        context = {
            'planttype_list': planttype_list,
        }
        return render(request, 'plant_view/planttype_list.html', context)
    
class PlantTypeDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        current_plant_type = get_object_or_404(PlantType, id=pk)
        plant_count = Plant.objects.all().filter(plant_type=current_plant_type).count()

        context = {
            'planttype': current_plant_type,
            'plantcount': plant_count,
        }
        return render(request, 'plant_view/planttype_detail.html', context)
    
class PlantTypeCreate(LoginRequiredMixin, CreateView):
    # CreateView basically does the same things as above:
    model = PlantType
    fields = "__all__"
    success_url = reverse_lazy("plant_view:planttype_list")

class PlantTypeUpdate(LoginRequiredMixin, UpdateView):
    model = PlantType
    fields = "__all__"
    success_url = reverse_lazy("plant_view:planttype_list")

class PlantTypeDelete(LoginRequiredMixin, DeleteView):
    model = PlantType
    fields = "__all__"
    success_url = reverse_lazy("plant_view:planttype_list")