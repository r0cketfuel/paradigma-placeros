from django.conf                            import settings
from django.conf.urls.static                import static
from django.urls                            import include, path
from rest_framework.permissions             import IsAuthenticated
from rest_framework_simplejwt.views         import TokenRefreshView
from rest_framework                         import routers
from apps.users.views                       import UserRegisterationViewSet, UserLoginViewSet, UserLogoutViewSet
from apps.user_type.views                   import UserTypeViewSet
from apps.cooperativas.views                import CooperativaViewSet, CantidadTrabajadoresPorCooperativa
from apps.espacios_trabajo.views            import EspacioTrabajoViewSet, PresentesPorEspacioDeTrabajo
from apps.planes_trabajo.views              import PlanTrabajoViewSet
from apps.incidentes.views                  import IncidenteViewSet, IncidentByMonthViewSet
from apps.trabajadores.views                import TrabajadorViewSet, CantidadTrabajadoresCargadosViewSet, CantidadTrabajadoresActivosViewSet
from apps.evaluacion_trabajador.views       import EvaluacionTrabajadorViewSet
from apps.planillas_trabajo.views           import PlanillaTrabajoViewSet, TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet, PresentesEntreFechasPorIdTrabajador
from apps.cuestionarios.views               import CuestionarioViewSet
from apps.respuestas_cuestionarios.views    import RespuestaCuestionarioViewSet
from apps.evaluaciones_desempeño.views      import EvaluacionDesempeñoViewSet
from apps.feriados.views                    import FeriadoViewSet
from apps.dias_no_laborables.views          import DiaNoLaborableViewSet
from apps.user_type.permisions              import IsSuper
from drf_yasg.views                         import get_schema_view
from drf_yasg                               import openapi

schema_view = get_schema_view(
    openapi.Info(
        title           = 'Paradigma - Plaza Control API',
        default_version = 'v1.0',
        description     = 'Documentacion API REST para Paradigma - Plaza Control',
    ),
    public=True,
    permission_classes=[IsSuper],
)

routes = routers.DefaultRouter()

routes.register(r'user',                                    UserRegisterationViewSet,                               basename='user')
routes.register(r'usertype',                                UserTypeViewSet,                                        basename='usertype')
routes.register(r'login',                                   UserLoginViewSet,                                       basename='login')
routes.register(r'logout',                                  UserLogoutViewSet,                                      basename='logout')

routes.register(r'feriados',                                FeriadoViewSet,                                         basename='feriados')
routes.register(r'dias_no_laborables',                      DiaNoLaborableViewSet,                                  basename='dias_no_laborables')

routes.register(r'cooperativas',                            CooperativaViewSet,                                     basename='cooperativa')

routes.register(r'espacios_trabajo',                        EspacioTrabajoViewSet,                                  basename='espacio_trabajo')
routes.register(r'planes_trabajo',                          PlanTrabajoViewSet,                                     basename='plantrabajo')

routes.register(r'incidentes',                              IncidenteViewSet,                                       basename='incidentes')
#routes.register(r'incidentes_mes',                          IncidentByMonthViewSet,                                 basename='incidentes_por_mes')

routes.register(r'trabajadores',                            TrabajadorViewSet,                                      basename='trabajadores')
routes.register(r'evaluaciones_trabajadores',               EvaluacionTrabajadorViewSet,                            basename='evaluaciones_trabajador')
routes.register(r'planillas_trabajo',                       PlanillaTrabajoViewSet,                                 basename='planillas_trabajo')
#routes.register(r'presentes',                               PresenteViewSet,                                        basename='presente')

routes.register(r'trabajadores_por_id_plantrabajo',         TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet,    basename='trabajadores_por_id_plantrabajo')
routes.register(r'cuestionarios',                           CuestionarioViewSet,                                    basename='cuestionario')
routes.register(r'respuestas_cuestionario',                 RespuestaCuestionarioViewSet,                           basename='respuesta_cuestionario')
routes.register(r'evaluaciones_desempenio',                 EvaluacionDesempeñoViewSet,                             basename='evaluacion_desempenio')

#====================#
# Rutas estadísticas #
#====================#
routes.register(r'cantidad_trabajadores_cargados',          CantidadTrabajadoresCargadosViewSet,                    basename='cantidad_trabajadores_cargados')
routes.register(r'cantidad_trabajadores_activos',           CantidadTrabajadoresActivosViewSet,                     basename='cantidad_trabajadores_activos')
routes.register(r'cantidad_trabajadores_cooperativas',      CantidadTrabajadoresPorCooperativa,                     basename='cantidad_trabajadores_cooperativa')

#routes.register(r'presentes_por_espacio_trabajo_hoy',       PresentesPorEspacioDeTrabajo,                           basename='presentes_por_espacio_trabajo_hoy')
#routes.register(r'asistencias_entre_fechas_por_trabajador', PresentesEntreFechasPorIdTrabajador,                    basename='asistencias_entre_fechas_por_trabajador')

routes.registry.sort(key=lambda x: x[0])

routes.get_api_root_view().cls.__name__ = 'ParadigmaPlazaControlApiRoot'
routes.get_api_root_view().cls.__doc__  = 'Documentacion en /snippets & /doc&test'
routes.get_api_root_view().cls.permission_classes = [IsAuthenticated]

urlpatterns = [
    path(r'snippets/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path(r'doc&test/', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(routes.urls)),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
