# Generated by Django 4.1.2 on 2023-05-17 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_dni_customuser_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.TextField(default=''),
        ),
    ]
