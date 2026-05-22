"""
URL configuration for uniweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from estudiantes.views import (
    home, registrar_producto, lista_productos, eliminar_producto
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('home/', home, name="home_alt"),
    path("registrar_producto/", registrar_producto, name="registrar_producto"),
    path("lista_productos/", lista_productos, name="lista_productos"),
    path("eliminar_producto/<int:id>/", eliminar_producto, name="eliminar_producto"),
]


