from django.contrib import admin

from Posts.models import Comment, Favorite, Like, Post, Rating

admin.site.register(Post)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Like)
