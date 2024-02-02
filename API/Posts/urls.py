from django.urls import path

from Posts.views import GetPostView, GetPostsView, CreatePostView, DeletePostView, LikePostView, GetPostLikesView, \
    GetLikedPostsView, UnLikePostView, FavoritePostView, GetFavoritedPostsView, UnFavoritePostView, CommentPostView, \
    GetCommentPostView, GetCommentedPostsView, EditCommentPostView, UnCommentPostView, RatePostView, GetRatePostView, \
    EditRatingPostView, UnRatePostView, GetCommentsPostView, GetRatingsPostView, MyRecipes, GetPostFavoritesView, \
    SearchPostsView

urlpatterns = [
    path('create/', CreatePostView.as_view()),
    path('<int:pk>/', GetPostView.as_view()),
    path('<str:sort>/all/', GetPostsView.as_view()),
    path('search/<str:sort>/', SearchPostsView.as_view()),
    path('<int:pk>/edit/', GetPostsView.as_view()),
    path('<int:pk>/delete/', DeletePostView.as_view()),
    path('<int:post>/favorite/', FavoritePostView.as_view()),
    path('<int:user>/favorites/', GetFavoritedPostsView.as_view()),
    path('<int:post>/favorites/all/', GetPostFavoritesView.as_view()),
    path('<int:post>/unfavorite/', UnFavoritePostView.as_view()),
    path('<int:post>/like/', LikePostView.as_view()),
    path('<int:post>/like/all/', GetPostLikesView.as_view()),
    path('<int:user>/likes/', GetLikedPostsView.as_view()),
    path('<int:post>/unlike/', UnLikePostView.as_view()),
    path('<int:post>/comment/', CommentPostView.as_view()),
    path('comment/<int:pk>/view/', GetCommentPostView.as_view()),
    path('<int:post>/comment/view/all/', GetCommentsPostView.as_view()),
    path('<int:user>/comments/', GetCommentedPostsView.as_view()),
    path('comment/<int:pk>/edit/', EditCommentPostView.as_view()),
    path('<int:post>/comment/<int:pk>/delete/', UnCommentPostView.as_view()),
    path('<int:post>/rate/', RatePostView.as_view()),
    path('<int:post>/rating/view/', GetRatePostView.as_view()),
    path('<int:post>/rating/view/all/', GetRatingsPostView.as_view()),
    path('rating/<int:pk>/edit/', EditRatingPostView.as_view()),
    path('rating/<int:pk>/delete/', UnRatePostView.as_view()),
    path('myrecipes/', MyRecipes)
]
