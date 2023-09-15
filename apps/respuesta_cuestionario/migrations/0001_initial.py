# Generated by Django 4.1.2 on 2023-09-15 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuestionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespuestaCuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('answer1', models.BooleanField(default=False)),
                ('answer2', models.BooleanField(default=False)),
                ('answer3', models.BooleanField(default=False)),
                ('answer4', models.BooleanField(default=False)),
                ('answer5', models.BooleanField(default=False)),
                ('answer6', models.BooleanField(default=False)),
                ('answer7', models.BooleanField(default=False)),
                ('answer8', models.BooleanField(default=False)),
                ('answer9', models.BooleanField(default=False)),
                ('answer10', models.BooleanField(default=False)),
                ('answer11', models.BooleanField(default=False)),
                ('answer12', models.BooleanField(default=False)),
                ('answer13', models.BooleanField(default=False)),
                ('answer14', models.BooleanField(default=False)),
                ('answer15', models.BooleanField(default=False)),
                ('answer16', models.BooleanField(default=False)),
                ('answer17', models.BooleanField(default=False)),
                ('answer18', models.BooleanField(default=False)),
                ('id_cuestionario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cuestionario.cuestionario')),
            ],
        ),
    ]
