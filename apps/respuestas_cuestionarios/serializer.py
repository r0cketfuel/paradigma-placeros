from rest_framework     import serializers
from .models            import RespuestaCuestionario

class RespuestaCuestionarioSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase RespuestaCuestionario.

    Este serializador se utiliza para convertir instancias de la clase RespuestaCuestionario
    en representaciones JSON y viceversa. Se utiliza en la vista para realizar operaciones
    CRUD (Crear, Leer, Actualizar, Eliminar) en las respuestas a cuestionarios.

    Campos serializados:
    - Todos los campos de la clase RespuestaCuestionario.

    """

    class Meta:
        model = RespuestaCuestionario
        fields = '__all__'
