from django.urls import path
from modulo.mProducto.views import planta
from .views import planta


carritoUrls=[
    # path('agregar_producto/',agregar_producto,name='agregar_producto'),
    # path('formcarrito/',formcarrito,name='formcarrito'),  
    path('planta/',planta,name='planta'),         
]

urlpatterns = [
    path('planta/',planta,name='planta'),
]