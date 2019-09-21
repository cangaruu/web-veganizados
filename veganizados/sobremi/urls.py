from django.urls import path
from . import views


urlpatterns = [
    path('', views.autora, name="autora"),
]