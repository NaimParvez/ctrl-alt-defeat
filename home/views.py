from django.shortcuts import render
from members.views import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, 'home.html')

def landing_view(request):
    return render(request, 'landing.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('home')