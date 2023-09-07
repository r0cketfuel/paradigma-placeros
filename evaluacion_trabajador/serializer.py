from rest_framework import serializers
from .models import EvaluacionTrabajador


class EvaluacionTrabajadorSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase EvaluacionTrabajador.

    Este serializador se utiliza para convertir instancias de la clase EvaluacionTrabajador
    en representaciones JSON y viceversa. Se utiliza en la vista para realizar operaciones
    CRUD (Crear, Leer, Actualizar, Eliminar) en las evaluaciones de trabajadores.

    Campos serializados:
    - Todos los campos de la clase EvaluacionTrabajador.

    """

    class Meta:
        model = EvaluacionTrabajador
        fields = '__all__'
