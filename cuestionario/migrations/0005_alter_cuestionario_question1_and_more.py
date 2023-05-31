# Generated by Django 4.1.2 on 2023-05-31 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionario', '0004_remove_cuestionario_questions_cuestionario_question1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuestionario',
            name='question1',
            field=models.TextField(default='Cumplimiento del horario de inicio.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question10',
            field=models.TextField(default='Limpiar la zona de juegos infantiles y sus alrededores.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question11',
            field=models.TextField(default='Limpiar la zona de gimnasia al aire libre y sus alrededores.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question12',
            field=models.TextField(default='Limpiar la zona de paradas de colectivo y sus alrededores.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question13',
            field=models.TextField(default='Embolsado de los residuos secos juntados en las zonas descritas anteriormente.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question14',
            field=models.TextField(default='Depósito de todo lo recolectado y embolsado en el sitio determinado e informado por la Coordinadora/or'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question15',
            field=models.TextField(default='Control de ataduras y tutores asegurando que estén firmemente atados y en posición vertical.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question16',
            field=models.TextField(default='Mantenerse visible en el sitio durante la jornada laboral y atento al arribo de la Coordinadora/or y acudir a su encuentro.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question17',
            field=models.TextField(default='Fomentar buena relación con vecinas/os generando lazos de pertenecía e identificación con los espacios públicos.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question18',
            field=models.TextField(default='Fomentar buena relación con vecinas/os generando lazos de pertenecía e identificación con los espacios públicos.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question2',
            field=models.TextField(default='Aviso a la Coordinadora/o de llegada al espacio público.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question3',
            field=models.TextField(default='Aviso a la Coordinadora/o de riesgos o incidencias en el espacio público.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question4',
            field=models.TextField(default='Recolección de residuos secos y papeles en veredas y zonas verdes.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question5',
            field=models.TextField(default='Embolsado de residuos.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question6',
            field=models.TextField(default='Apilar residuos que por su tamaño no entran en bolsas.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question7',
            field=models.TextField(default='Vaciar las papeleras que haya en el espacio asignado.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question8',
            field=models.TextField(default='Cambiar las bolsas de las papeleras.'),
        ),
        migrations.AlterField(
            model_name='cuestionario',
            name='question9',
            field=models.TextField(default='Limpiar debajo de los bancos y sus alrededores.'),
        ),
    ]
