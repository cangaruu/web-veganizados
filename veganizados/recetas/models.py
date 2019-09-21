from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Receta(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre de Receta")
    content = RichTextField( verbose_name="Contenido", null=True, blank=True )
    imageC = models.ImageField( verbose_name="Imagen Chica", upload_to="img_receta_guardada", null=True, blank=True )
    imageG = models.ImageField( verbose_name="Imagen Grande", upload_to="img_receta_guardada", null=True, blank=True )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Momento de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Momento de edicion")
    
    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Las recetas"
        ordering = ['-created']

    def __str__(self):
        return self.name
