from django.urls                        import path, include
from rest_framework.routers             import DefaultRouter
from apps.evaluaciones_desempeño.views  import EvaluacionDesempeñoViewSet


router = DefaultRouter()
router.register(r'evaluaciones_desempenio', EvaluacionDesempeñoViewSet, basename='evaluacion_desempenio')

urlpatterns = [
    path('', include(router.urls)),
]
