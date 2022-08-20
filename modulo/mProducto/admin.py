from django.contrib import admin
from modulo.mProducto.models import Categoria
from modulo.mProducto.models import Producto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)