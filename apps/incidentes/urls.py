from django.urls            import path, include
from rest_framework.routers import DefaultRouter
from apps.incidentes.views  import IncidenteViewSet, IncidentByMonthViewSet

router = DefaultRouter()
router.register(r'incidentes',      IncidenteViewSet,       basename='incidentes')
#router.register(r'incidentes_mes', IncidentByMonthViewSet, basename='incidentes_por_mes')

urlpatterns = [
    path('', include(router.urls)),
]
