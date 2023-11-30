from rest_framework import permissions

from .models import UserType

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
POST_METHOD = ('POST',)


class IsSuper(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            return request.user.type_user == UserType.objects.filter(id=UserType.get_super_pk()).first()


class IsAdministrador(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_anonymous:
            return False
        else:
            return request.user.type_user == UserType.objects.filter(id=UserType.get_administrador_pk()).first()


class IsSupervisor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            if request.user.type_user == UserType.objects.filter(id=UserType.get_supervisor_pk()).first():
                if request.method in SAFE_METHODS:
                    return True
            return False


class IsCoordinador(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            if request.user.type_user == UserType.objects.filter(id=UserType.get_coordinador_pk()).first():
                if request.method in SAFE_METHODS:
                    return True
            return False
