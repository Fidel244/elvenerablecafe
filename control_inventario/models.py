from django.db import models


class articulo(models.Model):
    nombre = models.CharField(max_length=70)
    cantidad = models.IntegerField(null=True)
    precio = models.FloatField(null=True)
    moneda = models.BooleanField(null=True)

    def __str__(self):
        return self.nombre

class venta(models.Model):
    nombre_articulo_vendido = models.CharField(max_length=70)
    fecha = models.CharField(max_length=70, null=True)
    unidades_vendidas = models.IntegerField(null=True)
    ganancia = models.FloatField(null=True)
    moneda = models.BooleanField(null=True)

    def __str__(self):
        return self.fecha
