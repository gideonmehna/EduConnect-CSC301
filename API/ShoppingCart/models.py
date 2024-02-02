from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, SET_NULL

from Accounts.models import UserProfile
from Recipes.models import Recipe


class ShoppingCart(models.Model):
    recipe = models.ManyToManyField(to=Recipe, null=False)
    owner = models.OneToOneField(to=UserProfile, null = False, related_name='ShoppingCart', on_delete=CASCADE)

    def __str__(self):
        return f"{self.owner}'s shopping cart"
