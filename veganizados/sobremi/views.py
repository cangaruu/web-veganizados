from django.shortcuts import render, HttpResponse
from .models import SobreMi
# Create your views here.

def autora(request):
    sobremi = SobreMi.objects.all()
    return render(request, 'sobremi/autora.html', {'sobremi':sobremi})