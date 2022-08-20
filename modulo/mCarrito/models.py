from datetime import datetime
from pyexpat import model
from tkinter import CASCADE
from unittest.mock import DEFAULT
from django.db import models
from modulo.mProducto.models import Producto


CATEGORIA_PREPARACION="PRE"
CATEGORIA_ENVIADO="ENV"
CATEGORIA_ENTREGADO="ENT"
CHOICES_CATEGORIA=(
    (CATEGORIA_PREPARACION,"PRODUCTO PREPARADO"),
    (CATEGORIA_ENVIADO,"PRODUCTO ENVIADO"),
    (CATEGORIA_ENTREGADO,"PRODUCTO ENTREGADO"))

class CarritoProducto(models.Model):
    cantidad=models.PositiveSmallIntegerField()
    descuento=models.SmallIntegerField()
    fecha=models.DateField(auto_now=True)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
        
#class Carrito(models.Model):
#    id_productos=models.ForeignKey(CarritoProducto, on_delete=models.CASCADE)
    
class Compra(models.Model):
    estado=models.CharField(
        choices=CHOICES_CATEGORIA,
        max_length=3,
        default=CATEGORIA_PREPARACION
    )
    fecha=models.DateField(auto_now=True)
    id_CarritoProducto=models.ForeignKey(CarritoProducto,on_delete=models.CASCADE)
    

            
    
