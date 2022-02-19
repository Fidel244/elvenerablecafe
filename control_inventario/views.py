from django.shortcuts import render, redirect
from .models import articulo, venta
from datetime import datetime

def venerable_cafe(request):
    return render(request, 'index.html')

def agregar_articulo(request):
    try:
        art = articulo.objects.get(nombre=request.POST["nombre"])
        if request.POST["cantidad"] != "":
            art.cantidad += int(request.POST["cantidad"])
        if request.POST["precio"] != "":
            art.precio = float(request.POST["precio"])
        art.save()
    except:
        articulo_nuevo = articulo(nombre=request.POST["nombre"],
        cantidad=request.POST["cantidad"],
        precio=request.POST["precio"]) 
        articulo_nuevo.save()
    return redirect("/")

def registrar_venta(request):
    tiempo = datetime.now()
    fecha = str(tiempo.day) + "/" + str(tiempo.month) + "/"+ str(tiempo.year)
    articulo_vendido = articulo.objects.get(nombre=request.POST["nombre"])
    venta_nueva = venta(nombre_articulo_vendido=request.POST["nombre"],
        unidades_vendidas=request.POST["cantidad"],
        fecha = fecha,
        ganancia= int(request.POST["cantidad"])*float(articulo_vendido.precio))
    articulo_vendido.cantidad -= int(request.POST["cantidad"])
    articulo_vendido.save()
    venta_nueva.save()
    return redirect("/")

def ver_articulos(request):
    articulos = articulo.objects.order_by("nombre")
    return render(request, "articulos.html", {"articulos":articulos})

def ver_ventas(request):
    ventas = venta.objects.all()
    return render(request, "ventas.html", {"ventas":ventas})