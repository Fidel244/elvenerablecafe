from django.urls import path
from . import views

app_name = "inventario"

urlpatterns = [
    path('', views.venerable_cafe),
    path('agregar', views.agregar_articulo),
    path('registrar', views.registrar_venta),
    path('ver_articulos', views.ver_articulos),
    path('ver_ventas', views.ver_ventas),
    path('ver_reporte_semanal', views.ver_reporte_semanal),
]