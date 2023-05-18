import os

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"))
    name = models.TextField(default="")
    last_name = models.TextField(default="")
    dni = models.IntegerField(unique=True)

    USERNAME_FIELD = "dni"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username


def get_image_filename(instance, filename):
    name = instance.product.name
    slug = slugify(name)
    return f"products/{slug}-{filename}"


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_image_filename, blank=True)
    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.name

    @property
    def filename(self):
        return os.path.basename(self.user.name)
