from rest_framework import serializers
from .models        import Cuestionario


class CuestionarioSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase Cuestionario.

    Este serializador se utiliza para convertir instancias de la clase Cuestionario
    en representaciones JSON y viceversa. Se utiliza en la vista para realizar operaciones
    CRUD (Crear, Leer, Actualizar, Eliminar) en los cuestionarios.

    Campos serializados:
    - Todos los campos de la clase Cuestionario.

    """

    class Meta:
        model = Cuestionario
        fields = '__all__'
