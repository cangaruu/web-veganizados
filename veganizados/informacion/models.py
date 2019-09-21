from django.db import models
from ckeditor.fields import RichTextField
from emprendimientos.models import Categoria

# Create your models here.

class Informacion(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = RichTextField( verbose_name="Contenido", null=True, blank=True )
    image = models.ImageField( verbose_name="Imagen", upload_to="img_emprendimientos", null=True, blank=True)
    categories = models.ManyToManyField( Categoria, verbose_name="Categorias", related_name="get_post") # Clashea con emprendimientos, solo quite la 's'
    url = models.URLField(verbose_name="Enlace o Iframe", max_length=500, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Momento de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Momento de edicion")
    
    class Meta:
        verbose_name = "Informacion"
        verbose_name_plural = "Informacion"
        ordering = ['-created']

    def __str__(self):
        return self.title