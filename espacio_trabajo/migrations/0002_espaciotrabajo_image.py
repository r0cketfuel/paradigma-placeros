# Generated by Django 4.1.2 on 2023-06-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacio_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='espaciotrabajo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='espacio_trabajo_images/'),
        ),
    ]