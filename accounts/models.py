from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        HOUSEHOLD_USER = "HOUSEHOLD_USER", "Household user"
        HOUSEHOLD_ADMIN = "HOUSEHOLD_ADMIN", "Household administrator"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.HOUSEHOLD_USER,
    )

    household_name = models.CharField(max_length=100, blank=True, null=True)