# Generated by Django 4.1.2 on 2023-06-28 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajador', '0003_alter_trabajador_dni_alter_trabajador_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]