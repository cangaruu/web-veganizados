from django.shortcuts import render, get_list_or_404
from .models import Informacion
from emprendimientos.models import Categoria

# Create your views here.
def info(request):
    info = get_list_or_404(Categoria)
    return render(request, 'informacion/info.html', {'info':info} )