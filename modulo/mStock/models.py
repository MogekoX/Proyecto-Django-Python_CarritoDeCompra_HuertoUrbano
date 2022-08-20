from django.db import models
from modulo.mProducto.models import Producto
# Create your models here.

class Movimiento(models.Model):
    detalleMovimiento = models.CharField(max_length=50, unique=True)
    estado =  models.PositiveSmallIntegerField(default=1)

class Historial(models.Model):
    fecha = models.DateField(auto_now=True)
    cantidad = models.PositiveSmallIntegerField()
    idMovimiento = models.ForeignKey(Movimiento, on_delete=models.DO_NOTHING)
    idProducto = models.ForeignKey(Producto, on_delete= models.DO_NOTHING)