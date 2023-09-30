from django.urls            import path, include
from rest_framework.routers import DefaultRouter
from .views                 import TrabajadorViewSet, CantidadTrabajadoresCargadosViewSet, CantidadTrabajadoresActivosViewSet


router = DefaultRouter()
router.register(r'trabajadores',                    TrabajadorViewSet,                      basename='trabajadores')
router.register(r'cantidad_trabajadores_cargados',  CantidadTrabajadoresCargadosViewSet,    basename='cantidad_trabajadores_cargados')
router.register(r'cantidad_trabajadores_activos',   CantidadTrabajadoresActivosViewSet,     basename='cantidad_trabajadores_activos')

urlpatterns = [
    path('', include(router.urls)),
]
