
from django import forms 
from .models import  Donaciones

class DonacionForm(forms.ModelForm):
    
    class Meta:
        model = Donaciones
        fields='__all__'