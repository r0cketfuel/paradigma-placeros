import django_filters
from .models import Incidente

class IncidenteFilter(django_filters.FilterSet):
    
    month = django_filters.NumberFilter(field_name='date', lookup_expr='month')

    class Meta:
        model = Incidente
        fields = ['month']
