from rest_framework import serializers
from .models        import PlanillaTrabajo


class PlanillaTrabajoSerializer(serializers.ModelSerializer):
    """
    Este serializador se utiliza para convertir instancias de la clase PlanillaTrabajo
    en representaciones JSON y viceversa. Se utiliza en la vista para realizar operaciones
    CRUD (Crear, Leer, Actualizar, Eliminar) en las planillas de trabajo.

    Campos serializados:
    - Todos los campos de la clase PlanillaTrabajo.

    """

    class Meta:
        model = PlanillaTrabajo
        fields = '__all__'