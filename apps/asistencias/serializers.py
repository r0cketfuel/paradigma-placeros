from rest_framework import serializers
from .models        import Asistencia


class AsistenciaSerializer(serializers.ModelSerializer):

    fecha = serializers.SerializerMethodField()

    class Meta:
        model = Asistencia
        fields = ['trabajador', 'espacio_trabajo', 'presente', 'observaciones', 'fecha']

    def get_fecha(self, obj):
        return obj.fecha.strftime('%Y-%m-%d')

    def to_representation(self, instance):
        # Si estamos serializando una lista de objetos, usar un formato de lista
        if isinstance(instance, list):
            return super().to_representation(instance, many=True)
        return super().to_representation(instance)
