from django.urls                    import path, include
from rest_framework.routers         import DefaultRouter
from apps.planillas_trabajo.views   import PlanillaTrabajoViewSet, TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet, PresentesEntreFechasPorIdTrabajador

router = DefaultRouter()
router.register(r'planillas_trabajo',                           PlanillaTrabajoViewSet,                                 basename='planillas_trabajo')
router.register(r'trabajadores_por_id_plantrabajo',             TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet,    basename='trabajadores_por_id_plantrabajo')
#router.register(r'asistencias_entre_fechas_por_trabajador',    PresentesEntreFechasPorIdTrabajador,                    basename='asistencias_entre_fechas_por_trabajador')

urlpatterns = [
    path('', include(router.urls)),
]
