"""tulibroenlinea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tulibroenlinea.views import *

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('inicio2/', inicio2),
    path('registro/', registro),
    path('registro2/', registro2),
    path('usobase/', usobase),
    


    path('moduloRoot/', moduloRoot),

    path('moduloRoot/crearAdmin', moduloRoot_crearAdmin),
    path('moduloRoot/genInforme', moduloRoot_genInforme),



    path('moduloAdmin/', moduloAdmin),

    path('moduloAdmin/Usuario/Crear', moduloAdmin_Usuario_Crear),
    path('moduloAdmin/Usuario/Crear2', moduloAdmin_Usuario_Crear2),
    path('moduloAdmin/Usuario/Modificar', moduloAdmin_Usuario_Modificar),
    path('moduloAdmin/Usuario/Modificar2', moduloAdmin_Usuario_Modificar2),
    path('moduloAdmin/Usuario/Modificar3', moduloAdmin_Usuario_Modificar3),
    path('moduloAdmin/Usuario/Listar', moduloAdmin_Usuario_Listar),
    path('moduloAdmin/Usuario/Buscar', moduloAdmin_Usuario_Buscar),
    path('moduloAdmin/Usuario/Buscar2', moduloAdmin_Usuario_Buscar2),
    path('moduloAdmin/Usuario/Eliminar', moduloAdmin_Usuario_Eliminar),
    path('moduloAdmin/Usuario/Eliminar2', moduloAdmin_Usuario_Eliminar2),
    path('moduloAdmin/Usuario/Eliminar3', moduloAdmin_Usuario_Eliminar3),

    path('moduloAdmin/Libro/Crear', moduloAdmin_Libro_Crear),
    path('moduloAdmin/Libro/Modificar', moduloAdmin_Libro_Modificar),
    path('moduloAdmin/Libro/Listar', moduloAdmin_Libro_Listar),
    path('moduloAdmin/Libro/Buscar', moduloAdmin_Libro_Buscar),
    path('moduloAdmin/Libro/Eliminar', moduloAdmin_Libro_Eliminar),
    path('moduloAdmin/Compra/Historico', moduloAdmin_Compra_Historico),
    path('moduloAdmin/Compra/HistoricoCanc', moduloAdmin_Compra_HistoricoCanc),
    path('moduloAdmin/Reserva/Historico', moduloAdmin_Reserva_Historico),
    path('moduloAdmin/Reserva/HistoricoCanc', moduloAdmin_Reserva_HistoricoCanc),
    path('moduloAdmin/Devolucion/Atender', moduloAdmin_Devolucion_Atender),
    path('moduloAdmin/Devolucion/Historico', moduloAdmin_Devolucion_Historico),



    path('moduloUsuario/', moduloUsuario),

    path('moduloUsuario/Usuario/Modificar', moduloUsuario_Usuario_Modificar),
    path('moduloUsuario/Usuario/Modificar2', moduloUsuario_Usuario_Modificar2),
    path('moduloUsuario/Usuario/Eliminar', moduloUsuario_Usuario_Eliminar),
    path('moduloUsuario/Usuario/Eliminar2', moduloUsuario_Usuario_Eliminar2),

    
    path('moduloUsuario/Perfil/Crear', moduloUsuario_Perfil_Crear),
    path('moduloUsuario/Perfil/Crear2', moduloUsuario_Perfil_Crear2),
    path('moduloUsuario/Perfil/Modificar', moduloUsuario_Perfil_Modificar),
    path('moduloUsuario/Perfil/Modificar2', moduloUsuario_Perfil_Modificar2),
    path('moduloUsuario/Usuario/Mensajeria', moduloUsuario_Usuario_Mensajeria),


    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
