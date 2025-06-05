from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birhdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.username}"
