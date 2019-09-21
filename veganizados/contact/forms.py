from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control',  'placeholder': 'Tu nombre'}
    ), min_length=3, max_length=100)  # min_length, max_length...
    email = forms.EmailField(label="Correo Electronico", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'tu-mail@dominio.com'}
    ), min_length=3, max_length=100)

    OPCIONES = ( ('Vegano', 'Vegano'), ('Transicion', 'En transición al Veganismo'), ('Vegetariano', 'Vegetariano'), ('Ninguno', 'Ninguno'))
    eleccion = forms.ChoiceField(label="¿Sos vegano o vegetariano?" ,required=True, choices=OPCIONES, widget=forms.Select(
        attrs={'class':'form-control'}
        )
    )

    OPCIONES_2= [('S', 'Si'), ('N', 'No')]
    organizacion = forms.ChoiceField(label="Organización", required=True, choices=OPCIONES_2, widget=forms.RadioSelect(attrs={'class':'sin-puntos'}) )

    content = forms.CharField(label="Dejanos un mensaje", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 4, 'placeholder': '...'}
    ), min_length=10, max_length=1000)


