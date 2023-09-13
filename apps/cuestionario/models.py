from django.db import models


class Cuestionario(models.Model):
    """
    Modelo para representar un cuestionario.

    Este modelo define los campos necesarios para representar un cuestionario, que
    incluye una descripción y una serie de preguntas relacionadas con las tareas
    realizadas en espacios públicos.

    Campos del modelo:
    - description: Descripción del cuestionario.
    - question1 a question18: Preguntas relacionadas con tareas específicas.
    - latitud: Coordenada de latitud (decimal) asociada al cuestionario.
    - longitud: Coordenada de longitud (decimal) asociada al cuestionario.

    """
    description = models.TextField()
    question1 = models.TextField(default="Cumplimiento del horario de inicio.")
    question2 = models.TextField(
        default="Aviso a la Coordinadora/o de llegada al espacio público.")
    question3 = models.TextField(
        default="Aviso a la Coordinadora/o de riesgos o incidencias en el espacio público.")
    question4 = models.TextField(
        default="Recolección de residuos secos y papeles en veredas y zonas verdes.")
    question5 = models.TextField(default="Embolsado de residuos.")
    question6 = models.TextField(
        default="Apilar residuos que por su tamaño no entran en bolsas.")
    question7 = models.TextField(
        default="Vaciar las papeleras que haya en el espacio asignado.")
    question8 = models.TextField(
        default="Cambiar las bolsas de las papeleras.")
    question9 = models.TextField(
        default="Limpiar debajo de los bancos y sus alrededores.")
    question10 = models.TextField(
        default="Limpiar la zona de juegos infantiles y sus alrededores.")
    question11 = models.TextField(
        default="Limpiar la zona de gimnasia al aire libre y sus alrededores.")
    question12 = models.TextField(
        default="Limpiar la zona de paradas de colectivo y sus alrededores.")
    question13 = models.TextField(
        default="Embolsado de los residuos secos juntados en las zonas descritas anteriormente.")
    question14 = models.TextField(
        default="Depósito de todo lo recolectado y embolsado en el sitio determinado e informado por la Coordinadora/or")
    question15 = models.TextField(
        default="Control de ataduras y tutores asegurando que estén firmemente atados y en posición vertical.")
    question16 = models.TextField(
        default="Mantenerse visible en el sitio durante la jornada laboral y atento al arribo de la Coordinadora/or y acudir a su encuentro.")
    question17 = models.TextField(
        default="Fomentar buena relación con vecinas/os generando lazos de pertenecía e identificación con los espacios públicos.")
    question18 = models.TextField(
        default="Fomentar buena relación con vecinas/os generando lazos de pertenecía e identificación con los espacios públicos.")

    def __str__(self):
        return self.description
