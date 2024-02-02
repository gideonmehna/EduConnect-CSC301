from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, SET_NULL

from Accounts.models import UserProfile


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=50)
    serving = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images/recipe/',
                              default='default/easychef.png')
    prep_time = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=50)
    owner = models.ForeignKey(to=UserProfile, null = False, related_name = 'Recipes', on_delete=CASCADE)

    def __str__(self):
        return self.name

class Step(models.Model):
    number = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images/steps/', default='default/easychef.png')
    description = models.CharField(max_length=250)
    recipe_ID = models.ForeignKey(to=Recipe, null=False,
                              related_name='step_list', on_delete=CASCADE)
    def __str__(self):
        return "%s: %s" % (self.number, self.description)

class Diet(models.Model):
    name = models.CharField(max_length=50, unique=True)
    recipe_ID = models.ManyToManyField(to=Recipe, related_name='diets')



    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    TSP = 'Tablespoon'
    TS = 'Teaspoon'
    OZ = 'Ounces'
    LB = 'Pounds'
    ML = 'Milliliter'
    MG = 'Milligram'
    G = 'Gram'
    C = 'Cup'

    CHOICES = (
        (TSP, TSP),
        (TS, TS),
        (OZ, OZ),
        (LB, LB),
        (ML, ML),
        (MG, MG),
        (G, G),
        (C, C),
    )

    amount_type = models.CharField(max_length=20, choices=CHOICES, default=G)
    recipe_ID = models.ManyToManyField(to=Recipe, related_name='Ingredients')

    def __str__(self):
        return self.name





