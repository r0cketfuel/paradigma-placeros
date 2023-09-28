from rest_framework import serializers
from .models        import PlanTrabajo

class PlanTrabajoSerializer(serializers.ModelSerializer):
    
    nombre          = serializers.CharField()
    tipo_servicio   = serializers.CharField()
    espacio         = serializers.SerializerMethodField()
    supervisor      = serializers.SerializerMethodField()
    cooperativa     = serializers.SerializerMethodField()

    class Meta:
        model = PlanTrabajo
        fields =  '__all__'

    def get_espacio(self, obj):
        return {
            'id':           obj.espacio.id,
            'espacio_name': obj.espacio.description
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
