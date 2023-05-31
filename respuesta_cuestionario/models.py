from django.db import models
from cuestionario.models import Cuestionario


class RespuestaCuestionario(models.Model):
    description = models.TextField()
    id_cuestionario = models.ForeignKey(
        Cuestionario, on_delete=models.CASCADE, null=False, default=None)
    answer1 = models.BooleanField(default=False)
    answer2 = models.BooleanField(default=False)
    answer3 = models.BooleanField(default=False)
    answer4 = models.BooleanField(default=False)
    answer5 = models.BooleanField(default=False)
    answer6 = models.BooleanField(default=False)
    answer7 = models.BooleanField(default=False)
    answer8 = models.BooleanField(default=False)
    answer9 = models.BooleanField(default=False)
    answer10 = models.BooleanField(default=False)
    answer11 = models.BooleanField(default=False)
    answer12 = models.BooleanField(default=False)
    answer13 = models.BooleanField(default=False)
    answer14 = models.BooleanField(default=False)
    answer15 = models.BooleanField(default=False)
    answer16 = models.BooleanField(default=False)
    answer17 = models.BooleanField(default=False)
    answer18 = models.BooleanField(default=False)

    def __str__(self):
        return self.description
# TODO
# IMPLEMENT CLASSMETHOD FOR GET PK USERS
