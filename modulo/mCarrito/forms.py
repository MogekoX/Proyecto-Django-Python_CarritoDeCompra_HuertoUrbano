from socket import fromshare
from django import forms
from .models import CarritoProducto

class FormCarrito(forms.ModelForm):
    class Meta:
        model = CarritoProducto
        fields = '__all__'
        exclude = None
        widgets ={
            "nombreProducto": forms.TextInput(
                attrs={
                    "class":"form-control",
                }
            ),
            "precioProducto": forms.NumberInput(
                attrs={
                    "class":"form-control"
                }
            ),
            "imagenProducto": forms.FileInput(
                attrs={
                    "class":"form-control"
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "class":"+1"
                }
            ),
            "descuento": forms.NumberInput(
                attrs={
                    "class":"form-control"
                }
            ),
            "fecha": forms.DateInput(
                attrs={
                    "class":"forms-control"
                }
            )
        }