from django.db                  import models
from apps.cuestionario.models   import Cuestionario

class RespuestaCuestionario(models.Model):
    """
    Modelo para representar respuestas a un cuestionario.

    Este modelo define los campos necesarios para representar las respuestas a un cuestionario,
    incluyendo la descripción, el cuestionario al que está asociado y una serie de respuestas
    booleanas para cada pregunta del cuestionario.

    Campos del modelo:
    - description: Descripción de la respuesta.
    - id_cuestionario: Referencia al cuestionario al que pertenece la respuesta.
    - answer1 a answer18: Respuestas booleanas a las preguntas del cuestionario.

    """
    description     = models.TextField()
    id_cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE, null=False, default=None)
    answer1         = models.BooleanField(default=False)
    answer2         = models.BooleanField(default=False)
    answer3         = models.BooleanField(default=False)
    answer4         = models.BooleanField(default=False)
    answer5         = models.BooleanField(default=False)
    answer6         = models.BooleanField(default=False)
    answer7         = models.BooleanField(default=False)
    answer8         = models.BooleanField(default=False)
    answer9         = models.BooleanField(default=False)
    answer10        = models.BooleanField(default=False)
    answer11        = models.BooleanField(default=False)
    answer12        = models.BooleanField(default=False)
    answer13        = models.BooleanField(default=False)
    answer14        = models.BooleanField(default=False)
    answer15        = models.BooleanField(default=False)
    answer16        = models.BooleanField(default=False)
    answer17        = models.BooleanField(default=False)
    answer18        = models.BooleanField(default=False)

    def __str__(self):
        return self.description

