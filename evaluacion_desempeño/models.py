from django.db import models
from cuestionario.models import Cuestionario
from plan_trabajo.models import PlanTrabajo


class EvaluacionDesempeño(models.Model):
    description = models.TextField()
    id_cuestionario = models.ForeignKey(
        Cuestionario, on_delete=models.CASCADE, null=False, default=None)
    id_plan_trabajo = models.ForeignKey(
        PlanTrabajo, on_delete=models.CASCADE, null=False, default=None)
    fecha = models.DateField(null=False)
    ubicacion = models.TextField()

    def __str__(self):
        return self.description
# TODO
# IMPLEMENT CLASSMETHOD FOR GET PK USERS
