from django.urls                    import path, include
from rest_framework.routers         import DefaultRouter
from apps.planillas_trabajo.views   import PlanillaTrabajoViewSet


router = DefaultRouter()
router.register(r'planillas_trabajo', PlanillaTrabajoViewSet, basename='planillas_trabajo')

urlpatterns = [
    path('', include(router.urls)),
]
