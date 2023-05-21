from rest_framework import serializers
from .models import EspacioTrabajo


class EspacioTrabajoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EspacioTrabajo
        fields = '__all__'
