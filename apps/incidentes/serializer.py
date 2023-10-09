from rest_framework import serializers
from .models        import Incidente


class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incidente
        fields = '__all__'
