from django.db import models
from trabajador.models import Trabajador
from users.models import CustomUser


class EvaluacionTrabajador(models.Model):
    EVALUATION_RESULT = [
        ('bueno', 'Bueno'),
        ('regular', 'Regular'),
        ('malo', 'Malo'),
    ]
    EVALUATION_TYPE = [
        ('uniforme', 'Uniforme'),
        ('epp', 'EPP'),
        ('herramientas', 'Herramientas'),
    ]

    id_trabajador = models.ForeignKey(
        Trabajador, null=False, on_delete=models.CASCADE)
    id_coordinador = models.ForeignKey(
        CustomUser, null=False, on_delete=models.CASCADE)
    evaluation_result = models.CharField(
        max_length=20, choices=EVALUATION_RESULT, default='malo', null=False)
    evaluation_type = models.CharField(
        max_length=20, choices=EVALUATION_TYPE, default='Uniforme', null=False)

    def __str__(self):
        return self.name
# TODO
# IMPLEMENT CLASSMETHOD FOR GET PK USERS
