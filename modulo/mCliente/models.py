
import email
from pyexpat import model
from django.db import models



# Create your models here.

    
class Comentario(models.Model):  
    comentario=models.CharField(max_length=100)
    
        

class Direccion(models.Model):
    descripcion=models.TimeField() 