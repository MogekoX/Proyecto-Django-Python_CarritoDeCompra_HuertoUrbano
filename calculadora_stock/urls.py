"""programaEjemplo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import global_settings as settings 
from django.conf.urls import static
from modulo.mProducto.urls import productoUrls,cateogiraUrls
from modulo.mProducto.urls import urlpatterns
from modulo.mStock.urls import urlpatterns as urlStock
from modulo.mHistorial.urls import urlpatterns as urlHistorial
from modulo.mCliente.urls import redstone
from modulo.mDonacion.urls import redstone2
from modulo.mDonacion.urls import urlpatterns3
from modulo.mCarrito.ulrs import carritoUrls
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('', include(urlpatterns)),
    path('', include(urlHistorial)),
    path('', include(productoUrls)),
    path('',include(carritoUrls)),
    path('categoria/', include(cateogiraUrls)),
    path('stock/', include(urlStock)),
    path('', include(redstone)),
    path('', include(redstone2)),
    path('admin/',admin.site.urls),
    path('listar_donaciones',include(urlpatterns3)),

    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

