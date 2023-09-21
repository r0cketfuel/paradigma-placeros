from django.db import models

class DiaNoLaborable(models.Model):
    """
    Modelo para representar un dia no laborable.

    Este modelo define los campos necesarios para representar un dia no laborable, incluyendo su
    descripción y la fecha en la que ocurre.

    Campos del modelo:
    - descripcion: Descripción del dia no laborable.
    - fecha: Fecha en la que ocurre el dia no laborable.

    """
    fecha       = models.DateField()
    descripcion = models.CharField(max_length=200)

    class Meta:
        db_table = 'dias_no_laborables'

    def __str__(self):
        return self.descripcion
