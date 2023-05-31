from rest_framework import serializers
from .models import RespuestaCuestionario


class RespuestaCuestionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = RespuestaCuestionario
        fields = '__all__'
