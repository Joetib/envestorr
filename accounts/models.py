from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    picture = models.ImageField(upload_to="users/%Y/")

    def __str__(self):
        return self.email



