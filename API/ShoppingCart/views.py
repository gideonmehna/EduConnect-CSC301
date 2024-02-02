from django.http import JsonResponse, QueryDict
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from Recipes.models import Recipe, Ingredient
from ShoppingCart.models import ShoppingCart
from ShoppingCart.serializers import ShoppingSerializer

#
class CreateShoppingCartView(CreateAPIView):
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ShoppingSerializer

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




@csrf_exempt
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def RetrieveShoppingCartView(request, *args, **kwargs):
    if request.method == 'GET':
        s = get_object_or_404(ShoppingCart, owner=request.user.id)
        lst = []
        for r in s.recipe.all():
            lst.append(r.id)

        return JsonResponse({'recipes': lst})
    return Response(status=405)



@csrf_exempt
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def RemoveItemView(request, *args, **kwargs):
    s = get_object_or_404(ShoppingCart, owner=request.user.id)
    if request.method  == 'GET':
        if rid := kwargs['recipe_ID']:
            s.recipe.remove(rid)
    s.save()
    return Response(status=204)


@csrf_exempt
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def AddItemView(request, *args, **kwargs):
    print("is this shit even running")
    s = get_object_or_404(ShoppingCart, owner=request.user.id)
    if request.method  == 'GET':
        if rid := kwargs['recipe_ID']:
            print("rid", rid)
            print("before", s.recipe)
            s.recipe.add(rid)
            print("after", s.recipe)
    s.save()
    return Response(status=204)







