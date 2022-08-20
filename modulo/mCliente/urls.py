from django.urls import path
from .views import cerrar_sesion, registar_usuario, iniciar_sesion,home,index,seguimiento,producto,macetero,otro,pagina_segura,medioPago,carrito,comentario

redstone = [
    path('logn', iniciar_sesion, name='logn'),
    path('registrar/', registar_usuario, name='registrar_usuario'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('home/',home,name='home'),
    path('index',index,name='index'),
    path('carrito',carrito,name='carrito'),
    path('seguimiento',seguimiento,name='seguimiento'),
    path('comentario',comentario,name='comentario'),
    path('producto',producto,name='producto'),   
    path('macetero',macetero,name='macetero'),
    path('otro',otro,name='otro'),
    path('pagina_segura',pagina_segura,name='pagina_segura'),
    path('medio_pago',medioPago,name='medio_pago'),
]

