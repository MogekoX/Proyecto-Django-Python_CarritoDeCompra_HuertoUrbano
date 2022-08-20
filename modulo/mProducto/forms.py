from dataclasses import fields
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model= Producto
        fields= '__all__'
        widgets={
            "nombreProducto": forms.TextInput(
                attrs={
                    "class":"form-control"                 
                }
            ),
            "idCategoria": forms.Select(
                attrs={
                    "class":"form-control"
                }
            ),
            "imagenProducto": forms.ClearableFileInput(
                attrs={
                    "class":"form-control"
                }
            ),
            "stockProducto": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "precioProducto": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),
            
        }

