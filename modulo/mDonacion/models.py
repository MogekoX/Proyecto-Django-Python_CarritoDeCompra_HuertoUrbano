
from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator,EmailValidator 

# Create your models here.

class Donaciones(models.Model):
    nombre=models.CharField(max_length=50,verbose_name="Nombre",validators=[MaxLengthValidator(50),MinLengthValidator(5)])
    apellido=models.CharField(max_length=50,verbose_name="Apellido",validators=[MaxLengthValidator(50),MinLengthValidator(5)])
    correo=models.EmailField(validators=[EmailValidator])
    direccion=models.TextField(validators=[MaxLengthValidator(50),MinLengthValidator(10)])
    numeroTarjeta=models.PositiveBigIntegerField()
    
    monto=models.PositiveSmallIntegerField()
    def __str__(self):
        return self.nombre