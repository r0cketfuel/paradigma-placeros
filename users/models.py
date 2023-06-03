
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from user_type.models import UserType
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"))
    name = models.TextField(default="")
    last_name = models.TextField(default="")
    dni = models.IntegerField(unique=True)
    type_user = models.ForeignKey(
        UserType, default=1, null=False, on_delete=models.CASCADE)

    USERNAME_FIELD = "dni"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
