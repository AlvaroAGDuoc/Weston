# Generated by Django 4.0.2 on 2022-05-29 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_producto_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.status'),
        ),
    ]
