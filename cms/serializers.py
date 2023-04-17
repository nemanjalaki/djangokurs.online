from rest_framework import serializers
from .models import Author, Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []

