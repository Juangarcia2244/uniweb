from django.contrib import admin
from django.urls import path
from estudiantes.views import (
    home, registrar_producto, lista_productos, eliminar_producto, editar_producto
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('home/', home, name="home_alt"),
    path("registrar_producto/", registrar_producto, name="registrar_producto"),
    path("lista_productos/", lista_productos, name="lista_productos"),
    path("eliminar_producto/<int:id>/", eliminar_producto, name="eliminar_producto"),
    path("editar_producto/<int:id>/", editar_producto, name="editar_producto"),
]
