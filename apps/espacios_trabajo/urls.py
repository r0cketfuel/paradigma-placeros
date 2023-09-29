from django.urls                    import path, include
from rest_framework.routers         import DefaultRouter
from apps.espacios_trabajo.views    import EspacioTrabajoViewSet, RutaUnoViewSet

router = DefaultRouter()
router.register(r'espacios_trabajo', EspacioTrabajoViewSet, basename='espacio_trabajo')

urlpatterns = [
    path('', include(router.urls)),
    #path('espacios_trabajo/trabajadores/<int:espacio_trabajo_id>', RutaUnoViewSet.as_view({'get': 'list'}), name='espacio_trabajo_trabajadores'),
]
