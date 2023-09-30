from django.urls                import path, include
from rest_framework.routers     import DefaultRouter
from apps.planes_trabajo.views  import PlanTrabajoViewSet


router = DefaultRouter()
router.register(r'planes_trabajo', PlanTrabajoViewSet, basename='plantrabajo')

urlpatterns = [
    path('', include(router.urls)),
]
