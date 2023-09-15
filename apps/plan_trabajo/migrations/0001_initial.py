# Generated by Django 4.1.2 on 2023-09-15 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cooperativa', '0001_initial'),
        ('espacio_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('tipo_servicio', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('id_cooperativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooperativa.cooperativa')),
                ('id_espacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espacio_trabajo.espaciotrabajo')),
            ],
        ),
    ]
