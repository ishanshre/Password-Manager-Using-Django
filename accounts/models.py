from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank = True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_avatar', blank=True, null=True)
    body = models.TextField()
    address = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user.first_name} {self.last_name}"
