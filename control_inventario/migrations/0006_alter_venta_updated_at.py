# Generated by Django 4.0.1 on 2022-02-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_inventario', '0005_venta_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]