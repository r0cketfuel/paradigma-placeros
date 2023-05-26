from rest_framework import serializers
from .models import EvaluacionTrabajador


class EvaluacionTrabajadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = EvaluacionTrabajador
        fields = '__all__'
