from django.utils import timezone
from django.db import models
from apps.plan_trabajo.models import PlanTrabajo
# from django.contrib.postgres.fields import ArrayField


class Incident(models.Model):
    STATE_INCIDENTS = [
        ('pendiente',   'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('finalizado',  'Finalizado'),
        ('informado',   'Informado'),
    ]

    description     = models.TextField()
    state           = models.CharField(max_length=20, choices=STATE_INCIDENTS, default='new')
    id_plan_trabajo = models.ForeignKey(PlanTrabajo, null=False, on_delete=models.CASCADE)
    image           = models.ImageField(upload_to='incidente_images/', null=True, blank=True)
    date            = models.DateTimeField(default=timezone.now, editable=False)  # type: ignore

    def __str__(self):
        return self.description
