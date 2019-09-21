from django.contrib import admin
from .models import Emprendimiento, Categoria


# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class EmprendimientoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'post_categories')
    search_fields = ('name', 'categories__name') # author__username, categories__name
    list_filter = ('categories__name',)

    def post_categories(self, obj):
        return ", ".join([ c.name for c in obj.categories.all() ])

admin.site.register( Categoria, CategoriaAdmin )
admin.site.register( Emprendimiento, EmprendimientoAdmin )