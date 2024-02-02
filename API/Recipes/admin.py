from django.contrib import admin
from Recipes.models import Recipe, Ingredient, Diet, Step

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Diet)
admin.site.register(Step)
