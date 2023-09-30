from django.urls            import path, include
from rest_framework.routers import DefaultRouter
from .views                 import CooperativaViewSet, CantidadTrabajadoresPorCooperativa


router = DefaultRouter()
router.register(r'cooperativas',                        CooperativaViewSet,                 basename='cooperativa')
router.register(r'cantidad_trabajadores_cooperativas',  CantidadTrabajadoresPorCooperativa, basename='cantidad_trabajadores_cooperativa')

urlpatterns = [
    path('', include(router.urls)),
]
