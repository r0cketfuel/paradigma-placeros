from django.urls                import path, include
from rest_framework.routers     import DefaultRouter
from apps.cuestionarios.views   import CuestionarioViewSet

router = DefaultRouter()
router.register(r'cuestionarios', CuestionarioViewSet, basename='cuestionario')

urlpatterns = [
    path('', include(router.urls)),
]
