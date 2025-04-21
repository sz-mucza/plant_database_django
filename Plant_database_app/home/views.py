from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.contrib.auth.forms import *
from django.contrib.auth import login

from .forms import RegistrationForm

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations
class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'home/main.html', context)

class SignUpView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'home/register.html', { 'form': form })
        
    def post(self, request):
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('')
        else:
            return render(request, 'home/register.html', {'form': form})