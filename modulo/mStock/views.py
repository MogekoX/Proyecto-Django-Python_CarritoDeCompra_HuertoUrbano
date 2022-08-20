from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Movimiento, Historial
from modulo.mProducto.models import Producto
# Create your views here.
def total(request):
    return render(request, 'stock/total.html')
def entrada(request):
    entradas = Historial.objects.filter(
        idMovimiento__detalleMovimiento = "Entrada"
    )
    contexto = {
        'entradas': entradas
    }
    return render(request, 'stock/entrada.html', contexto)
def salida(request):
    return render(request, 'stock/salida.html')
def nuevaEntrada(request):
    movimientoEntrada = Movimiento.objects.get(detalleMovimiento = 'Entrada')
    if request.method == 'GET':
        productos = Producto.objects.all()
        contexto = {
            'productos': productos
        }
        return render(request, 'stock/nueva-entrada.html', contexto)
    elif request.method == 'POST':
        producto = Producto.objects.get(id = request.POST['idProducto'])
        cantidad = int(request.POST['cantidad'])
        nuevaEntrada = Historial()
        nuevaEntrada.cantidad = cantidad
        nuevaEntrada.idProducto = producto
        nuevaEntrada.idMovimiento = movimientoEntrada
        nuevaEntrada.save()
        return HttpResponseRedirect(reverse('entrada'))
def nuevaSalida(request):

    return render(request, 'stock/nueva-entrada.html')
