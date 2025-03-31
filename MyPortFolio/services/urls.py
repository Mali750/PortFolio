from django.urls import path 
from . import views

urlpatterns = [
    path('services/', views.service_function, name='Services')
]