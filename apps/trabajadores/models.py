from django.db                  import models
from apps.cooperativas.models   import Cooperativa


class Trabajador(models.Model):
    """
    Modelo para representar a un trabajador.

    Este modelo define los campos necesarios para representar a un trabajador, incluyendo su
    nombre, apellido y número de documento de identidad (DNI).
    """

    apellido        = models.CharField(max_length=50)
    nombre          = models.CharField(max_length=50)
    documento_nro   = models.IntegerField(unique=True)
    cooperativa     = models.ForeignKey(Cooperativa, null=False, on_delete=models.RESTRICT)
    activo          = models.BooleanField(null=False, default=True)
    
    class Meta:
        db_table = 'trabajadores'

    def __str__(self):
        return f"{self.id}"

    def delete(self):
        self.activo = False
        self.save()