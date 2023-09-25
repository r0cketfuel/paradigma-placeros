from django.urls                        import path, include
from rest_framework.routers             import DefaultRouter
from apps.evaluacion_trabajador.views   import EvaluacionTrabajadorViewSet

router = DefaultRouter()
router.register(r'evaluaciones_trabajadores', EvaluacionTrabajadorViewSet, basename='evaluaciones_trabajador')

urlpatterns = [
    path('', include(router.urls)),
]
