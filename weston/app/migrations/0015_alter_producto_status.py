# Generated by Django 4.0.2 on 2022-05-29 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_detalle_compra_remove_detalle_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='status',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, to='app.status'),
        ),
    ]
