from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contacto(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)   # Datos del cliente
        if contact_form.is_valid(): # Devuelve True si todo es correcto
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            eleccion = request.POST.get('eleccion', '')
            organizacion = request.POST.get('organizacion', '')
            content = request.POST.get('content', '')
            
            # Desarrollo
            subject = "Nuevo mensaje de Veganizados!"
            contenido = "Nombre: {}\nEmail: {}\nVegano o Vegetariano: {}\nOrganizacion: {}\nContenido: {}".format(name, email, eleccion, organizacion, content)
            # Desarrollo
            #print(contenido)
            
            try:
                send_mail(subject, contenido, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
                return redirect(reverse('contacto') + "?ok")
            except:
                return redirect(reverse('contacto') + "?fail")
                

            return redirect(reverse('contacto')+"?ok")
    return render(request, 'contact/contacto.html', {'form':contact_form})
