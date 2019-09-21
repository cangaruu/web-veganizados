from django.contrib import admin
from .models import SobreMi

# Register your models here.

class SobreMiAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(SobreMi, SobreMiAdmin)
