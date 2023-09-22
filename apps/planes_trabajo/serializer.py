from rest_framework import serializers
from .models        import PlanTrabajo

class PlanTrabajoSerializer(serializers.ModelSerializer):
    
    name            = serializers.CharField()
    tipo_servicio   = serializers.CharField()
    espacio         = serializers.SerializerMethodField()
    supervisor      = serializers.SerializerMethodField()
    cooperativa     = serializers.SerializerMethodField()

    class Meta:
        model = PlanTrabajo
        fields =  '__all__'

    def get_espacio(self, obj):
        return {
            'id':           obj.id_espacio.id,
            'espacio_name': obj.id_espacio.description
        }

    def get_supervisor(self, obj):
        return {
            'id':           obj.id_supervisor.id,
            'supervisor':   obj.id_supervisor.username
        }

    def get_cooperativa(self, obj):
        return {
            'id':           obj.id_cooperativa.id,
            'cooperativa':  obj.id_cooperativa.nombre
        }
