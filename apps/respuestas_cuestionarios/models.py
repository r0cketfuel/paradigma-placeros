from django.db                  import models
from apps.cuestionarios.models  import Cuestionario


class RespuestaCuestionario(models.Model):
    """
    Modelo para representar respuestas a un cuestionario.

    Este modelo define los campos necesarios para representar las respuestas a un cuestionario,
    incluyendo la descripción, el cuestionario al que está asociado y una serie de respuestas
    booleanas para cada pregunta del cuestionario.
    """

    cuestionario    = models.ForeignKey(Cuestionario, on_delete=models.RESTRICT, null=False, default=None)
    respuesta1      = models.BooleanField(default=False)
    respuesta2      = models.BooleanField(default=False)
    respuesta3      = models.BooleanField(default=False)
    respuesta4      = models.BooleanField(default=False)
    respuesta5      = models.BooleanField(default=False)
    respuesta6      = models.BooleanField(default=False)
    respuesta7      = models.BooleanField(default=False)
    respuesta8      = models.BooleanField(default=False)
    respuesta9      = models.BooleanField(default=False)
    respuesta10     = models.BooleanField(default=False)
    respuesta11     = models.BooleanField(default=False)
    respuesta12     = models.BooleanField(default=False)
    respuesta13     = models.BooleanField(default=False)
    respuesta14     = models.BooleanField(default=False)
    respuesta15     = models.BooleanField(default=False)
    respuesta16     = models.BooleanField(default=False)
    respuesta17     = models.BooleanField(default=False)
    respuesta18     = models.BooleanField(default=False)
    respuesta19     = models.BooleanField(default=False)
    respuesta20     = models.BooleanField(default=False)

    class Meta:
        db_table = 'respuestas_cuestionarios'
