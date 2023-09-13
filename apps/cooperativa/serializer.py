from rest_framework import serializers
from .models import Cooperativa


class CooperativaSerializer(serializers.ModelSerializer):
    """
    Este serializador se utiliza para convertir instancias de la clase Cooperativa
    en representaciones JSON y viceversa. Se utiliza en la vista para realizar operaciones
    CRUD (Crear, Leer, Actualizar, Eliminar) en las cooperativas.

    Campos serializados:
    - Todos los campos de la clase Cooperativa.

    """

    class Meta:
        model = Cooperativa
        fields = '__all__'
