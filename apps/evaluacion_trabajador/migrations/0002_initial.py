# Generated by Django 4.1.2 on 2023-09-15 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trabajador', '0001_initial'),
        ('evaluacion_trabajador', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluaciontrabajador',
            name='id_coordinador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evaluaciontrabajador',
            name='id_trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajador.trabajador'),
        ),
    ]
