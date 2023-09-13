from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from apps.users.views import UserRegisterationViewSet, UserLoginViewSet, UserLogoutViewSet
from apps.user_type.views import UserTypeViewSet
from apps.cooperativa.views import CooperativaViewSet, EmpleadosPorCooperativa
from apps.espacio_trabajo.views import EspacioTrabajoViewSet, PresentesPorEspacioDeTrabajo
from apps.plan_trabajo.views import PlanTrabajoViewSet
from apps.incidente.views import IncidentViewSet, IncidentByMonthViewSet
from apps.trabajador.views import TrabajadorViewSet, TrabajadoresCargadosViewSet
from apps.evaluacion_trabajador.views import EvaluacionTrabajadorViewSet
from apps.planilla_trabajo.views import (
    PlanillaTrabajoViewSet,
    PresenteViewSet,
    TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet,
    PresentesEntreFechasPorIdTrabajador
)
from apps.cuestionario.views import CuestionarioViewSet
from apps.respuesta_cuestionario.views import RespuestaCuestionarioViewSet
from apps.evaluacion_desempeño.views import EvaluacionDesempeñoViewSet
from apps.feriados.views import FeriadoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.user_type.permisions import IsSuper

schema_view = get_schema_view(
    openapi.Info(
        title="Paradigma - Plaza COntrol API",
        default_version='v1',
        description="documentacion API REST para Paradigma -  Plaza Control ",
    ),
    public=True,
    permission_classes=[IsSuper],
)


routes = routers.DefaultRouter()
routes.register(r'login', UserLoginViewSet, basename='login')
routes.register(r'logout', UserLogoutViewSet, basename='logout')
routes.register(r'user', UserRegisterationViewSet, basename='user')
routes.register(r'usertype', UserTypeViewSet, basename='usertype')
routes.register(r'cooperativa', CooperativaViewSet, basename='cooperativa')
routes.register(r'espacio_trabajo', EspacioTrabajoViewSet,
                basename='espacio_trabajo')
routes.register(r'plandetrabajo', PlanTrabajoViewSet,
                basename='plandetrabajo')
routes.register(r'incidente', IncidentViewSet,
                basename='incidente')
routes.register(r'trabajador', TrabajadorViewSet,
                basename='trabajador')
routes.register(r'evaluacion', EvaluacionTrabajadorViewSet,
                basename='evaluacion')
routes.register(r'planilla_trabajo', PlanillaTrabajoViewSet,
                basename='planilla_trabajo')
routes.register(r'presente', PresenteViewSet,
                basename='presente')
routes.register(r'trabajadores_por_id_plantrabajo', TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet,
                basename='trabajadores_por_id_plantrabajo')
routes.register(r'cuestionario', CuestionarioViewSet,
                basename='cuestionario')
routes.register(r'respuesta_cuestionario', RespuestaCuestionarioViewSet,
                basename='respuesta_cuestionario')
routes.register(r'evaluacion_desempenio', EvaluacionDesempeñoViewSet,
                basename='evaluacion_desempenio')
routes.register(r'trabajadores_cargados', TrabajadoresCargadosViewSet,
                basename='trabajadores_cargados')
routes.register(r'empleados_por_cooperativa', EmpleadosPorCooperativa,
                basename='empleados_por_cooperativa')
routes.register(r'presentes_por_espacio_trabajo_hoy', PresentesPorEspacioDeTrabajo,
                basename='presentes_por_espacio_trabajo_hoy')
routes.register(r'incidentes_por_mes', IncidentByMonthViewSet,
                basename='incidentes_por_mes')
routes.register(r'feriados', FeriadoViewSet)
routes.register(r'asistencias_entre_fechas_por_trabajador', PresentesEntreFechasPorIdTrabajador, basename='asistencias_entre_fechas_por_trabajador')

routes.registry.sort(key=lambda x: x[0])


routes.get_api_root_view().cls.__name__ = "Paradigma Plaza Control Api Root"
routes.get_api_root_view().cls.__doc__ = "Documentacion en /snippets & /doc&test"
routes.get_api_root_view().cls.permission_classes = [IsAuthenticated]

urlpatterns = [
    path(r'snippets/', schema_view.with_ui('redoc',
                                           cache_timeout=0), name='schema-redoc'),
    path(r'doc&test/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path("api-auth/", include("rest_framework.urls")),
    path('', include(routes.urls)),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
