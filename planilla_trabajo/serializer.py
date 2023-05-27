from rest_framework import serializers
from .models import PlanillaTrabajo


class PlanillaTrabajoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanillaTrabajo
        fields = '__all__'
