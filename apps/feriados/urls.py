from django.urls            import path, include
from rest_framework.routers import DefaultRouter
from apps.feriados.views    import FeriadoViewSet

router = DefaultRouter()
router.register(r'feriados', FeriadoViewSet, basename='feriados')

urlpatterns = [
    path('', include(router.urls)),
]
