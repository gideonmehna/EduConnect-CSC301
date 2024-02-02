from rest_framework import serializers

from Recipes.models import Recipe, Diet, Ingredient, Step


class RecipeSerializer(serializers.ModelSerializer):
    step_list = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    diets  = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'owner', 'cuisine', 'image','diets','serving', 'step_list', 'prep_time', 'cook_time']


class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ['id', 'number', 'description','image', 'recipe_ID']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'recipe_ID', 'amount', 'amount_type']


class DietSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diet
        fields = ['id', 'name',]
