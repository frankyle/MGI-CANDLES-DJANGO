from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    # Extend the default User model with additional fields
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    work = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
