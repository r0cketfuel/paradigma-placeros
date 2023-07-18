import django_filters
from .models import Incident


class IncidentFilter(django_filters.FilterSet):
    month = django_filters.NumberFilter(field_name='date', lookup_expr='month')

    class Meta:
        model = Incident
        fields = ['month']
