# Generated by Django 4.1.2 on 2023-06-27 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidente', '0004_incident_images_incident_latitude_incident_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='images',
        ),
    ]
