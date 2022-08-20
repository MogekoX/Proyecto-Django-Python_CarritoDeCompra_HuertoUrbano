from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ComentarioForm

from datetime import date
# Create your views here.
def cerrar_sesion(request):
    if request.user is not None:
        logout(request)
    return HttpResponseRedirect(reverse('logn'))

def registar_usuario(request):
    if request.method == 'GET':
        return render(request,'base/registrar.html')
    elif request.method == 'POST':
        contexto = {}
        # username Nombre usuario ( unico ) **
        # email correo **
        # password contraseña **
        # <input name="nombre_usuario">
        # POST
        nombre_usuario = request.POST.get('nombre_usuario',False)
        contrasenia = request.POST.get('contrasenia',False)
        email = request.POST['email']
        # Objeto User, Bool
        usuario_creado, se_creo = User.objects.get_or_create(
            username = nombre_usuario, 
            password = contrasenia,
            email = email
        )
        if se_creo:
            usuario_creado.set_password(contrasenia) # Importante!!!
            usuario_creado.save() # Se guarda en la base de datos
            return HttpResponseRedirect(reverse('logn'))
        contexto['nombre_usuario'] = nombre_usuario
        contexto['email'] = email
        contexto['mensaje'] = 'Usuario o Correo, ya registrados :('
        return render(request, 'base/registrar.html', contexto)

    

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'base/logn.html')
    elif request.method == 'POST':
        contexto = {}
        nombre_usuario = request.POST['nombre_usuario']
        contrasenia = request.POST['contrasenia']
        usuario_encontrado = authenticate( 
            username = nombre_usuario,
            password = contrasenia
        )
        if usuario_encontrado is not None:
            login(request, usuario_encontrado)
            return HttpResponseRedirect(reverse('pagina_segura'))
        contexto['mensaje'] = 'Usuario y contraseña no coinciden....'
        return render(request, 'base/logn.html', contexto)
    
def home(request):
    return render(request,'base/home.html')

def index(request):
    return render(request,'base/index.html')


def seguimiento(request):
    return render(request,'base/seguimiento.html')




def producto(request):
    return render(request,'base/producto.html')



def macetero(request):
    return render(request,'base/macetero.html')

def otro(request):
    return render(request,'base/otro.html')

@login_required()
def pagina_segura(request):
    return render(request,'base/pagina_segura.html')

def medioPago(request):
    return render(request,'base/medio_pago.html')

@login_required()
def carrito(request):
    return render(request,'base/carrito.html')



def agregarComentario(request):
    data={
        'hola': ComentarioForm()
    }
    if request.method=='POST':
        formulario=ComentarioForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Comentario Realizado"
        else:
            data["form"]=formulario
    return render(request,'base/index.html',data)
        

def comentario(request):
    return render(request,'base/comentario.html')