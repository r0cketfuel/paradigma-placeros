from rest_framework import serializers
from .models import EspacioTrabajo


class EspacioTrabajoSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase EspacioTrabajo.

    Este serializador se utiliza para convertir instancias de la clase EspacioTrabajo
    en representaciones JSON y viceversa. Se utiliza en la vista para realizar operaciones
    CRUD (Crear, Leer, Actualizar, Eliminar) en los espacios de trabajo.

    Campos serializados:
    - Todos los campos de la clase EspacioTrabajo.

    """
    class Meta:
        model = EspacioTrabajo
        fields = '__all__'
