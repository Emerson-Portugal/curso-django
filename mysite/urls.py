# Aqui estaran las URL de nuestro Proyecto

from django.contrib import admin
from django.urls import path, include
#from django.http import HttpResponse

## Se van a crear dos rutas raiz


#---------------------------------------------------
# def home(request):
#     # devolvemos un valor por Web
#     return HttpResponse("Home Page")



urlpatterns = [
    #path("", home),# aqui vamos por defecto a la ruta home
    #path("home/", room),# aqui vamos a la ruta room

    path("admin/", admin.site.urls),# aqui vamos a la ruta admin/
    path("", include('base.urls')),# vamos a traer las URL de nuestra aplicacion
]
