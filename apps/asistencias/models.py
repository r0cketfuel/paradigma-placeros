from django.db                  import models
from apps.trabajadores.models   import Trabajador


class Cooperativa(models.Model):

    trabajador      = models.ForeignKey(Trabajador, on_delete=models.RESTRICT)
    fecha           = models.DateTimeField(null=False)
    presente        = models.BooleanField(default=False)
    observaciones   = models.CharField(null=True)
    
    class Meta:
        db_table = 'asistencias'
