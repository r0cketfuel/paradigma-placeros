from django.urls                    import path, include
from rest_framework.routers         import DefaultRouter
from apps.espacios_trabajo.views    import EspacioTrabajoViewSet, PresentesPorEspacioDeTrabajo

router = DefaultRouter()
router.register(r'espacios_trabajo', EspacioTrabajoViewSet, basename='espacio_trabajo')

urlpatterns = [
    path('', include(router.urls)),
]
