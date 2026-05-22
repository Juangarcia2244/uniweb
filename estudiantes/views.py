from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  Producto

def home(request):

    contexto = {"titulo": "Home / Estudiantes"}

    return render(request, "estudiantes/home.html", contexto)

    
def registrar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")

        # Validamos que si ingrese el nombre y el precio
        if not nombre:
            return render(request, 'estudiantes/registrar_producto.html', {
                'error': 'El nombre es obligatorio'
            })

        if not precio:
            return render(request, 'estudiantes/registrar_producto.html', {
                'error': 'El precio es obligatorio'
            })

        # Validamos que el precio si sea un número
        try:
            precio = float(precio)
        except ValueError:
            return render(request, 'estudiantes/registrar_producto.html', {
                'error': 'El precio debe ser un número válido'
            })

        # Validamos que el precio no sea negativo
        if precio <= 0:
            return render(request, 'estudiantes/registrar_producto.html', {
                'error': 'El precio debe ser mayor a 0'
            })

        Producto.objects.create(
            nombre=nombre,
            precio=precio
        )

        return redirect("lista_productos")
    return render (request, "estudiantes/registrar_producto.html")



def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "estudiantes/lista_productos.html", {"productos": productos})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('lista_productos')

