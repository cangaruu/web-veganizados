from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre de categoria")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Momento de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Momento de edicion")
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name

class Emprendimiento(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre de Emprendimiento")
    content = RichTextField( verbose_name="Contenido", null=True, blank=True )
    image = models.ImageField( verbose_name="Imagen", upload_to="img_emprendimientos", null=True, blank=True)
    categories = models.ManyToManyField( Categoria, verbose_name="Categorias", related_name="get_posts") # related_to=getposts
    url = models.URLField(verbose_name="Enlace", max_length=400, null=True, blank=True)
    url_iframe = models.URLField(verbose_name="Enlace Iframe", max_length=400, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Momento de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Momento de edicion")
    
    class Meta:
        verbose_name = "Emprendimiento"
        verbose_name_plural = "Emprendimientos"
        ordering = ['-created']

    def __str__(self):
        return self.name

