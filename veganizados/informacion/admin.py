from django.contrib import admin
from .models import Informacion

# Register your models here.

class InformacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'post_categories')
    search_fields = ('title', 'categories__name') # author__username, categories__name
    list_filter = ('categories__name',)

    def post_categories(self, obj):
        return ", ".join([ c.name for c in obj.categories.all() ])

admin.site.register( Informacion, InformacionAdmin )

