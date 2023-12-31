from django.db                  import models
from apps.planes_trabajo.models import PlanTrabajo
from apps.trabajadores.models   import Trabajador


class PlanillaTrabajo(models.Model):
    """
    Modelo para representar una planilla de trabajo.

    Este modelo define los campos necesarios para representar una planilla de trabajo, incluyendo
    la referencia al plan de trabajo al que está asociada, la referencia al trabajador asignado,
    la fecha, el horario de inicio y fin, si es laborable y si el trabajador estuvo presente.

    Campos del modelo:
    - plan_trabajo: Referencia al plan de trabajo asociado.
    - trabajador: Referencia al trabajador asignado.
    - fecha: Fecha de la planilla de trabajo.
    - horario_inicio: Hora de inicio del trabajo.
    - horario_fin: Hora de finalización del trabajo.
    - laborable: Indica si el día es laborable (por defecto True).
    - presente: Indica si el trabajador estuvo presente (por defecto False).

    """
    plan_trabajo    = models.ForeignKey(PlanTrabajo, null=False, on_delete=models.RESTRICT)
    trabajador      = models.ForeignKey(Trabajador, null=False, on_delete=models.RESTRICT)
    dias_semana     = models.CharField(max_length=7)
    horario_inicio  = models.TimeField()
    horario_fin     = models.TimeField()

    class Meta:
        db_table = 'planillas_trabajo'

    def __str__(self):
        return self.plan_trabajo.nombre
