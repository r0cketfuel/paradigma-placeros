from rest_framework import serializers
from .models        import DiaNoLaborable


class DiaNoLaborableSerializer(serializers.ModelSerializer):
    class Meta:
        model   = DiaNoLaborable
        fields  = '__all__'
