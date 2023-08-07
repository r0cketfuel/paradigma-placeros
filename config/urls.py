from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from users.views import UserRegisterationViewSet, UserLoginViewSet, UserLogoutViewSet
from user_type.views import UserTypeViewSet
from cooperativa.views import CooperativaViewSet, EmpleadosPorCooperativa
from espacio_trabajo.views import EspacioTrabajoViewSet, PresentesPorEspacioDeTrabajo
from plan_trabajo.views import PlanTrabajoViewSet
from incidente.views import IncidentViewSet, IncidentByMonthViewSet
from trabajador.views import TrabajadorViewSet, TrabajadoresCargadosViewSet
from evaluacion_trabajador.views import EvaluacionTrabajadorViewSet
from planilla_trabajo.views import PlanillaTrabajoViewSet, PresenteViewSet, TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet
from cuestionario.views import CuestionarioViewSet
from respuesta_cuestionario.views import RespuestaCuestionarioViewSet
from evaluacion_desempeño.views import EvaluacionDesempeñoViewSet
from feriados.views import FeriadoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from user_type.permisions import IsSuper

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
routes.register(r'evaluacion_desempeño', EvaluacionDesempeñoViewSet,
                basename='evaluacion_desempeño')
routes.register(r'trabajadores_cargados', TrabajadoresCargadosViewSet,
                basename='trabajadores_cargados')
routes.register(r'empleados_por_cooperativa', EmpleadosPorCooperativa,
                basename='empleados_por_cooperativa')
routes.register(r'presentes_por_espacio_trabajo_hoy', PresentesPorEspacioDeTrabajo,
                basename='presentes_por_espacio_trabajo_hoy')
routes.register(r'incidentes_por_mes', IncidentByMonthViewSet,
                basename='incidentes_por_mes')
routes.register(r'feriados', FeriadoViewSet)

routes.registry.sort(key=lambda x: x[0])


routes.get_api_root_view().cls.__name__ = "Paradigma Plaza Control Api Root"
routes.get_api_root_view().cls.__doc__ = "Documentation in /snippets & /doc&test"


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def paradigma_plaza_control_api_root(request, format=None):
    """
    Documentation:
    /snippets
    /doc&test
    """
    if request.user.is_authenticated:
        # Si el usuario está autenticado, muestra las rutas protegidas
        data = {
            'users': reverse('user-list', request=request, format=format),
            'usertypes': reverse('usertype-list', request=request, format=format),
            'cooperativa': reverse('cooperativa-list', request=request, format=format),
            'espacio_trabajo': reverse('espacio_trabajo-list', request=request, format=format),
            'plandetrabajo': reverse('plandetrabajo-list', request=request, format=format),
            'incidente': reverse('incidente-list', request=request, format=format),
            'trabajador': reverse('trabajador-list', request=request, format=format),
            'evaluacion': reverse('evaluacion-list', request=request, format=format),
            'planilla_trabajo': reverse('planilla_trabajo-list', request=request, format=format),
            'presente': reverse('presente-list', request=request, format=format),
            'trabajadores_por_id_plantrabajo': reverse('trabajadores_por_id_plantrabajo-list', request=request, format=format),
            'cuestionario': reverse('cuestionario-list', request=request, format=format),
            'respuesta_cuestionario': reverse('respuesta_cuestionario-list', request=request, format=format),
            'evaluacion_desempeño': reverse('evaluacion_desempeño-list', request=request, format=format),
            'trabajadores_cargados': reverse('trabajadores_cargados-list', request=request, format=format),
            'empleados_por_cooperativa': reverse('empleados_por_cooperativa-list', request=request, format=format),
            'presentes_por_espacio_trabajo_hoy': reverse('presentes_por_espacio_trabajo_hoy-list', request=request, format=format),
            'incidentes_por_mes': reverse('incidentes_por_mes-list', request=request, format=format),
            'feriados': reverse('feriado-list', request=request, format=format),
        }
        return Response(data)
    else:
        # Si el usuario no está autenticado, redirige a la página de autenticación
        return Response({
            'auth': reverse('api-auth:login', request=request, format=format),
        })


urlpatterns = [
    path('', paradigma_plaza_control_api_root, name='api-root'),
    path(r'snippets/', schema_view.with_ui('redoc',
                                           cache_timeout=0), name='schema-redoc'),
    path(r'doc&test/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path("api-auth/", include("rest_framework.urls")),
    path('', include(routes.urls)),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
