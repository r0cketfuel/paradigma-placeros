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
from planilla_trabajo.views import PlanillaTrabajoViewSet
from cuestionario.views import CuestionarioViewSet
from respuesta_cuestionario.views import RespuestaCuestionarioViewSet
from evaluacion_desempeño.views import EvaluacionDesempeñoViewSet


router = routers.DefaultRouter()
router.register(r'login', UserLoginViewSet, basename='login')
router.register(r'logout', UserLogoutViewSet, basename='logout')
router.register(r'user', UserRegisterationViewSet, basename='user')
router.register(r'usertype', UserTypeViewSet, basename='usertype')
router.register(r'cooperativa', CooperativaViewSet, basename='cooperativa')
router.register(r'espacio_trabajo', EspacioTrabajoViewSet,
                basename='espacio_trabajo')
router.register(r'plandetrabajo', PlanTrabajoViewSet,
                basename='plandetrabajo')
router.register(r'incidente', IncidenteViewSet,
                basename='incidente')
router.register(r'trabajador', TrabajadorViewSet,
                basename='trabajador')
router.register(r'evaluacion', EvaluacionTrabajadorViewSet,
                basename='evaluacion')
router.register(r'planilla_trabajo', PlanillaTrabajoViewSet,
                basename='planilla_trabajo')
router.register(r'cuestionario', CuestionarioViewSet,
                basename='cuestionario')
router.register(r'respuesta_cuestionario', RespuestaCuestionarioViewSet,
                basename='respuesta_cuestionario')
router.register(r'evaluacion_desempeño', EvaluacionDesempeñoViewSet,
                basename='evaluacion_desempeño')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('', include(router.urls)),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
