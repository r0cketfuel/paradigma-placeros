from django.contrib.auth.base_user  import BaseUserManager
from django.utils.translation       import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Gestor personalizado de usuarios.

    Este gestor se utiliza para crear y gestionar usuarios personalizados en la aplicación.
    Define métodos para crear usuarios y superusuarios, estableciendo los campos necesarios
    como el DNI y la contraseña. También proporciona métodos para definir las propiedades
    de los usuarios, como el estado de activo, el estado de personal de staff y el estado de superusuario.

    Métodos:
    - create_user: Crea un usuario normal con DNI y contraseña.
    - create_superuser: Crea un superusuario con DNI y contraseña y establece las propiedades de staff y superusuario.

    """

    def create_user(self, dni, password, **extra_fields):
        if not dni:
            raise ValueError(_("Users must have an email address"))
        dni = dni
        user = self.model(dni=dni, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, dni, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(dni, password, **extra_fields)
