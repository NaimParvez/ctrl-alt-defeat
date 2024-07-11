from django.urls import path
from . import views

app_name = 'members'  # This is important for namespacing

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='registration'),
    # path('home/', views.logout_view, name='logout'),
    
    # other URL patterns...
]