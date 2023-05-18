from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users.views import UserRegisterationViewSet
from user_type.views import UserTypeViewSet
from cooperativa.views import CooperativaViewSet
from espacio_trabajo.views import EspacioTrabajoViewSet

router = routers.DefaultRouter()
router.register(r'user', UserRegisterationViewSet, basename='user')
router.register(r'usertype', UserTypeViewSet, basename='usertype')
router.register(r'cooperativa', CooperativaViewSet, basename='cooperativa')
router.register(r'espacio_trabajo', EspacioTrabajoViewSet,
                basename='espacio_trabajo')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
