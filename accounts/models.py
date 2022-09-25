from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank = True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
