from django.db import models

# Create your models here.


class boleta(models.Model):
    fecha=models.DateField()
    precio=models.PositiveSmallIntegerField()
    cantidad=models.PositiveSmallIntegerField()
    total=models.PositiveSmallIntegerField()
    descuento=models.PositiveSmallIntegerField()
    nombreProducto=models.TextField()
    
    