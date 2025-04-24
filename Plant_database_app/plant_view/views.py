import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from plant_view.models import Plant, PlantType, DurationPlantEvent
from plant_view.forms import PlantCreateForm, DurationPlantEventCreateForm


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# PLANT RELATED VIEWS
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        plant_list = Plant.objects.all()
        plant_type_list = PlantType.objects.all()

        context = {
            'plant_list': plant_list,
            'plant_type_list': plant_type_list,
        }
        return render(request, 'plant_view/plant_list.html', context)
    
class MyPlantsView(LoginRequiredMixin, View):
    def get(self, request):
        plant_list = Plant.objects.all().filter(user=self.request.user)

        context = {
            'plant_list': plant_list,
        }
        return render(request, 'plant_view/my_plant_list.html', context)
    
class PlantDetailView(LoginRequiredMixin, DeleteView):
    def get(self, request, pk):
        current_plant = get_object_or_404(Plant, id=pk)
        plant_timeline = DurationPlantEvent.objects.filter(plant=current_plant)
        event_form = DurationPlantEventCreateForm()
        context = {
            'plant': current_plant,
            'plant_timeline': plant_timeline,
            'event_form': event_form,
        }
        return render(request, 'plant_view/plant_detail.html', context)
    

class PlantCreateView(LoginRequiredMixin, View):
    success_url = reverse_lazy("plant_view:all")
    template_name = 'plant_view/plant_form.html'

    def get(self, request, pk=None):
        logging.info("Plant create form GET called")
        log.info("")
        form = PlantCreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)
    
    def post(self, request, pk=None):
        logging.info("Plant create form POST called")
        form = PlantCreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            logging.info("Plant create form is not valid, return.")
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        plant = form.save(commit=False)
        plant.user = self.request.user
        plant.save()
        logging.info("Plant create form POST done, to be redirected...")
        return redirect(self.success_url)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy("plant_view:all")
    template_name = 'plant_view/plant_form.html'

    def get(self, request, pk=None):
        plant = get_object_or_404(Plant, id=pk, user=self.request.user)
        form = PlantCreateForm(instance=plant)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)
    
    def post(self, request, pk=None):
        plant = get_object_or_404(Plant, id=pk, user=self.request.user)
        form = PlantCreateForm(request.POST, request.FILES or None, instance=plant)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        plant = form.save(commit=False)
        plant.save()
        return redirect(self.success_url)


class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    fields = "__all__"
    success_url = reverse_lazy("plant_view:all")

    def get_queryset(self):
        qs = super(DeleteView, self).get_queryset()
        return qs.filter(user=self.request.user)


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


# PLANT EVENT, TIMELINE RELATED VIEWS:
class PlantEventCreateView(LoginRequiredMixin, View):
    
    def post(self, request, pk):
        p = get_object_or_404(Plant, id=pk)

        print("DEBUG:", pk, p)
        print(request.POST)
        plant_event = DurationPlantEvent(
            title=request.POST['title'],
            description=request.POST['description'],
            plant=p,
            author=request.user,
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            event_type=request.POST['end_date'],
            )
        plant_event.save()
        return redirect(reverse('plant_view:plant_detail', args=[pk]))