from django.urls import path
from .views import total,entrada,salida,nuevaEntrada, nuevaSalida
urlpatterns = [
    path('total/', total, name='total'),
    path('entrada/', entrada, name='entrada'),
    path('salida/', salida, name='salida'),
    path('nueva-entrada/', nuevaEntrada, name='nuevaEntrada'),
    path('nueva-salida/', nuevaSalida, name='nuevaSalida')
]