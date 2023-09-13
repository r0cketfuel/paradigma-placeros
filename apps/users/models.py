
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.user_type.models import UserType
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Usuario personalizado de la aplicación.

    Esta clase define un usuario personalizado que extiende la funcionalidad de
    la clase AbstractUser de Django. Los usuarios personalizados tienen campos
    adicionales como el DNI, el tipo de usuario y se autentican utilizando el DNI
    como campo de inicio de sesión.

    Atributos:
    - email: Dirección de correo electrónico del usuario.
    - name: Nombre del usuario.
    - last_name: Apellido del usuario.
    - dni: Número de DNI del usuario (debe ser único).
    - type_user: Tipo de usuario al que pertenece el usuario.
    - USERNAME_FIELD: Campo utilizado para iniciar sesión (DNI en este caso).
    - REQUIRED_FIELDS: Campos requeridos para la creación de usuarios.
    - objects: Gestor personalizado de usuarios.

    Métodos:
    - __str__: Devuelve una representación de cadena del usuario en el formato "apellido, nombre".

    """
    email = models.EmailField(_("email address"))
    name = models.TextField(default="")
    last_name = models.TextField(default="")
    dni = models.IntegerField(unique=True)
    type_user = models.ForeignKey(
        UserType, default=1, null=False, on_delete=models.CASCADE)  # type: ignore

    USERNAME_FIELD = "dni"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.last_name}, {self.name}"
