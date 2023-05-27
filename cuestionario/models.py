from django.db import models


class Cuestionario(models.Model):
    description = models.TextField()
    question = models.TextField()

    def __str__(self):
        return self.description
# TODO
# IMPLEMENT CLASSMETHOD FOR GET PK USERS
