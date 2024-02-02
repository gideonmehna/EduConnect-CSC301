from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from Recipes.models import Recipe
from ShoppingCart.models import ShoppingCart

class ShoppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = ['id', 'recipe', 'owner']

    # def create(self, validated_data):
    #     recipes = validated_data.get('recipe')
    #
    #     for i in recipes:
    #         recipe = get_object_or_404(Recipe, id=i.id)

