from django.urls import path
from .views import listarCategoria,agregarCategoria,borrarCategoria,modificarCategoria,planta,agregar_productos,listar_productos,modificar_productos,eliminar_productos

productoUrls = [
    path('listar_productos/',listar_productos,name='listar_productos'),
    path('agregar_productos/', agregar_productos, name='agregar_productos'),
    path('eliminar_productos/<int:idProducto>', eliminar_productos, name='eliminar_productos'),
    path('modificar_productos/<int:idProducto>', modificar_productos, name='modificar_productos'),    
]
cateogiraUrls = [
    path('', listarCategoria, name='listarCategoria'),
    path('agregar/', agregarCategoria, name='agregarCategoria'),
    path('borrar/<int:idCategoria>', borrarCategoria, name='borrarCategoria'),
    path('modificar/<int:idCategoria>', modificarCategoria, name='modificarCategoria'),
]
urlpatterns = [
    path('planta/',planta,name='planta'),
]
