# Generated by Django 4.0.1 on 2022-02-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_inventario', '0008_alter_venta_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='moneda',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='tasa',
            field=models.FloatField(null=True),
        ),
    ]