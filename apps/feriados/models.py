from django.db import models

class Feriado(models.Model):
    """
    Modelo para representar un feriado.

    Este modelo define los campos necesarios para representar un feriado, incluyendo su
    descripción y la fecha en la que ocurre.

    Campos del modelo:
    - descripcion: Descripción del feriado.
    - fecha: Fecha en la que ocurre el feriado.

    """
    descripcion = models.CharField(max_length=200)
    fecha       = models.DateField()

    class Meta:
        db_table = 'feriados'

    def __str__(self):
        return self.descripcion
