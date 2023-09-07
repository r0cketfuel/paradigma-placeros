from django.db import models
from plan_trabajo.models import PlanTrabajo
from trabajador.models import Trabajador


class PlanillaTrabajo(models.Model):
    """
    Modelo para representar una planilla de trabajo.

    Este modelo define los campos necesarios para representar una planilla de trabajo, incluyendo
    la referencia al plan de trabajo al que está asociada, la referencia al trabajador asignado,
    la fecha, el horario de inicio y fin, si es laborable y si el trabajador estuvo presente.

    Campos del modelo:
    - id_plan_trabajo: Referencia al plan de trabajo asociado.
    - id_trabajador: Referencia al trabajador asignado.
    - fecha: Fecha de la planilla de trabajo.
    - horario_inicio: Hora de inicio del trabajo.
    - horario_fin: Hora de finalización del trabajo.
    - laborable: Indica si el día es laborable (por defecto True).
    - presente: Indica si el trabajador estuvo presente (por defecto False).

    """
    id_plan_trabajo = models.ForeignKey(
        PlanTrabajo, null=False, on_delete=models.CASCADE)
    id_trabajador = models.ForeignKey(
        Trabajador, null=False, on_delete=models.CASCADE)
    fecha = models.DateField()
    horario_inicio = models.TimeField()
    horario_fin = models.TimeField()
    laborable = models.BooleanField(default=True)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return self.id_plan_trabajo.name
