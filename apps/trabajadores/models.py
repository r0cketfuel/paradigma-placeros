from django.db                  import models
from apps.cooperativas.models   import Cooperativa

class Trabajador(models.Model):
    """
    Modelo para representar a un trabajador.

    Este modelo define los campos necesarios para representar a un trabajador, incluyendo su
    nombre, apellido y número de documento de identidad (DNI).

    Campos del modelo:
    - nombre: Nombre del trabajador.
    - last_name: Apellido del trabajador.
    - dni: Número de documento de identidad único del trabajador.

    """
    apellido        = models.CharField(max_length=50)
    nombre          = models.CharField(max_length=50)
    documento_nro   = models.IntegerField(unique=True)
    id_cooperativa  = models.ForeignKey(Cooperativa, null=False, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'trabajadores'

    def __str__(self):
        return f"{self.id}"  # type: ignore
