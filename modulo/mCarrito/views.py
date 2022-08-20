from dataclasses import field
from pickle import GET
from pkgutil import get_data
from pyexpat import model
from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect
from modulo.mCarrito.forms import FormCarrito
from modulo.mCarrito.models import CarritoProducto
from modulo.mProducto.models import Producto

def planta(request):
   productosCarrito=Producto.objects.get(request.user.id)
   contexto={} 
   contexto['formulario']=FormCarrito(instance=productosCarrito)
   formulario=FormCarrito(data=request.GET,files=request.FILES,instance=productosCarrito)
   es_valido=formulario.is_valid()
   if es_valido:
       formulario.save()
       return render(request,'base/planta.html',contexto)

def eliminar_producto(request,producto_id):
    carrito= carrito(request)
    producto=Producto.objects.get(id=producto_id)
    
    carrito.eliminarProducto(producto=producto)
    return redirect("carrito")



def limpiar_producto(request,producto_id):
    carrito= carrito(request)
    carrito.limpiarCarrito()
    return redirect("carrito")

def planta(request):
    productos = Producto.objects.all()
   
    contexto= {
        'productos': productos,        
    }
    return render(request,'base/planta.html',contexto)