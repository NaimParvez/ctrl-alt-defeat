from django.shortcuts import render
from members.views import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

# def dir_login(request):
#     return render(request, 'authentication/login.html')