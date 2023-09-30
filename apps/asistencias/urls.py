from django.urls            import path, include
from rest_framework.routers import DefaultRouter
from .views                 import AsistenciaTrabajadorViewSet


router = DefaultRouter()
router.register(r'asistencias', AsistenciaTrabajadorViewSet, basename='asistencias')

urlpatterns = [
    path('', include(router.urls)),
]
