# Generated by Django 4.2.5 on 2023-09-22 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('incidentes', '0001_initial'),
        ('planes_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='id_plan_trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planes_trabajo.plantrabajo'),
        ),
    ]
