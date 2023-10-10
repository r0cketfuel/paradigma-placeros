from rest_framework import serializers
from .models        import PlanTrabajo

from apps.espacios_trabajo.models import EspacioTrabajo
from apps.users.models import CustomUser
from apps.cooperativas.models import Cooperativa

class PlanTrabajoSerializer(serializers.ModelSerializer):
    
    nombre          = serializers.CharField()
    tipo_servicio   = serializers.CharField()
    espacio_id      = serializers.PrimaryKeyRelatedField(queryset=EspacioTrabajo.objects.all(), source='espacio', write_only=True)
    supervisor_id   = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='supervisor', write_only=True)
    cooperativa_id  = serializers.PrimaryKeyRelatedField(queryset=Cooperativa.objects.all(), source='cooperativa', write_only=True)

    espacio         = serializers.SerializerMethodField()
    supervisor      = serializers.SerializerMethodField()
    cooperativa     = serializers.SerializerMethodField()

    class Meta:
        model = PlanTrabajo
        fields =  '__all__'

    def get_espacio(self, obj):
        return {
            'id':           obj.espacio.id,
            'nombre':       obj.espacio.nombre
        }

    def get_supervisor(self, obj):
        return {
            'id':           obj.supervisor.id,
            'supervisor':   obj.supervisor.username
        }

    def get_cooperativa(self, obj):
        return {
            'id':           obj.cooperativa.id,
            'cooperativa':  obj.cooperativa.nombre
        }
