from django.db import models
from plan_trabajo.models import PlanTrabajo


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

    def __str__(self):
        return self.description

    @classmethod
    def get_user_pks(cls):
        return cls.objects.values_list('id', flat=True)


# TODO
# IMPLEMENT CLASSMETHOD FOR GET PK USERS
