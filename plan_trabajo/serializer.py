from rest_framework import serializers
from .models import PlanTrabajo


class PlanTrabajoSerializer(serializers.ModelSerializer):

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

        }
        return data
