# Generated by Django 4.0.1 on 2022-02-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_inventario', '0007_remove_venta_updated_at_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
