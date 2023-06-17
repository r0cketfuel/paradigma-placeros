from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users.views import UserRegisterationViewSet, UserLoginViewSet, UserLogoutViewSet
from user_type.views import UserTypeViewSet
from cooperativa.views import CooperativaViewSet
from espacio_trabajo.views import EspacioTrabajoViewSet
from plan_trabajo.views import PlanTrabajoViewSet
from incidente.views import IncidenteViewSet
from trabajador.views import TrabajadorViewSet
from evaluacion_trabajador.views import EvaluacionTrabajadorViewSet
from planilla_trabajo.views import PlanillaTrabajoViewSet, PresenteViewSet, TrabajadoresInPlanillaTrabajoByIdPlanTrabajoViewSet
from cuestionario.views import CuestionarioViewSet
from respuesta_cuestionario.views import RespuestaCuestionarioViewSet
from evaluacion_desempeño.views import EvaluacionDesempeñoViewSet


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
routes.register(r'incidente', IncidenteViewSet,
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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('', include(routes.urls)),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
