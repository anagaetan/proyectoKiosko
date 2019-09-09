from django.contrib import admin
from .models import Producto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'precio']
    list_filter = ['codigo', 'nombre']
    search_fields = ['nombre', 'codigo']
    #prepopulated_fields = {'nombre': ('nombre','descripcion',)}

admin.site.register(Producto, ProductoAdmin)