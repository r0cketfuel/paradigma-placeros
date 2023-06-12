from django.db import models
from plan_trabajo.models import PlanTrabajo
from trabajador.models import Trabajador


class PlanillaTrabajo(models.Model):
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
# TODO
# IMPLEMENT CLASSMETHOD FOR GET PK USERS
