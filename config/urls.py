from rest_framework_simplejwt.views import TokenRefreshView
from users import views
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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('', include(router.urls)),
    # path("register/", UserRegisterationViewSet, name="create-user"),
    # path("login/", UserLoginViewSet, name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    # path("logout/", UserLogoutViewSet, name="logout-user"),
    path("", views.UserAPIView.as_view(), name="user-info"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
