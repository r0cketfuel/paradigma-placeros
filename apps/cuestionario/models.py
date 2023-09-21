from django.db import models


class Cuestionario(models.Model):
    """
    Modelo para representar un cuestionario.

    Este modelo define los campos necesarios para representar un cuestionario, que
    incluye una descripción y una serie de preguntas relacionadas con las tareas
    realizadas en espacios públicos.
    """
    descripcion = models.TextField(null=True)
    pregunta1   = models.TextField(null=True)
    pregunta2   = models.TextField(null=True)
    pregunta3   = models.TextField(null=True)
    pregunta4   = models.TextField(null=True)
    pregunta5   = models.TextField(null=True)
    pregunta6   = models.TextField(null=True)
    pregunta7   = models.TextField(null=True)
    pregunta8   = models.TextField(null=True)
    pregunta9   = models.TextField(null=True)
    pregunta10  = models.TextField(null=True)
    pregunta11  = models.TextField(null=True)
    pregunta12  = models.TextField(null=True)
    pregunta13  = models.TextField(null=True)
    pregunta14  = models.TextField(null=True)
    pregunta15  = models.TextField(null=True)
    pregunta16  = models.TextField(null=True)
    pregunta17  = models.TextField(null=True)
    pregunta18  = models.TextField(null=True)
    pregunta19  = models.TextField(null=True)
    pregunta20  = models.TextField(null=True)
    activo      = models.BooleanField(null=False, default=True)

    class Meta:
        db_table = 'cuestionario'

    def __str__(self):
        return self.nombre
    
    def delete(self):
        self.activo = False
        self.save()
