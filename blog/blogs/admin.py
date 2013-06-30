from blogs.models import Blog, Comment, Post
from django.contrib import admin
admin.autodiscover()

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Post)