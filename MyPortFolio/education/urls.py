from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.skill_function, name='Skill')
]
