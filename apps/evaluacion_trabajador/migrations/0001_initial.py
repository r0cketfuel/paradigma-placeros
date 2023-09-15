# Generated by Django 4.1.2 on 2023-09-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionTrabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_result', models.CharField(choices=[('bueno', 'Bueno'), ('regular', 'Regular'), ('malo', 'Malo')], default='malo', max_length=20)),
                ('evaluation_type', models.CharField(choices=[('uniforme', 'Uniforme'), ('epp', 'EPP'), ('herramientas', 'Herramientas')], default='Uniforme', max_length=20)),
            ],
        ),
    ]
