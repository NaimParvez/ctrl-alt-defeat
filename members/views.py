from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['user_email']
        password = request.POST['user_password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.info(request, 'Logged in successfully')
            return redirect('landing')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')
    else:    
        return render(request, 'registration/login.html',{})
    

# def logout_view(request):
#     logout(request)
#     messages.info(request, 'Logged out successfully')
#     return redirect('home')
    
def register(request):
    return render(request, 'registration/register.html',{})