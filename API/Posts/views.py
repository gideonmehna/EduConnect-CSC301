from django.db.models import Avg, Count
from django.http import JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, authentication, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404, ListAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json

from Accounts.models import UserProfile
from Posts.models import Post, Like, Favorite, Comment, Rating
from Posts.serializers import PostSerializer, LikeSerializer, FavoriteSerializer, CommentSerializer, RatingSerializer
from Recipes.models import Recipe, Ingredient


class GetPostView(RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self):
        print(f"pk: {self.kwargs['pk']}")
        return get_object_or_404(Post, id=self.kwargs['pk'])


class GetPostsView(ListAPIView, UpdateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        if filter:=self.kwargs.get('sort', None):
            if filter == 'ratings':
                posts = Post.objects.annotate(avg_rating=Avg('Rating__score')).order_by(
                    '-avg_rating')
                return posts
            elif filter == 'favorites':
                posts = Post.objects.annotate(num_favorites=Count('Favorited_by')).order_by('-num_favorites')
                return posts
        return Response(status=405)


class GetUserPostsView(ListAPIView, UpdateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(owner=self.kwargs.get("user", None))


class CreatePostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer


class DeletePostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class FavoritePostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def create(self, request, *args, **kwargs):
        data = QueryDict('', mutable=True)
        data['post'] = kwargs["post"]
        data['user'] = self.request.user.id
        data.update(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class GetPostFavoritesView(ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(post=self.kwargs.get("post", None))


class GetFavoritedPostsView(ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.kwargs.get('user', None))


class UnFavoritePostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavoriteSerializer

    def get_object(self):
        return get_object_or_404(Favorite, post=self.kwargs.get("post", None), user=self.request.user.id)


class LikePostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        data = QueryDict('', mutable=True)
        data['post'] = kwargs["post"]
        data['user'] = self.request.user.id
        data.update(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class GetPostLikesView(ListAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(post=self.kwargs.get("post", None))


class GetLikedPostsView(ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(user=self.kwargs.get("user", None))


class UnLikePostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def get_object(self):
        return get_object_or_404(Like, post=self.kwargs.get("post", None), user=self.request.user.id)


class CommentPostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        data = QueryDict('', mutable=True)
        data['post'] = kwargs["post"]
        data.update(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class GetCommentPostView(RetrieveAPIView):
    serializer_class = CommentSerializer

    def get_object(self):
        return get_object_or_404(Comment, id=self.kwargs.get("pk", None))


class EditCommentPostView(UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class GetCommentsPostView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs.get("post", None))


class GetCommentedPostsView(ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(user=self.kwargs.get("user", None))


class UnCommentPostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_object(self):
        return get_object_or_404(Comment, id=self.kwargs.get("pk", None), post=self.kwargs.get("post", None),
                                 user=self.request.data.get("user", None))


class RatePostView(CreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingSerializer

    def create(self, request, *args, **kwargs):
        data = QueryDict('', mutable=True)
        data['post'] = kwargs["post"]
        data['user'] = self.request.user.id
        data.update(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class GetRatePostView(RetrieveAPIView):
    serializer_class = RatingSerializer

    def get_object(self):
        return get_object_or_404(Rating, post=self.kwargs.get("post", None), user=self.request.user.id)


class GetRatingsPostView(ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(post=self.kwargs.get("post", None))


class EditRatingPostView(UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()


class UnRatePostView(DestroyAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingSerializer

    def get_object(self):
        return get_object_or_404(Rating, post=self.request.data.get("post", None),
                                 user=self.request.data.get("user", None))





@csrf_exempt
@api_view(('GET',))
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def MyRecipes(request, *args, **kwargs):
    if request.method == 'GET':
        fav = Favorite.objects.filter(user=request.user.id)
        likes = Like.objects.filter(user=request.user.id)
        comments = Comment.objects.filter(user=request.user.id)
        recipes = Recipe.objects.filter(owner=request.user.id)
        rated = Rating.objects.filter(user=request.user.id)
        lst = set()
        lst_create = set()
        lst_fav = set()
        for i in fav:
            lst.add(i.post.recipe.id)
            lst_fav.add(i.post.recipe.id)
        for i in likes:
            lst.add(i.post.recipe.id)
        for i in comments:
            lst.add(i.post.recipe.id)

        for i in recipes:
            lst.add(i.id)
            lst_create.add(i.id)

        for i in rated:
            lst.add(i.post.recipe.id)

        jresponse = {}
        jresponse["fav"] = json.dumps(list(lst_fav))
        jresponse["created"] = json.dumps(list(lst_create))
        jresponse["all"] = json.dumps(list(lst))
        return JsonResponse(jresponse, safe=False)
    return Response(status=405)


class SearchPostsView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        title = self.request.query_params.getlist('title')
        ingredient = self.request.query_params.getlist('ingredient')
        owner = self.request.query_params.getlist('owner')

        if title:
            queryset = queryset.filter(title__in=title)
        if owner:
            queryset = queryset.filter(owner__username__in=owner)
        if ingredient:
            queryset = queryset.filter(recipe__ingredients__name__in=ingredient).distinct()

        if filter:=self.kwargs.get('sort', None):
            if filter == 'ratings':
                posts = queryset.annotate(avg_rating=Avg('Rating__score')).order_by(
                    '-avg_rating')
                return posts
            elif filter == 'favorites':
                posts = queryset.annotate(num_favorites=Count('Favorited_by')).order_by('-num_favorites')
                return posts
        return queryset
