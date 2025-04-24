from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "plant_view" # applicaition namespace
urlpatterns = [
        # Plant list, plant related urls:
        path('', views.MainView.as_view(), name='all'),
        path('main/myplants/', views.MyPlantsView.as_view(), name='plant_myplants'),
        path('main/create/', views.PlantCreateView.as_view(), name='plant_create'),
        path('main/<int:pk>/', views.PlantDetailView.as_view(), name='plant_detail'),
        path('main/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant_update'),
        path('main/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant_delete'),

        # Plant type related urls:
        path('ptview', views.PlantTypeListView.as_view(), name='planttype_list'),
        path('ptview/<int:pk>/', views.PlantTypeDetailView.as_view(), name='planttype_detail'),
        path('ptview/create/', views.PlantTypeCreate.as_view(), name='planttype_create'),
        path('ptview/<int:pk>/update/', views.PlantTypeUpdate.as_view(), name='planttype_update'),
        path('ptview/<int:pk>/delete/', views.PlantTypeDelete.as_view(), name='planttype_delete'),

        # Plant timeline related urls:
        path('main/<int:pk>/createevent/', views.PlantEventCreateView.as_view() , name='plantevent_create'),
        # path('ptevent/<int:pk>/update/', , name='planteventupdate'),
        # path('ptevent/<int:pk>/delete/', , name='plantevent_delete'),
    ]