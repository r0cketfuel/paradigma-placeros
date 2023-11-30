from django.db                  import models
from django.utils               import timezone
from apps.trabajadores.models   import Trabajador
from apps.planes_trabajo.models import PlanTrabajo


class Asistencia(models.Model):

    trabajador      = models.ForeignKey(Trabajador, on_delete=models.RESTRICT)
    espacio_trabajo = models.ForeignKey(PlanTrabajo, null=True, on_delete=models.RESTRICT)
    fecha           = models.DateTimeField(default=timezone.now)
    presente        = models.BooleanField(default=False)
    observaciones   = models.CharField(null=True)
    
    class Meta:
        db_table = 'asistencias'
