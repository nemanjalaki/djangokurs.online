from django.contrib import admin
from .models import Author, Post, Comment
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'surname')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'body','author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','body', 'author','post')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)