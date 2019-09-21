from django.urls import path
from . import views


urlpatterns = [
    path('', views.recetario, name="recetario"),
]