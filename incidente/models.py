from django.db import models
from plan_trabajo.models import PlanTrabajo
# from django.contrib.postgres.fields import ArrayField


class Incident(models.Model):
    STATE_INCIDENTS = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('finalizado', 'Finalizado'),
        ('informado', 'Informado'),
    ]

    description = models.TextField()
    state = models.CharField(
        max_length=20, choices=STATE_INCIDENTS, default='new')
    id_plan_trabajo = models.ForeignKey(
        PlanTrabajo, null=False, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='incidente_images/', null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, default=0.0, blank=True)  # type: ignore
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, default=0.0, blank=True)  # type: ignore
    # images = ArrayField(models.ImageField(
    #     upload_to='incident_images/', blank=True), default=list, blank=True, null=True)

    def __str__(self):
        return self.description
