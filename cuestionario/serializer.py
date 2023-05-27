from rest_framework import serializers
from .models import Cuestionario


class CuestionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuestionario
        fields = '__all__'
