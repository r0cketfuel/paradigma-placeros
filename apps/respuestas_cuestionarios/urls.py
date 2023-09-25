from django.urls                            import path, include
from rest_framework.routers                 import DefaultRouter
from apps.respuestas_cuestionarios.views    import RespuestaCuestionarioViewSet

router = DefaultRouter()
router.register(r'respuestas_cuestionario', RespuestaCuestionarioViewSet, basename='respuesta_cuestionario')

urlpatterns = [
    path('', include(router.urls)),
]
