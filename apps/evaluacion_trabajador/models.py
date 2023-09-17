from django.db                  import models
from apps.trabajadores.models   import Trabajador
from apps.users.models          import CustomUser


class EvaluacionTrabajador(models.Model):
    """
    Modelo para representar una evaluación de trabajador.

    Este modelo define los campos necesarios para representar una evaluación de trabajador,
    incluyendo el trabajador evaluado, el coordinador que realiza la evaluación, el resultado
    de la evaluación y el tipo de evaluación (por ejemplo, uniforme, EPP, herramientas).

    Campos del modelo:
    - id_trabajador: Referencia al trabajador evaluado.
    - id_coordinador: Referencia al coordinador que realiza la evaluación.
    - evaluation_result: Resultado de la evaluación (opciones: bueno, regular, malo).
    - evaluation_type: Tipo de evaluación (opciones: uniforme, EPP, herramientas).

    """
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
        return f"{self.id_trabajador}  {self.id_coordinador}"
