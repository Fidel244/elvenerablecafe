# Generated by Django 4.0.2 on 2022-02-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_inventario', '0009_articulo_moneda_venta_tasa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='tasa',
        ),
        migrations.AddField(
            model_name='venta',
            name='moneda',
            field=models.BooleanField(null=True),
        ),
    ]
