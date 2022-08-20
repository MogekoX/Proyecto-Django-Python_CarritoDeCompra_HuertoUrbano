from django.contrib import admin
from modulo.mCarrito.models import CarritoProducto, Compra

# Register your models here.
admin.site.register(Compra)
admin.site.register(CarritoProducto)