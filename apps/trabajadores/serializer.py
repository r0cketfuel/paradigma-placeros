from rest_framework             import serializers
from .models                    import Trabajador
from apps.cooperativas.models   import Cooperativa


class CooperativaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Cooperativa
        fields  = ['nombre']


class TrabajadorSerializer(serializers.ModelSerializer):

    cooperativa_nombre = serializers.ReadOnlyField(source='id_cooperativa.nombre')

    class Meta:
        model   = Trabajador
        fields  = '__all__'
