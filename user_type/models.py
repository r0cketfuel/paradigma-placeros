from django.db import models


class UserType(models.Model):
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.description

    @classmethod
    def get_super_pk(cls):
        try:
            id_tipo_agente = 0
            tipo_agente = UserType.objects.filter(
                description='Super').first()
            if tipo_agente is not None:
                id_tipo_agente = tipo_agente.id  # type: ignore
            return id_tipo_agente
        except Exception:
            return 0

    @classmethod
    def get_administrador_pk(cls):
        try:
            id_tipo_agente = 0
            tipo_agente = UserType.objects.filter(
                t='Administrador').first()
            if tipo_agente is not None:
                id_tipo_agente = tipo_agente.id  # type: ignore
            return id_tipo_agente
        except Exception:
            return 0

    @classmethod
    def get_supervisor_pk(cls):
        try:
            id_tipo_agente = 0
            tipo_agente = UserType.objects.filter(
                t='Supervisor').first()
            if tipo_agente is not None:
                id_tipo_agente = tipo_agente.id  # type: ignore
            return id_tipo_agente
        except Exception:
            return 0

    @classmethod
    def get_coordinador_pk(cls):
        try:
            id_tipo_agente = 0
            tipo_agente = UserType.objects.filter(
                description='Coordinador').first()
            if tipo_agente is not None:
                id_tipo_agente = tipo_agente.id  # type: ignore
            return id_tipo_agente
        except Exception:
            return 0
