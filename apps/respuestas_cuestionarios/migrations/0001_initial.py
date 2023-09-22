# Generated by Django 4.2.5 on 2023-09-22 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuestionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespuestaCuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta1', models.BooleanField(default=False)),
                ('respuesta2', models.BooleanField(default=False)),
                ('respuesta3', models.BooleanField(default=False)),
                ('respuesta4', models.BooleanField(default=False)),
                ('respuesta5', models.BooleanField(default=False)),
                ('respuesta6', models.BooleanField(default=False)),
                ('respuesta7', models.BooleanField(default=False)),
                ('respuesta8', models.BooleanField(default=False)),
                ('respuesta9', models.BooleanField(default=False)),
                ('respuesta10', models.BooleanField(default=False)),
                ('respuesta11', models.BooleanField(default=False)),
                ('respuesta12', models.BooleanField(default=False)),
                ('respuesta13', models.BooleanField(default=False)),
                ('respuesta14', models.BooleanField(default=False)),
                ('respuesta15', models.BooleanField(default=False)),
                ('respuesta16', models.BooleanField(default=False)),
                ('respuesta17', models.BooleanField(default=False)),
                ('respuesta18', models.BooleanField(default=False)),
                ('respuesta19', models.BooleanField(default=False)),
                ('respuesta20', models.BooleanField(default=False)),
                ('id_cuestionario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='cuestionarios.cuestionario')),
            ],
            options={
                'db_table': 'respuestas_cuestionarios',
            },
        ),
    ]
