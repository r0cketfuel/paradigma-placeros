from rest_framework import serializers
from .models import PlanTrabajo


class PlanTrabajoSerializer(serializers.ModelSerializer):
    """
    Serializador para la clase PlanTrabajo.

    Este serializador se utiliza para convertir instancias de la clase PlanTrabajo
    en representaciones JSON y viceversa. Se utiliza en la vista para realizar operaciones
    CRUD (Crear, Leer, Actualizar, Eliminar) en los planes de trabajo.

    Campos serializados:
    - Todos los campos de la clase PlanTrabajo.

    """

    class Meta:
        model = PlanTrabajo
        fields = '__all__'

    def to_representation(self, instance):

        data = {
            "id": instance.id,
            "name": instance.name,
            "tipo_servicio": instance.tipo_servicio,
            "id_espacio": instance.id_espacio.id,
            "espacio_name": instance.id_espacio.__str__(),
            "id_supervisor": instance.id_supervisor.id,
            "supervisor": instance.id_supervisor.__str__(),
            "id_cooperativa": instance.id_cooperativa.id,
            "cooperativa": instance.id_cooperativa.__str__(),
            "creado": instance.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')

        }
        return data
