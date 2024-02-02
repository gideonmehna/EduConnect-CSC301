from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.db import models
from django.db.models import CASCADE, SET_NULL

from Recipes.models import Recipe
from Accounts.models import UserProfile


class Post(models.Model):
    title = models.CharField(max_length=50)
    recipe = models.ForeignKey(to=Recipe, null=False, on_delete=CASCADE)
    description = models.TextField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True, auto_created=True)
    date_modified = models.DateTimeField(auto_now=True, auto_created=True)
    owner = models.ForeignKey(to=UserProfile, null = False, related_name = 'Posts', on_delete=CASCADE)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(to=UserProfile, null = False, related_name = 'Favorites', on_delete=CASCADE)
    post = models.ForeignKey(to=Post, null = False, related_name = 'Favorited_by', on_delete=CASCADE)

    def __str__(self):
        return "%s favorites %s" % (self.user, self.post)

    class Meta:
        unique_together = (('user', 'post'),)


class Like(models.Model):
    user = models.ForeignKey(to=UserProfile, null=False, related_name='Liked', on_delete=CASCADE)
    post = models.ForeignKey(to=Post, null=False, related_name='Likes', on_delete=CASCADE)

    def __str__(self):
        return "%s likes %s" % (self.user, self.post)

    class Meta:
        unique_together = (('user', 'post'),)


class Comment(models.Model):
    content = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, auto_created=True)
    photo = models.ImageField(blank=True, upload_to='images/')
    vid = models.FileField(upload_to='files/', null=True,
validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    user = models.ForeignKey(to=UserProfile, null=False,
                             related_name='commented', on_delete=CASCADE)
    post = models.ForeignKey(to=Post, null=False, related_name='comments',
                             on_delete=CASCADE)

    def __str__(self):
        return "%s comments on %s" % (self.user, self.post)


class Rating(models.Model):
    score = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True, auto_created=True)
    user = models.ForeignKey(to=UserProfile, null=False,
                             related_name='Rated', on_delete=CASCADE)
    post = models.ForeignKey(to=Post, null=False, related_name='Rating',
                             on_delete=CASCADE)

    def __str__(self):
        return "%s rate %s" % (self.user, self.post)

    class Meta:
        unique_together = (('user', 'post'),)
