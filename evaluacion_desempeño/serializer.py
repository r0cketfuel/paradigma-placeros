from rest_framework import serializers
from .models import EvaluacionDesempeño


class EvaluacionDesempeñoSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase EvaluacionDesempeño.

    Este serializador se utiliza para convertir instancias de la clase EvaluacionDesempeño
    en representaciones JSON y viceversa. Se utiliza en la vista para realizar operaciones
    CRUD (Crear, Leer, Actualizar, Eliminar) en las evaluaciones de desempeño.

    Campos serializados:
    - Todos los campos de la clase EvaluacionDesempeño.

    """
    class Meta:
        model = EvaluacionDesempeño
        fields = '__all__'
