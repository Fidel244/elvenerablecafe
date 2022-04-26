from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import articulo, venta
from datetime import datetime

def venerable_cafe(request):
    return render(request, 'index.html')

def agregar_articulo(request):

    if request.POST["moneda"].upper() == "ELIMINAR":
        articulo.objects.get(nombre=request.POST["nombre"]).delete()
        return redirect("/")

    try:
        art = articulo.objects.get(nombre=request.POST["nombre"])
        if request.POST["cantidad"] != "":
            art.cantidad += int(request.POST["cantidad"])
        if request.POST["precio"] != "":
            art.precio = float(request.POST["precio"])
        if request.POST["moneda"] != "":
            if request.POST["moneda"].upper() == "DOLLAR":
                art.moneda = True
            else:
                art.moneda = False
        art.save()
    except:

        if request.POST["moneda"].upper() == "DOLLAR":
            bool = True
        else:
            bool = False
        articulo_nuevo = articulo(nombre=request.POST["nombre"].upper(),
        cantidad=int(request.POST["cantidad"]),
        precio=float(request.POST["precio"]),
        moneda = bool) 
        articulo_nuevo.save()
    return redirect("/")

def registrar_venta(request):

    if request.POST["fechax"] == "":
        tiempo = datetime.now()
        fecha = str(tiempo.day) + "/" + str(tiempo.month) + "/"+ str(tiempo.year)
    else:
        fecha = request.POST["fechax"]

    try:
        articulo_vendido = articulo.objects.get(nombre=request.POST["nombre"])
    except:
        return HttpResponse("El nombre que colocó no está registrado en el sistema")

    if articulo_vendido.cantidad < int(request.POST["cantidad"]):
        return HttpResponse("La cantidad de productos a vender que colocó es mayor que la cantidad de productos que se tiene, intentelo nuevamente")

    venta_nueva = venta(nombre_articulo_vendido=request.POST["nombre"],
        unidades_vendidas=request.POST["cantidad"],
        fecha = fecha,
        ganancia = int(request.POST["cantidad"])*float(articulo_vendido.precio),
        moneda = articulo_vendido.moneda)
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


class objeto_report:
    cantidad = 0
    ganancia = 0
    def __init__(self, nombre, cantidad, ganancia, moneda):
        self.nombre = nombre
        self.cantidad = cantidad 
        self.ganancia = ganancia
        self.moneda = moneda



def ver_reporte_semanal(request):


    ventas = venta.objects.all()
    cantidad_total = len(ventas)

    if cantidad_total == 0:
        return render(request, "reporte_semanal.html")
    contador = 1

    if cantidad_total < 7:
        maximo = cantidad_total
    else: 
        maximo = 7

    if contador == 1:
        maximo = 2

    ventas_aux =[]
    nueva_lista = []
    fecha_inicial = ventas[cantidad_total-1].fecha

    for i in ventas:
        ventas_aux.append(i)

    fecha_inicio = ""
    contador = 0
    for i in reversed(ventas_aux):
        if contador == 0:
            fecha_inicio = i.fecha
        if contador != 7:
            nueva_lista.append(i)
            if contador!=0:
                if fecha_inicio != i.fecha:
                    contador+=1
 
            


    '''
    for i in range(cantidad_total):
        if contador == maximo: break
        if ventas[cantidad_total-(i+1)].fecha != fecha_inicial:
            contador+=1
            fecha_inicial = ventas[cantidad_total-(i+1)].fecha
        nueva_lista.append(ventas[cantidad_total-(i+1)])
    '''
    print(nueva_lista)

    lista_objetos = []
    nombres_leidos = []
    for i in nueva_lista:
        if not (i.nombre_articulo_vendido in nombres_leidos):
            nombres_leidos.append(i.nombre_articulo_vendido)
            obj = objeto_report(i.nombre_articulo_vendido,0,0, i.moneda)
            lista_objetos.append(obj)
    
    for i in lista_objetos:
        for k in nueva_lista:
            if i.nombre == k.nombre_articulo_vendido:
                i.cantidad += k.unidades_vendidas
                i.ganancia += k.ganancia

    print(lista_objetos)

    return render(request, "reporte_semanal.html", {"objetos":lista_objetos})