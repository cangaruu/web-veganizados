from django.shortcuts import render, get_list_or_404
from .models import Emprendimiento, Categoria
# Create your views here.

def emprendimientos(request):
    #amigos = Emprendimiento.objects.all()
    amigos = get_list_or_404( Categoria )
    return render(request, 'emprendimientos/emprendimientos.html', {'amigos': amigos})