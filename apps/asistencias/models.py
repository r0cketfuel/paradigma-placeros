from django.db                  import models
from apps.trabajadores.models   import Trabajador
from datetime                   import datetime 

class Asistencia(models.Model):

    trabajador      = models.ForeignKey(Trabajador, on_delete=models.RESTRICT)
    fecha           = models.DateTimeField(auto_now_add=datetime.now())
    presente        = models.BooleanField(default=False)
    observaciones   = models.CharField(null=True)
    
    class Meta:
        db_table = 'asistencias'
