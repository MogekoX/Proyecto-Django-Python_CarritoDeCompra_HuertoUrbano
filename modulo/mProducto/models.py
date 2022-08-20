from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator

# Create your models here.
class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=45, unique=True,verbose_name="Nombre de Categoria",validators=[MaxLengthValidator(45),MinLengthValidator(5)])
    detalleCategoria = models.TextField(max_length=150,verbose_name="Detalle Categoría",validators=[MaxLengthValidator(100),MinLengthValidator(5)])
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=45,verbose_name="Nombre de Producto",validators=[MaxLengthValidator(45),MinLengthValidator(5)])
    imagenProducto = models.ImageField(upload_to='productos/',null=True,verbose_name="Asignar Imagen")
    stockProducto = models.PositiveSmallIntegerField(null=True,verbose_name="Disponibilidad de Producto")
    precioProducto = models.PositiveSmallIntegerField(verbose_name="Precio de Producto") # 9
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,verbose_name="Asignar Categoría")
    def __str__(self):
        return self.nombreProducto