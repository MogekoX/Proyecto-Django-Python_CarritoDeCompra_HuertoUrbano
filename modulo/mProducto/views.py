
from msilib.schema import Shortcut
from multiprocessing import context
from webbrowser import get
from .models import Producto
from .models import Categoria
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.utils import DataError
from django.http import HttpResponseRedirect
from django.shortcuts import  redirect,render,get_list_or_404,get_object_or_404
from .forms import ProductoForm


# Create your views here.




def borrar(request, idProducto):
    try:
        productoEncontrado = Producto.objects.get(id = idProducto)
    except Producto.DoesNotExist:
        return HttpResponseRedirect(reverse('listarProducto'))
    if request.method == 'GET':
        contexto = {
            'producto': productoEncontrado
        }
        return render(request, 'producto/borrar.html', contexto)
    elif request.method == 'POST':
        productoEncontrado.delete()
        return HttpResponseRedirect(reverse('listarProducto'))
    return render(request,'producto/borrar.html')

def listarCategoria(request):
    categorias  = Categoria.objects.all()
    contexto = {
        'categorias': categorias 
    }
    return render(request, 'categoria/listar.html', contexto)

def agregarCategoria(request):
    # En caso de entrar por metodo GET
    if request.method == 'GET':
        return render(request, 'categoria/agregar.html')
    elif request.method == 'POST':
        nuevaCategoria = Categoria()
        nuevaCategoria.nombreCategoria = request.POST['nombreCategoria']
        nuevaCategoria.detalleCategoria = request.POST['detalleCategoria']
        nuevaCategoria.save()
        return HttpResponseRedirect(reverse('listarCategoria'))

def borrarCategoria(request,idCategoria):
    # Select * from categoria where id = $
    try:
        categoriaEntrada = Categoria.objects.get(id=idCategoria)
    except Categoria.DoesNotExist:
        return HttpResponseRedirect(reverse('listarCategoria'))
    if request.method == 'GET':
        contexto = {
            'categoria': categoriaEntrada
        }
        return render(request,'categoria/borrar.html', contexto)
    elif request.method == 'POST':
        categoriaEntrada.delete()
        ## Que pasa si no esta? c: Q.Q
        return HttpResponseRedirect(reverse('listarCategoria'))

def modificarCategoria(request,idCategoria):
    try:
        categoriaEntrada = Categoria.objects.get(id=idCategoria)
    except Categoria.DoesNotExist:
        return HttpResponseRedirect(reverse('listarCategoria'))
    if request.method == 'GET':
        contexto = {
            'categoria': categoriaEntrada
        }
        return render(request, 'categoria/modificar.html', contexto)
    elif request.method == 'POST':
        categoriaEntrada.nombreCategoria = request.POST['nombreCategoria']
        categoriaEntrada.detalleCategoria = request.POST['detalleCategoria']
        
        categoriaEntrada.save()
        return HttpResponseRedirect(reverse('listarCategoria'))
    
def planta(request):
    productos = Producto.objects.all()
   
    contexto= {
        'productos': productos,

        
    }
    return render(request,'base/planta.html',contexto)




def agregar_productos(request):
    contexto={
        'form': ProductoForm()
    }
    if request.method== 'POST':
        formulario= ProductoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            contexto["mensaje"]= "guardado correctamente"
        else:
            contexto["form"] = formulario
    return render(request,'producto/agregar_productos.html',contexto)

def listar_productos(request):
    productos = Producto.objects.all()
    contexto={
        'productos': productos
    }
    return render (request,'producto/listar_productos.html',contexto)

def modificar_productos(request,idProducto):
    
    producto= get_object_or_404(Producto,id = idProducto)
    
    contexto={
        'form': ProductoForm(instance=producto)
        
    }
    producto.save()
    return render(request,'producto/modificar_productos.html',contexto)

def eliminar_productos(request,idProducto):
    producto = get_object_or_404(Producto, id=idProducto)
    
    producto.delete()
    return redirect(to= "listar_productos")

#-----------------------------------------------------------#

