from django.db import models
from cooperativa.models import Cooperativa
from espacio_trabajo.models import EspacioTrabajo
from users.models import CustomUser


class PlanTrabajo(models.Model):
    name = models.TextField()
    id_cooperativa = models.ForeignKey(
        Cooperativa, null=False, on_delete=models.CASCADE)
    id_espacio = models.ForeignKey(
        EspacioTrabajo, null=False, on_delete=models.CASCADE)
    id_supervisor = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE)
    tipo_servicio = models.TextField()

    def __str__(self):
        return self.name
# TODO
# IMPLEMENT CLASSMETHOD FOR GET PK USERS
