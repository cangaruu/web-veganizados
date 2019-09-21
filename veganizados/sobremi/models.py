from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class SobreMi(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo. Ej: 'Sobre Mí'")
    content = RichTextField( verbose_name="Contenido")
    image = models.ImageField( verbose_name="Imagen", upload_to="img_sobremi", null=True, blank=True )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Momento de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Momento de edicion")
    
    class Meta:
        verbose_name = "Sobre mi"

    def __str__(self):
        return self.title
