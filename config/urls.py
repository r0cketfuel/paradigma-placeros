from django.conf                            import settings
from django.conf.urls.static                import static
from django.urls                            import include, path
from rest_framework.permissions             import IsAuthenticated
from rest_framework_simplejwt.views         import TokenRefreshView
from rest_framework                         import routers
from apps.users.views                       import UserRegisterationViewSet, UserLoginViewSet, UserLogoutViewSet
from apps.user_type.views                   import UserTypeViewSet
from apps.planes_trabajo.views              import PlanTrabajoViewSet
from apps.incidentes.views                  import IncidenteViewSet, IncidentByMonthViewSet
from apps.evaluacion_trabajador.views       import EvaluacionTrabajadorViewSet
from apps.planillas_trabajo.views           import PlanillaTrabajoViewSet, TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet, PresentesEntreFechasPorIdTrabajador
from apps.respuestas_cuestionarios.views    import RespuestaCuestionarioViewSet
from apps.evaluaciones_desempeño.views      import EvaluacionDesempeñoViewSet
from apps.user_type.permisions              import IsSuper
from drf_yasg.views                         import get_schema_view
from drf_yasg                               import openapi

# Importa los routers de las aplicaciones
from apps.cooperativas.urls                 import router as cooperativas_router
from apps.trabajadores.urls                 import router as trabajadores_router
from apps.cuestionarios.urls                import router as cuestionarios_router
from apps.dias_no_laborables.urls           import router as dias_no_laborables_router
from apps.feriados.urls                     import router as feriados_router

schema_view = get_schema_view(
    openapi.Info(
        title           = 'Paradigma - Plaza Control API',
        default_version = 'v1.0',
        description     = 'Documentacion API REST para Paradigma - Plaza Control',
    ),
    public=True,
    permission_classes=[IsSuper],
)

router = routers.DefaultRouter()

# Registra los routers de las aplicaciones en el router de nivel superior
router.registry.extend(cooperativas_router.registry)
router.registry.extend(trabajadores_router.registry)
router.registry.extend(cuestionarios_router.registry)
router.registry.extend(dias_no_laborables_router.registry)
router.registry.extend(feriados_router.registry)

router.register(r'user',                                    UserRegisterationViewSet,                               basename='user')
router.register(r'usertype',                                UserTypeViewSet,                                        basename='usertype')
router.register(r'login',                                   UserLoginViewSet,                                       basename='login')
router.register(r'logout',                                  UserLogoutViewSet,                                      basename='logout')

router.register(r'planes_trabajo',                          PlanTrabajoViewSet,                                     basename='plantrabajo')

router.register(r'incidentes',                              IncidenteViewSet,                                       basename='incidentes')
#router.register(r'incidentes_mes',                          IncidentByMonthViewSet,                                 basename='incidentes_por_mes')

router.register(r'evaluaciones_trabajadores',               EvaluacionTrabajadorViewSet,                            basename='evaluaciones_trabajador')
router.register(r'planillas_trabajo',                       PlanillaTrabajoViewSet,                                 basename='planillas_trabajo')
#router.register(r'presentes',                               PresenteViewSet,                                        basename='presente')

router.register(r'trabajadores_por_id_plantrabajo',         TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet,    basename='trabajadores_por_id_plantrabajo')

router.register(r'respuestas_cuestionario',                 RespuestaCuestionarioViewSet,                           basename='respuesta_cuestionario')
router.register(r'evaluaciones_desempenio',                 EvaluacionDesempeñoViewSet,                             basename='evaluacion_desempenio')

#router.register(r'presentes_por_espacio_trabajo_hoy',       PresentesPorEspacioDeTrabajo,                           basename='presentes_por_espacio_trabajo_hoy')
#router.register(r'asistencias_entre_fechas_por_trabajador', PresentesEntreFechasPorIdTrabajador,                    basename='asistencias_entre_fechas_por_trabajador')

router.registry.sort(key=lambda x: x[0])

router.get_api_root_view().cls.__name__ = 'ParadigmaPlazaControlApiRoot'
router.get_api_root_view().cls.__doc__  = 'Documentacion en /snippets & /doc&test'
router.get_api_root_view().cls.permission_classes = [IsAuthenticated]

urlpatterns = [
    path('', include(router.urls)),

    path(r'snippets/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(r'doc&test/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
