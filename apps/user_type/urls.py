from django.urls            import path, include
from rest_framework.routers import DefaultRouter
from apps.user_type.views   import UserTypeViewSet

router = DefaultRouter()
router.register(r'usertype', UserTypeViewSet, basename='usertype')

urlpatterns = [
    path('', include(router.urls)),
]
