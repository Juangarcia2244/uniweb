from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto


def home(request):
    contexto = {"titulo": "Home / Estudiantes"}
    return render(request, "estudiantes/home.html", contexto)


def registrar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")

        if not nombre:
            return render(request, 'estudiantes/registrar_producto.html', {
                'error': 'El nombre es obligatorio'
            })

        if not precio:
            return render(request, 'estudiantes/registrar_producto.html', {
                'error': 'El precio es obligatorio'
            })

        try:
            precio = float(precio)
        except ValueError:
            return render(request, 'estudiantes/registrar_producto.html', {
                'error': 'El precio debe ser un número válido'
            })

        if precio <= 0:
            return render(request, 'estudiantes/registrar_producto.html', {
                'error': 'El precio debe ser mayor a 0'
            })

        Producto.objects.create(nombre=nombre, precio=precio)
        return redirect("lista_productos")

    return render(request, "estudiantes/registrar_producto.html")


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "estudiantes/lista_productos.html", {"productos": productos})


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
    return redirect('lista_productos')


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")

        if not nombre:
            return render(request, 'estudiantes/editar_producto.html', {
                'producto': producto,
                'error': 'El nombre es obligatorio'
            })

        if not precio:
            return render(request, 'estudiantes/editar_producto.html', {
                'producto': producto,
                'error': 'El precio es obligatorio'
            })

        try:
            precio = float(precio)
        except ValueError:
            return render(request, 'estudiantes/editar_producto.html', {
                'producto': producto,
                'error': 'El precio debe ser un número válido'
            })

        if precio <= 0:
            return render(request, 'estudiantes/editar_producto.html', {
                'producto': producto,
                'error': 'El precio debe ser mayor a 0'
            })

        producto.nombre = nombre
        producto.precio = precio
        producto.save()
        return redirect('lista_productos')

    return render(request, 'estudiantes/editar_producto.html', {'producto': producto})
