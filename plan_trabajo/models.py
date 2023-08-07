from django.db import models
from cooperativa.models import Cooperativa
from espacio_trabajo.models import EspacioTrabajo
from users.models import CustomUser


class PlanTrabajo(models.Model):
    name = models.TextField()
    id_cooperativa = models.ForeignKey(
        Cooperativa, null=False, on_delete=models.CASCADE)  # type: ignore
    id_espacio = models.ForeignKey(
        EspacioTrabajo, null=False, on_delete=models.CASCADE)
    id_supervisor = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE)
    tipo_servicio = models.TextField()
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, null=True)

    def __str__(self):
        return self.name
