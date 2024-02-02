from django.db import models

# Create your models here.
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.db.models import CASCADE
from django.db.models.signals import post_save


class UserProfile(AbstractUser):
    phone_number = models.CharField(max_length=20)
    avatar = models.ImageField(blank=True, upload_to='images/', default='default/avatar.png')

    def __str__(self):
        return f"{self.username}'s profile"



