from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users.views import UserRegisterationViewSet
from posts.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'user', UserRegisterationViewSet, basename='user')
router.register(r'post', PostViewSet, basename='post')
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # path("", include("users.urls", namespace="users")),
    path('', include(router.urls)),
    path("post/", include("posts.urls", namespace="posts")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
