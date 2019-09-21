from django.shortcuts import render
from .models import Receta
# Create your views here.

def recetario(request):
    receta = Receta.objects.all()
    return render(request, 'recetas/recetario.html', {'receta': receta})