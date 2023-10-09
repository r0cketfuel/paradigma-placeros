from rest_framework import serializers
from .models        import Incidente


class IncidenteSerializer(serializers.ModelSerializer):

    espacio_trabajo = serializers.CharField(source='plan_trabajo.espacio.nombre', read_only=True)

    class Meta:
        model = Incidente
        fields = '__all__'
