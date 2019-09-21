from django.shortcuts import render, HttpResponse

# Create your views here.

def conciencia(request):
    return render(request, 'core/conciencia.html')



def foro(request):
    return render(request, 'core/foro.html')

def index(request):
    return render(request, 'core/index.html')



def nutricion(request):
    return render(request, 'core/nutricion.html')
