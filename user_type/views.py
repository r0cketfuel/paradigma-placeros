from rest_framework import viewsets
from .models import UserType
from .serializer import UserTypeSerializer
from rest_framework.permissions import IsAuthenticated


class UserTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
    permission_classes = [IsAuthenticated]
