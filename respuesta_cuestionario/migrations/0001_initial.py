# Generated by Django 4.1.2 on 2023-05-31 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
        ),
    ]