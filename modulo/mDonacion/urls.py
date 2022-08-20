from django.urls import path
from .views import donarDinero,listarDonacion

redstone2=[
    path('donarDinero',donarDinero,name='donarDinero')
    
]

urlpatterns3 = [
    path('listarDonacion',listarDonacion,name='listarDonacion')
]
