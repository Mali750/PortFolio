from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='Home'),
    path('thank-you/', views.Submission, name='submission'),
    path('contact/', views .contact_function, name='Contact'),
    path('form-data/', views.form_view, name='form-data'),
    path('login/', views.login_view, name='login'),
    path('delete/', views.delete_dashboard, name='delete_dashboard'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
]
