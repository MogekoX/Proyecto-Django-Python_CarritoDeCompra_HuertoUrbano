from multiprocessing import context
from django.shortcuts import render
from .models import Donaciones
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import DonacionForm


# Create your views here.


def donarDinero(request):
    data={
        'formu': DonacionForm()
        
    }
    if request.method=='POST':
        formulario = DonacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Estamos Procesando tu Donación"
    return render(request,'donaciones/donarDinero.html',data)



def listarDonacion(request):
    donaciones=Donaciones.objects.all()
    contexto={
        'donaciones':donaciones
    }
    return render(request,'donaciones/listar_donaciones.html',contexto)