from django.urls                    import path, include
from rest_framework.routers         import DefaultRouter
from apps.planillas_trabajo.views   import PlanillaTrabajoViewSet, TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet


router = DefaultRouter()
router.register(r'planillas_trabajo',               PlanillaTrabajoViewSet,                                 basename='planillas_trabajo')
router.register(r'trabajadores_por_id_plantrabajo', TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet,    basename='trabajadores_por_id_plantrabajo')

urlpatterns = [
    path('', include(router.urls)),
]
