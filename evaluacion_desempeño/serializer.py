from rest_framework import serializers
from .models import EvaluacionDesempeño


class EvaluacionDesempeñoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EvaluacionDesempeño
        fields = '__all__'
