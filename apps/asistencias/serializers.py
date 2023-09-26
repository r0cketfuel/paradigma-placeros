from rest_framework import serializers
from .models import Asistencia


class AsistenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asistencia
        fields = '__all__'

    def to_representation(self, instance):
        # Si estamos serializando una lista de objetos, usar un formato de lista
        if isinstance(instance, list):
            return super().to_representation(instance, many=True)
        return super().to_representation(instance)
