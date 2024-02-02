import json

from django.http import JsonResponse, QueryDict
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions, authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Recipes.Trie import trie

from Recipes.models import Diet, Ingredient, Recipe, Step
from Recipes.serializers import DietSerializer, IngredientSerializer, \
    RecipeSerializer, StepSerializer


class RecipesView(ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.all()


class IngredientsView(ListAPIView):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        return Ingredient.objects.filter(recipe_ID=self.kwargs['recipe_id'])


class StepsView(ListAPIView):
    serializer_class = StepSerializer

    def get_queryset(self):
        return Step.objects.filter(recipe_ID=self.kwargs['recipe_id'])



class AllDiets(ListAPIView):
    serializer_class = DietSerializer

    def get_queryset(self):
        return Diet.objects.filter(recipe_ID=self.kwargs['recipe_id'])


class CreateRecipeView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        data = QueryDict('', mutable=True)
        data['owner'] = self.request.user.id
        data.update(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class CreateStepView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StepSerializer

    def create(self, request, *args, **kwargs):
        data = QueryDict('', mutable=True)
        data['recipe_ID'] = self.kwargs['recipe_id']
        data.update(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)




class CreateIngredientView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IngredientSerializer

    def create(self, request, *args, **kwargs):
        data = QueryDict('', mutable=True)
        data['recipe_ID'] = self.kwargs['recipe_id']
        data.update(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class CreateDietView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DietSerializer



class AccessRecipeView(RetrieveAPIView):
    serializer_class = RecipeSerializer

    def get_object(self):
        return get_object_or_404(Recipe, id=self.kwargs['recipe_id'])




@csrf_exempt
@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def UpdateRecipeView(request, *args, **kwargs):
    jresponse = {}
    r = get_object_or_404(Recipe, id=kwargs['recipe_id'])
    if request.method == 'POST':
        if name := request.data.get('name', None):
            r.name = name
            jresponse['name'] = name
        if cuisine := request.data.get('cuisine', None):
            r.cuisine = cuisine
            jresponse['cuisine'] = cuisine
        if serving := request.data.get('serving', None):
            r.serving = serving
            jresponse['serving'] = serving
        if step_list := request.data.get('step_list', None):
            r.step_list = step_list
            jresponse['step_list'] = step_list
        if prep_time := request.data.get('prep_time', None):
            r.prep_time = prep_time
            jresponse['prep_time'] = prep_time
        if cook_time := request.data.get('cook_time', None):
            r.cook_time = cook_time
            jresponse['cook_time'] = cook_time
        if image := request.FILES['image']:
            r.image = image


    r.save()
    return JsonResponse(jresponse)


@csrf_exempt
@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def UpdateIngredientView(request, *args, **kwargs):
    jresponse = {}
    r = get_object_or_404(Ingredient, id=kwargs['id'])
    if request.method   == 'POST':
        if name := request.data.get('name', None):
            r.name = name
            jresponse['name'] = name
        if amount := request.data.get('amount', None):
            r.amount = amount
            jresponse['amount'] = amount
        if amount_type := request.data.get('amount_type', None):
            r.amount_type = amount_type
            jresponse['amount_type'] = amount_type
        if recipe_ID := request.data.get('recipe_ID', None):
            r.recipe_ID = get_object_or_404(Recipe, id=recipe_ID)
            jresponse['recipe_ID'] = recipe_ID

    r.save()
    return JsonResponse(jresponse)


@csrf_exempt
@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def UpdateStepView(request, *args, **kwargs):
    jresponse = {}
    r = get_object_or_404(Step, id=kwargs['id'])
    if request.method   == 'POST':
        if number := request.data.get('number', None):
            r.number = number
            jresponse['number'] = number
        if description := request.data.get('description', None):
            r.description = description
            jresponse['description'] = description
        if image := request.FILES['image']:
            r.image = image

    r.save()
    return JsonResponse(jresponse)


@csrf_exempt
@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def UpdateDietView(request, *args, **kwargs):
    r = get_object_or_404(Diet, id=kwargs['id'])
    if request.method  == 'POST':

        if rid := request.data.get('recipe_ID', None):
            r.recipe_ID.remove(rid)
    r.save()
    return Response(status=204)

@csrf_exempt
@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def AddDietView(request, *args, **kwargs):
    r = get_object_or_404(Diet, name=kwargs['name'])
    if request.method  == 'POST':

        if rid := request.data.get('recipe_ID', None):
            r.recipe_ID.add(rid)

    r.save()
    return Response(status=204)



@csrf_exempt
@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def AddIngredientView(request, *args, **kwargs):
    r = get_object_or_404(Ingredient, name=kwargs['name'])
    if request.method  == 'POST':

        if rid := request.data.get('recipe_ID', None):
            r.recipe_ID.add(rid)

    r.save()
    return Response(status=204)

class GetDiets(ListAPIView):
    serializer_class = DietSerializer

    def get_queryset(self):
        return Diet.objects.all()
    

class GetDietId(RetrieveAPIView):
    serializer_class = DietSerializer

    def get_object(self):
        return get_object_or_404(Diet, name=self.kwargs['diet'])


@csrf_exempt
@api_view(('POST',))
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def DeleteRecipe(request, *args, **kwargs):
    if request.method == 'POST':
        r = get_object_or_404(Recipe, id=kwargs['recipe_id'])
        r.delete()
        return Response(status=204)
    return Response(status=405)


@csrf_exempt
@api_view(('POST',))
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def DeleteIngredient(request, *args, **kwargs):
    if request.method == 'POST':
        r = get_object_or_404(Ingredient, id=kwargs['id'])
        r.delete()
        return Response(status=204)
    return Response(status=405)


@csrf_exempt
@api_view(('POST',))
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def DeleteStep(request, *args, **kwargs):
    if request.method == 'POST':
        r = get_object_or_404(Step, id=kwargs['id'])
        r.delete()
        return Response(status=204)
    return Response(status=405)




@csrf_exempt
@api_view(('POST',))
def AutoComplete(request, *args, **kwargs):
    jresponse = {}
    if request.method == 'POST':
        if ingredient := request.data.get('ingredient', None):
            lst = trie.autoComplete(ingredient)
            lst2 = trie.autoCorrect(ingredient, errorMax=10)
            jresponse['auto_correct'] = lst2
            jresponse['auto_complete'] = lst
            jresponse['response'] = lst + list(set(lst2) - set(lst))

        if recipe := request.data.get('recipe', None):
            lst = trie.autoComplete(ingredient)
            lst2 = trie.autoCorrect(ingredient, errorMax=10)
            jresponse['auto_correct'] = lst2
            jresponse['auto_complete'] = lst
            jresponse['response'] = lst + list(set(lst2) - set(lst))
        return JsonResponse(jresponse)
    return Response(status=405)

